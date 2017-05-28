"""
WSGI config for horas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from configurations.wsgi import get_wsgi_application

ENVIRONMENT = os.getenv('ENVIRONMENT', 'DEVELOPMENT').title()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'horas.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', ENVIRONMENT)

application = get_wsgi_application()
