from django.contrib import admin

# from local
from .models import Patient, Stuff, Doctor, AvailableTime
from .specialization_models import StuffSpecialization, DoctorSpecialization


# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'gender', 
                    'date_of_birth', 'phone', 'address']
    list_display_links = ['first_name']
    list_editable = ['phone', 'address']
    exclude = ('username', 'password', 'last_login', 'is_active', 'is_staff',  
                    'is_superuser', 'groups', 'user_permissions')
admin.site.register(Patient, PatientAdmin)


class StuffAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'gender', 
                    'phone', 'address', 'specialization',
                    'department', 'working', 'salary', 
                    'salary_currency', 'date_joined', 'edited_at']
    list_display_links = ['first_name']
    list_editable = ['phone', 'address']
    exclude = ('username', 'password', 'last_login', 'is_active',  
               'is_superuser', 'groups', 'user_permissions')
admin.site.register(Stuff, StuffAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'gender', 
                    'phone', 'address', 'profession',
                    'department', 'working', 'salary', 
                    'salary_currency', 'date_joined', 'edited_at']
    list_display_links = ['first_name']
    list_editable = ['phone', 'address']
    exclude = ('username', 'password', 'last_login', 'is_active',  
                'specialization', 'is_superuser', 'groups', 'user_permissions')
            
admin.site.register(Doctor, DoctorAdmin)