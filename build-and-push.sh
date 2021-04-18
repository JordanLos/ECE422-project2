#!/bin/bash

docker build -t jordanlos/autoscaler-server docker-images/autoscaler-server/ &&
docker push jordanlos/autoscaler-server
docker build -t jordanlos/autoscaler-client docker-images/autoscaler-client/ &&
docker push jordanlos/autoscaler-client
