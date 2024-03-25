from django.urls import path
from . import views

urlpatterns = [
    path('finance_management/', views.finance_management,
         name='finance_management'),
]
