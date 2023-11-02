from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# from local
from departments.models import Department, Room
from hr_management.models import Staff, Patient
from hr_management.validators import validate_staff_is_vorking
from .validators import validate_diagnoz
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
    responsible_person = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True,
                validators=[validate_staff_is_vorking])
    room = models.OneToOneField(Room, on_delete=models.CASCADE, null=True)
    STATUS_CHOICES = (
        (0, "Inactive"),
        (1, "Active"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Diagnoses'
    

class DiagnozProductUsage(models.Model):
    diagnoz = models.ForeignKey(Diagnoz, on_delete=models.CASCADE, validators=[validate_diagnoz])
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



    