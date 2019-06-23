import os

from configurations import Configuration, values
from django.utils.translation import gettext_lazy as _


class Common(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    ENVIRONMENT = values.Value(environ_prefix=None, default="development")

    APPNAME = "horas"

    DEBUG = False

    SECRET_KEY = values.SecretValue(environ_prefix=None)
    SSO_SECRET_KEY = values.SecretValue(environ_prefix=None)

    DISCOURSE_SSO_REDIRECT_URL = "http://comunidad.1hora.org/session/sso_login?"

    ALLOWED_HOSTS = ["unahora.herokuapp.com", "1hora.org"]

    SITE_ID = 1

    DATE_FORMAT = "D, F j, Y"

    # Application definition
    INSTALLED_APPS = (
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        # Third-party
        "django_extensions",
        "allauth",
        "allauth.account",
        "allauth.socialaccount",
        "allauth.socialaccount.providers.twitter",
        "allauth.socialaccount.providers.facebook",
        "allauth.socialaccount.providers.google",
        "taggit",
        "pinax.notifications",
        "gunicorn",
        "storages",
        "collectfast",
        "bootstrap3",
        "markdown_deux",
        "django_fsm_log",
        # Local apps
        "apps.core",
        "apps.profiles",
        "apps.search",
        "apps.meetings",
        "apps.stats",
        "apps.sso",
        "apps.comments",
    )

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.locale.LocaleMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "apps.core.middleware.TimezoneMiddleware",
        "apps.core.middleware.EnsureCompleteProfileMiddleware",
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "templates")],
            "APP_DIRS": True,
            "OPTIONS": {
                "debug": DEBUG,
                "context_processors": [
                    "django.contrib.auth.context_processors.auth",
                    "django.template.context_processors.debug",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                    "django.template.context_processors.tz",
                    "django.contrib.messages.context_processors.messages",
                    "django.template.context_processors.request",
                ],
            },
        }
    ]

    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    )

    # Custom user model
    AUTH_USER_MODEL = "profiles.User"
    LOGIN_URL = "/accounts/login/"

    # allauth settings
    ACCOUNT_ADAPTER = "apps.profiles.adapters.AccountAdapter"
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
    ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Horas] "
    ACCOUNT_LOGOUT_ON_GET = True
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False
    ACCOUNT_CONFIRM_EMAIL_ON_GET = True
    ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_URL
    ACCOUNT_USERNAME_BLACKLIST = ["admin"]
    ACCOUNT_SIGNUP_FORM_CLASS = "apps.profiles.forms.SignupForm"

    ROOT_URLCONF = "horas.urls"

    WSGI_APPLICATION = "horas.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(
        "sqlite://{}".format(os.path.join(BASE_DIR, "db.sqlite3"))
    )

    # Internationalization
    # https://docs.djangoproject.com/en/dev/topics/i18n/
    LANGUAGE_CODE = "es"

    LOCALE_PATHS = [os.path.join(os.path.dirname(__file__), "locale")]
    LANGUAGES = (("es", _("Spanish")), ("en", _("English")))

    TIME_ZONE = "UTC"
    HORAS_DEFAULT_TZ = os.environ.get("HORAS_DEFAULT_TZ")

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"

    AWS_PRELOAD_METADATA = True
    AWS_ACCESS_KEY_ID = values.Value(environ_prefix=None)
    AWS_SECRET_ACCESS_KEY = values.Value(environ_prefix=None)
    AWS_STORAGE_BUCKET_NAME = values.Value(environ_prefix=None)

    STATIC_URL = "/static/public/"

    STATIC_ROOT = os.path.join(BASE_DIR, "static")

    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static", "public"),)

    ANNOUNCE_TEST_MODE = False


class Development(Common):
    DEBUG = True

    PROTOCOL = "http"

    Common.ALLOWED_HOSTS += ["127.0.0.1", "localhost", "0.0.0.0"]

    INSTALLED_APPS = Common.INSTALLED_APPS + ("debug_toolbar",)

    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

    # Dummy cache for development
    CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}


class Testing(Common):
    LOGGING_CONFIG = None

    PROTOCOL = "http"

    # Remove social logins
    INSTALLED_APPS = [
        a for a in Common.INSTALLED_APPS if not a.startswith("allauth.socialaccount.")
    ]

    # Email Settings
    EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"

    # Debug Toolbar
    DEBUG_TOOLBAR_PATCH_SETTINGS = False

    # Dummy cache for development
    CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}

    ANNOUNCE_TEST_MODE = True


class Production(Common):
    INSTALLED_APPS = Common.INSTALLED_APPS + ("raven.contrib.django.raven_compat",)

    # django-secure settings
    PROTOCOL = "https"
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_FRAME_DENY = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    STATICFILES_STORAGE = "storages.backends.s3boto.S3BotoStorage"
    STATIC_URL = "https://d2kmfhumajdz54.cloudfront.net/"

    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = values.Value()
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.SecretValue()
    EMAIL_PORT = values.IntegerValue()
    EMAIL_USE_TLS = values.BooleanValue(True)
    DEFAULT_FROM_EMAIL = values.Value(environ_prefix=None)

    # cached sessions
    SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

    # Memcache setup
    os.environ["MEMCACHE_SERVERS"] = os.environ.get("MEMCACHIER_SERVERS", "").replace(
        ",", ";"
    )
    os.environ["MEMCACHE_USERNAME"] = os.environ.get("MEMCACHIER_USERNAME", "")
    os.environ["MEMCACHE_PASSWORD"] = os.environ.get("MEMCACHIER_PASSWORD", "")

    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.memcached.PyLibMCCache",
            "LOCATION": "127.0.0.1:11211",
            "OPTIONS": {"binary": True},
        }
    }
