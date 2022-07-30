from django.urls import path

from .views import (DashboardPage, WorkoutPage, WorkoutCreatePage)

app_name = "dashboard"
urlpatterns = [
    path('dashboard', DashboardPage.as_view(), name="dashboard-page"),
    path('dashboard/workout', WorkoutPage.as_view(), name="workout-page"),
    path('dashboard/workout/create', WorkoutCreatePage.as_view(), name="workout-create-page"),
]
