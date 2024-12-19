#!/usr/bin/env bash

PIDFILE=/var/run/gunicorn/dev.pid

if test -f "$PIDFILE"; then
    echo "Found $PIDFILE"
    PID=$(cat $PIDFILE)
    kill $PID
    sleep 3
    ps -ef | grep gunicorn
    exit 0
fi

echo "PID file not found... Quiting"
exit 1
