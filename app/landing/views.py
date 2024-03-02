from django.shortcuts import render, get_object_or_404, redirect


from allauth.account.forms import LoginForm

# Create your views here.


def landing(request):
    """
        Landing page

        Provides the base login for the user base at all levels

    """

    login = LoginForm()

    template = 'landing.html'

    context = {
        'from_landing': True,
        'login': login,
    }

    return render(request, template, context)
