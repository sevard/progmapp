#!/usr/bin/env bash

set -x

GUNICORN_CONFIG_FILE=${HOME}/local/progmapp/utils/gunicorn_prod_config.py
PIDFILE=${HOME}/local/logs/gunicorn_pid

#GUNICORN_CONFIG_FILE=utils/gunicorn_dev_config.py
#PIDFILE=/var/run/gunicorn/dev.pid

# Activate virtual environment
source $HOME/local/progmapp/venv/bin/activate

# Test gunicorn config
#/usr/bin/gunicorn --check-config -c $GUNICORN_CONFIG_FILE
gunicorn --check-config -c $GUNICORN_CONFIG_FILE
rc=$?
if [ $rc -ne 0 ]; then
    echo "gunicorn config file test failed.."
    exit 0
fi

# check if existing process is running
if test -s $PIDFILE; then
    echo "Quit starting server"
    echo "Found existing PID: $(cat $PIDFILE)"
    exit 2
fi

#DEBUG
##exit 0

# start gunicorn and wait PID file
gunicorn -c $GUNICORN_CONFIG_FILE
rc=$?
if [ $rc -ne 0 ]; then
    echo "Failed to start gunicorn server.."
    exit 3
fi

while true; do

    timestamp=$(date +"%a %Y-%m-%d %T")

    echo -ne "Waiting for gunicorn to start.. $timestamp \r"
    sleep 1

    if test -s "$PIDFILE"; then
	    echo $timestamp
	    echo -ne "gunicorn started. pid $(cat $PIDFILE)\n"
	    exit 0
    fi

done
