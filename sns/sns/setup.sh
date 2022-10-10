#!/bin/sh

echo DB_USER=root >.env
echo DB_PASSWORD=password >>.env
echo DB_HOST=localhost >>.env
echo DB_PORT=27017 >>.env
echo SECRET_KEY=$(openssl rand -hex 32) >>.env

cp .env ./backend

docker-compose up -d
