"""
The blog API provides endpoints to get the latest articles, articles by section, 
and a specific article by name or ID using a MongoDB database.
"""

# Import statements
from flask import Blueprint, jsonify, request
from services.mongo_services import db_helper_mongo
from pymongo.errors import PyMongoError
from http import HTTPStatus
from bson import json_util
import json

# Define the blueprint for the blog API
blog_bp = Blueprint('blog_bp', __name__)

# MongoDB settings (make sure these are set somewhere globally or passed in)
#mongo database infomation
MONGO_DB_NAME = "test-main-database"
MONGO_COLLECTION_NAME = "test-article-collections"
MONGO_HOST_NAME = "localhost"
MONGO_SECTION_NAME = ["tech", "project", "life"]






@blog_bp.route("/blog/section/<category>/article/<article_name>", methods=["GET"])
def get_article_data(category, article_name):
    """
    Get the article data from a specific category.

    Args:
        category (str): The category name from the URL.
        article_name (str): The article name from the URL.

    Returns:
        JSON response:
            - 200 OK: Article data if found.
            - 404 Not Found: Article not found.
            - 500 Internal Server Error: Any unexpected/database error.
    """
    try:
        data = db_helper_mongo.get_article_data(
            MONGO_DB_NAME,
            MONGO_COLLECTION_NAME,
            category,
            article_name
        )

        if not data:
            return jsonify({
                "status": "fail",
                "message": f"Article '{article_name}' in category '{category}' not found."
            }), HTTPStatus.NOT_FOUND

        article_data = json.loads(json_util.dumps(data))

        return jsonify({
            "status": "success",
            "data": article_data
        }), HTTPStatus.OK

    except PyMongoError as e:
        return jsonify({
            "status": "error",
            "message": "A database error occurred.",
            "details": str(e)
        }), HTTPStatus.INTERNAL_SERVER_ERROR

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred.",
            "details": str(e)
        }), HTTPStatus.INTERNAL_SERVER_ERROR




@blog_bp.route("/blog/section/<category>", methods=["GET"])
def get_section_data(category):
    """
    Get section data (in card format) from a specific category.

    Query Params:
        limit (int, optional): Number of items to fetch. Minimum is 3; defaults to all if not provided.

    Example:
        GET /mongo/section/tech?limit=5

    Args:
        category (str): The section/category name from the URL.

    Returns:
        JSON response:
            - 200 OK: List of card data.
            - 404 Not Found: No data found for the given category.
            - 500 Internal Server Error: Any unexpected/database error.
    """
    try:
        limit = request.args.get("limit", type=int)

        # Enforce minimum limit of 3
        if limit is None or limit < 3:
            limit = 3

        data = db_helper_mongo.get_card_data(
            MONGO_DB_NAME,
            MONGO_COLLECTION_NAME,
            category,
            limit
        )

        if not data:
            return jsonify({
                "status": "fail",
                "message": f"No data found for category '{category}'."
            }), HTTPStatus.NOT_FOUND

        section_data = json.loads(json_util.dumps(data))

        return jsonify({
            "status": "success",
            "data": section_data
        }), HTTPStatus.OK

    except PyMongoError as e:
        return jsonify({
            "status": "error",
            "message": "A database error occurred.",
            "details": str(e)
        }), HTTPStatus.INTERNAL_SERVER_ERROR

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred.",
            "details": str(e)
        }), HTTPStatus.INTERNAL_SERVER_ERROR





@blog_bp.route("/blog/section/explore", methods=["GET"])
def getExploreData():
    """
    The function to get the explore data of mixed sections.
    Gets the maximum data of cards from multiple sections, with a configurable limit (default: 15).

    Query Params:
        limit (int, optional): Number of items to fetch. Minimum is 3; defaults to 15 if not provided.

    Example:
        GET /mongo/section/explore?limit=5

    Returns:
        JSON response:
            - 200 OK: Combined data from all sections.
            - 500 Internal Server Error: If any database or unexpected error occurs.
    """
    try:
        # Get the limit from the query parameters, default to 15 if not provided
        limit = request.args.get("limit", type=int)

        # Enforce a minimum limit of 3
        if limit is None or limit < 3:
            limit = 15

        # Fetch data for each section based on the provided limit
        data_section_one = db_helper_mongo.get_card_data(MONGO_DB_NAME, MONGO_COLLECTION_NAME, MONGO_SECTION_NAME[0], limit)
        data_section_two = db_helper_mongo.get_card_data(MONGO_DB_NAME, MONGO_COLLECTION_NAME, MONGO_SECTION_NAME[1], limit)
        data_section_three = db_helper_mongo.get_card_data(MONGO_DB_NAME, MONGO_COLLECTION_NAME, MONGO_SECTION_NAME[2], limit)

        # Combine all data from the sections
        combined_data = data_section_one + data_section_two + data_section_three

        # Return the combined data as a JSON response
        return jsonify({
            "status": "success",
            "data": combined_data
        }), HTTPStatus.OK

    except PyMongoError as e:
        return jsonify({
            "status": "error",
            "message": "A database error occurred while fetching the explore data.",
            "details": str(e)
        }), HTTPStatus.INTERNAL_SERVER_ERROR

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred while processing your request.",
            "details": str(e)
        }), HTTPStatus.INTERNAL_SERVER_ERROR





@blog_bp.route("/blog/search", methods=["GET"])
def getSearchData():
    """
    Search the database for documents matching the given keyword.

    Query Params:
        keyword (str, required): The search keyword.


    Example:
        GET /mongo/search?keyword=a

    Returns:
        JSON response:
            - 200 OK: List of matching documents.
            - 400 Bad Request: If the keyword is missing.
            - 404 Not Found: No results found for the given keyword.
            - 500 Internal Server Error: Any unexpected/database error.
    """
    try:
        # Get query parameters
        keyword = request.args.get("keyword")
        
        # Validate keyword
        if not keyword:
            return jsonify({
                "status": "fail",
                "message": "The 'keyword' query parameter is required."
            }), 400

        # Ensure keyword is a string
        if not isinstance(keyword, str):    
            return jsonify({
                "status": "fail",
                "message": "The 'keyword' query parameter must be a string."
            }), 400

        # Perform the search
        data = db_helper_mongo.search_database(MONGO_DB_NAME, MONGO_COLLECTION_NAME, keyword)

        if not data:
            return jsonify({
                "status": "fail",
                "message": f"No results found for keyword '{keyword}'."
            }), 404

        search_results = json.loads(json_util.dumps(data))

        return jsonify({
            "status": "success",
            "data": search_results
        }), HTTPStatus.OK

    except PyMongoError as e:
        return jsonify({
            "status": "error",
            "message": "A database error occurred while performing the search.",
            "details": str(e)
        }), HTTPStatus.INTERNAL_SERVER_ERROR

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred while processing your search request.",
            "details": str(e)
        }), HTTPStatus.INTERNAL_SERVER_ERROR


