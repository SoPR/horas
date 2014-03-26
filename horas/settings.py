"""
Django settings for horas project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Current environment, defaults to development
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')

APPNAME = 'horas'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
SSO_SECRET_KEY = os.environ.get('SSO_SECRET_KEY')

DISCOURSE_SSO_REDIRECT_URL='http://comunidad.1hora.org/session/sso_login?'

ALLOWED_HOSTS = ['localhost', 'unahora.herokuapp.com']

SITE_ID = 1

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third-party
    'south',
    'django_extensions',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.persona',
    'taggit',
    'notification',
    'cities_light',
    'gunicorn',
    'storages',
    'collectfast',
    'djangosecure',
    'bootstrap3',

    # Local apps
    'apps.core',
    'apps.profiles',
    'apps.search',
    'apps.meetings',
    'apps.sso',
)

MIDDLEWARE_CLASSES = (
    'djangosecure.middleware.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.core.middleware.TimezoneMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',

    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

# Custom user model
AUTH_USER_MODEL = 'profiles.User'
LOGIN_URL = '/accounts/login/'

# allauth settings
ACCOUNT_ADAPTER = 'apps.profiles.adapters.AccountAdapter'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Horas] '
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_URL
ACCOUNT_USERNAME_BLACKLIST = ['admin']
ACCOUNT_SIGNUP_FORM_CLASS = 'apps.profiles.forms.SignupForm'

ROOT_URLCONF = 'horas.urls'

WSGI_APPLICATION = 'horas.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
HORAS_DEFAULT_TZ = os.environ.get('HORAS_DEFAULT_TZ')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
BRUNCH_DIR = os.path.join(BASE_DIR, 'static', 'src')

DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'

AWS_PRELOAD_METADATA = True
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

STATIC_URL = '/static/dist/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'public')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'dist'),
)


# Load environment specific settings
if ENVIRONMENT == 'production':
    from settings_prod import *
else:
    from settings_dev import *

MIDDLEWARE_CLASSES = ENV_MIDDLEWARE + MIDDLEWARE_CLASSES
INSTALLED_APPS = ENV_INSTALLED_APPS + INSTALLED_APPS
