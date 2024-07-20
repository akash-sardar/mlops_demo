# MLOPS - Demo for Production ready project
## Pre-requisites and tools
* Anaconda Installation
* VS Code
* GIT Bash
* MLOPS using - Evidently AI - https://www.evidentlyai.com/
* Database used - MongoDB
## Commands to create a VENV
* conda create -n project_01 python=3.8 -y
* conda activate project_01
* install requirements: pip install -r requirements.txt
## Source Data
* https://www.kaggle.com/datasets/moro23/easyvisa-dataset
## Note:
Project workflow usually follows the path - for each component - update constants, update entity, update components, update pipeline, test in demo, update main file
## Project Workflow
* 1. Update the contructor in  "Constants" with CONSTANT Variable values such as DB Name, Model Name etc.
* 2a. Update "Entities" - creates the path for config entity and artifact entity
* 2b. Add 'mongo_db_connection' in Configuration - this will create a class MongoDBClient which will establish a connection with the database when invoked
* 2c. Create a data_access folder in project_01 with a constructor and source_data_import.py. This utility will createa class SourceData which will return a dataframe from mongoDB collection
* 2d. Update the Components - Data Ingestion : Incorporate entity items, data_access items and extracts data from MongoDB and creates a CSV file in Feature Store folder/artifacts. Also splits data into Train-Test_split format
* 2e. Update (assimilate) the pipeline (class TrainingPipeline) with Components from Data Ingestion package.
* 3a. Update the components - Data Validation : Check for Columns, Check for Data Drift using Evidently ML Monitoring tool
* 3b. Update config/Schema.yaml with schema details such as columns, numeric columns, categorical columns, dropped columns, numerical features for transformation, Ordinal encoding columns, one hot encoding columns, transformation columns etc.
* 3c. Update "entity" for data validation - config entity with validation directory and drift report directory and artifact entity with message, validation status path
* 3d. Update the data_validation component
* 3e. Update Training Pipeline
* 4a. Update "Data Transformation" component - will contain any feature engineering required : Constants. Entities, Components, Pipeline




