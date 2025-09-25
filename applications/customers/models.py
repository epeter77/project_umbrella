# applications/customers/models.py

from django.db import models
from applications.tenants.models import AdminTenant




class Customer(models.Model):
    tenant = models.ForeignKey(AdminTenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name'] # Keep the customer list alphabetized

    def __str__(self):
        return self.name