from django.contrib import admin
from .models import (
        Curing, CuringRegimen, 
        DiagnozProductUsage, Diagnoz,
        )
from .consulting_models import (
    DiagnozPatientUsage, Consulting,
    ConsultingPatientUsage, Prescription
    )

# Register your models here.
class CuringAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['name']
admin.site.register(Curing, CuringAdmin)


class CuringRegimenAdmin(admin.ModelAdmin):
    list_display = ['id', 'curing', 'drug', 'dosage', 'times_in_a_day']
    search_fields = ['curing__name', 'drug', 'dosage', 'time_in_a_day']
admin.site.register(CuringRegimen, CuringRegimenAdmin)


class DiagnozAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'responsible_person', 'room']
    list_display_links = ['name']
    search_fields = ['id', 'name', 'price', 
    'responsible_person__first_name', 'responsible_person__last_name']
    list_editable = ['price', 'responsible_person']
admin.site.register(Diagnoz, DiagnozAdmin)


class DiagnozProductUsageAdmin(admin.ModelAdmin):
    list_display = ['id', 'diagnoz', 'amount', 'measure']
    list_filter = ['measure']
    search_fields = ['amount', 'diagnoz__name']
    list_editable = ['amount', 'measure']
admin.site.register(DiagnozProductUsage, DiagnozProductUsageAdmin)


class DiagnozPatientUsageAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'diagnoz', 'status', 'created_at', 'updated_at']
    list_filter = ['status']
    list_editable = ['status']
admin.site.register(DiagnozPatientUsage, DiagnozPatientUsageAdmin)


class ConsultingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'consultant', 'price', 'room', 'status', 'created_at']
    list_filter = ['status']
    list_editable = ['price', 'status']
    search_fields = ['name', 'id', 'consultant__firt_name', 'consultant__last_name', 'price', 'room__name']
admin.site.register(Consulting, ConsultingAdmin)


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'consulting_patient_usage', 'drug', 'dosage', 'times_in_a_day']
    list_editable = ['drug', 'dosage', 'times_in_a_day']
    search_fields = ['id', 'consulting_patient_usage', 'drug', 'dosage', 'times_in_a_day']
admin.site.register(Prescription, PrescriptionAdmin)


class ConsultingPatientUsageAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'consulting', 'status', 'created_at', 'updated_at']
    list_filter = ['status']
    list_editable = ['status']
admin.site.register(ConsultingPatientUsage, ConsultingPatientUsageAdmin)
