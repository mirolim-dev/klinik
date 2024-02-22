from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from datetime import datetime, date

# from warehouse.models import ProductUsage, ProductsCollection, Product
from .models import Invoice, InvoiceService, Payment
from events.consulting_models import DiagnozPatientUsage, ConsultingPatientUsage

@receiver(post_save, sender=DiagnozPatientUsage)
def create_invoice_service_by_diagnoz(sender, instance, **kwargs):
    if not instance.pk:
        patient = instance.patient
        invoice = Invoice.objects.filter(patient=patient, status__in=[1, 2])[0]
        InvoiceService.objects.create(
            content_type=ContentType.objects.get_for_model(instance),
            object_id=instance.id,
            invoice=invoice,
            paid=False,
        )
    
@receiver(post_save, sender=ConsultingPatientUsage)
def create_invoice_service_by_consulting(sender, instance, **kwargs):
    if not instance.pk:
        patient = instance.patient
        invoice = Invoice.objects.filter(patient=patient, status__in=[1, 2])[0]
        InvoiceService.objects.create(
            content_type=ContentType.objects.get_for_model(instance),
            object_id=instance.id,
            invoice=invoice,
            paid=False,
        )


@receiver(post_save, sender=Payment)
def update_invoice_service_status(sender, instance, **kwargs):
    if not instance.pk:
        invoice_service = instance.invoice_service
        if instance.amount >= invoice_service.get_total_amount():
            invoice_service.paid = True
            invoice_service.save()



        