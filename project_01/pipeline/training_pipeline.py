import sys

from project_01.exception import project_01_exception
from project_01.logger import logging
from project_01.components.data_ingestion import DataIngestion
from project_01.components.data_validation import DataValidation
from project_01.entity.config_entity import DataIngestionConfig, DataValidationConfig
from project_01.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
    
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
        
    def start_data_validation(self, data_ingestion_artifact:DataIngestionArtifact) -> DataValidationArtifact:
        '''
        This method of the TrainingPipeline is responsible for staring data validation thru data_validation component
        '''
        try:
            logging.info("PROCESS START: TRAINING PIPELINE: DATA VALIDATION")
            data_validation = DataValidation(data_validation_config=self.data_validation_config, data_ingestion_artifact=data_ingestion_artifact)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("PROCESS END: TRAING PIPELINE: DATA VALIDATION")
            return data_validation_artifact
        except Exception as e:
            raise project_01_exception(e, sys) from e        
    
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact)
        except Exception as e:
            raise project_01_exception(e, sys) from e
        