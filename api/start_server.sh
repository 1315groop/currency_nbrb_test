#!/bin/bash
# Check PostgreSQL readiness
DB_HOST="db"
DB_PORT="5432"
RETRIES=10
SLEEP_INTERVAL=5
echo "Checking if PostgreSQL is ready..."
until pg_isready -h "$DB_HOST" -p "$DB_PORT"; do
  RETRIES=$((RETRIES - 1))
  if [ $RETRIES -le 0 ]; then
    echo "PostgreSQL is not ready after multiple attempts, exiting."
    exit 1
  fi
  echo "PostgreSQL is not ready yet. Retrying in $SLEEP_INTERVAL seconds..."
  sleep $SLEEP_INTERVAL
done

echo "PostgreSQL is ready, applying migrations."



# Run migrations and start server
python -u manage.py migrate
python -u manage.py runserver 0.0.0.0:8000
