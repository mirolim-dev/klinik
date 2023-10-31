from django.db import models
from account.models import CustomUser
import random
import string

# from local
from .validators import validate_insurance_fields
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
