FROM ubuntu:latest

EXPOSE 80

RUN apt-get update \
&& apt-get install -y python-pip \
&& cd ~ \
&& git clone https://github.com/0xporky/mgnemu-python.git
