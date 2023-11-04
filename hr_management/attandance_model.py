from django.db import models

# from .specialization_models import DoctorSpecialization
from .models import Staff, AvailableTime
from datetime import datetime

class Attandance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    arrived_at = models.DateTimeField(auto_now_add=True)
    left_at = models.DateTimeField(auto_now=True)
    in_available_day = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.staff} | {self.in_available_day}"

    def save(self, *args, **kwargs):
        avilable_days = AvailableTime.objects.filter(staff=self.staff).values_list('week_day', flat=True)
        if datetime.now().weekday() not in avilable_days:
            self.in_available_day = False
        super().save(*args, **kwargs)

    