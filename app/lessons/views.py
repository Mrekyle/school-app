from django.shortcuts import render

# Create your views here.


def lesson_management(request):
    """
        Driving lesson management
    """

    template = 'lesson_management.html'

    context = {

    }

    return render(request, template, context)
