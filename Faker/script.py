from .departments.department_faker import(
    create_admission_objects, create_bed_objects,
    create_department_objects, create_meal_amount, create_meal_objects, 
    create_meals_time, create_room_and_room_stuff_objects
)
from .hr_management.hr_faker import (
    create_doctor_objects, create_doctor_specializations,
    create_patients_objects, 
    create_staff_specializations, create_staffs_objects,
)
from .events.event_data_faker import (
    create_consultation_onjects, create_curing_objects,
    create_curing_regimens, create_diagnose_objects
)


def manage_functions():
    #1 create Patient objects
    create_patients_objects()
    #2 create Department objects
    create_department_objects()
    #3 create Staff specializations
    create_staff_specializations()
    #4 create Dcotor specializations
    create_doctor_specializations()
    #5 create Staff objects
    create_staffs_objects()
    #6 create Doctor objects
    create_doctor_objects()
    #7 create Room and RoomStuffs objects
    create_room_and_room_stuff_objects()
    #8 create Bed objects
    create_bed_objects()
    #9 create Meal objects
    create_meal_objects()
    #10 create MealAmount objects
    create_meal_amount()
    #11 Create MealTime objects
    create_meals_time()
    #12 Create Diagnoz(Diagnose) objects
    create_diagnose_objects()
    #13 Create Consulting(Consultation) objects
    create_consultation_onjects()
    #14 create Curing objects
    create_curing_objects()
    #15 create CuringRegimen objects
    create_curing_regimens()
    #16 create Admission objects
    create_admission_objects()

    print(f"<{15*'=='}>\nObjects created Successfully\n<\{15*'=='}>")

if __name__ == '__main__':
    manage_functions()