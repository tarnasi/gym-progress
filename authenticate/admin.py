from django.contrib import admin
from .models import User, PersonalInfo

admin.site.site_header = "مدیریت برنامه ورزشی"
admin.site.site_title = "GYM Progress"
admin.site.index_title = "به مدیریت برنامه ورزشی خوش آمدید"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_login', 'is_email_verified', 'date_joined', 'id')


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('weight', 'height', 'user', 'blood_type', 'id')

