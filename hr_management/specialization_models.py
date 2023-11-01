from  django.db import models


class StaffSpecialization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='specializations/staffs/image/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DoctorSpecialization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='specializations/doctors/image/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
