# apps/users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User

# Unregister the original Group admin
admin.site.unregister(Group)

# Create a new Group admin that is tenant-aware
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        """
        Only show this model in the admin on the public schema.
        """
        return request.tenant.schema_name == 'public'

# Re-register our custom User admin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Tenant Access', {'fields': ('tenants',)}),
    )
    filter_horizontal = ('tenants',)

    def has_module_permission(self, request):
        """
        Only show this model in the admin on the public schema.
        """
        return request.tenant.schema_name == 'public'