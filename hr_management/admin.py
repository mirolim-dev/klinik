from django.contrib import admin

# from local
from .models import Patient, Staff, Doctor, AvailableTime, Achievement
from .specialization_models import StaffSpecialization, DoctorSpecialization
from .attandance_model import Attandance


# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'gender', 
                    'date_of_birth', 'phone', 'address']
    list_display_links = ['first_name']
    list_editable = ['phone', 'address']
    exclude = ('username', 'password', 'last_login', 'is_active', 'is_staff',  
                    'is_superuser', 'groups', 'user_permissions')
admin.site.register(Patient, PatientAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'gender', 
                    'phone', 'address', 'specialization',
                    'department', 'working', 'salary', 
                    'salary_currency', 'date_joined', 'edited_at']
    list_display_links = ['first_name']
    list_editable = ['phone', 'address']
    exclude = ('username', 'password', 'last_login', 'is_active',  
               'is_superuser', 'groups', 'user_permissions')
admin.site.register(Staff, StaffAdmin)


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


class AvailableTimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'staff', 'week_day', 'from_time', 'to']
    list_display_links = ['staff']
    list_editable = ['week_day', 'from_time', 'to']
admin.site.register(AvailableTime, AvailableTimeAdmin)


class StaffSpecializationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'display_image', 'created_at']
    list_display_links = ['name']
    def display_image(self, obj):
        return obj.image.url if obj.image else None
    display_image.short_description = 'Image'
admin.site.register(StaffSpecialization, StaffSpecializationAdmin)


class DoctorSpecializationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'display_image', 'created_at']
    list_display_links = ['name']
    def display_image(self, obj):
        return obj.image.url if obj.image else None
    display_image.short_description = 'Image'
admin.site.register(DoctorSpecialization, DoctorSpecializationAdmin)


class AchievementAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'name', '_file', 'description', 'uploaded_at']
    list_display_links = ['name']
admin.site.register(Achievement, AchievementAdmin)


class AttandanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'staff', 'arrived_at', 'left_at', 'in_available_day']
    search_fields = ['staff__first_name', 'staff__last_name', 'arrived_at', 'left_at']
    list_filter = ['in_available_day']
admin.site.register(Attandance, AttandanceAdmin)
