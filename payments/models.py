from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver

# from local
from hr_management.models import Patient

# Create your models here.
class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    residual_amount = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Partly paid'),
        (3, 'Done'),
        (4, 'Cancelled'),
        (5, 'Expired')
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    description = models.TextField()
    craeted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available_till = models.DateTimeField()

    def __str__(self):
        return f"{self.patient}|{self.total_amount}"
    
    def clean(self):
        super().clean()
        if self.total_amount <= 0:
            raise ValidationError("total amount should be greater then 0")
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.residual_amount = self.total_amount
        super().save(*args, **kwargs)

    def get_all_payments(self):
        return self.payments_set.select_related('invoice')

    def get_string_data_of_status(self)->str:
        return self.STATUS_CHOICES[[self.status-1][1]]


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
        return self.PAYMENT_TYPE_CHOICES[[self.payment_type-1][1]]

    def save(self, *args, **kwargs):
        if self.invoice.status > 2:
            raise ValidationError(f"You can't do payment for this Invoice. Because it is \
                {self.invoice.get_string_data_of_status()}")
    
    def clean(self):
        super().clean()
        if self.invoice.residual_mount < self.amount <= 0:
            raise ValidationError(f"amount shoud be greater then 0 and less then invoice's residual_amount")

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


