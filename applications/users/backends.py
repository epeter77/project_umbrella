# applications/users/backends.py

from django.contrib.auth.backends import ModelBackend
from django_tenants.utils import get_tenant
from .models import User

class TenantAwareBackend(ModelBackend):
    """
    A self-contained, tenant-aware authentication backend with
    corrected business logic and diagnostic logging.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        print("\n--- [DEBUG] New Login Attempt ---")
        
        tenant = get_tenant(request)
        print(f"-> Tenant: '{tenant.name}' ({tenant.schema_name})")
        
        try:
            user = User.objects.get(username__iexact=username)
            print(f"-> User Found: '{user.username}' (PK: {user.pk})")
        except User.DoesNotExist:
            print("-> User Found: No")
            print("--- [DEBUG] Outcome: FAILED ---\n")
            return None

        # --- Check 1: Password ---
        if not user.check_password(password):
            print("-> Password Check: FAILED")
            print("--- [DEBUG] Outcome: FAILED ---\n")
            return None
        print("-> Password Check: PASSED")

        # --- Check 2: User is Active ---
        if not self.user_can_authenticate(user):
            print("-> Active Check: FAILED")
            print("--- [DEBUG] Outcome: FAILED ---\n")
            return None
        print("-> Active Check: PASSED")

        # --- NEW LOGIC ---
        # Rule: To log into the main Umbrella Admin (public schema), user MUST be staff.
        if tenant.schema_name == 'public':
            if not user.is_staff:
                print(f"-> Staff Check for Public Site: FAILED (user.is_staff is {user.is_staff})")
                print("--- [DEBUG] Outcome: FAILED ---\n")
                return None
            print("-> Staff Check for Public Site: PASSED")
            print("--- [DEBUG] Outcome: SUCCESS ---\n")
            return user

        # Rule: To log into a client tenant, user must be assigned to that tenant.
        else:
            print("-> Site Type: Client Tenant (Staff status not required for login)")
            user_tenants = list(user.tenants.all())
            print(f"-> User is assigned to tenants: {[t.name for t in user_tenants]}")
            if tenant not in user_tenants:
                print(f"-> Tenant Membership Check: FAILED ('{tenant.name}' is not in user's tenant list)")
                print("--- [DEBUG] Outcome: FAILED ---\n")
                return None
            
            print(f"-> Tenant Membership Check: PASSED")
            print("--- [DEBUG] Outcome: SUCCESS ---\n")
            return user