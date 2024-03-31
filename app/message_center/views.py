from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from .models import Support
from .forms import SupportForm

from django.contrib.auth.decorators import login_required
from portal.decorators import admin_only, allowed_users

# Create your views here.


@login_required(login_url='landing')
@allowed_users(allowed_roles=['admin', 'owners', 'instructors'])
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
                support_form = form.save(commit=True)
                messages.success(
                    request, f'Thank you for contacting us. We will get back to you as soon as our team have reviewed your email.')

                name = request.POST.get('name')
                email = request.POST.get('email')
                # driving_school = form.cleaned_data['driving_school']
                reason = form.cleaned_data['reason']
                text = request.POST.get('text_field')
                subject = f'New Support Request from {name}'
                subject_copy = f'COPY: {subject}'
                send_copy = request.POST.get('send-copy')

                """
                    Contact email
                """
                contact_email = f"""
                    {subject}
                    --------------------------------------------

                    New Support Request:

                    Name: {name}
                    Driving School: 
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
                        Driving School: 
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
            else:
                messages.error(
                    request, f'Oop\'s.. something has gone wrong. Please check the form and try again')
                return redirect('support')

    template = 'support.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
