#!/usr/bin/env bash


echo "gunicorn process id: $(cat /var/run/gunicorn/dev.pid)"
echo "stopping..."
kill $(cat /var/run/gunicorn/dev.pid)

echo "gunicorn stopped with exit status ${?}"
