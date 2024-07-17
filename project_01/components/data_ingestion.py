import os
import sys
from pandas import DataFrame
from sklearn.model_selection import train_test_split

from project_01.entity.config_entity import DataIngestionConfig
from project_01.entity.artifact_entity import DataIngestionArtifact
from project_01.logger import logging
from project_01.exception import project_01_exception
from project_01.data_access.source_data_import import SourceData

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        '''
        :param data_ingestion_config: configuration for data ingestion
        returns: DataIngestion object
        '''
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise project_01_exception(e, sys) from e
    
    def export_data_into_feature_store(self)-> DataFrame:
        '''
        Method Name: export_data_into_feature_store
        Description: This class method exports data from MongoDB to CSV File in DataFrame format

        Output: Data is returned as artifact of DataIngestion Components
        on Failure: Writes an exception log and then raises an exception
        '''
        try:
            logging.info("PROCESS START: Exporting data from MongoDB")
            source_data = SourceData()
            dataframe = source_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            logging.info(f"PROCESS END: Dataframe Extracted: Shape:{dataframe.shape}")
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok = True)
            logging.info(f"Exported Data saved in Feature Store File Path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path, index = False, header = True)
            return dataframe
        except Exception as e:
            raise project_01_exception(e, sys) from e
    
    def split_data_as_train_test(self, dataframe: DataFrame)-> None:
        '''
        Method name: split_data_as_train_test
        Description: This method splits the dataframe into train set and test set based on split ratio
        Output: Folder is created in local
        On Failure: Write an exception log and then raise an exception
        '''
        logging.info("PROCESS START: Splitting the dataset into train set and test set")
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio, shuffle = True, random_state = 42)
            logging.info("PROCESS END: Splitting")
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok= True)
            logging.info(f"Exporting train and test set into csv files")
            train_set.to_csv(self.data_ingestion_config.training_file_path, index = False, header = True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index = False, header = True)
            logging.info(f"Export complete")
        except Exception as e:
            raise project_01_exception(e, sys) from e
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        '''
        Method name: initiate_data_ingestion
        Description: This method drives the data ingestion
        Output: DataIngestionArtifact with path for training file and testing file
        On Failure: Write an exception log and then raise an exception
        '''        
        logging.info("PROCESS START: Initiate Data Ingestion")
        try:
            dataframe = self.export_data_into_feature_store()
            logging.info("Data Export complete")
            self.split_data_as_train_test(dataframe)
            logging.info("Data Split is complete")
            logging.info("PROCESS END: Data Ingestion")
            data_ingestion_artifact = DataIngestionArtifact(training_file_path= self.data_ingestion_config.training_file_path, testing_file_path=self.data_ingestion_config.testing_file_path)
            logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise project_01_exception(e, sys) from e
        
        