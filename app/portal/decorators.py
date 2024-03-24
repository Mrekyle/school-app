from django.http import HttpResponse
from django.shortcuts import redirect

"""
    Custom decorator to check is a user is authenticated.

    Stopping the user from being able to access login pages 
    By checking if the user is authenticated or not
"""


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('student_portal')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


"""
    Allowing certain user groups to access certain pages/content

    Setting the allowed roles to the user based on the user groups

    Using as a decorator and passing in select user groups to allow 
    access to the content 
"""


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                # Change to error 404 redirect or something
                return HttpResponse('You are not allowed to view this page')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'student':
            return redirect('student_portal')
        elif group == 'instructor':
            return redirect('instructor_portal')
        elif group == 'owner':
            return redirect('owner_portal')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function


def owner_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'student':
            return redirect('student_portal')
        elif group == 'instructor':
            return redirect('instructor_portal')
        elif group == 'admin':
            return redirect('admin_portal')

        if group == 'owner':
            return view_func(request, *args, **kwargs)

    return wrapper_function


def instructor_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'student':
            return redirect('student_portal')
        elif group == 'owner':
            return redirect('owner_portal')
        elif group == 'admin':
            return redirect('admin_portal')

        if group == 'instructor':
            return view_func(request, *args, **kwargs)

    return wrapper_function


def student_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'owner':
            return redirect('owner_portal')
        elif group == 'instructor':
            return redirect('instructor_portal')
        elif group == 'admin':
            return redirect('admin_portal')

        if group == 'student':
            return view_func(request, *args, **kwargs)

    return wrapper_function
