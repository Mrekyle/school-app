from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from portal.decorators import allowed_users


# Create your views here.

@login_required(login_url='landing')
@allowed_users(allowed_roles=['admin'])
def admin_portal(request):
    """
        Admin portal 
    """

    if request.user.is_authenticated:
        messages.info(request, 'User logged in as admin')

    template = 'admin_portal.html'

    context = {

    }

    return render(request, template, context)


@login_required(login_url='landing')
def owner_portal(request):
    """
        Driving school owner portal 
    """

    template = 'owner_portal.html'

    context = {

    }

    return render(request, template, context)
