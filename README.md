# mgnemu

[![Build Status](https://travis-ci.org/0xporky/mgnemu-python.svg?branch=master)](https://travis-ci.org/0xporky/mgnemu-python)
[![Docker Automated buil](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg)](https://hub.docker.com/r/0xporky/mgnemu-python/builds/)
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat)](http://badges.mit-license.org)

**Software emulator of MG-N707TS cash machime.**

## Installation guideline ##
1. Clone repository using command.
```bash
git clone https://github.com/0xporky/mgnemu-python.git
```
2. Move to catalog mgnemu-python and run command.
```bash
pip install -e .
```

## Run the emulator using docker compose ##
1. Clone docker image using the command:
```bash
docker pull 0xporky/mgnemu-python
```
2. After pulling the image you need to move into mgnemu-python:
```bash
cd ./mgnemu-python
```
3. Then you need to start emulating process using docker compose:
```bash
docker-compose up -d
```
