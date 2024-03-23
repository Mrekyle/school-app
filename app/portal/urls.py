from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portal, name='portal'),
    path('admin_settings', views.admin_settings, name='admin_settings'),
]
