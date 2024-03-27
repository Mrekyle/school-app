from django.urls import path
from . import views

urlpatterns = [
    path('message_center/', views.message_center, name='message_center'),
    path('support/', views.support, name='support'),
]
