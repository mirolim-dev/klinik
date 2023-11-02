from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# from local
from departments.models import Department, Room
from hr_management.models import Staff, Patient

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
    name = models.CharField(max_length=255, null=True, unique=True)
    price = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    responsible_person = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    room = models.OneToOneField(Room, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name
    

class DiagnoseProductUsage(models.Model):
    diagnoz = models.ForeignKey(Diagnoz, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE) #it comes from warehouse
    amount = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    MEASURE_CHOICES = (
        (1, "MilliGramm"),
        (2, "MilliLiter"),
        (3, "Number of"),
    ) 
    measure = models.IntegerField(choices=MEASURE_CHOICES, default=1)

    def __str__(self) -> str:
        return f"{self.amount} {self.measure}"


class DiagnosePatientUsage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnoz = models.ForeignKey(Diagnoz, on_delete=models.CASCADE)
    # consulting_patient_usage = models.ForeignKey(ConsultingPatientUsage, on_delete=models.CASCADE, null=True)
    STATUS_CHOICES = (
        (1, "Waiting payment"),
        (2, "In que"),
        (3, "Done"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    result = RichTextUploadingField(default="Nothing in here")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.patient.__str__()} | {self.diagnoz.name} | {self.status}"
    