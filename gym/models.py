from django.db import models

from authenticate.models import User


class GymTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gym_name = models.CharField(max_length=100, null=True, blank=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField(blank=True, null=True)
    exercise_in_week = models.PositiveBigIntegerField(default=1)
    exercise_in_day = models.PositiveBigIntegerField(default=1)

    def get_program_day1(self):
        return self.program_set.filter(day='day1')

    def get_program_day2(self):
        return self.program_set.filter(day='day2')

    def get_program_day3(self):
        return self.program_set.filter(day='day3')

    def get_program_day4(self):
        return self.program_set.filter(day='day4')

    def get_program_day5(self):
        return self.program_set.filter(day='day5')

    def get_program_day6(self):
        return self.program_set.filter(day='day6')

    def get_program_day7(self):
        return self.program_set.filter(day='day7')

    def get_program_day8(self):
        return self.program_set.filter(day='day8')

    def get_program_day9(self):
        return self.program_set.filter(day='day9')

    def get_program_day10(self):
        return self.program_set.filter(day='day10')
