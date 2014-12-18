from .base import *

SECRET_KEY = get_env_variable("SECRET_KEY")

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS += ('website',
                   'django_medusa')

PROJECT_DIR = os.path.dirname(__file__)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "static/",
)

TEMPLATE_DIRS = (
    "templates",
)

# django_medusa -- Render templates to html
MEDUSA_RENDERER_CLASS = "django_medusa.renderers.DiskStaticSiteRenderer"
MEDUSA_DEPLOY_DIR = os.path.join(
    PROJECT_DIR, '..', "_output"
)

