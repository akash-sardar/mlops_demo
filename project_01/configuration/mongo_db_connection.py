import os
import sys
import pymongo
import certifi
ca = certifi.where()

from project_01.constants import DATABASE_NAME, MONGODB_URL_KEY
from project_01.logger import logging
from project_01.exception import project_01_exception


class MongoDBClient:
    '''
    Class name: MongoDBCClient
    Description: Creates connection with DB
    Output: Connection to MongoDB Database
    on Failure: Raise Exception
    '''
    client = None
    def __init__(self, database_name = DATABASE_NAME):
        try:
            if MongoDBClient.client is None:
                mongo_db_url = MONGODB_URL_KEY
                if mongo_db_url is None:
                    raise Exception(f"Environment Key: {mongo_db_url} is not set")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection is successful")
        except Exception as e:
            raise project_01_exception(e, sys)
        

