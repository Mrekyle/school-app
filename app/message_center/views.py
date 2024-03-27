from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from .models import Support
from .forms import SupportForm

from django.contrib.auth.decorators import login_required
from portal.decorators import admin_only

# Create your views here.


@login_required(login_url='landing')
@admin_only
def message_center(request):
    """
        Message center Home 
    """

    form = SupportForm
    model = Support

    template = 'message_center.html'

    context = {
        'admin': True,
        'form': form,
        'model': model
    }

    return render(request, template, context)


@login_required(login_url='landing')
def support(request):
    """
        User Support Form

        Form validation 

        Handling the sending of emails to the admin
        Emails to the user if they request a copy
    """

    form = SupportForm

    if request.method == 'POST':
        form = SupportForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                support_form = form.save()
                messages.success(
                    request, f'Thank you for contacting us. We will get back to you as soon as our team have reviewed your email.')

                name = form.cleaned_data('name')
                email = form.cleaned_data('email')
                reason = form.cleaned_data('reason')
                text = form.cleaned_data('text_field')
                subject = f'New Support Request from {name}'
                subject_copy = f'COPY: {subject}'
                send_copy = request.post.get('send-copy')

                """
                    Contact email
                """
                contact_email = f"""
                    {subject}
                    --------------------------------------------

                    New Support Request:

                    Name: {name}
                    Reason: {reason}
                
                    {text}

                    ---------------------------------------------

                    Please reply to {email}

                    """

                send_mail(
                    subject=subject,
                    message=contact_email,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL]
                )

                if send_copy == 'on':
                    """
                        Send a copy to the user
                    """
                    user_copy = f"""
                        {subject}
                        --------------------------------------------

                        Hello {name}, Here is a copy of the request you sent.

                        New Support Request:

                        Name: {name}
                        Reason: {reason}
                    
                        {text}

                        ---------------------------------------------

                        If everything seems correct, then please wait for us to get back to you.
                        
                        If something seems wrong please submit another contact request.
                        
                        """

                    send_mail(
                        subject=subject_copy,
                        message=contact_email,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[email]
                    )

    template = 'support.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
