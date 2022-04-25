from django.db import models

from django.contrib.auth import get_user_model
from gym.models import GymTracker

User = get_user_model()


class Program(models.Model):
    DAYS = [
        ('day1', 'Day 1'),
        ('day2', 'Day 2'),
        ('day3', 'Day 3'),
        ('day4', 'Day 4'),
        ('day5', 'Day 5'),
        ('day6', 'Day 6'),
        ('day7', 'Day 7'),
        ('day8', 'Day 8'),
        ('day9', 'Day 9'),
        ('day10', 'Day 10'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    gym = models.ForeignKey(GymTracker, on_delete=models.CASCADE, blank=True)
    day = models.CharField(max_length=120, choices=DAYS, default=DAYS[0][0])
    move = models.CharField(max_length=150)
    set = models.PositiveIntegerField()
    repetition = models.PositiveIntegerField()
    last_weight = models.CharField(max_length=200, blank=True, null=True)
