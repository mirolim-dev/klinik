from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q

from departments.models import (
    Department,
)
from payments.models import Invoice, Payment
from .models import (
    Patient, 
    )

# Create your views here.

def patient_profile(request, patient_id:int):
    patient = get_object_or_404(Patient, id=patient_id)
    searched_invoices = None
    if request.POST:
        search_input = request.POST.get('search_input')
        searched_invoices = Invoice.objects.filter(
            Q(patient=patient) & (
                Q(id__icontains=search_input)|
                Q(total_amount__icontains=search_input)|
                Q(description__icontains=search_input)
            )
        )
        context = {
            'patient': patient,
            'searched_invoices': searched_invoices
        }
        return render(request, 'partials/hrm/invoice_search_result_by_patient.html', context)
    context = {
        'patient': patient,
    }
    return render(request, 'hr_management/patient_profile.html', context)

