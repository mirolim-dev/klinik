from django.db import models

# from local
# from hr_management.doctor_models import Doctor
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    building = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



