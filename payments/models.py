from django.db import models

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
    available_till = models.DateTimeField(auto_now=True)
    available_till = models.DateTimeField()

    def __str__(self):
        return f"{self.patient}|{self.total_amount}"