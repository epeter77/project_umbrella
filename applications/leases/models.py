# applications/leases/models.py

from django.db import models
from applications.customers.models import Customer
from django.utils.translation import gettext_lazy as _

class Lease(models.Model):
    """
    Represents a rental lease agreement for a customer.
    This is a tenant-specific model.
    """
    class LeaseStatus(models.TextChoices):
        ACTIVE = 'ACTIVE', _('Active')
        EXPIRED = 'EXPIRED', _('Expired')
        PENDING = 'PENDING', _('Pending')
        TERMINATED = 'TERMINATED', _('Terminated')

    # --- Core Lease Details ---
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE, 
        related_name='leases',
        help_text="The customer who holds this lease."
    )
    property_address = models.TextField(
        help_text="The full address of the leased property."
    )
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text="The monthly rent amount."
    )
    status = models.CharField(
        max_length=20,
        choices=LeaseStatus.choices,
        default=LeaseStatus.PENDING
    )

    # --- Timestamps ---
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date'] # Show newest leases first by default

    def __str__(self):
        return f"Lease for {self.customer.name} ({self.get_status_display()})"