# project_umbrella/middleware.py

from django.conf import settings
from copy import deepcopy

class TenantBrandingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Add a print statement to confirm the middleware is running
        print(f"\n--- [DEBUG] Middleware is running for path: {request.path} ---")

        tenant = request.tenant
        print(f"--- [DEBUG] Current tenant is: {tenant.name} ({tenant.schema_name}) ---")

        # Check if we are on a specific tenant's domain
        if tenant.schema_name != 'public':
            print(f"--- [DEBUG] Entering branding logic for tenant: {tenant.name} ---")
            
            jazzmin_settings = deepcopy(settings.JAZZMIN_SETTINGS)
            
            # Print the raw branding values from the database model
            print(f"--- [DEBUG] Raw logo object from DB: {tenant.branding_logo}")
            print(f"--- [DEBUG] Raw site_title from DB: '{tenant.branding_site_title}'")
            print(f"--- [DEBUG] Raw welcome_sign from DB: '{tenant.branding_welcome_sign}'")
            
            # Override settings with the tenant's branding
            if tenant.branding_site_title:
                jazzmin_settings['site_title'] = tenant.branding_site_title
            
            if tenant.branding_site_header:
                jazzmin_settings['site_header'] = tenant.branding_site_header
            
            if tenant.branding_welcome_sign:
                jazzmin_settings['welcome_sign'] = tenant.branding_welcome_sign
            
            if tenant.branding_logo and hasattr(tenant.branding_logo, 'url'):
                print(f"--- [DEBUG] Logo URL found: {tenant.branding_logo.url}")
                jazzmin_settings['site_logo'] = tenant.branding_logo.url
            else:
                print("--- [DEBUG] No logo or logo URL found for this tenant.")

            # Attach the customized settings to the request
            request.jazzmin_settings = jazzmin_settings
            
            # Print the final values being used for the template
            print(f"--- [DEBUG] Final 'site_logo' being used: {jazzmin_settings.get('site_logo')} ---")
            print(f"--- [DEBUG] Final 'site_title' being used: {jazzmin_settings.get('site_title')} ---\n")

        response = self.get_response(request)
        return response