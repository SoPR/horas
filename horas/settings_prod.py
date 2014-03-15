import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ENV_MIDDLEWARE = ()
ENV_INSTALLED_APPS = ()

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config()
}

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
