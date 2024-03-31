from django.db import models
from django.contrib.auth.models import User


# from driving_school.models import DrivingSchool

# Extend the base user and add user information
# Create your models here.


class UserManagement(User):
    """
        Extending base user class
    """

    phone_number = models.CharField(max_length=14, blank=True, null=True)
    gender = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)
    bio = models.TextField()
    # age = models.CharField(max_length=2, null=True, blank=True)


class Owner(UserManagement):
    """
        Driving school Owner model
    """

    # profile_pic = models.ImageField()
    area = models.CharField(max_length=25, blank=True, null=True)
    transmission = models.ForeignKey(
        'Transmission', on_delete=models.SET_NULL, null=True)
    car = models.CharField(max_length=50, blank=True, null=True)
    # car_image = models.ImageField()

    instructor = models.ForeignKey(
        'Instructors', on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(
        'Students', on_delete=models.SET_NULL, null=True)

    class Meta():
        verbose_name_plural = 'Driving Instructor\'s'
        verbose_name = 'Driving Instructor'

    def __str__(self):
        return self.name


class Instructors(UserManagement):
    """
        Driving instructor model
    """

    # profile_pic = models.ImageField()
    area = models.CharField(max_length=25, blank=True, null=True)
    transmission = models.ForeignKey(
        'Transmission', on_delete=models.SET_NULL, null=True)
    car = models.CharField(max_length=50, blank=True, null=True)
    # car_image = models.ImageField()

    student = models.ForeignKey(
        'Students', on_delete=models.SET_NULL, null=True)

    class Meta():
        verbose_name_plural = 'Driving Instructor\'s'
        verbose_name = 'Driving Instructor'

    def __str__(self):
        return self.name


class Students(UserManagement):
    """
        Student driver model
    """

    default_pickup_location = models.CharField(
        max_length=100, blank=True, null=True)
    secondary_pickup = models.CharField(max_length=100, blank=True, null=True)

    instructor = models.ForeignKey(
        'Instructors', on_delete=models.SET_NULL, null=True)

    class Meta():
        verbose_name_plural = 'Student Driver\'s'

    def __str__(self):
        return self.name


class Subscription(models.Model):
    """
        Subscription Tier model

        Tier 1:

        Basic app use
        30 students
        3 instructors

        Tier 2:

        Tier 1 +
        Finance app

        Tier 3:

        Tier 2 +
        Website development
        Website Hosting and setup
        Website Management
        Database Setup

    """


class Transmission(models.Model):
    """
        Transmission options for cars
    """

    transmission = models.CharField(max_length=15, blank=True, null=True)
    friendly = models.CharField(max_length=15, blank=True, null=True)

    def get_friendly(self):
        return self.friendly

    def __str__(self):
        return self.transmission

    class Meta():
        verbose_name_plural = 'Car Transmission'


class Gender(models.Model):
    """
        Gender model
    """

    gender = models.CharField(max_length=15, blank=True, null=True)
    pronouns = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.gender

    class Meta():
        verbose_name_plural = 'Gender Settings'
