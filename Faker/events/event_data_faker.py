import random
from hr_management.models import (
    Patient, Doctor, Staff
    )
from hr_management.specialization_models import StaffSpecialization
from departments.models import Room, Department

from events.models import (
    CuringRegimen, Curing, Diagnoz,
    DiagnozProductUsage,
)

from events.consulting_models import (
    Consulting, ConsultingPatientUsage,
    Prescription, DiagnozPatientUsage,
)

def create_curing_objects():
    from Faker.fake_data_center.events_data.curing import curings_data
    countdown = 0
    for curing_data in curings_data:
        try:
            Curing.objects.create(**curing_data)
            countdown += 1
        except:
            continue
    print(f"{countdown} Objects created successfully✅✅ for Curing mode\n{15*'--'}\n")


def create_curing_regimens():
    from Faker.fake_data_center.events_data.curing_regimens import curings_regimens
    curings = Curing.objects.all()
    countdown = 0
    for curing in curings:
        number_of_curing_regimens = random.choice(range(1, 5))
        random_curing_regimens_data = random.sample(list(curings_regimens), number_of_curing_regimens)
        for curing_regimen in random_curing_regimens_data:
            try:
                CuringRegimen.objects.create(curing=curing, **curing_regimen)
                countdown += 1
            except:
                continue
    print(f"{countdown} Objects created successfully✅✅ for CuringRegimen model\n{15*'=='}\n")


def create_diagnose_objects():
    from Faker.fake_data_center.events_data.diagnoses import diagnoses
    responsible_persons = Staff.objects.filter(specialization__name__icontains="Laboratory", working=True) 
    if responsible_persons.count() == 0:
        persons = [
        {
            'username': 'stafLab1',
            'first_name': 'EmilyLab',
            'last_name': 'GarciaS',
            'phone': '4324178944',
            'gender': 0,
            'address': '1011 Pine Lane',
        },
        {
            'username': 'stafLab2',
            'first_name': 'David',
            'last_name': 'Kevin',
            'phone': '3213334587',
            'gender': 1,
            'address': '2222 Maple Street',
        },
        {
            'username': 'stafLab3',
            'first_name': 'John',
            'last_name': 'Smith',
            'phone': '1234566547',
            'gender': 1,
            'address': '123 Main Street',
        },
        {
            'username': 'stafLab4',
            'first_name': 'Rakxima',
            'last_name': 'Johnson',
            'phone': '9876543210',
            'gender': 0,
            'address': '456 Elm Avenue',
        }]
        specialization = StaffSpecialization.objects.get_or_create(name="Laboratory")[0]
        responsible_persons = []
        departments = Department.objects.all()
        for person in persons:
            salary = round(random.uniform(15000.00, 20000000.00), 2)
            salary_currency = random.choice([0, 1, 2])
            department = random.choice(departments)
            try:
                r_person = Staff.objects.create(
                            **person, department=department,
                            specialization=specialization,
                            salary=salary, salary_currency=salary_currency
                            )
                responsible_persons.add(r_person)
            except:
                continue
    rooms = Room.objects.filter(bed__isnull=True)
    countdown = 0
    for diagnose in diagnoses:
        responsible_person = random.choice(responsible_persons)
        room = random.choice(rooms)
        try:
            Diagnoz.objects.create(responsible_person=responsible_person, room=room, **diagnose)
            countdown += 1
        except:
            continue
    print(f"{countdown} Objects created successfully✅✅ for Diagnoz model\n{15*'=='}\n")


def create_consultation_onjects():
    from Faker.fake_data_center.events_data.consultation import consultation_services
    consultants = Doctor.objects.filter(position__in=[1, 2], working=True)
    rooms = Room.objects.filter(bed__isnull=True, diagnoz__isnull=True)
    if consultants and rooms:
        countdown = 0
        for consultation in consultation_services:
            consultant = random.choice(consultants)
            room = random.choice(rooms)
            try:
                Consulting.objects.create(**consultation, consultant=consultant, room=room)
                countdown += 1
            except:
                continue
        print(f"{countdown} Objects created successfully✅✅ for Consulting model\n{15*'=='}\n")
    else:
        print(f"Consultants: {consultants} | Rooms: {rooms} | Should be exist to create Consulting objects\n{10*'<?>'}\n")
    

 

    