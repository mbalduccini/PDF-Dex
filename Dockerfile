FROM python:3.8-slim-buster
LABEL MAINTAINER="David Tippett"

ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /code
COPY . .

# Setting default argument values
ARG ES_IP="127.0.0.0"
ARG ES_PORT=9200

# Map them to environment variables
ENV ES_IP=${ES_IP}
ENV ES_PORT=${ES_PORT}

CMD python /code/pdf-dex/main.py --threads $THREADS
