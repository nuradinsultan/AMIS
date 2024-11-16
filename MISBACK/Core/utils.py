# backend/core/utils.py
import os
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

def get_env_variable(var_name):
    """
    Get the environment variable or return an exception.
    """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f"Set the {var_name} environment variable"
        raise ImproperlyConfigured(error_msg)


def send_welcome_email(user):
    subject = "Welcome to Our Medical Information System"
    message = f"Hi {user.first_name},\n\nThank you for registering. We're glad to have you!"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])


def format_date(date, format='%Y-%m-%d'):
    """
    Format a datetime object into a string.
    """
    if not isinstance(date, datetime):
        raise ValueError("The provided value must be a datetime object")
    return date.strftime(format)
