# from django.db import models

# # from local
# from hr_management.models import Doctor
# from hr_management.validators import validate_stuff_is_vorking
# from .models import Department

# class HeadDoctor(models.Model):
#     doctor = models.OneToOneField(Doctor, on_delete=models.DO_NOTHING, 
#                                 validators=[validate_stuff_is_vorking])
#     department = models.OneToOneField(Department, on_delete=models.DO_NOTHING)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return f"{self.doctor.__str__()} | {self.department.__str__()}"