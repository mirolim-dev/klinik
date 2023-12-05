from django.shortcuts import render

from .models import Department
# Create your views here.

def main_index(request):
    departments = Department.objects.all()
    context = {
        'departments': departments,
    }

    return render(request, "departments/main_index.html", context)