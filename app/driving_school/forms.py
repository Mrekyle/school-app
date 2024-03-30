from django import forms

from driving_school.models import DrivingSchool, Locations, LessonTypes


class DrivingSchoolForm(forms.ModelForm):
    """
        Add new driving school 
    """

    class Meta():
        model = DrivingSchool
        fields = ('name', 'school_email', 'website',
                  'phone_number', 'location')

    def __init__(self, *args, **kwargs):
        """
            Setting form classes, placeholders and autofocus
        """

        super().__init__(*args, **kwargs)

        self.fields['name'].autofocus = True


class FranchiseFee(forms.ModelForm):
    """
        Set a new franchise fee
    """

    class Meta():
        model = DrivingSchool
        fields = ('franchise_fee',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['franchise_fee'].autofocus = True
