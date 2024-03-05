from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver

from .consulting_models import ConsultingPatientUsage, DiagnozPatientUsage
from payments.models import Invoice, InvoiceService
from django.contrib.contenttypes.models import ContentType
from datetime import datetime, date, timedelta


@receiver(m2m_changed, sender=ConsultingPatientUsage.required_diagnoses.through)
def create_diagnoz_patient_usage_by_consulting(sender, instance, action, **kwargs):
    if instance.status in [1, 2, 3] and action == "post_add":
        if instance.status == 1:
            patient = instance.patient
            invoice = Invoice.objects.filter(patient=patient, status__in=[1, 2]) 
            if not invoice:
                invoice = Invoice.objects.create(patient=patient,
                                                description="any description",
                                                available_till=(datetime.now()+timedelta(days=30))
                                                )
            else:
                invoice = invoice[0]
            InvoiceService.objects.create(
                    content_type=ContentType.objects.get_for_model(instance),
                    object_id=instance.id,
                    invoice=invoice,
                    paid=False,
                )
        required_diagnoses = instance.required_diagnoses.all()

        for diagnose in required_diagnoses:
            DiagnozPatientUsage.objects.create(
            patient=instance.patient,
            diagnoz=diagnose,
            consulting_patient_usage=instance,
            status=1,
        ) 
 

@receiver(post_save, sender=DiagnozPatientUsage)
def create_invoice_service_by_diagnoz(sender, instance, **kwargs):
    patient = instance.patient
    invoice = Invoice.objects.filter(patient=patient, status__in=[1, 2])[0]
    InvoiceService.objects.create(
        content_type=ContentType.objects.get_for_model(instance),
        object_id=instance.id,
        invoice=invoice,
        paid=False,
    )