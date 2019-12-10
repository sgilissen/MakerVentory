#!/bin/bash

# Prepare log files and start outputting logs to stdout
touch ./logs/makerventory-gunicorn.log
touch ./logs/makerventory-gunicorn-access.log
tail -n 0 -f ./logs/makervenotry-gunicorn*.log &

export DJANGO_SETTINGS_MODULE=makerventory.settings

exec gunicorn projectx.wsgi:application \
    --name makerventory_django \
    --bind 0.0.0.0:8000 \
    --workers 5 \
    --log-level=info \
    --log-file=./logs/gunicorn.log \
    --access-logfile=./logs/gunicorn-access.log \
"$@"