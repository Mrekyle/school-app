from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """
        User Model
    """

    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        OWNER = "OWNER", "School Owner"
        INSTRUCTOR = "INSTRUCTOR", "Driving Instructor"
        STUDENT = "STUDENT", "Student DRIVER"

    base_role = Roles.STUDENT

    role = models.CharField(max_length=50, choices=Roles.choices)
