#!/bin/env bash

port=$1

python manage.py check
rc=$?

if [ ${rc} -eq 0 ]; then
    python manage.py runserver $port
fi

