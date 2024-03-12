#!/bin/sh

SCRIPT=$(readlink -f "$0")
DIR=$(dirname "$SCRIPT")
cd $DIR

echo
echo "Iniciando os containers no ambiente <$ENV>"
echo

docker compose -f docker-compose.yml  up --build -d
echo
sleep 5
docker compose ps
echo
