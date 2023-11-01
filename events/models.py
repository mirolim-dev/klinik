from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# from local
from departments.models import Department
# Create your models here.

class Curing(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True)
    price = models.DecimalField(max_digits=25, decimal_places=2, default=1.00)
    description = RichTextUploadingField(default="Some Text")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name

    def get_all_curing_regimens(self):
        return self.curingregimen_set.select_related('curing')

class CuringRegimen(models.Model):
    curing = models.ForeignKey(Curing, on_delete=models.CASCADE)
    drug = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    times_in_a_day = models.PositiveBigIntegerField(default=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.drug} | {self.dosage}"
    

class Diagnoz(models.Model):
    pass