from django.urls import path

from .views import (UserProfileAPIView, )

app_name = "authenticate"
urlpatterns = [
    path('profile', UserProfileAPIView.as_view(), name="user-profile"),
]
