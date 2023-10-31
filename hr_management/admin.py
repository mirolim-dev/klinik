from django.contrib import admin

# from local
from .models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'gender', 
                    'date_of_birth', 'phone', 'address']
    list_display_links = ['first_name']
    list_editable = ['phone', 'address']
    exclude = ('username', 'password', 'last_login', 'is_active', 'is_staff',  
                'is_superuser', 'groups', 'user_permissions')
admin.site.register(Patient, PatientAdmin)