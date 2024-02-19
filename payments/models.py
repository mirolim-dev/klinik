from django.db import models
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# from local
from hr_management.models import Patient
from departments.meals_models import Admission
from events.consulting_models import DiagnozPatientUsage, ConsultingPatientUsage
from .validators import (
    validate_invoice_to_create,
    )
# Create your models here.
class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    residual_amount = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    discount = models.PositiveBigIntegerField(default=0) #by presentage
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Partly paid'),
        (3, 'Done'),
        (4, 'Cancelled'),
        (5, 'Expired')
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available_till = models.DateTimeField()

    def __str__(self):
        return f"{self.patient}|{self.total_amount}"
    
    def clean(self):
        super().clean()
        if self.total_amount <= 0:
            raise ValidationError("total amount should be greater then 0")
        if self.pk:
            validate_invoice_to_update(self.pk, self.status)
    def save(self, *args, **kwargs):
        if not self.pk:
            validate_invoice_to_create(self.patient)
            self.residual_amount = self.total_amount

        super().save(*args, **kwargs)

    def get_all_payments(self):
        return self.payments_set.select_related('invoice')

    def get_string_data_of_status(self)->str:
        return self.STATUS_CHOICES[self.status-1][1]

    def get_all_services(self):
        return self.invoiceservice_set.prefetch_related('service', 'invoice')

    def get_total_amount(self):
        admission_instance = Admission.objects.first() or None
        diagnoz_patient_usage_instance = DiagnozPatientUsage.objects.first() or None
        consulting_patient_usage_instance = ConsultingPatientUsage.objects.first() or None
        admission = self.invoiceservice_set.filter(content_type=ContentType.objects.get_for_model(admission_instance))[0]\
            if admission_instance else None
        diagnoz_ids = admission.diagnoses.values_list('id', flat=True) if admission else []
        diagnoz_patient_usages = self.invoiceservice_set.filter(content_type=ContentType.objects.get_for_model(diagnoz_patient_usage_instance)).exclude(object_id__in=diagnoz_ids)\
            if diagnoz_patient_usage_instance else None
        consulting_patient_usages = self.invoiceservice_set.filter(content_type=ContentType.objects.get_for_model(consulting_patient_usage_instance))\
            if consulting_patient_usage_instance else None

        admission_total_amount = admission.calculate_total_price() if admission else Decimal('0.00')
        diagnoz_patient_usages_total_amount = Decimal('0.00')
        if diagnoz_patient_usages:
            diagnoz_patient_usages_total_amount = diagnoz_patient_usages.aggregate(total_price=ExpressionWrapper(Sum('diagnoz__price'), output_field=DecimalField()))['total_price']
        consulting_patient_usages_total_amount = Decimal('0.00')
        if consulting_patient_usages:
            consulting_patient_usages_total_amount = consulting_patient_usages.aggregate(total_price=ExpressionWrapper(Sum('consulting__price'), \
                output_field=DecimalField()))['total_price']
        total_amount = admission_total_amount + diagnoz_patient_usages_total_amount + consulting_patient_usages_total_amount
        return total_amount

    def calculate_total_amount_after_discount(self):
        total_amount = self.get_total_amount()
        result_amount = total_amount - Decimal(total_amount/self.discount)
        return result_amount
        

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    PAYMENT_TYPE_CHOICES = (
        (1, 'Cash'),
        (2, 'Plastic Card'),
        (3, 'Insurance'),
    )
    payment_type = models.IntegerField(choices=PAYMENT_TYPE_CHOICES, default=1)
    amount = models.DecimalField(max_digits=25, decimal_places=2, default=1.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.invoice.patient} | {self.amount} | {self.get_string_data_of_payment_type()}"
    
    def get_string_data_of_payment_type(self)->str:
        print(f"Payment Type: {self.payment_type}")
        return self.PAYMENT_TYPE_CHOICES[self.payment_type-1][1]

    def clean(self):
        super().clean()
        if self.invoice.residual_amount < self.amount <= 0:
            raise ValidationError(f"amount should be greater then 0 and less then invoice's residual_amount")
        if self.invoice.status > 2:
            raise ValidationError(f"You can't do payment for this Invoice. Because it is {self.invoice.get_string_data_of_status()}")


class InvoiceService(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    service = GenericForeignKey('content_type', 'object_id')
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)   
    
    class Meta:
        unique_together = ('content_type', 'object_id', 'invoice')

    def __str__(self):
        return f"{self.service} | {self.invoice}"


@receiver(post_save, sender=Payment)
def update_invoice_status(sender, instance, **kwargs):
    invoice = instance.invoice
    total_payments = invoice.payment_set.aggregate(total_amount=models.Sum('amount'))['total_amount']
    if total_payments is None:
        total_payments = 0

    if total_payments == invoice.total_amount:
        invoice.status = 3  # Set status to 'Done' when total payments match the total amount
    elif total_payments > 0:
        invoice.status = 2  # Set status to 'Partly paid' when there are some payments

    invoice.residual_amount -= instance.amount
    invoice.save()


def validate_invoice_to_update(object_pk:int, new_status:int):
    """
    This validation:
    1) Doesn't allow to change back Invoices status to Pending
    2) Doesn't allow to complete(changing status to Done) before residual_amount = 0
    """
    invoice = Invoice.objects.get(pk=object_pk)
    old_status = invoice.status
    if old_status != new_status:
        if new_status == 1:
            raise ValidationError(f"Changing invoice's status to Pending is not allowed.")
        elif new_status == 3 and invoice.residual_amount > 0:
            raise ValidationError(f"This invoice has {invoice.residual_amount}. Patient should pay this amount first to complete Invoice")
