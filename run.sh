#!/bin/bash

# pyenv exec gunicorn --bind 0:8000 restapi.wsgi:application --reload

# pyenv exec python -m pip install uwsgi wsgi 설치

# static file 생성
# python manage.py collectstatic 


pyenv exec uwsgi --chdir=/Users/nhn/workspace/dev/project/apppaas/language/python/django/python2/sample-django1.11.1-python2.7.18 \
    --module=restapi.wsgi:application \
    --http :8000 \
    --static-map /static=/Users/nhn/workspace/dev/project/apppaas/language/python/django/python2/sample-django1.11.1-python2.7.18/static