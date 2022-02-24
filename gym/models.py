from django.db import models


class GymTracker(models.Model):
    gym_name = models.CharField(max_length=100, null=True, blank=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField(blank=True, null=True)
    exercise_in_week = models.PositiveBigIntegerField(default=1)
    exercise_in_day = models.PositiveBigIntegerField(default=1)
