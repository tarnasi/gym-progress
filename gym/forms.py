from django import forms

from .models import GymTracker


class CreateGymForm(forms.ModelForm):
    gym_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
    }))
    start_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        "class": "form-control",
        "type": "datetime-local"
    }))
    end_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        "class": "form-control",
        "type": "datetime-local"
    }))
    exercise_in_week = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-control",
    }))
    exercise_in_day = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-control",
    }))

    class Meta:
        model = GymTracker
        fields = ["gym_name", "start_at", "end_at", "exercise_in_week", "exercise_in_day"]
