#!/bin/sh

SCRIPT=$(readlink -f "$0")
DIR=$(dirname "$SCRIPT")
cd $DIR


echo
sleep 1
echo "Creating the docker-rabbit network..."
echo

docker network ls | grep "\bdocker-rabbit\b" || docker network create --driver=bridge docker-rabbit 2>&1 

echo
echo "Iniciando os containers no ambiente"
echo


docker compose -f docker-compose.yml  up --build -d
echo
sleep 5
docker compose ps
echo
