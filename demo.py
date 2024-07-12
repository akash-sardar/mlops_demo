from project_01.logger import logging
from project_01.exception import project_01_exception
import sys

logging.info("First Demo Custom Log")

try:
    a = 2/0
except Exception as e:
    logging.error(project_01_exception(e, sys))
