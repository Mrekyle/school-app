from django.shortcuts import render


def handler404(request, exception):
    """
        Handles the 404 error 
    """

    template = 'errors/404.html'

    context = {

    }

    return render(request, template, context)


def handler500(request):
    """
        Handles the 500 error
    """

    template = 'errors/500.html'

    context = {

    }

    return render(request, template, context)
