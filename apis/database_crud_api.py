"""
The database CRUD API provides endpoints to create, read, update, and delete articles in a MongoDB database.

The file will be wokrked on later to add the CRUD operations for the database not using right now.
"""

# Import statements
from flask import Blueprint, jsonify, request
from services.mongo_services import db_helper_mongo
from pymongo.errors import PyMongoError
from http import HTTPStatus
from bson import json_util
import json


# Define the blueprint for the blog API

dp_bp = Blueprint('dp_bp', __name__)



# MongoDB settings (make sure these are set somewhere globally or passed in)
# mongo database infomation

#MONGO_DB_NAME = "test-main-database"
#MONGO_COLLECTION_NAME = "test-article-collections"
#MONGO_HOST_NAME = "localhost"
#MONGO_SECTION_NAME = ["tech", "project", "life"]


#Make the functions and endpoints available in the blueprint

@dp_bp.route('/db/create', methods=['POST'])
def create_db_and_collection():
    """
    API endpoint to create a new MongoDB database and collection.

    Request JSON:
    {
        "db_name": "your_database_name",
        "collection_name": "your_collection_name"
    }

    Returns:
        JSON response:
            - 200 OK: If the database and collection were created successfully.
            - 400 Bad Request: If required fields are missing.
            - 500 Internal Server Error: If a database error occurs.
    """
    data = request.get_json()
    db_name = data.get('db_name')
    collection_name = data.get('collection_name')

    if not db_name or not collection_name:
        return jsonify({
            "status": "fail",
            "message": "Both 'db_name' and 'collection_name' are required."
        }), HTTPStatus.BAD_REQUEST

    try:
        db_helper_mongo.make_database_and_collection(db_name, collection_name)
        return jsonify({
            "status": "success",
            "message": f"Database '{db_name}' and collection '{collection_name}' created successfully."
        }), HTTPStatus.OK
    except PyMongoError as e:
        return jsonify({
            "status": "error",
            "message": f"Database error: {str(e)}"
        }), HTTPStatus.INTERNAL_SERVER_ERROR




@dp_bp.route('/db/insert', methods=['POST'])
def insert_data():
    """
    API endpoint to insert data into a MongoDB collection.

    Request JSON:
    {
        "db_name": "your_database_name",
        "collection_name": "your_collection_name",
        "article_data": {
            ... your document fields ...
        }
    }

    Returns:
        JSON response:
            - 201 Created: If data was inserted successfully.
            - 400 Bad Request: If required fields are missing.
            - 500 Internal Server Error: If a database error occurs.
    """

    data = request.get_json()
    db_name = data.get('db_name')
    collection_name = data.get('collection_name')
    article_data = data.get('article_data')

    if not all([db_name, collection_name, article_data]):
        return jsonify({
            "status": "fail",
            "message": "Fields 'db_name', 'collection_name', and 'article_data' are required."
        }), HTTPStatus.BAD_REQUEST

    try:
        db_helper_mongo.insert_data(db_name, collection_name, article_data)
        return jsonify({
            "status": "success",
            "message": "Data inserted successfully."
        }), HTTPStatus.CREATED
    except PyMongoError as e:
        return jsonify({
            "status": "error",
            "message": f"Database error: {str(e)}"
        }), HTTPStatus.INTERNAL_SERVER_ERROR



@dp_bp.route('/db/delete', methods=['DELETE'])
def delete_database():
    """
    API endpoint to delete (drop) a MongoDB database.

    Request JSON:
    {
        "db_name": "your_database_name"
    }

    Returns:
        JSON response:
            - 200 OK: If the database was deleted successfully.
            - 400 Bad Request: If the 'db_name' field is missing.
            - 500 Internal Server Error: If a database error occurs.
    """

    data = request.get_json()
    db_name = data.get('db_name')

    if not db_name:
        return jsonify({
            "status": "fail",
            "message": "The 'db_name' field is required."
        }), HTTPStatus.BAD_REQUEST

    try:
        db_helper_mongo.delete_db(db_name)
        return jsonify({
            "status": "success",
            "message": f"Database '{db_name}' deleted successfully."
        }), HTTPStatus.OK
    except PyMongoError as e:
        return jsonify({
            "status": "error",
            "message": f"Database error: {str(e)}"
        }), HTTPStatus.INTERNAL_SERVER_ERROR



@dp_bp.route('/db/fetch', methods=['POST'])
def fetch_all_data():
    """
    API endpoint to fetch all data from a MongoDB collection.

    Request JSON:
    {
        "db_name": "your_database_name",
        "collection_name": "your_collection_name"
    }

    Returns:
        JSON response:
            - 200 OK: Returns all documents in the collection.
            - 400 Bad Request: If 'db_name' or 'collection_name' is missing.
            - 500 Internal Server Error: If a database error occurs.
    """
    data = request.get_json()
    db_name = data.get('db_name')
    collection_name = data.get('collection_name')

    if not all([db_name, collection_name]):
        return jsonify({
            "status": "fail",
            "message": "Both 'db_name' and 'collection_name' are required."
        }), HTTPStatus.BAD_REQUEST

    try:
        result = db_helper_mongo.show_all_data(db_name, collection_name)
        # Convert any ObjectId to string if needed
        for doc in result:
            doc['_id'] = str(doc['_id'])
        return jsonify({
            "status": "success",
            "data": result
        }), HTTPStatus.OK
    except PyMongoError as e:
        return jsonify({
            "status": "error",
            "message": f"Database error: {str(e)}"
        }), HTTPStatus.INTERNAL_SERVER_ERROR





@dp_bp.route('/db/fetch-article', methods=['POST'])
def fetch_article_data():
    """
    API endpoint to fetch a specific article from a MongoDB collection.

    Request JSON:
    {
        "db_name": "your_database_name",
        "collection_name": "your_collection_name",
        "filter": {"article_name": "test1"}
    }

    Returns:
        JSON response:
            - 200 OK: Returns the matched article(s).
            - 400 Bad Request: If required fields are missing.
            - 404 Not Found: If no articles match the filter.
            - 500 Internal Server Error: If a database error occurs.
    """

    data = request.get_json()
    db_name = data.get('db_name')
    collection_name = data.get('collection_name')
    filter_query = data.get('filter')

    if not all([db_name, collection_name, filter_query]):
        return jsonify({
            "status": "fail",
            "message": "Fields 'db_name', 'collection_name', and 'filter' are required."
        }), HTTPStatus.BAD_REQUEST

    try:
        result = db_helper_mongo.show_article_data(db_name, collection_name, filter_query)
        
        # Handle case where nothing is found
        if not result:
            return jsonify({
                "status": "fail",
                "message": "No article found matching the given filter."
            }), HTTPStatus.NOT_FOUND

        # Convert ObjectIds to string if needed
        for doc in result:
            if '_id' in doc:
                doc['_id'] = str(doc['_id'])

        return jsonify({
            "status": "success",
            "data": result
        }), HTTPStatus.OK

    except PyMongoError as e:
        return jsonify({
            "status": "error",
            "message": f"Database error: {str(e)}"
        }), HTTPStatus.INTERNAL_SERVER_ERROR




