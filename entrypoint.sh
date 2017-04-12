export AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID:-""}
export AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY:-""}
export AWS_STORAGE_BUCKET_NAME=${AWS_STORAGE_BUCKET_NAME:-""}
export SECRET_KEY=${SECRET_KEY:-"dont-tell-eve"}
export SSO_SECRET_KEY=${SSO_SECRET_KEY:-"dont-tell-eve"}
export HORAS_DEFAULT_TZ=${HORAS_DEFAULT_TZ:-"America/Puerto_Rico"}
export DEFAULT_FROM_EMAIL=${DEFAULT_FROM_EMAIL:-"admin@example.com"}

gunicorn horas.wsgi