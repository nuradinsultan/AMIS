# backend/core/settings/production.py

from .base.py import *

DEBUG = False

ALLOWED_HOSTS = ['your.production.domain']

DATABASES['default'].update({
    'NAME': 'your_production_database_name',
    'USER': 'your_production_database_user',
    'PASSWORD': 'your_production_database_password',
})
