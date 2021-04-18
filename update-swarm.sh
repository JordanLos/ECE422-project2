#!/bin/bash

# For running on the swarm manager
docker stack rm app
rm docker-compose.yml
wget https://raw.githubusercontent.com/JordanLos/ECE422-project2/master/docker-compose.yml
echo -n "pausing for network to respawn "
sleep 1
echo -n ". "
sleep 1
echo -n ". "
sleep 1
echo -n ". "
sleep 1
echo -n ". "
sleep 1
echo -n ". "
sleep 1
echo -n ". "
sleep 1
echo "."
docker stack deploy --compose-file docker-compose.yml app
