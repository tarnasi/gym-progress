from django.db import models

from .utils import program_images


class Schedule(models.Model):
    YEAR_MONTHS = (
        ('January', 'january'),
        ('February', 'february'),
        ('March', 'march'),
        ('April', 'april'),
        ('May', 'may'),
        ('June', 'june'),
        ('July', 'july'),
        ('August', 'august'),
        ('September', 'september'),
        ('October', 'october'),
        ('November', 'november'),
        ('December', 'december'),
    )

    month = models.CharField(max_length=200, choices=YEAR_MONTHS)
    start_date = models.DateField()


class Program(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    set = models.PositiveIntegerField(default=0)
    rep = models.PositiveIntegerField(default=0)
    rest = models.PositiveIntegerField(default=0)
    last_weight = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=program_images)
