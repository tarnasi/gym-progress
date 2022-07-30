from django.urls import path

from .views import (DashboardPage, WorkoutPage, WorkoutCreatePage, WorkoutSinglePage)

app_name = "dashboard"
urlpatterns = [
    path('dashboard', DashboardPage.as_view(), name="dashboard-page"),
    path('dashboard/workout', WorkoutPage.as_view(), name="workout-page"),
    path('dashboard/workout/create', WorkoutCreatePage.as_view(), name="workout-create-page"),
    path('dashboard/workout/<int:id>', WorkoutSinglePage.as_view(), name="workout-single"),
]
