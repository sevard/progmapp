#!/usr/bin/env bash


if [ -n $1 ]; then
    GUNICORN_CONFIG_FILE=utils/gunicorn_prod_config.py
else
    GUNICORN_CONFIG_FILE=$1
fi

# test gunicorn config
/usr/bin/gunicorn --check-config -c $GUNICORN_CONFIG_FILE
rc=$?
if [ $rc -ne 0 ]; then
    echo "gunicorn config file test failed.."
    exit 0
fi

# check if existing process is running
if test -f /var/run/gunicorn/dev.pid; then
    echo "Quit starting server"
    echo "Found existing PID: $(cat /var/run/gunicorn/dev.pid)"
    exit 2
fi

# start gunicorn and wait PID file
/usr/bin/gunicorn -c $GUNICORN_CONFIG_FILE
rc=$?
if [ $rc -ne 0 ]; then
    echo "Failed to start gunicorn server.."
    exit 3
fi

PIDFILE=/var/run/gunicorn/dev.pid
while true; do

    timestamp=$(date +"%a %Y-%m-%d %T")

    echo -ne "Waiting for gunicorn to start.. $timestamp \r"
    sleep 1

    if test -f "$PIDFILE"; then
	    echo $timestamp
	    echo -ne "gunicorn started. pid $(cat $PIDFILE)\n"
	    exit 0
    fi

done

