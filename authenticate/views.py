from django.shortcuts import render, redirect
from django.views import generic
from django import forms
from django.contrib.auth import authenticate, login, logout

from .models import User

from .forms import LoginForm


class DashboardView(generic.View):

    @classmethod
    def get(cls, request):
        if request.user.is_authenticated:
            return render(request, "dashboard/dashboard.html", {})
        return redirect("/auth/login")


class LoginView(generic.View):

    @classmethod
    def get(cls, request):
        if request.user.is_authenticated:
            return redirect("dashboard/dashboard.html")

        form = LoginForm()
        return render(request, "auth/login.html", {'login_form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {email}")
                return redirect("/")
            else:
                # messages.error(request, "Invalid username or password.")
                form.add_error(None, "User Doesn't exist")
                return render(request, "auth/login.html", {"login_form": form})
        else:
            return render(request, "auth/login.html", {"login_form": form})


class RegisterView(generic.View):

    @classmethod
    def get(cls, request):
        if request.user.is_authenticated:
            return render(request, "dashboard/dashboard.html", {})
        return render(request, "auth/register.html", {})


class ForgetPasswordView(generic.View):

    @classmethod
    def get(cls, request):
        return render(request, "auth/forget-password.html", {})


class ResetPasswordView(generic.View):

    @classmethod
    def get(cls, request):
        return render(request, "auth/reset-password.html", {})


class LogoutView(generic.View):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect("/auth/login")
