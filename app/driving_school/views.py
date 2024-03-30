from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import DrivingSchool
from .forms import DrivingSchoolForm
from django.conf import settings
from django.core.mail import send_mail

from portal.decorators import admin_only

# Create your views here.


@login_required(login_url='landing')
@admin_only
def school_management(request):
    """
        Driving school management home page.
    """

    driving_school = DrivingSchool.objects.all().order_by('-date_joined')
    # Implement when students and instructors added

    # student_count = driving_school.students.count()
    # instructor_count = driving_school.instructors.count()

    template = 'school_management.html'

    context = {
        'admin': True,
        'schools': driving_school,
    }

    return render(request, template, context)


@login_required(login_url='landing')
@admin_only
def add_school(request):
    """
        Add a new driving school manually
    """

    form = DrivingSchoolForm

    if request.method == 'POST':
        form = DrivingSchoolForm(request.POST)
        if request.method == 'POST':
            school_name = request.POST.get('name')
            school_email = request.POST.get('school_email')
            subject = f'{school_name} was created on APP NAME'
            if form.is_valid():
                new_school = form.save(commit=True)
                # CREATE SCHOOL OWNER HERE
                messages.success(
                    request, f"{school_name} was created successfully")

                school_email = f"""

                Congratulations {school_name}. Your account was just created on APP NAME.
                By using the following email {school_email}

                Please follow this link to activate your account 

                LINK HERE

                If you didn't request this to happen please reply to this email letting us know we 
                made a mistake. 

                """

                send_mail(
                    subject=subject,
                    message=school_email,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL]
                )

                return redirect('school_management')
            else:
                messages.error(
                    request, f"Oops... Something went wrong. Please try again later. If the problem persists, please contact support")
                return redirect('add_school')

    template = 'add_school.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required(login_url='landing')
@admin_only
def edit_school(request, sch_id):
    """
        Manually edit a driving school 
    """

    school = get_object_or_404(DrivingSchool, pk=sch_id)

    if request.method == 'POST':
        form = DrivingSchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, f'Successfully edited {school.name}')
            return redirect('school_management')
        else:
            messages.error(
                request, f'Oops.. Something has gone wrong. Please try again later on. If the problem persists please contact support')
    else:
        form = DrivingSchoolForm(instance=school)
        messages.info(request, f'You are currently editing {school.name}')

    template = 'edit_school.html'

    context = {
        'school': school,
        'form': form,
    }

    return render(request, template, context)


@login_required(login_url='landing')
@admin_only
def delete_school(request, sch_id):
    """
        Handles the deletion of a driving school

        Will need to handle deletion of all data, instructors, students etc
    """

    school = get_object_or_404(DrivingSchool, pk=sch_id)
    school_name = request.POST.get('name')
    school.delete()
    messages.success(
        request, f'Successfully deleted driving school {school_name}')
    return redirect(reverse('school_management'))
