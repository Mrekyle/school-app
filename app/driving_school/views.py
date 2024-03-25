from django.shortcuts import render

# Create your views here.


def school_management(request):
    """
        Driving school management home page.
    """

    template = 'school_management.html'

    context = {
        'admin': True,
    }

    return render(request, template, context)
