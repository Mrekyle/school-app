from django.shortcuts import render

# Create your views here.


def landing(request):
    """
        Landing page

        Provides the base login for the user base at all levels

    """

    template = 'landing.html'

    context = {
        'from_landing': True,
    }

    return render(request, template, context)
