from django.shortcuts import render

# Create your views here.


def finance_management(request):
    """
        App Finance management home
    """

    template = 'finance_management.html'

    context = {
        'admin': True,
    }

    return render(request, template, context)
