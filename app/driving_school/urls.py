from django.urls import path
from . import views

urlpatterns = [
    path('school_management/', views.school_management, name='school_management'),
]
