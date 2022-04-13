from django.urls import path

from .views import CreateGYMView, DetailGYMView, UpdateGYMView

app_name = 'GYM'
urlpatterns = [
    path("detail/<int:pk>", DetailGYMView.as_view(), name="detail"),
    path("create", CreateGYMView.as_view(), name="create"),
    path("update/<int:pk>", UpdateGYMView.as_view(), name="update"),
]
