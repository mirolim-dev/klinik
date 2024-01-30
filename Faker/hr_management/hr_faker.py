from hr_management.models import (
    Patient, Staff, Doctor, DoctorSpecialization
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

