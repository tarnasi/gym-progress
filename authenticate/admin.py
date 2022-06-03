from django.contrib import admin
from .models import User, PersonalInfo


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_login', 'is_email_verified', 'date_joined', 'id')


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('weight', 'height', 'user', 'blood_type', 'id')

