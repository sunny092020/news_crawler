#!/bin/bash

docker-compose -f docker-compose.yml run --rm nc_backend bash -c "cd news_scrapy && scrapy genspider vnexpress vnexpress.net"
