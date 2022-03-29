from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import User
from gym.models import GymTracker

from .forms import LoginForm
from gym.forms import CreateGymForm


class DashboardView(generic.View):

    @classmethod
    def get(cls, request):
        form = CreateGymForm()

        if request.user.is_authenticated:
            context = {
                "form": form,
            }
            return render(request, "dashboard/dashboard.html", context)
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
            remember_me = form.cleaned_data['remember_me']

            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {email}")
                if not remember_me:
                    request.session.set_expiry(0)
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
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
            messages.info(request, f"You are now logged out")
            return redirect("/auth/login")
