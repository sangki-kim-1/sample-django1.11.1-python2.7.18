#!/bin/bash

BUILD_NAME=sample-django1.11-python2

docker rmi $BUILD_NAME
docker build -t $BUILD_NAME .

# foreground -> script exit = docker process stop
docker run --rm -p 8000:8000 --name $BUILD_NAME $BUILD_NAME

# background -> must docker stop manually for process exit
# docker run -d --rm -p 8000:8000 --name sample sample
# docker stop sample
