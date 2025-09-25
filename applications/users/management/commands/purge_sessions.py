# applications/users/management/commands/purge_sessions.py

from django.db import connection
from django_tenants.utils import tenant_context
from applications.tenants.models import AdminTenant
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Deletes all session data from all tenants to resolve state conflicts.'

    def handle(self, *args, **options):
        # Get all tenants, including the public schema
        all_tenants = AdminTenant.objects.all()
        
        self.stdout.write("--- Starting Session Purge ---")

        for tenant in all_tenants:
            with tenant_context(tenant):
                self.stdout.write(f"-> Truncating sessions for tenant: '{tenant.schema_name}'...", ending='')
                
                # Use the database connection for the current tenant
                with connection.cursor() as cursor:
                    # TRUNCATE is fast and resets any auto-incrementing counters
                    cursor.execute("TRUNCATE TABLE django_session RESTART IDENTITY CASCADE;")
                
                self.stdout.write(self.style.SUCCESS(" DONE"))
        
        self.stdout.write(self.style.SUCCESS("--- Session Purge Complete ---"))