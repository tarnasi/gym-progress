from django.contrib import admin

from .models import Schedule, Program, Workout


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['title', 'month', 'start_date', 'id']


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'schedule', 'workout_count', 'exersice_per_week', 'id']


@admin.register(Workout)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'set', 'rep', 'rest', 'last_weight', 'program', 'id']
