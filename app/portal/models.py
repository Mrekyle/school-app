from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Extend the base user and add user information
# Create your models here.


class Instructors(models.Model):
    """
        Driving instructor model
    """


class Students(models.Model):
    """
        Student driver model
    """


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
