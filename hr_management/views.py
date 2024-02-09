from django.shortcuts import render
from django.shortcuts import get_object_or_404

from departments.models import (
    Department,
)
from .models import (
    Patient, 
    )
# Create your views here.

def patient_profile(request, patient_id:int):
    patient = get_object_or_404(Patient, id=patient_id)

    context = {
        'patient': patient,
    }
    return render(request, 'hr_management/patient_profile.html', context)