#!/bin/bash

set -e;
python3 manage.py shell < ./scripts/start_spider.py
