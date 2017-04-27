from .base import *
from pathlib import Path
from .secret import RECAPTCHA_SECRET_KEY, TRACKER_LOGIN, TRACKER_PASSWORD


SECRET_KEY = "foobar"

DEBUG = True

# Show captchas on forms
CAPTCHA = False

# Autofill form entries
AUTOFILL = True

# List of IPs that will receive debug in their request context
INTERNAL_IPS = ['127.0.0.1', 'localhost']

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

INSTALLED_APPS += ('website',
                   'django_markdown',
                   'bootstrap3',
                   'captcha',
                    )

PROJECT_DIR = (Path(__file__) / "../../..").resolve()

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EVENT_EMAIL = "rmaratos@andrew.cmu.edu"
JOIN_EMAIL = "rmaratos@andrew.cmu.edu"

RECAPTCHA_SITE_KEY = '6LdvswQTAAAAAPhSuC25sVceWHEfpTIe3I0PuYnO'

TRACKER = 'https://abtech.andrew.cmu.edu/tracker-staging/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows1.
    # Don't forget to use absolute paths, not relative paths.
    "static/",
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            "templates/",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
            ],
        },
    },
]
