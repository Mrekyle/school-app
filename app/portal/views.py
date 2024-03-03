from django.shortcuts import render

# Create your views here.


def portal(request):
    """
        Portal Processing
    """
    # check the user role inside of the user model thats been extended to show a different page. Then depending on the
    # user from page context show a different dashboard using includes.

    if request.user.is_superuser:
        template = 'admin_portal.html'
    elif request.user.is_staff:
        template = 'owner_portal.html'
    elif request.user.is_staff:
        template = 'instructor_portal.html'
    else:
        template = 'student_portal.html'

    context = {
        'student': True,
        'instructor': True,
        'owner': True,
        'admin': True,

    }

    return render(request, template, context)