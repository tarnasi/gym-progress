from django.urls import path

from rest_framework import routers

from .views import (ScheduleViewSet, )

router = routers.SimpleRouter(trailing_slash=True)
router.register('schedule', ScheduleViewSet)

app_name = "program"
urlpatterns = [
]

urlpatterns += router.urls
