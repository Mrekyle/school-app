from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_portal/', views.admin_portal, name='admin_portal'),
    path('owner_portal/', views.owner_portal, name='owner_portal'),
]
