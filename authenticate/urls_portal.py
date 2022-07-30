from django.urls import path

from .views import (LoginPage, LogoutPage)

app_name = "auth"
urlpatterns = [
    path('login', LoginPage.as_view(), name="login-page"),
    path('logout', LogoutPage.as_view(), name="logout-page"),
]
