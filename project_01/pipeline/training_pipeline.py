import sys

from project_01.exception import project_01_exception
from project_01.logger import logging
from project_01.components.data_ingestion import DataIngestion
from project_01.components.data_validation import DataValidation
from project_01.components.data_transformation import DataTransformation
from project_01.components.model_trainer import ModelTrainer
from project_01.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from project_01.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.model_trainer_config = ModelTrainerConfig()
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        '''
        This method of the TrainingPipeline is responsible for staring data ingestion thru data_ingestion component
        '''
        try:
            logging.info("PROCESS START: TRAINING PIPELINE: DATA INGESTION")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("PROCESS END: TRAINING PIPELINE: DATA INGESTION")
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
            logging.info("PROCESS END: TRAINING PIPELINE: DATA VALIDATION")
            return data_validation_artifact
        except Exception as e:
            raise project_01_exception(e, sys) from e        
        
    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_artifact:DataValidationArtifact) -> DataTransformationArtifact:
        '''
        This method of the TrainingPipeline is responsible for staring data transformation
        '''
        try:
            logging.info("PROCESS START: TRAINING PIPELINE: DATA TRANSFORMATION")
            data_transformation = DataTransformation(data_transformation_config=self.data_transformation_config, data_validation_artifact=data_validation_artifact, 
                                                     data_ingestion_artifact = data_ingestion_artifact)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            logging.info("PROCESS END: TRAINING PIPELINE: DATA Transformation")
            return data_transformation_artifact
        except Exception as e:
            raise project_01_exception(e, sys) from e  

        
    def start_model_trainer(self,data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        '''
        This method of the TrainingPipeline is responsible for staring training Model
        '''
        try:
            logging.info("PROCESS START: TRAINING PIPELINE: MODEL TRAINER")
            model_trainer = ModelTrainer(data_transformation_artifact= data_transformation_artifact,
                                         model_trainer_config= self.model_trainer_config)
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            logging.info("PROCESS END: TRAINING PIPELINE: MODEL TRAINER")
            return model_trainer_artifact
        except Exception as e:
            raise project_01_exception(e, sys) from e                    
    
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(data_ingestion_artifact, data_validation_artifact)
            model_trainer_artifact = self.start_model_trainer(data_transformation_artifact)
        except Exception as e:
            raise project_01_exception(e, sys) from e
        