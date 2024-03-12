#!/usr/bin/env bash

PIDFILE=/var/run/gunicorn/dev.pid

if test -f "$PIDFILE"; then
    echo "Found $PIDFILE"
    PID=$(cat $PIDFILE)
    kill $PID
    kill_rc=$?
    echo "stopping... $PID"
    echo "gunicorn was stopped with (exit code $kill_rc)"
    exit 0
fi

echo "PID file not found... Quiting"
exit 1
