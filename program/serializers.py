from rest_framework import serializers

from .models import Schedule, Workout, Program


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['title', 'month', 'start_date', 'end_date', 'id']


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['name', 'workout_count', 'exersice_per_week', 'id']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['name', 'set', 'rep', 'rest', 'last_weight', 'id']


