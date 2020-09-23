#!/bin/sh
# Start Celery processes
echo Starting Celery Beat &
celery -A quiz beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler 





