from .base import *

SECRET_KEY = get_env_variable("SECRET_KEY")

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []