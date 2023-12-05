from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Department
# Create your views here.

def main_index(request):
    departments = Department.objects.all()
    paginator = Paginator(departments, 1)  # Show 10 departments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
  

    return render(request, "departments/main_index.html", context)