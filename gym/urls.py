from django.urls import path

from .views import CreateGYMView, DetailGYMView

app_name = 'GYM'
urlpatterns = [
    path("create", CreateGYMView.as_view(), name="create"),
    path("detail/<int:pk>", DetailGYMView.as_view(), name="detail"),
]
