from elasticsearch import Elasticsearch
from utilities.types import PDF
ELASTIC_IP = os.getenv('ES_IP')
ELASTIC_PORT = os.getenv('ES_PORT')



def file_exists(path:str, es: Elasticsearch):
    resp = es.exists(index="PDFS", id=path, ignore=[404])

    return resp != None


def get_elastic_instance():
    return Elasticsearch(
      [ELASTIC_IP]
      port=ELASTIC_PORT
    )


def insert_file(file: PDF, es: Elasticsearch):
    
    es.create(index="PDFS", id=file._id, body=dict(file))
