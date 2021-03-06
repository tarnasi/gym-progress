from django.db import models

from .utils import program_images


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
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    set = models.PositiveIntegerField(default=0)
    rep = models.PositiveIntegerField(default=0)
    rest = models.PositiveIntegerField(default=0)
    last_weight = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=program_images, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['program']
