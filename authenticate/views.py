from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .forms import LoginForm

from .serializers import ProfileUserSerializers


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(ProfileUserSerializers(request.user).data)


class LoginPage(View):

    def get(self, request):
        return render(request, "auth/login.html")

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
        message = 'Login failed!'
        return render(request, "auth/login.html", context={'form': form, 'message': message})


class LogoutPage(View):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('auth:login-page')



class DashboardPage(View):
    def get(self, request):
        return render(request, "dashboard/main.html")
