#!/bin/sh

# Start Celery processes
    echo Starting Celery Worker &
    celery -A quiz beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler 





