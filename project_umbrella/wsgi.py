"""
WSGI config for project_umbrella project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Check for the 'ENVIRONMENT' variable and default to 'development' if not set
environment = os.environ.get('ENVIRONMENT', 'development')

# Set the settings module based on the environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'project_umbrella.settings.{environment}')

application = get_wsgi_application()
