from django import forms

from .models import Program


class ProgramForm(forms.ModelForm):
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

    day = forms.CharField(widget=forms.Select(choices=DAYS, attrs={
        "class": "form-control",
        "value": "day1"
    }))
    move = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
    }))
    set = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-control",
    }))
    repetition = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-control",
    }))
    last_weight = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "required": False
    }))

    class Meta:
        model = Program
        fields = ["day", "move", "set", "repetition", "last_weight"]
