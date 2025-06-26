"""
The file to search the typesense for data and search in mongodb and return the list
"""

from bson.objectid import ObjectId
import typesense
import mongo_helper_kit
from services.typesense_client_service import typesense_client
from .config import MONGO_DB_NAME, MONGO_COLLECTION_NAME, MONGO_HOST_NAME, MONGO_SECTION_NAME





def search_typsense(search_query):
    """
    The function to search the typesense and return the id list for mongo db documnets 
    """

    #make the search paramaters
    search_parameters = {
    'q'         : search_query,
    'query_by': 'article_data',
    'prefix': 'all',
    'num_typos': 2,
    'split_join_tokens': True,
    'drop_tokens_threshold': 1,
    'exhaustive_search': False

    }

    #get the results
    res = typesense_client.collections['articles'].documents.search(search_parameters)

    #get the id numbers 
    id_numbers_list = [hit['document']['id'] for hit in res.get('hits', [])]

    return id_numbers_list




def search_mongodb_id(id_lst):
    """
    The function to search the mongo db with id from typesense 
    """

    #make the mongo client
    mongo_client = mongo_helper_kit.create_mongo_client(MONGO_HOST_NAME)

    #mongo db database
    db = mongo_client[MONGO_DB_NAME]

    #the mongo db collection
    collection = db[MONGO_COLLECTION_NAME]

    results = []

    for id in id_lst :

        obj_id = ObjectId(id)

        # Find the document
        doc = collection.find_one({"_id": obj_id})

        # Extract the necessary fields based on the new design
        card = {
            "card_title": doc.get("article_name", ""),
            "card_para": doc.get("article_para", ""),
            "img_src": doc.get("article_image", ""),
            "card_url": doc.get("article_link", "")
        }
        results.append(card)

    return results