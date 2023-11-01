from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# from local
from .models import Department, Bed
from hr_management.models import Patient
from events.models import Diagnoz, Curing

class Meal(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class MealAmount(models.Model):
    meal = models.OneToOneField(Meal, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    MEASURE_CHOICES = (
        (1, "Gramm"),
        (2, "Milliliter"),
    )
    measure = models.IntegerField(choices=MEASURE_CHOICES, default=1)

    def  __str__(self) -> str:
        return f"{self.meal.name} | {self.amount} {self.measure}"
    

class MealTime(models.Model):
    name = models.CharField(max_length=255, default="Breakfast")
    amount = models.ForeignKey(MealAmount, on_delete=models.CASCADE)
    department = models.ManyToManyField(Department)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    time = models.TimeField()

    class Meta:
        ordering = ['-time']


class Admission(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    bed = models.ForeignKey(Bed, on_delete=models.DO_NOTHING)
    diagnoses = models.ManyToManyField(Diagnoz, blank=True)
    meals = models.ManyToManyField(MealTime, blank=True)
    curings = models.ManyToManyField(Curing)
    starts_at = models.DateTimeField(default=timezone.now)
    finishes_at = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = (
        (1, "Pending"),
        (2, "In process"),
        (3, "Done"),
        (4, "Cancelled"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    description = RichTextUploadingField()

    class Meta:
        ordering = ['starts_at', 'status']

    def __str__(self):
        return f"{self.patient.__str__()} | {self.bed.__str__()}"
    
    

