FROM ubuntu:latest

EXPOSE 80

RUN apt-get install pip \
&& cd mgnemu-python \
&& pip install -e . \
&& ./bin/mgnemu -port=80
