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
## Project Workflow
1. Update the contructor in  "Constants" with CONSTANT Variable values such as DB Name, Model Name etc.
2. Update "Entities" - creates the path for config entity and artifact entity
3. Add 'mongo_db_connection' in Configuration - this will create a class MongoDBClient which will establish a connection with the database when invoked
4. Create a data_access folder in project_01 with a constructor and source_data_import.py. This utility will createa class SourceData which will return a dataframe from mongoDB collection
5. Update the Components - Data Ingestion : Incorporate entity items, data_access items and extracts data from MongoDB and creates a CSV file in Feature Store folder/artifacts. Also splits data into Train-Test_split format
6. Update (assimilate) the pipeline (class TrainingPipeline) with Components from Data Ingestion package.
7. Update the components - Data Validation : Check for Columns, Check for Data Drift using Evidently ML Monitoring tool



