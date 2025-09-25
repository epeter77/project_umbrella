# applications/utils/apps.py

from django.apps import AppConfig

class UtilsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.utils' # This MUST be the full path