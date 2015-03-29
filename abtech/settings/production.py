from .base import *
from pathlib import Path
from .secret import SECRET_KEY

DEBUG = True #False
TEMPLATE_DEBUG = True #False
ALLOWED_HOSTS = []

INSTALLED_APPS += ('website',
                   'django_markdown',
		   'bootstrap3'
                   )

PROJECT_DIR = (Path(__file__) / "../../..").resolve()

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows1.
    # Don't forget to use absolute paths, not relative paths.
    (PROJECT_DIR / "static/").resolve(),
)

TEMPLATE_DIRS = (
    (PROJECT_DIR / "templates/").resolve(),
)

