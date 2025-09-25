# project_umbrella/debug_middleware.py

from django_tenants.utils import get_tenant

class SessionDebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # --- This part runs on the INCOMING request ---
        tenant = get_tenant(request)
        print("\n--- [MIDDLEWARE] Inspecting Request ---")
        print(f"-> Path: {request.method} {request.path}")
        print(f"-> Tenant: {tenant.name} ({tenant.schema_name})")
        
        if request.user.is_authenticated:
            print(f"-> Session User: '{request.user.username}' (Authenticated)")
        else:
            print("-> Session User: AnonymousUser (Not Authenticated)")
        print("--------------------------------------")

        # Get the response from the view
        response = self.get_response(request)

        # --- This new part runs on the OUTGOING response ---
        print("\n--- [MIDDLEWARE] Inspecting Response ---")
        print(f"<- Path: {request.method} {request.path}")
        print(f"<- Status Code: {response.status_code}")

        # Check if the 'Set-Cookie' header for the session is present
        if 'Set-Cookie' in response.headers:
            cookie_header = response.headers['Set-Cookie']
            if 'sessionid' in cookie_header:
                print(f"<- Set-Cookie Header: FOUND sessionid -> {cookie_header}")
            else:
                print(f"<- Set-Cookie Header: FOUND, but no sessionid -> {cookie_header}")
        else:
            print("<- Set-Cookie Header: NOT FOUND")
        print("----------------------------------------")

        return response