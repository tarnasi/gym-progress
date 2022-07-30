from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)


class WorkoutCreateForm(forms.Form):
    name = forms.CharField(required=True)
    set = forms.IntegerField(required=True)
    rep = forms.IntegerField(required=True)
    rest = forms.IntegerField(required=True)
    workout_image = forms.ImageField()



