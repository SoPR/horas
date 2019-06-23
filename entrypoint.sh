#!/bin/ash

set -e

postgres_ready(){
python manage.py shell << END
import sys
import psycopg2
from django.db import connections
try:
    connections['default'].cursor()
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

if [ "$1" = 'serve' ]; then
  until postgres_ready; do
    >&2 echo "==> Waiting for Postgres..."
    sleep 1
  done

  echo "==> Running migrations..."
  pwd
  ls static
  python manage.py collectstatic --noinput
  python manage.py migrate
  python manage.py loaddata apps/profiles/fixtures/admin.json

  echo "==> Running gunicorn server..."
  gunicorn --bind=${BIND_ADDRESS:-0.0.0.0:8000} --workers=${WORKERS:-3} horas.wsgi
else
  exec "$@"
fi


