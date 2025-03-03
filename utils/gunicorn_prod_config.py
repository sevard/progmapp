"""Gunicorn *production* config file"""

import os

BASE = os.path.join(os.getenv("HOME"), "local")
ACCESS_LOG = os.path.join(BASE, "logs", "prod.access.log")
ERROR_LOG = os.path.join(BASE, "logs", "prod.error.log")
PIDFILE = os.path.join(BASE, "logs", "gunicorn_pid")

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "progmapp.wsgi:application" # ex: "project.wsgi:application"

# The granularity of Error log outputs
loglevel = "debug"

# The number of worker processes for handling requests
workers = 2

# The socket to bind
bind = "127.0.0.1:8000" #bind = "0.0.0.0:8000"

# Restart workers when code changes (development only!)
reload = False

# Write access and error info to /var/log
accesslog = ACCESS_LOG
errorlog = ERROR_LOG

# Redirect stdout/stderr to log file
capture_output = True

# PID file so you can easily fetch process ID
pidfile = PIDFILE

# Daemonize the Gunicorn process (detach & enter background)
daemon = True

