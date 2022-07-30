from django.urls import path

from .views import (DashboardPage, )

app_name = "dashboard"
urlpatterns = [
    path('dashboard', DashboardPage.as_view(), name="dashboard-page"),
]
