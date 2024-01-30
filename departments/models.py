from django.db import models
from django.core.exceptions import ValidationError

# from hr_management.models import Doctor
# from warehouse.models import Product, MeasureChoices
# from local
# from hr_management.doctor_models import Doctor
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    building = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_all_rooms(self):
        return self.room_set.select_related('department')

    def get_all_active_staffs(self):
        return self.staff_department.filter(working=True).select_related('specialization')
            
    def get_all_active_doctors(self):
        return self.staff_department.filter(working=True, doctor__isnull=False).select_related('specialization')
            

    def get_head_doctor(self):
        head_doctor = self.staff_department.filter(working=True, \
            doctor__isnull=False, doctor__position=4).select_related('specialization').first() or None
        # (4, "Head Doctor"),
        return head_doctor

    def get_all_beds(self):
        return self.room_set.filter(bed__isnull=False)

    def get_all_department_storages(self):
        return self.departmentstorage_set.select_related('department', 'room')

    def get_all_admissions(self):
        return self.admission_set.select_related('department', 'patient', 'bed')

    def get_all_patients(self):
        admissions = self.get_all_admissions()
        patients = tuple(set(admission.patinent for admission in admissions))
        return patients 


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True, default="Room 5-45A")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return self.name

    def get_all_stuffs(self):
        return self.roomstuff_set.select_related('room')


class RoomStuff(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Bed(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    # department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    number_of_beds = models.PositiveBigIntegerField(default=1)
    price_for_one_day = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    STATUS_CHOICES = (
        (0, "Available"),
        (1, "Occupied"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        ordering = ['status']

    def __str__(self):
        return f"{self.room.name} | {self.status}"

    def get_number_of_available_places(self):
        return self.admission_set.prefetch_related(
            'department', 'patient', 'bed', 'diagnoses', 'meals', 'curings'
            ).filter(status__in=(1, 2)).count()


class DepartmentStorage(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.department.name} | {self.room.name}"

    def clean(self) -> None:
        if self.department.id != self.room.department.id:
            raise ValidationError(f"Choose the room belonging to {self.department.name}")
        return super().clean()
