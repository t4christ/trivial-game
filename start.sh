#!/bin/sh

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn quiz.wsgi:application \
    --bind 0.0.0.0:8009 \
    --workers 1 &
    echo Starting Celery Worker &
    celery -A quiz worker -l info &
    echo Starting Celery Worker &
    celery -A quiz beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler




