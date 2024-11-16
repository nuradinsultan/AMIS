# backend/core/settings/development.py

from .base.py import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES['default'].update({
    'NAME': 'your_development_database_name',
})
