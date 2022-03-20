from django.urls import path, include

from rest_framework import routers

from .views import CreateNewGym


app_name = 'Gym'

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'gym', CreateNewGym)

urlpatterns = [
    path('', include(router.urls)),
]
