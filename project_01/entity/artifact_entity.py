import os
from project_01.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class DataIngestionArtifact:
    training_file_path: str
    testing_file_path: str