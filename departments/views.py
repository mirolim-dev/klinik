from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Department
from hr_management.models import Doctor
# Create your views here.

def main_index(request):
    departments = Department.objects.all()
    search_data = request.POST.get('search_input')
    if search_data:
        departments = Department.objects.filter(name__icontains=search_data)
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
    # fake_patient_data = [ #it should be removed before deploying
    #     {
    #         'id': 1,
    #         'first_name': "Ibragim",
    #         'last_name': "Xolmatov",
    #         'phone': "+998 95 978 45 65",
    #         'gender': "Male",
    #         'address': "Qo'qon",
    #         'date_of_birth': "2001-12-31",
    #         'insurance_provider': None,
    #         'insurance_policy_number': None,
    #     },
    #     {
    #         'id': 2,
    #         'first_name': "Iftixor",
    #         'last_name': "Xolmatov",
    #         'phone': "+998 95 978 45 66",
    #         'gender': "Male",
    #         'address': "Qo'qon",
    #         'date_of_birth': "2001-11-15",
    #         'insurance_provider': None,
    #         'insurance_policy_number': None,
    #     },
    # ]  
    context = {
        'department': department,
        'patients': page_patients,
    }
    return render(request, 'departments/show_patients.html', context)
# def update_doctor_detail(request, doctor_id:int):
#     doctor = Doctor.objects.get(id=doctor_id)
#     context = {'doctor': doctor}
#     return render('departments/update_doctor.html', context)