import os
from elasticsearch import Elasticsearch
from utilities.types import PDF

ELASTIC_IP = os.getenv('ES_IP')
ELASTIC_PORT = os.getenv('ES_PORT')

if ELASTIC_IP == None:
    ELASTIC_IP = "127.0.0.1"

if ELASTIC_PORT == None:
    ELASTIC_PORT = 9200


# ---------------------------------------------------------------------------------
# Logging initialization
import logging

logger = logging.getLogger(__name__)
consoleHandle = logging.StreamHandler()
consoleHandle.setLevel(logging.INFO)

# Setup the formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consoleHandle.setFormatter(formatter)
logger.addHandler(consoleHandle)

# ---------------------------------------------------------------------------------

def file_exists(path:str, es: Elasticsearch):
    resp = es.exists(index="pdfs", id=path, ignore=[404])

    return resp


def verify_indexes():
    es = get_elastic_instance()
    if "pdfs" not in es.indices.get_alias().keys():
        es.indices.create(index='pdfs')



def get_elastic_instance():
    return Elasticsearch(
      [ELASTIC_IP],
      port=ELASTIC_PORT
    )


def insert_file(file: PDF, es: Elasticsearch):
    document = dict(file)
    try:
        result = es.index(index="pdfs", id=file._id, body=document)
    except Exception as e:
        logger.exception(f"There was an exception: {e}")

    logger.info(f"Inserting file: {file._id}")
    return result
