from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructor_management, name='instructor_management'),
]
