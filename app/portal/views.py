from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from portal.decorators import admin_only, owner_only, instructor_only, student_only


# Create your views here.

@login_required(login_url='landing')
@admin_only
def admin_portal(request):
    """
        Admin portal 
    """

    template = 'admin_portal.html'

    context = {
        'admin': True,
    }

    return render(request, template, context)


@login_required(login_url='landing')
@owner_only
def owner_portal(request):
    """
        Driving school owner portal 
    """

    template = 'owner_portal.html'

    context = {

    }

    return render(request, template, context)


@login_required(login_url='landing')
@instructor_only
def instructor_portal(request):
    """
        Instructor Portal
    """

    template = 'instructor_portal.html'

    context = {

    }

    return render(request, template, context)


@login_required(login_url='landing')
@student_only
def student_portal(request):
    """
        Student portal
    """

    template = 'student_portal.html'

    context = {

    }

    return render(request, template, context)
