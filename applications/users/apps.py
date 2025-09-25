# applications/users/apps.py

from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.users'

    def ready(self):
        # This line is crucial for connecting the signals.
        import applications.users.signals