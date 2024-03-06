from django.shortcuts import render

# Create your views here.


def school_management(request):
    """
        Driving school Management hub of the application
    """

    template = 'school_management.html'

    context = {

    }

    return render(request, template, context)
