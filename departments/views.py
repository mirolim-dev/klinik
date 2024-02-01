from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Department
from hr_management.models import Doctor, Patient
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
    if page_patients:
        pass
    else:
        from .fake_patients import fake_patient_data
        page_patients = fake_patient_data
    context = {
        'department': department,
        'patients': page_patients,
    }
    return render(request, 'departments/show_patients.html', context)


 
def search_patients(request, department_id:int):
    search_input = request.GET.get('search_input')
    print("Search input: ", search_input)
    department_patients = get_object_or_404(Department, id=department_id).get_all_patients()
    patients_ids = [patient.id for patient in department_patients]
    filtered_patients = Patient.objects.filter(
        (
            Q(first_name__icontains=search_input) |
            Q(last_name__icontains=search_input) |
            Q(phone__icontains=search_input) |
            Q(address__icontains=search_input) |
            Q(insurance_provider__icontains=search_input) |
            Q(insurance_policy_number__icontains=search_input)
        ), id__in=patients_ids
    )
    print(f"Filtered patients", filtered_patients)
    context = {
        'searched_patients': filtered_patients,
    }
    return render(request, 'partials/patients_search_results.html', context)