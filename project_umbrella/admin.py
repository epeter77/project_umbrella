# project_umbrella/admin.py
from django.contrib import admin
from django.contrib.sites.models import Site

# Unregister the original Site admin
admin.site.unregister(Site)

# Create a new Site admin that is tenant-aware
@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        """
        Only show this model in the admin on the public schema.
        """
        return request.tenant.schema_name == 'public'