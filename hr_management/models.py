from django.db import models
from account.models import CustomUser
import random
import string

# from local
from .validators import validate_insurance_fields
from .specialization_models import StuffSpecialization, DoctorSpecialization
from datetime import datetime, timedelta
from .utils import generate_barcode

from departments.models import Department
# Create your models here.
class Patient(CustomUser):
    date_of_birth = models.DateField()
    insurance_provider = models.CharField(max_length=255, blank=True)
    insurance_policy_number = models.CharField(max_length=100, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        if not self.pk:#works when Patient created
            self.__set_password()
        super().save(*args, **kwargs)
    
    def clean(self) -> None:
        super().clean()
        validate_insurance_fields(self.insurance_provider, self.insurance_policy_number)

    def __set_password(self):
        """Sets random password to CustomUser's password field"""
        password_length = 8
        chars = string.ascii_letters + string.digits
        random_pasword = ''.join(random.choice(chars) for _ in range(password_length)) 
        self.password = random_pasword

    def get_all_service_useages(self):
        pass


class Stuff(CustomUser):
    specialization = models.ForeignKey(StuffSpecialization, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to="stuffs/images/", blank=True)
    working = models.BooleanField(default=True)
    salary = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    CURRENCY_CHOICES = (
        (0, 'UZS'),
        (1, 'USD'),
        (2, 'EUR')
    )
    salary_currency = models.IntegerField(choices=CURRENCY_CHOICES, default=0)
    barcode_data = models.CharField(max_length=100, unique=True, blank=True)
    barcode_file_path = models.CharField(max_length=255, unique=True, blank=True)
    # date_joined = models.DateTimeField(auto_now_add=True)  #already exist in CustomUser
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        """Method is being handled because of barcode_data and 
            barcode_file_path shoul be created automatically"""
        if not self.pk:#checking is object creating or updating
            self.barcode_data = ''.join((string.digits) for _ in range(13))
            self.barcode_file_path = f"media/stuffs/barcodes/{self.first_name}_{self.last_name}.png"
            generate_barcode(self.barcode_data, self.barcode_file_path)
        super().save(*args, **kwargs)

class Doctor(Stuff):
    perofession = models.ForeignKey(DoctorSpecialization, on_delete=models.DO_NOTHING)
    POSITION_CHOICES = (
        (0, "Junior"),
        (1, "Senior"),
        (2, "Consultant"),
        (3, "Surgeon")
    )
    postion = models.IntegerField(choices=POSITION_CHOICES, default=0)

    def __str__(self):
        return super().__str__()

    def save(self, *args, **kwargs):
        """method is Handling because of stuff's specialiation should be set 
            automatically when Doctor has been created"""
        if not self.pk:
            stuff_specialization = StuffSpecialization.objects.get(name='Doctor')
            if not bool(stuff_specialization):
                stuff_specialization = StuffSpecialization.objects.create(name="Doctor")
            self.specialization = stuff_specialization
        super().save(*args, **kwargs)


class AvailableTime(models.Model):
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    WEEK_DAYS = (
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thoursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday")
    )
    week_day = models.IntegerField(choices=WEEK_DAYS, default=1)
    from_time = models.TimeField(default=datetime.now().time())
    __default_time = datetime.now() + timedelta(8) #private fields will not be migrated and it 
                                                   #is not accessable from outside of the model
    to = models.TimeField(default=__default_time.time())
