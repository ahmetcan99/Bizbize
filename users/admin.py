from django.contrib import admin
from .models import CustomUser, Profile

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)