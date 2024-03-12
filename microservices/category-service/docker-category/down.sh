#!/bin/sh

SCRIPT=$(readlink -f "$0")
DIR=$(dirname "$SCRIPT")
cd $DIR

echo
echo "Finalizando os containers no ambiente <$ENV>"
echo

docker compose -f docker-compose.yml down
