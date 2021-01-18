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
git-clone the present project

From the folder that contains pdf-dex run:
```
docker build --tag pdf-dex .
```

### Running Image
Find the ip of the elastic image by running `docker inspect elastic`

```
data="path/to/pdfs/here"
docker run \
    --name pdf-dex \
    -e "THREADS=1" \
    -e "ES_IP=172.17.0.2" \
    -e "ES_PORT=9200" \
    --network bridge \
    -v "$data":/data \
    pdf-dex
```
