from django.db import models

from portal.models import Instructors, Students, Subscription

# Create your models here.


class DrivingSchool(models.Model):
    """
        Driving schools model
    """

    date_joined = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    school_email = models.EmailField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, null=True, blank=True)

    franchise_fee = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, default=0)
    # lesson_types = models.ForeignKey(
    #     'LessonTypes', on_delete=models.CASCADE, null=True, blank=True)

    # students = models.ForeignKey(Students, on_delete=models.CASCADE)
    # instructors = models.ForeignKey(Instructors, on_delete=models.CASCADE)
    # subscription_plan = models.ForeignKey(
    # Subscription, on_delete=models.CASCADE)

    class Meta():
        """
            Setting Admin Names
        """

        verbose_name_plural = 'Driving School\'s'
        verbose_name = 'Driving School'

    def __str__(self):
        return self.name


class Locations(models.Model):
    """
        Driving school Locations
    """

    school = models.ForeignKey(
        'DrivingSchool', on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=25, blank=True, null=True)

    class Meta():
        verbose_name_plural = 'School Locations'

    def __str__(self):
        return self.school


class LessonTypes(models.Model):
    """
        Driving school lesson types

        Add lesson types 
    """

    school = models.ForeignKey(
        'DrivingSchool', on_delete=models.SET_NULL, null=True)

    class Meta():

        verbose_name_plural = 'Lesson Type\'s'
        verbose_name = 'Lesson Type'
