from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import GymTracker

from .serializers import GymSerializer


class CreateNewGym(viewsets.ModelViewSet):
    queryset = GymTracker.objects.all()
    serializer_class = GymSerializer
    permission_classes = [IsAuthenticated]
