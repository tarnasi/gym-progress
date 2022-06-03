from rest_framework import serializers

from .models import User, PersonalInfo


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = ('id', 'weight', 'height', 'blood_type')


class ProfileUserSerializers(serializers.ModelSerializer):
    personalinfo = PersonalInfoSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'last_login', 'date_joined', 'email_verify_at', 'is_email_verified', 'is_active',
                  'avatar', 'personalinfo')
