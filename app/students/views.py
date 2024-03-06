from django.shortcuts import render

# Create your views here.


def student_management(request):
    """
        Student management for the application
    """

    template = 'student_management.html'

    context = {

    }

    return render(request, template, context)
