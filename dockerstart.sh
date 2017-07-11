#!/bin/bash

docker-machine create ninjagold --driver "virtualbox" --virtualbox-disk-size 5000 --virtualbox-cpu-count 2 --virtualbox-memory 4096
docker-machine env ninjagold
