from django.urls import path

from . import views

urlpatterns = [
    path('lesson_management/', views.lesson_management, name='lesson_management'),
]
