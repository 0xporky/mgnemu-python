FROM ubuntu:latest

EXPOSE 80

COPY . /root/

RUN apt-get update \
&& apt-get install -y python-pip \
