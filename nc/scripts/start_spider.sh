#!/bin/bash

docker exec -it nc_backend bash -c "cd news_scrapy && scrapy crawl vnexpress"
