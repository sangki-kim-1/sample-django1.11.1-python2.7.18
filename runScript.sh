#!/bin/bash

BUILD_NAME=sample-django1.11.1-python2.7.18

docker rmi $BUILD_NAME
docker build -t $BUILD_NAME .

# foreground -> script exit = docker process stop
docker run --rm -p 8000:8000 --name $BUILD_NAME $BUILD_NAME

# for docker data remaining local
#docker run --rm -p 8000:8000 --name $BUILD_NAME -v ./:/app $BUILD_NAME

# background -> must docker stop manually for process exit
# docker run -d --rm -p 8000:8000 --name $BUILD_NAME $BUILD_NAME
# docker stop $BUILD_NAME
