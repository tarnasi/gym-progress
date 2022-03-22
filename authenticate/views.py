from django.shortcuts import render

from .models import User

from django.views import generic


class LoginView(generic.View):

    @classmethod
    def get(cls, request):
        return render(request, "auth/login.html", {})


class RegisterView(generic.View):

    @classmethod
    def get(cls, request):
        return render(request, "auth/register.html", {})


class ForgetPasswordView(generic.View):

    @classmethod
    def get(cls, request):
        return render(request, "auth/forget-password.html", {})


class ResetPasswordView(generic.View):

    @classmethod
    def get(cls, request):
        return render(request, "auth/reset-password.html", {})
