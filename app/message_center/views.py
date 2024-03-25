from django.shortcuts import render

# Create your views here.


def message_center(request):
    """
        Message center Home 
    """

    template = 'message_center.html'

    context = {
        'admin': True,
    }

    return render(request, template, context)
