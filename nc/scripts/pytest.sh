#!/bin/bash

reset

docker-compose run --rm nc_backend pytest nc/tests/test_api.py -s
