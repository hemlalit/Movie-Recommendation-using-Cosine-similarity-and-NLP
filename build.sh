#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic -m gunicorn mysite.asgi:application -k uvicorn.workers.UvicornWorkerstatic --no-input

python manage.py migrate