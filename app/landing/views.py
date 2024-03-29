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

        """
        
        Filtering each users groups to check what portal they have access to

        Then authenticating the user and sending them to the correct portal.
        Providing the login details match and are able to be

        """

        admin = user.groups.filter(name='admin').exists()
        owner = user.groups.filter(name='owner').exists()
        instructor = user.groups.filter(name='instructor').exists()
        student = user.groups.filter(name='student').exists()

        if admin:
            login(request, user)
            return redirect('admin_portal')
        elif owner:
            login(request, user)
            return redirect('owner_portal')
        elif instructor:
            login(request, user)
            return redirect('instructor_portal')
        elif student:
            login(request, user)
            return redirect('student_portal')
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

        By redirecting them to the base landing page of the app.
    """
    logout(request)
    return redirect('landing')
