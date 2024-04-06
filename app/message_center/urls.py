from django.urls import path
from . import views

urlpatterns = [
    path('message_center/', views.message_center, name='message_center'),
    path('delete_message/<int:msg_id>/',
         views.delete_message, name='delete_message'),
    path('support/', views.support, name='support'),
]
