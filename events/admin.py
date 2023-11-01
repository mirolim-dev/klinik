from django.contrib import admin
from .models import Curing, CuringRegimen

# Register your models here.
class CuringAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['name']
admin.site.register(Curing, CuringAdmin)


class CuringRegimenAdmin(admin.ModelAdmin):
    list_display = ['id', 'curing', 'drug', 'dosage', 'times_in_a_day']
    search_fields = ['curing__name', 'drug', 'dosage', 'time_in_a_day']
admin.site.register(CuringRegimen, CuringRegimenAdmin)
