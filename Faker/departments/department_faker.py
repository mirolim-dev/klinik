"""In this file I'll create object for all models belonging to department models"""
import random
from datetime import datetime, timedelta
from datetime import time

from departments.models import (
    Department, Room, RoomStuff, Bed
    )

from departments.meals_models import (
    MealAmount, Meal, MealTime, Admission
)

from hr_management.models import Patient


def create_department_objects():
    from Faker.fake_data_center.departments_data.departments import departments_data
    countdown = 0
    for department_data in departments_data:
        try:
            Department.objects.create(**department_data)
            countdown += 1
        except:
            continue
    print(f"{countdown} objects created for Department model\n{15*'--'}\n")


def create_room_and_room_stuff_objects():
    from Faker.fake_data_center.departments_data.rooms import room_names, stuff_names
    departments = Department.objects.all()
    # Generate 20 Room data
    rooms = []
    for name in room_names:
        department = random.choice(departments)
        name = f"{department.name} | {name}"
        try:
            room = Room.objects.create(name=name, department=department)
            rooms.append(room)
        except:
            continue

    # Generate 20 RoomStuff data
    for _ in range(50):
        room = random.choice(rooms)
        name = random.choice(stuff_names)
        quantity = random.randint(1, 10)
        RoomStuff.objects.create(room=room, name=name, quantity=quantity)
    print(f"20 Rooms and 50 RoomStuffs created successfully✅✅")


def create_bed_objects(numbers_of_objects=20):
    """Generates Bed data"""
    # Generate Bed data
    rooms = Room.objects.select_related('department')
    
    for _ in range(numbers_of_objects):
        room = random.choice(rooms)
        number_of_beds = random.randint(1, 4)
        price_for_one_day = round(random.uniform(150000.00, 2000000.00), 2)
        try:
            Bed.objects.create(room=room, number_of_beds=number_of_beds, price_for_one_day=price_for_one_day, status=0)
        except:
            continue

def create_meal_objects():
    from Faker.fake_data_center.departments_data.meals import meals_data
    countdown = 0
    for meal_data in meals_data:
        try:
            Meal.objects.create(**meal_data)
            countdown += 1
        except:
            continue
    print(f"{countdown} objects created successfully✅✅ for Meal model\n{15*'--'}\n")


def create_meal_amount():
    """This functions comes after create_meal_objects function"""
    meals = Meal.objects.all()
    countdown = 0
    for meal in meals:
        amount = round(random.uniform(150.00, 250.00), 2)
        measure = random.choice([1, 2])
        try:
            MealAmount.objects.create(meal=meal, amount=amount, measure=measure)
            countdown += 1
        except:
            continue
    print(f"{countdown} objects created successfully✅✅ for MealAmount model\n{15*'--'}\n")
            

def create_meals_time(number_of_meals_time=20):
    """This functions comes after create_meal_amount function"""
    meal_amounts = MealAmount.objects.select_related('meal')
    departments = Department.objects.all()
    countdown = 0
    for _ in range(number_of_meals_time):
        name = random.choice(["Breakfast", "Lunch", "Dinner"])
        amount = random.choice(meal_amounts)
        random_departments = random.sample(list(departments), 3)
        price = round(random.uniform(25000.00, 200000.00), 2)
        time_value = time(random.randint(6, 12), random.randint(0, 59))
        try:
            meal_time = MealTime.objects.create(name=name, amount=amount, price=price, time=time_value)
            for random_department in random_departments:
                meal_time.department.add(random_department)
            countdown += 1
        except:
            continue
    print(f"{countdown} objects created successfully✅✅ for MealTime model\n{15*'--'}\n")


def create_admission_objects():
    """before using this funtion Department, Patient, Bed, Diagnose, Curing models' dat should be exist"""
    from datetime import timedelta
    from django.utils import    timezone
    from events.models import Diagnoz, Curing
    departments = Department.objects.all()
    patients = Patient.objects.all()
    beds = Bed.objects.select_related('room')
    diagnoses = Diagnoz.objects.select_related("room", 'responsible_person')
    curings = Curing.objects.all()
    mealtimes = MealTime.objects.select_related('amount')
    # Create 25 different Admission objects
    for _ in range(25):
        department = random.choice(departments)
        patient = random.choice(patients)
        bed = random.choice(beds)
        status = random.choice([1, 2, 3, 4])
        description = "This is a sample description for the admission."

        # Generate random start and finish datetimes within a range
        start_time = timezone.now() - timedelta(days=random.randint(1, 30))
        finish_time = start_time + timedelta(days=random.randint(3, 10))
        try:
            admission = Admission.objects.create(
                department=department,
                patient=patient,
                bed=bed,
                starts_at=start_time,
                finishes_at=finish_time,
                status=status,
                description=description
            )

            admission.diagnoses.set(random.sample(list(diagnoses), random.randint(2, 5)))
            admission.meals.set(random.sample(list(mealtimes), random.randint(0, 3)))
            admission.curings.set(random.sample(list(curings), random.randint(1, 4)))
        except:
            continue
    print(f"Objects created successfully✅✅ for MealTime model\n{15*'--'}\n")

