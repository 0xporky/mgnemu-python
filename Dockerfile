FROM ubuntu:latest

EXPOSE 80

RUN apt-get update
RUN apt-get install -y python-pip 
RUN pip install -e . 
RUN ./bin/mgnemu -port=80
