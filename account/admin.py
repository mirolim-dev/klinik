from django.contrib import admin
from .models import CustomUser
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'phone', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active']
    list_display_links = ['username']

admin.site.register(CustomUser, UserAdmin)