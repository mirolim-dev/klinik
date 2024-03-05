from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from datetime import datetime, date
from decimal import Decimal

# from warehouse.models import ProductUsage, ProductsCollection, Product
from .models import Invoice, InvoiceService, Payment
from events.consulting_models import DiagnozPatientUsage, ConsultingPatientUsage

@receiver(post_save, sender=InvoiceService)
def update_invoice_amount(sender, instance, **kwargs):
    invoice = instance.invoice
    # print(f"Type invoice total amount: {type(invoice.total_amount)} \nType of service amount: {instance.get_total_amount()}")
    invoice.total_amount = Decimal(invoice.total_amount) + instance.get_total_amount()
    invoice.residual_amount = Decimal(invoice.residual_amount) + instance.get_total_amount()
    invoice.save()

@receiver(post_save, sender=Payment)
def update_invoice_service_status(sender, instance, **kwargs):
    if not instance.pk:
        invoice_service = instance.invoice_service
        if instance.amount >= invoice_service.get_total_amount():
            invoice_service.paid = True
            invoice_service.save()



        