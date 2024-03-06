from django.shortcuts import render

# Create your views here.


def instructor_management(request):
    """
        Driving instructor management for the application
    """

    template = 'instructor_management.html'

    context = {

    }

    return render(request, template, context)
