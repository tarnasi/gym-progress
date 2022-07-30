from django.urls import path, include
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('devices', FCMDeviceAuthorizedViewSet)

app_name = "notification"
urlpatterns = [
    path('', include(router.urls)),
]
