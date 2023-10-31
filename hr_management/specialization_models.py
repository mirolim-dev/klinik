from  django.db import models


class StuffSpecialization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='specializations/stuffs/image/', blank=True)
    craeted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DoctorSpecialization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='specializations/doctors/image/', blank=True)
    craeted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
