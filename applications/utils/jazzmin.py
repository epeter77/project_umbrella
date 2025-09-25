# applications/utils/jazzmin.py

from django.conf import settings
from copy import deepcopy

def get_jazzmin_settings(request):
    """
    Dynamically sets Jazzmin settings based on the current tenant.
    This function is called by Jazzmin for every request.
    """
    # Start with a copy of the default settings
    jazzmin_settings = deepcopy(settings.JAZZMIN_SETTINGS)

    # If there's no tenant (e.g., on the public schema landing page),
    # or if the tenant is the public one, return the default settings.
    if not hasattr(request, 'tenant') or request.tenant.schema_name == 'public':
        return jazzmin_settings

    tenant = request.tenant

    # Override settings with the tenant's branding if they exist
    if tenant.branding_site_title:
        jazzmin_settings['site_title'] = tenant.branding_site_title
    
    if tenant.branding_site_header:
        jazzmin_settings['site_header'] = tenant.branding_site_header
    
    if tenant.branding_welcome_sign:
        jazzmin_settings['welcome_sign'] = tenant.branding_welcome_sign
    
    # Check for the logo URL specifically
    if tenant.branding_logo and hasattr(tenant.branding_logo, 'url'):
        jazzmin_settings['site_logo'] = tenant.branding_logo.url
        # Also set the login logo, which is often desired
        jazzmin_settings['login_logo'] = tenant.branding_logo.url

    return jazzmin_settings