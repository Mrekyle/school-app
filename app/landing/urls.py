from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('logout/', views.logoutUser, name='logout'),
]
