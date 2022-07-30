from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)


class WorkoutCreateForm(forms.Form):
    name = forms.CharField(required=True)
    set = forms.IntegerField(required=False)
    rep = forms.IntegerField(required=False)
    rest = forms.IntegerField(required=False)
    workout_image = forms.ImageField()



