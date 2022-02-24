from rest_framework import serializers

from gym.models import GymTracker

from program.serializers import ProgramSerializer


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymTracker
        fields = '__all__'


class GymWithProgramSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True, read_only=True)

    class Meta:
        model = GymTracker
        fields = ['gym_name', 'start_at', 'end_at', 'exercise_in_week', 'exercise_in_day']
