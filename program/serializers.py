from rest_framework import serializers

from program.models import Program

from gym.serializers import GymSerializer


class ProgramWithGymSerializer(serializers.ModelSerializer):
    gym = GymSerializer(read_only=True)

    class Meta:
        model = Program
        fields = ["gym", 'move', 'set', 'repetition']


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"
