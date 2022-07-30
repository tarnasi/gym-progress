from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .forms import LoginForm, WorkoutCreateForm

from .serializers import ProfileUserSerializers

from program.models import Workout


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


class WorkoutPage(View):
    def get(self, request):
        context = {
            "workouts": Workout.objects.all()
        }
        return render(request, "dashboard/workout/index.html", context=context)


class WorkoutCreatePage(View):
    def get(self, request):
        return render(request, "dashboard/workout/create.html")

    def post(self, request):
        form = WorkoutCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_w = Workout()
            new_w.name = form.cleaned_data['name']
            new_w.set = form.cleaned_data['set']
            new_w.rep = form.cleaned_data['rep']
            new_w.rest = form.cleaned_data['rest']
            new_w.image = form.cleaned_data['workout_image']
            result = new_w.save()

            if result:
                return redirect('dashboard:workout-page')

        return redirect('dashboard:workout-create-page')


class WorkoutSinglePage(View):
    def get(self, request, id):
        workout = Workout.objects.get(id=id)
        context = {
            "workout": workout
        }
        return render(request, "dashboard/workout/single.html", context=context)
