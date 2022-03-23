from django.urls import path

from .views import (LoginView, RegisterView, ForgetPasswordView, ResetPasswordView, LogoutView)

app_name = "authenticate"
urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('register', RegisterView.as_view(), name="register"),
    path('forget-password', ForgetPasswordView.as_view(), name="forget-password"),
    path('reset-password', ResetPasswordView.as_view(), name="reset-password"),
]
