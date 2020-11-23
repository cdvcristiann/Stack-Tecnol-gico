from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
path("Gestor/", views.index, name="index"),
]