from django.db import models
from django.core.exceptions import ValidationError
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
        return f"{self.invoice.patient} | {self.amount} | {self.payment_type}"

