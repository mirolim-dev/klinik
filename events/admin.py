from django.contrib import admin
from .models import (
        Curing, CuringRegimen, 
        DiagnozPatientUsage,
        DiagnozProductUsage, Diagnoz,
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
