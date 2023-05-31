#!/bin/bash

reset

docker-compose -f docker-compose.yml run --rm nc_backend ./scripts/init_data.sh
