from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from portal.decorators import unauthenticated_user

# Create your views here.


@unauthenticated_user
def landing(request):
    """
        Landing page

        Provides the base login for the users at all user levels

        Handles user authentication manually
        Checking the users group and directing based on user group

    """
    """
        Handling manual authentication of a user by checking user and pass
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('portal')
        else:
            messages.info(
                request, f'Username or Password is incorrect. Please try again.')

    template = 'landing.html'

    context = {
    }

    return render(request, template, context)


def logoutUser(request):
    """
        Handles the user logging out of the application

        By redirecting them to the home page of the app.
    """
    logout(request)
    return redirect('landing')
