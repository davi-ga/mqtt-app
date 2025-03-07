#!/bin/sh
export $(grep -v '^#' ../.env | xargs)

while ! nc -z db 5432 ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done

python manage.py migrate
python manage.py runserver 0.0.0.0:${API_PORT}
