FROM ubuntu:latest
MAINTAINER Andrew Komar 0xporky@gmail.com
EXPOSE 80

COPY . /mgnemu-python

WORKDIR /mgnemu-python

RUN apt-get update \
&& apt-get install -y python3-pip nginx \
&& pip3 install -e . \
&& ln -s mgnemu_nginx.conf /etc/nginx/sites-enabled/ \
&& mkdir -p /tmp/socket \
&& chown www-data:www-data /tmp/socket \
&& rm -rf /var/lib/apt/lists/*

ENV HOST=0.0.0.0 \
PORT=5005 \
DEBUG=Off \
DB_HOST=0.0.0.0 \
DB_PORT=27017 \
DB_USER=admin \
DB_PASS=password

CMD bash -c "/etc/init.d/nginx start && uwsgi \
--socket /tmp/socket/mgnemu.sock \
--wsgi-file mgnemu/run.py \
--processes 4 \
--callable app \
--uid=www-data \
--gid=www-data"
