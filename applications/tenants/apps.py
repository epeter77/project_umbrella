# applications/tenants/apps.py

from django.apps import AppConfig

class TenantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.tenants'    # This MUST be the full Python path