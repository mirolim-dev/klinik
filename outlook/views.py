from django.shortcuts import render

# Create your views here.

def home_view(request):
    context = {}
    return render(request, 'outlook/index.html', context)


def dash_home1(request):
    context = {}
    return render(request, 'departments/index.html', context)