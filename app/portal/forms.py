from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import UserManagement, Owner, Students, Instructors
from driving_school.models import DrivingSchool


class CreateCustomUser(UserCreationForm):
    """
        Custom user creation form
    """

    group_choices = {
        'student': 'Student',
        'instructor': 'Instructor',
        'owner': 'Owner'
    }

    username = forms.CharField(
        label='username', min_length=2, max_length=25)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)
    group = forms.ChoiceField(
        widget=forms.Select, choices=(['Student', 'Student'], ['Instructor', 'Instructor'], ['Owner', 'Owner']), required=True, label='User group')
    # school = forms.ChoiceField(
    #     widget=forms.Select, choices=DrivingSchool, required=True)

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = UserManagement.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = UserManagement.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def group_clean(self):
        group = self.cleaned_data['group'].lower()
        new = UserManagement.objects.filter(group=group)
        if new.count():
            raise ValidationError("Group doesn\'t exist")
        return group

    def save(self, commit=True):
        user = UserManagement.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class CreateStudent(forms.ModelForm):
    class Meta():
        model = Students
        fields = ['default_pickup_location',]

    group = forms.ChoiceField(
        widget=forms.Select, choices=(['Student', 'Student'],), required=True, label='User group')


class CreateInstructor(forms.ModelForm):
    class Meta():
        model = Instructors
        fields = ['car',]

    group = forms.ChoiceField(
        widget=forms.Select, choices=(['Instructor', 'Instructor'],), required=True, label='User group')


class CreateOwner(forms.ModelForm):
    class Meta():
        model = Owner
        fields = ['car',]

    group = forms.BooleanField()
