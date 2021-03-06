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
For basic HTTP authentication and https: (see below to change port mappings on the fly and for setup)
```
docker run \
    --name elastic \
    -itd \
    -p 127.0.0.1:9201:9200 \
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


### Securing with basic HTTP Auth and HTTPS
Changing docker port redirects on the fly:

[https://stackoverflow.com/questions/19335444/how-do-i-assign-a-port-mapping-to-an-existing-docker-container

0. You can change the port mapping by directly editing the hostconfig.json file at /var/lib/docker/containers/[hash_of_the_container]/hostconfig.json or /var/snap/docker/common/var-lib-docker/containers/[hash_of_the_container]/hostconfig.json, I believe, if You installed Docker as a snap.
You can determine the [hash_of_the_container] via the docker inspect <container_name> command and the value of the "Id" field is the hash.]
1. Stop the container (docker stop <container_name>).
2. Stop docker service (per Tacsiazuma's comment)
3. Change the file, i.e.:
	"PortBindings":{"9200/tcp":[{"HostIp":"127.0.0.1","HostPort":"9201"}]}
4. Restart your docker engine (to flush/clear config caches).
5. Start the container (docker start <container_name>).

Setting up docker ports with docker run:
```
docker run \
    --name elastic \
    -itd \
    -p 127.0.0.1:9201:9200 \
    -e "discovery.type=single-node" \
    --network bridge  \
    docker.elastic.co/elasticsearch/elasticsearch:7.10.0
```

Authentication:

https://docs.bitnami.com/aws/apps/elasticsearch/administration/add-basic-auth-and-tls/

and add in the <Location> scope:
```
Required valid-user
```
Apache needs to listen on 9200 and redirect to 127.0.0.1:9201
