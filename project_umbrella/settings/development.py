# development.py

from .base import *
import os

# Development-specific settings
DEBUG = True

# Get the secret key from the .env file for local development
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Add any other development-specific settings here