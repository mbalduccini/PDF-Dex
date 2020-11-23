FROM python:3.8-alpine
LABEL MAINTAINER="David Tippett"
COPY . /pdf-dex/
WORKDIR /pdf-dex/
RUN pip install -r /pdf-dex/requirements.txt
CMD python /pdf-dex $THREADS