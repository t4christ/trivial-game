#!/bin/sh

# Start Celery processes
    echo Starting Celery Worker &
    celery -A quiz worker -l info 




