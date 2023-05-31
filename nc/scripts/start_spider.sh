#!/bin/bash

reset
echo "Start spider..."

docker exec -it nc_backend bash -c "./scripts/start_spider.sh"
