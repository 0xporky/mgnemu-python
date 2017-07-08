FROM ubuntu:latest

EXPOSE 80

COPY . ~/

RUN apt-get update \
&& apt-get install -y python-pip \
&& cd ~ \
