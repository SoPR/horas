# Horas basic configs
export ENVIRONMENT=${ENVIRONMENT:-"development"}
export SECRET_KEY=${SECRET_KEY:-"dont-tell-eve"}
export SSO_SECRET_KEY=${SSO_SECRET_KEY:-"dont-tell-eve"}
export HORAS_DEFAULT_TZ=${HORAS_DEFAULT_TZ:-"America/New_York"}
export DEFAULT_FROM_EMAIL=${DEFAULT_FROM_EMAIL:-"admin@example.com"}
export DATABASE_URL=${DATABASE_URL:-"postgres://db:5432"}

#
# PSA: DO NOT COMMIT THIS FILE WITH YOUR CREDENTIALS :)
#

# Put your AWS credentials here. 
export AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID:-""}
export AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY:-""}
export AWS_STORAGE_BUCKET_NAME=${AWS_STORAGE_BUCKET_NAME:-""}

# Memcache configuration
export MEMCACHIER_SERVERS=${MEMCACHIER_SERVERS:-""}
export MEMCACHIER_USERNAME=${MEMCACHIER_USERNAME:-""}
export MEMCACHIER_PASSWORD=${MEMCACHIER_PASSWORD:-""}

gunicorn --bind=${BIND_ADDRESS:-0.0.0.0:8000} --workers=${WORKERS:-3} horas.wsgi
