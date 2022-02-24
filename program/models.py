from django.db import models

from django.contrib.auth import get_user_model
from gym.models import GymTracker


User = get_user_model()


class Program(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gym = models.ForeignKey(GymTracker, on_delete=models.CASCADE)
    move = models.CharField(max_length=150)
    set = models.PositiveIntegerField()
    repetition = models.PositiveIntegerField()

