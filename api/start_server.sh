#!/bin/bash
# run migrations and start server
python -u manage.py migrate
python -u manage.py runserver 0.0.0.0:8000
