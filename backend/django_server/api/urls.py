from django.urls import path
from . import views

urlpatterns = [
    path("post", views.index, name="index"),
    path("react", views.index, name="index"),
]