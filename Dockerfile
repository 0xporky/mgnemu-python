FROM ubuntu:latest

EXPOSE 80

RUN apt-get update
RUN apt-get install python-pip
RUN cd mgnemu-python 
RUN pip install -e . 
RUN ./bin/mgnemu -port=80
