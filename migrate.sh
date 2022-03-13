#!/bin/bash

cd /app/

/opt/venv/bin/python manage.py migrate --noinput
# this code will fail on second run as superuser data is not unique || true is used for catching the exception
/opt/venv/bin/python manage.py createsuperuser --email ${DJANGO_SUPERUSER_EMAIL} --user_name ${DJANGO_SUPERUSER_USERNAME} --noinput || true