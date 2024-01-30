import random

from hr_management.models import (
    Patient, Staff, Doctor, DoctorSpecialization
)
from hr_management.specialization_models import StaffSpecialization, DoctorSpecialization
from departments.models import (
    Department,
)


def create_patients_objects():
    from fake_data_center.hr_management_data.patients import patients_data
    countdown = 0
    for patient_data in patients_data:
        try:
            Patient.objects.create(**patient_data)
            countdown += 1
        except:
            continue
    print(f"{countdown} objects created for Patient model\n{15*'--'}\n")


def create_staff_specializations():
    from fake_data_center.hr_management_data.specializations import staff_specializations
    countdown = 0
    for staff_spc in staff_specializations:
        try:
            StaffSpecialization.objects.create(**staff_spc)
            countdown += 1
        except:
            continue
    print(f"{countdown} objects created for StaffSpecialization model\n{15*'--'}\n")


def create_doctor_specializations():
    from fake_data_center.hr_management_data.specializations import doctor_specializations
    countdown = 0
    for doctor_spc in doctor_specializations:
        try:
            DoctorSpecialization.objects.create(**doctor_spc)
            countdown += 1
        except:
            continue
    print(f"{countdown} objects created for DoctorSpecialization model\n{15*'--'}\n")


def create_staffs_objects():
    from fake_data_center.hr_management_data.staffs import staffs_data
    departments = Department.objects.all()
    staff_specializations = StaffSpecialization.objects.all()
    countdown = 0
    for staff_data in staffs_data:
        department = random.choice(departments)
        staff_specialization = random.choice(staff_specializations)
        salary = round(random.uniform(15000.00, 20000000.00), 2)
        salary_currency = random.choice([0, 1, 2])
        try:
            StaffSpecialization.objects.create(
                **staff_data, department=department,
                staff_specialization=staff_specialization,
                salary=salary, salary_currency=salary_currency
                )
            countdown += 1
        except:
            continue
    print(f"{countdown} objects created for Staff model\n{15*'--'}\n")


def create_doctor_objects():
    from fake_data_center.hr_management_data.doctors import doctors_data
    departments = Department.objects.all()
    doctor_specializations = DoctorSpecialization.objects.all()
    countdown = 0
    for doctor_data in doctors_data:
        department = random.choice(departments)
        salary = round(random.uniform(15000.00, 20000000.00), 2)
        salary_currency = random.choice([0, 1, 2])
        profession = random.choice(doctor_specializations)
        position = random.choice([0, 1, 2, 3, 4])
        try:
            StaffSpecialization.objects.create(
                **doctor_data, department=department,
                salary=salary, salary_currency=salary_currency,
                profession=profession, position=position
                )
            countdown += 1
        except:
            continue
    print(f"{countdown} objects created for Doctor model\n{15*'--'}\n")
