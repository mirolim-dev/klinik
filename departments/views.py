from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import (
    Department, Room, Bed
    )
from .meals_models import (
    Admission,
)
from hr_management.models import (
    Doctor, Patient, Staff,
    )
# Create your views here.

def main_index(request):
    departments = Department.objects.all()
    search_data = request.POST.get('search_input')
    if search_data:
        departments = Department.objects.filter(name__icontains=search_data).order_by('id')
    paginator = Paginator(departments, 10)  # Show 10 departments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_data': search_data,
    }   
  
    return render(request, "departments/main_index.html", context)


def main_index2(request):
    context = {

    }
    return render(request, "departments/index3.html", context)


def department_detail(request, pk:int):
    department = get_object_or_404(Department, id=pk)
    context = {
        'department': department,    
    }
    return render(request, 'departments/single_department.html', context)


def show_all_patients_by_department(request, department_id:int):
    department = get_object_or_404(Department, id=department_id)
    patients = department.get_all_patients()
    paginator = Paginator(patients, 10)  # Show 10 departments per page
    page_number = request.GET.get('page')
    page_patients = paginator.get_page(page_number)
    if not page_patients:
        from .fake_patients import fake_patient_data
        page_patients = fake_patient_data
    context = {
        'department': department,
        'patients': page_patients,
    }
    return render(request, 'departments/show_patients.html', context)


 
def search_patients(request, department_id:int):
    search_input = request.GET.get('search_input')
    department_patients = get_object_or_404(Department, id=department_id).get_all_patients()
    patients_ids = [patient.id for patient in department_patients]
    filtered_patients = Patient.objects.filter(
        (
            Q(first_name__icontains=search_input) |
            Q(last_name__icontains=search_input) |
            Q(phone__icontains=search_input) |
            Q(address__icontains=search_input) |
            Q(insurance_provider__icontains=search_input) |
            Q(insurance_policy_number__icontains=search_input) |
            Q(id__contains=search_input)
        ), id__in=patients_ids
    )
    context = {
        'searched_patients': filtered_patients,
    }
    return render(request, 'partials/patients_search_results.html', context)


def show_all_rooms(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    rooms = department.get_all_rooms()
    paginator = Paginator(rooms, 10)
    page = request.GET.get('page')
    paginated_rooms = paginator.get_page(page)
    context = {
        'department': department,
        'rooms': paginated_rooms,
    }
    return render(request, 'departments/show_all_rooms.html', context)


def search_rooms(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    search_input = request.POST.get('search_input')
    searched_rooms = Room.objects.filter(
        Q(department=department) & 
        Q(name__icontains=search_input)
    )
    context = {
        'searched_rooms': searched_rooms
    }
    return render(request, 'partials/room_search_results.html', context)


def show_doctors_by_department(request, department_id:int):
    department = get_object_or_404(Department, id=department_id)
    doctors = Doctor.objects.filter(department=department)
    page = request.GET.get('page')
    paginator = Paginator(doctors, 10)
    paginated_doctors = paginator.get_page(page)
    context = {
        'department': department,
        'doctors': paginated_doctors,
    }
    return render(request, 'departments/show_doctors.html', context)


def search_doctors_by_department(request, department_id:int):
    department = get_object_or_404(Department, id=department_id)
    search_input = request.POST.get('search_input')
    searched_doctors = Doctor.objects.filter(
        Q(department=department) & 
        (
            Q(username__icontains=search_input) |
            Q(first_name__icontains=search_input) |
            Q(last_name__icontains=search_input) |
            Q(phone__icontains=search_input) |
            Q(address__icontains=search_input) |
            Q(profession__name__icontains=search_input) |
            Q(salary__icontains=search_input)
        )
    )
    context = {
        'searched_doctors': searched_doctors
    }
    return render(request, 'partials/doctor_search_results.html', context)


def show_staffs_by_department(request, department_id:int):
    department = get_object_or_404(Department, id=department_id)
    staffs = Staff.objects.filter(department=department)
    page = request.GET.get('page')
    paginator = Paginator(staffs, 10)
    paginated_staffs = paginator.get_page(page)
    context = {
        'department': department,
        'staffs': paginated_staffs,
    }
    return render(request, 'departments/show_staffs.html', context)


def search_staffs_by_department(request, department_id:int):
    department = get_object_or_404(Department, id=department_id)
    search_input = request.POST.get('search_input')
    searched_staffs = Staff.objects.filter(
        Q(department=department) & 
        (
            Q(username__icontains=search_input) |
            Q(first_name__icontains=search_input) |
            Q(last_name__icontains=search_input) |
            Q(phone__icontains=search_input) |
            Q(address__icontains=search_input) |
            Q(specialization__name__icontains=search_input) |
            Q(salary__icontains=search_input)
        )
    )
    context = {
        'searched_staffs': searched_staffs
    }
    return render(request, 'partials/staff_search_results.html', context)


def show_admissions_by_department(request, department_id:int):
    department = get_object_or_404(Department, id=department_id)
    admissions = Admission.objects.filter(department=department)
    page = request.GET.get('page')
    paginator = Paginator(admissions, 10)
    paginated_admissions = paginator.get_page(page)
    context = {
        'department': department,
        'admissions': paginated_admissions,
    }
    return render(request, 'departments/show_admissions.html', context)


def search_admissions_by_department(request, department_id:int):
    department = get_object_or_404(Department, id=department_id)
    search_input = request.POST.get('search_input')
    searched_admissions = Admission.objects.filter(
        Q(department=department) & 
        (
         Q(patient__first_name__icontains=search_input) |
         Q(patient__last_name__icontains=search_input) |
         Q(bed__room__name__icontains=search_input)   
        )
    )
    context = {
        'searched_admissions': searched_admissions
    }
    return render(request, 'partials/admission_search_results.html', context)


def show_beds_by_department(request, department_id:int):
    department = get_object_or_404(Department, id=department_id)
    beds = Bed.objects.filter(room__department=department)
    page = request.GET.get('page')
    paginator = Paginator(beds, 10)
    paginated_beds = paginator.get_page(page)
    context = {
        'department': department,
        'beds': paginated_beds,
    }
    return render(request, 'departments/show_all_beds.html', context)


def search_beds_by_department(request, department_id:int):
    department = get_object_or_404(Department, id=department_id)
    search_input = request.POST.get('search_input')
    searched_beds = Bed.objects.filter(
        Q(room__department=department) & 
        (
            Q(room__name__icontains=search_input) |
            Q(number_of_beds__icontains=search_input) |
            Q(price_for_one_day__icontains=search_input)   
        )
    )
    context = {
        'searched_beds': searched_beds
    }
    return render(request, 'partials/bed_search_results.html', context)