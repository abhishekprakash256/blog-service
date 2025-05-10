"""
The MongoDB services module provides functions to interact with a MongoDB database.
"""
import mongo_helper_kit



#these are the information can chnage in future
#mongo database infomation

from apis.config import MONGO_HOST_NAME




#helper method instance
db_helper_mongo = mongo_helper_kit.Helper_fun(MONGO_HOST_NAME)





