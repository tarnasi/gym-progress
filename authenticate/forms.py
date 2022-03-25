from django import forms

from authenticate.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email",
        "aria-label": "Email",
        "aria-describedby": "email-addon"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password",
        "aria-label": "Password",
        "aria-describedby": "password-addon"
    }))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "checked": "",
        "id": "rememberMe",
        "class": "form-check-input"
    }))

    class Meta:
        fields = ['email', 'password', 'remember_me']


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email",
        "aria-label": "Email",
        "aria-describedby": "email-addon"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password",
        "aria-label": "Password",
        "aria-describedby": "password-addon"
    }))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "checked": "",
        "id": "rememberMe",
        "class": "form-check-input"
    }))

    class Meta:
        fields = ['email', 'password', 'remember_me']
