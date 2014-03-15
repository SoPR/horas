import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

# django-secure settings
PROTOCOL = 'https'
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ENV_MIDDLEWARE = ()
ENV_INSTALLED_APPS = ()

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config()
}

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
