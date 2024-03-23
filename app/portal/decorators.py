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
            return redirect('portal')
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
            return wrapper_func(request, *args, **kwargs)
        return wrapper_func
    return decorator
