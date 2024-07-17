from project_01.configuration.mongo_db_connection import MongoDBClient
from project_01.constants import DATABASE_NAME
from project_01.exception import project_01_exception

import pandas as pd
import sys
from typing import Optional
import numpy as np

class SourceData:
    '''
    This class will export entire mongo db record into pandas dataframe
    '''
    def __init__(self):
        '''
        '''
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise project_01_exception(e,sys)
        
    def export_collection_as_dataframe( self, collection_name:str, database_name:Optional[str]=None)->pd.DataFrame:
        '''
        Returns entire MongoDB collection in Dataframe format
        returns: pd.DataFrame of collection
        '''
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis = 1)
            df.replace({"na":np.nan}, inplace = True)
            return df
        except Exception as e:
            raise project_01_exception(e, sys)

        