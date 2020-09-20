#!/bin/sh

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn quiz.wsgi:application \
    --bind 0.0.0.0:8009 \
    --workers 1 &
    echo Migrating Database Models
    python manage.py makemigrations &
    python manage.py migrate &
    # echo Loading Database With Questions &
    # python manage.py loaddata recharge/fixtures/recharge.json --app recharge




