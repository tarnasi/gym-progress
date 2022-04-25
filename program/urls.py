from django.urls import path

from .views import CreateProgramView

app_name = 'Program'
urlpatterns = [
    path("<int:pk>/create", CreateProgramView.as_view(), name="create"),
]
