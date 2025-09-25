# apps/tenants/models.py
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class AdminTenant(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True
    # --- BRANDING FIELDS ---
    branding_logo = models.ImageField(upload_to='tenant_logos/', blank=True, null=True)
    branding_site_title = models.CharField(max_length=100, blank=True)
    branding_site_header = models.CharField(max_length=100, blank=True)
    branding_welcome_sign = models.CharField(max_length=255, blank=True)

    # Automatically set the schema name from the tenant name
    auto_create_schema = True
    
    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass

# We will add the CustomerTenant model here in a later phase.
# For now, we are focusing on the top-level Admin Tenants.

