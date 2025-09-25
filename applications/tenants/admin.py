# apps/tenants/admin.py
from django.contrib import admin
from django.contrib import messages
from django.db import IntegrityError
from django_tenants.utils import get_tenant
from .models import AdminTenant, Domain

@admin.register(AdminTenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'schema_name', 'created_on')

    # This is the updated, more robust save_model method
    def save_model(self, request, obj, form, change):
        """
        Catches the IntegrityError and displays a friendly message
        instead of an error page if a duplicate is created.
        """
        try:
            # The default behavior is just to save the object.
            obj.save()
            # If the save is successful, show the success message.
            messages.success(request, f"The Tenant '{obj.name}' was saved successfully. A new database schema named '{obj.schema_name}' has been created.")
        except IntegrityError:
            # If the save fails because of a duplicate, show a warning.
            messages.warning(request, f"A tenant with the schema name '{obj.schema_name}' already exists. No new tenant was created.")

    def has_module_permission(self, request):
        """
        Only show this model in the admin on the public schema.
        """
        return request.tenant.schema_name == 'public'
    
@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')

    def has_module_permission(self, request):
            """
            Only show this model in the admin on the public schema.
            """
            return request.tenant.schema_name == 'public'

