FROM ubuntu:latest

EXPOSE 80

RUN apt-get install pip \
&& pip install -e .
&& ./bin/mgnemu -port=80
