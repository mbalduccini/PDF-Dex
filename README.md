# PDF-Dex

A container for indexing pdf's in an elastic search instance.


### Starting ElasticSearch
```
docker run \
    --name elastic \
    -itd \
    -p 9200:9200 \
    -e "discovery.type=single-node" \
    --network bridge  \
    docker.elastic.co/elasticsearch/elasticsearch:7.10.0
```

### Building Image
From the root folder of the project run the following. 
```dockdocker build --tag pdf-dex:0.1 .```

### Running Image
Find the ip of the elastic image by running `docker inspect elastic`

```
docker run \
    --name pdf-dex \
    -e "THREADS=1" \
    -e "ES_IP=172.17.0.2" \
    -e "ES_PORT=9200" \
    --network bridge \
    -v /Users/dtippett/Data:/data \
    pdf-dex:0.1
```


### Sample Queries
Get documents that contain the word general more than 5 times
```
GET /pdfs/_search
{
	"query": {
        "range": {
            "tokenized_words.general": {
                "gte": 5
            }
		}
    }
}
```

Get documents that contain the field fragmentation
```
GET /pdfs/_search
{
	"query": {
        "exists": {
            "field":"tokenized_words.fragmentation"
		}
    }
}
```


Get documents that contain multiple fields
```
GET /pdfs/_search
{
	"query": {
        "bool": {
            "should": [
                {
                    "exists": {
                        "field":"tokenized_words.fragmentation"
                    }
                },
                {
                    "exists": {
                        "field":"tokenized_words.general"
                    }
                }
            ]
        }
    }
}
```