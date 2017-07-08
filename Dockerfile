FROM ubuntu:latest

EXPOSE 80

COPY . /root/

WORKDIR /root

RUN apt-get update \
&& apt-get install -y python-pip \
&& pip install -e . \
&& apt-get purge -y python-pip

CMD ["./bin/mgnemu"]
