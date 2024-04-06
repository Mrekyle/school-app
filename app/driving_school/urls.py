from django.urls import path
from . import views

urlpatterns = [
    path('school_management/', views.school_management, name='school_management'),
    path('add_school/', views.add_school, name='add_school'),
    path('delete_school/<uuid:sch_id>/',
         views.delete_school, name='delete_school'),
    path('edit_school/<uuid:sch_id>/', views.edit_school, name='edit_school'),
]
