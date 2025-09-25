from django.contrib import admin
from .models import Lease

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'property_address', 'status', 'start_date', 'end_date')
    list_filter = ('status',)
    search_fields = ('customer__name', 'property_address')