from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from datetime import datetime, date

# from warehouse.models import ProductUsage, ProductsCollection, Product
from payments.models import Invoice, InvoiceService
from .meals_models import Admission

@receiver(pre_save, sender=Admission)
def update_invoice_amount_by_admission(sender, instance, **kwargs):
    patient = instance.patient
    admission_total_price = instance.calculate_total_price()
    invoice = Invoice.objects.filter(status__in=[1, 2])
    if invoice.count() == 0:
        invoice = Invoice.objects.create(patient=patient, total_amount=admission_total_price,
        description="any description",
        available_till=(datetime.now()+date(30)))
    else:
        invoice = invoice[0]
        invoice.total_amount += admission_total_price
        invoice.residual_amount += admission_total_price
        invoice.save()


@receiver(post_save, sender=Admission)
def create_invoice_service_by_admission(sender, instance, **kwargs):
    patient = instance.patient
    invoice = Invoice.objects.filter(patient=patient, status__in=[1, 2])[0]
    InvoiceService.objects.create(
        content_type=ContentType.objects.get_for_model(instance),
        object_id=instance.id,
        invoice=invoice
    )