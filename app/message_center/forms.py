from django import forms
from .models import Support, SupportReason


class SupportForm(forms.ModelForm):
    """
        Customer support form
    """

    class Meta():
        model = Support
        fields = ('name', 'email', 'reason', 'text_field')

    def __init__(self, *args, **kwargs):
        """
            Setting classes and placeholders and autofocus
        """

        super().__init__(*args, **kwargs)
        support_reason = SupportReason.objects.all()

        # Friendly name for reasons
        reason = [(c.id, c.get_friendly()) for c in support_reason]

        self.fields['name'].autofocus = True

        self.fields['name'].widget.attrs['placeholder'] = 'John Smith'
        self.fields['email'].widget.attrs['placeholder'] = 'john.smith@example.com'
        self.fields['text_field'].widget.attrs['placeholder'] = 'Enter your message here....'
        # self.fields['driving_school'].widget.attrs['placeholder'] = 'Your driving school'

        # Setting base class and reasons to support form
        for field in self.fields:
            self.fields['reason'].choices = reason
            self.fields[field].widget.attrs['class'] = 'rounded-1 mb-2 form-control'
            self.fields[field].label = False
