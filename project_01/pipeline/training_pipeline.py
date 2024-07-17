import sys

from project_01.exception import project_01_exception
from project_01.logger import logging
from project_01.components.data_ingestion import DataIngestion
from project_01.entity.config_entity import DataIngestionConfig
from project_01.entity.artifact_entity import DataIngestionArtifact

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        '''
        This method of the TrainingPipeline is responsible for staring data ingestion thru data_ingestion component
        '''
        try:
            logging.info("PROCESS START: TRAINING PIPELINE: DATA INGESTION")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("PROCESS END: TRAING PIPELINE: DATA INGESTION")
            return data_ingestion_artifact
        except Exception as e:
            raise project_01_exception(e, sys) from e
    
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise project_01_exception(e, sys) from e
        