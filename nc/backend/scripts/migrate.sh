#!/bin/bash

set -e

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
