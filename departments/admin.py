from django.contrib import admin
from .models import (
    Department, DepartmentStorage,
    Room, RoomStuff, Bed,
    )
from .meals_models import Meal, MealAmount, MealTime, Admission
# from .head_doctor_models import HeadDoctor

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'building', 'created_at']
    list_display_links = ['name']
admin.site.register(Department, DepartmentAdmin)


class DepartmentStorageAdmin(admin.ModelAdmin):
    list_display = ['id', 'department', 'room']
admin.site.register(DepartmentStorage, DepartmentStorageAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department']
admin.site.register(Room, RoomAdmin)


class RoomStuffAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'name', 'quantity',
    'created_at', ]
admin.site.register(RoomStuff, RoomStuffAdmin)


class BedAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'number_of_beds',
    'price_for_one_day', 'status']
    filter_fields = ['status']
admin.site.register(Bed, BedAdmin)


class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'department', 'patient', 'bed', 'starts_at', 'finishes_at', 'status']
admin.site.register(Admission, AdmissionAdmin)


class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Meal, MealAdmin)


class MealAmountAdmin(admin.ModelAdmin):
    list_display = ['id', 'meal', 'amount', 'measure']
    list_editable = ['amount']    
    list_filter = ['measure']
    search_fields = ['meal__name', 'amount']
admin.site.register(MealAmount, MealAmountAdmin)


class MealTimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'amount', 'price', 'time']
    list_display_links = ['name']
    search_fields = ['name', 'department__name', 'price', 'time']
admin.site.register(MealTime, MealTimeAdmin)
# class HeadDoctorAdmin(admin.ModelAdmin):
#     list_display = ['id', 'doctor', 'department']
# admin.site.register(HeadDoctor, HeadDoctorAdmin)