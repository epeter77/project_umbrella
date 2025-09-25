# apps/utils/context_processors.py
from django.conf import settings
from django_tenants.utils import get_tenant

def tenant_context(request):
    """
    Dynamically overrides Jazzmin's settings based on the current tenant,
    providing custom branding for each tenant's admin site.
    """
    # Start with a copy of the default JAZZMIN_SETTINGS
    jazzmin_settings = settings.JAZZMIN_SETTINGS.copy()

    # Get the current tenant from the request
    tenant = get_tenant(request)

    # Check if a specific tenant is active (not the public schema)
    if tenant and tenant.schema_name != 'public':
        # Override settings with the tenant's branding if they exist
        if tenant.branding_logo:
            jazzmin_settings['site_logo'] = tenant.branding_logo.url
        if tenant.branding_site_title:
            jazzmin_settings['site_title'] = tenant.branding_site_title
        if tenant.branding_site_header:
            jazzmin_settings['site_header'] = tenant.branding_site_header
        if tenant.branding_welcome_sign:
            jazzmin_settings['welcome_sign'] = tenant.branding_welcome_sign

    # Return the final settings dictionary for Jazzmin to use
    return {'jazzmin_settings': jazzmin_settings}