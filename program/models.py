from django.db import models

from .utils import workout_images

from django.contrib.auth import get_user_model

User = get_user_model()


class Schedule(models.Model):
    YEAR_MONTHS = (
        ('january', 'january'),
        ('february', 'february'),
        ('march', 'march'),
        ('april', 'april'),
        ('may', 'may'),
        ('june', 'june'),
        ('july', 'july'),
        ('august', 'august'),
        ('september', 'september'),
        ('october', 'october'),
        ('november', 'november'),
        ('december', 'december'),
    )

    title = models.CharField(max_length=100, blank=True, null=True)
    month = models.CharField(max_length=200, choices=YEAR_MONTHS)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Program(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    workout_count = models.PositiveBigIntegerField(default=0)
    exersice_per_week = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['schedule']


class Workout(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=200)
    set = models.PositiveIntegerField(default=0, null=True, blank=True)
    rep = models.PositiveIntegerField(default=0, null=True, blank=True)
    rest = models.PositiveIntegerField(default=0, null=True, blank=True)
    last_weight = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=workout_images, null=True, blank=True)
    language = models.CharField(max_length=10, default="fa")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['program']
