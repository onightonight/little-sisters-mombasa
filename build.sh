#!/usr/bin/env bash
set -o errexit

pip install -r requirements_render.txt
python manage.py collectstatic --noinput
python manage.py migrate
