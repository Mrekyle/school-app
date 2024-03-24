from django.urls import path
from . import views

urlpatterns = [
    path('admin_portal/', views.admin_portal, name='admin_portal'),
    path('owner_portal/', views.owner_portal, name='owner_portal'),
    path('instructor_portal/', views.instructor_portal, name='instructor_portal'),
    path('student_portal/', views.student_portal, name='student_portal'),
]
