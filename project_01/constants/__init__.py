import os
from datetime import date

# Global/Project Constants
DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "visa_data"
MONGODB_URL_KEY = os.environ["MONGODB_URL"] # read from .env file
PIPELINE_NAME: str = "project_01"
ARTIFACT_DIR: str = "artifacts"
FILE_NAME: str = "usvisa.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
MODEL_FILE_NAME = "model.pkl"

# Data Ingestion related Constants
DATA_INGESTION_COLLECTION_NAME: str = 'visa_data'
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
