from rest_framework import serializers

from program.models import Program


class ProgramWithGymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ["gym", 'move', 'set', 'repetition']


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"
