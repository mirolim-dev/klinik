from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# from local
from hr_management.models import Doctor, Patient
from .models import Diagnoz
from departments.models import Room

class Consulting(models.Model):
    name = models.CharField(max_length=150, unique=True)
    consultant = models.OneToOneField(Doctor, on_delete=models.CASCADE) #validation required (only consultants or seniors can be choosen)
    price = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    room = models.OneToOneField(Room, on_delete=models.DO_NOTHING)
    description = RichTextUploadingField(default="type description in here")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return self.name

    def get_all_consulting_patient_usages(self):
        return self.consultingpatientusage_set.select_related('patient')
    

class ConsultingPatientUsage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    required_diagnoses = models.ManyToManyField(Diagnoz)
    consulting = models.ForeignKey(Consulting, on_delete=models.DO_NOTHING)
    STATUS_CHOICES = (
        (0, "Cancelled"),
        (1, "Waiting payment"),
        (2, "In que"),
        (3, "Waiting diagnoses"),
        (4, "Done"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    result = RichTextUploadingField()
    advice = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self) -> str:
        return f"{self.patient} | {self.consulting}"
    
    def get_all_diagnoses(self):
        return self.diagnozpatientusage_set.select_related('patient', 'diagnoz', 'consulting_patient_usage')
    
    def get_all_prescriptions(self):
        return self.prescription_set.select_related('consulting_patient_usage')


class DiagnozPatientUsage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnoz = models.ForeignKey(Diagnoz, on_delete=models.CASCADE)
    consulting_patient_usage = models.ForeignKey(ConsultingPatientUsage, on_delete=models.CASCADE, blank=True, null=True)
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


class Prescription(models.Model):
    consulting_patient_usage = models.ForeignKey(ConsultingPatientUsage, on_delete=models.CASCADE)
    drug = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    times_in_a_day = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return f"{self.drug} |dosage: {self.dosage}"
