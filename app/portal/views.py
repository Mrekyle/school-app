from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.utils.safestring import mark_safe

from django.contrib.auth.decorators import login_required

from portal.decorators import admin_only, owner_only, instructor_only, student_only
from message_center.models import Support
from .forms import CreateCustomUser
from .models import Owner

# Create your views here.


@login_required(login_url='landing')
@admin_only
def admin_portal(request):
    """
        Admin portal 
    """

    support_form = Support.objects.all()
    create_user = CreateCustomUser

    """
        User creation 

        Assigning users to correct groups and schools
    """
    if request.method == 'POST':
        create_user = CreateCustomUser(request.POST)
        if request.method == 'POST':
            if create_user.is_valid():

                user = request.POST.get('username')
                # school = request.POST.get('school')
                group = request.POST.get('group')

                if group == 'Student':

                    create_user = create_user.save()

                    username = User.objects.get(username=user)
                    student = Group.objects.get(name='student')
                    username.groups.add(student)

                    messages.success(
                        request, mark_safe(f'{username} was created successfully!<br><hr><br> Group: <span class="f-bold">{student}</span> School: <span class="f-bold">SCHOOL</span>'))
                    return redirect('admin_portal')
                elif group == 'Instructor':

                    create_user = create_user.save()

                    username = User.objects.get(username=user)
                    instructor = Group.objects.get(name='instructor')
                    username.groups.add(instructor)

                    messages.success(
                        request, mark_safe(f'{username} was created successfully!<br><hr><br> Group: <span class="f-bold">{instructor}</span> School: <span class="f-bold">SCHOOL</span>'))
                    return redirect('admin_portal')
                elif group == 'Owner':

                    create_user = create_user.save()

                    username = User.objects.get(username=user)
                    owner = Group.objects.get(name='owner')
                    username.groups.add(owner)

                    messages.success(
                        request, mark_safe(f'{username} was created successfully!<br><hr><br> Group: <span class="f-bold">{owner}</span> School: <span class="f-bold">SCHOOL</span>'))
                    return redirect('admin_portal')
            else:
                create_user = CreateCustomUser()
                messages.error(request, f'Error')

    template = 'admin_portal.html'

    context = {
        'support': support_form,
        'create_user': create_user,
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
