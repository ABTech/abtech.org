from .base import *
from pathlib import Path

SECRET_KEY = "asdfasdf"

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS += ('website',
                   'django_markdown',
                   'bootstrap3'
                   )

PROJECT_DIR = (Path(__file__) / "../../..").resolve()

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows1.
    # Don't forget to use absolute paths, not relative paths.
    "static/",
)

TEMPLATE_DIRS = (
    "templates/",
)

