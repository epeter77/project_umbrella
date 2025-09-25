# applications/users/signals.py

from django.contrib.auth import user_logged_in
from django.dispatch import receiver
from django_tenants.utils import schema_context
from .models import User 

#@receiver(user_logged_in)
#def on_user_logged_in(sender, request, user, **kwargs):
#    """
#    When a user logs in, this signal re-fetches the user object from the
#    public schema to ensure the permission cache is correctly populated
#    across tenant contexts.
#    """
#    # Force the following code to run within the 'public' schema
#    with schema_context('public'):
#        try:
#            # Re-fetch a "fresh" user object from the database 
#            fresh_user = User.objects.get(pk=user.pk)
#            
#            # This is the standard way to force a permissions refresh.
#            # This call will now succeed because the backend is fixed.
#            _ = fresh_user.get_all_permissions()
#
#        except User.DoesNotExist:
#            # This case is unlikely but good to handle.
#            pass