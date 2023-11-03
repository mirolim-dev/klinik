from django.db import models

# from .specialization_models import DoctorSpecialization
from .models import Staff

class Attandance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    arrived_at = models.DateTimeField(auto_now_add=True)
    left_at = models.DateTimeField(auto_now=True)
    in_available_day = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.staff} | {self.in_available_day}"


