#!/usr/bin/env bash


/usr/bin/gunicorn -c dev_config.py 

sleep 5

PID=$(cat /var/run/gunicorn/dev.pid)
echo "Started gunicorn process id : ${PID}"
