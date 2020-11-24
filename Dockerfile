FROM python:3.8-alpine
LABEL MAINTAINER="David Tippett"
COPY . /pdf-dex/
WORKDIR /pdf-dex/

# Setting default argument values
ARG ES_IP="127.0.0.0"
ARG ES_PORT=9300

# Map them to environment variables
ENV ES_IP=${ES_IP}
ENV ES_PORT=${ES_PORT}

RUN pip install -r /pdf-dex/requirements.txt
CMD python /pdf-dex/pdf-dex/main.py $THREADS
