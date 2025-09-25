# apps/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from applications.tenants.models import AdminTenant

class User(AbstractUser):
    class Role(models.TextChoices):
        UMBRELLA_ADMIN = "UMBRELLA_ADMIN", "Umbrella Admin"
        ADMIN_USER = "ADMIN_USER", "Admin User"
        CUSTOMER_USER = "CUSTOMER_USER", "Customer User"

    base_role = Role.UMBRELLA_ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    tenants = models.ManyToManyField(
        AdminTenant,
        blank=True,
        help_text="The tenants this user has access to."
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)