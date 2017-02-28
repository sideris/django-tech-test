#!/usr/bin/env bash
# only if we set postgres
#docker-compose run -d app python -u manage.py migrate --noinput
#docker-compose run -d app python -u manage.py create_admin

python manage.py migrate --noinput
python manage.py create_admin