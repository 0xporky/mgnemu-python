# mgnemu

[![Build Status](https://travis-ci.org/0xporky/mgnemu-python.svg?branch=master)](https://travis-ci.org/0xporky/mgnemu-python)

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

## Starting the emulator ##
After installation you can run the emulator from mgnemu-python catalog using commad.
```bash
./bin/mgnemu
```
Also you can use some command line parameters to customise emultor networking:
* --port=port
* --host=host
* --debug=debug

For more info see:
```bash
./bin/mgnemu --help
```

## Run the emulator using docker image ##
1. Clone docker image using the command:
```bash
docker pull 0xporky/mgnemu-python
```
2. After pulling the image you need to start container with command:
```bash
docker run -d -p 80:80 0xporky/mgnemu-python
```
That command will run the emulator with parameters:
```bash
./bin/mgnemu --host=0.0.0.0
```
