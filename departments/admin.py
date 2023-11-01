from django.contrib import admin
from .models import Department
# from .head_doctor_models import HeadDoctor

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'building', 'created_at']
    list_display_links = ['name']
admin.site.register(Department, DepartmentAdmin)


# class HeadDoctorAdmin(admin.ModelAdmin):
#     list_display = ['id', 'doctor', 'department']
# admin.site.register(HeadDoctor, HeadDoctorAdmin)