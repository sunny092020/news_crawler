#!/bin/bash

set -e

docker-compose -f docker-compose.yml run --rm nc_backend scrapy startproject $1
