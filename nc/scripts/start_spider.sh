#!/bin/bash

reset
echo "Start spider..."

docker exec -it nc_backend bash -c "cd news_scrapy && scrapy crawl vnexpress"
