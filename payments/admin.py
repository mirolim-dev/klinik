from django.contrib import admin

from .models import Payment, Invoice
# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'total_amount', 'residual_amount', 
                    'status', 'created_at', 'updated_at', 'available_till']
    list_filter = ['status']
    search_fields = ['id', 'patient__first_name', 'patient__last_name',
                    'total_amount', 'created_at', 'available_till']
admin.site.register(Invoice, InvoiceAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice', 'payment_type', 'amount', 'created_at']
    list_filter = ['payment_type']
    search_fields = ['id', 'invoice__patient__first_name', 'invoice__patient__last_name', 'amount', 'created_at']
admin.site.register(Payment, PaymentAdmin)

