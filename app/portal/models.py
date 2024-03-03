import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


"""

    SCHOOL LOCATIONS

"""


class SchoolLocation(models.Model):
    """
        Driving school locations
    """

    base_location = models.CharField(max_length=50, blank=True, null=True)
    sub_location1 = models.CharField(max_length=50, blank=True, null=True)
    sub_location2 = models.CharField(max_length=50, blank=True, null=True)
    sub_location3 = models.CharField(max_length=50, blank=True, null=True)


"""

    DRIVING SCHOOL MODEL

"""


class DrivingSchool(models.Model):
    """
        Setting a driving school 

        Add finances onto the model or foreign key to another
        model in a separate app

        add students
    """

    date_created = models.DateField(blank=True, null=True)
    school_name = models.CharField(max_length=100, blank=True, null=True)
    school_website = models.CharField(max_length=100, blank=True, null=True)
    school_number = models.IntegerField(blank=True, null=True)
    school_email = models.EmailField(max_length=50, blank=True, null=True)
    school_location = models.ForeignKey(
        SchoolLocation, on_delete=models.SET_NULL)
    school_bio = models.TextField()
    school_owner = models.ForeignKey(Owner, on_delete=models.SET_NULL)
    instructors = models.ForeignKey(Instructor, on_delete=models.SET_NULL)


"""

    USER MODELS

"""


class User_Extended(AbstractUser):
    """
        User Model

        Add Other information here required for base user

        Inside of each level of user add required information for role
    """

    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        OWNER = "OWNER", "School Owner"
        INSTRUCTOR = "INSTRUCTOR", "Driving Instructor"
        STUDENT = "STUDENT", "Student DRIVER"

    base_role = Roles.ADMIN

    role = models.CharField(max_length=50, choices=Roles.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class StudentManager(BaseUserManager):
    """
        Filters all students
    """

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User_Extended.Roles.STUDENT)


class Student(User_Extended):
    """
        Builds a student profile
    """
    base_role = User_Extended.Roles.STUDENT
    student = StudentManager()
    age = models.IntegerField(null=True, blank=True)
    default_pickup = models.CharField(max_length=100, blank=True, null=True)
    secondary_pickup = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    driving_school = models.ForeignKey(
        DrivingSchool, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(Instructor, on_delete=models.SET_NULL)

    class Meta:
        proxy = True

    def welcome(self):
        return "Welcome new student"

    # Generate emails when created


class StudentProfile(models.Model):
    """
        Creates a student profile
    """

    user = models.OneToOneField(User_Extended, on_delete=models.CASCADE)
    student_id = models.IntegerField(null=True, blank=True)

    def gen_student_id():
        return uuid.uuid().hex.upper()

    def __str__(self):
        return self.student_id


@receiver(post_save, sender=Student)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'STUDENT':
        StudentProfile.objects.create(user=instance)


class InstructorManager(BaseUserManager):
    """
        Filters all students
    """

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User_Extended.Roles.INSTRUCTOR)


class Instructor(User_Extended):
    """
        Builds a instructor profile
    """

    base_role = User_Extended.Roles.INSTRUCTOR
    number = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    students = models.ForeignKey(Student, on_delete=models.SET_NULL)
    school = models.ForeignKey(DrivingSchool, on_delete=models.SET_NULL)

    instructor = InstructorManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Welcome new Instructor"


class InstructorProfile(models.Model):
    """
        Creates a Instructor profile
    """

    user = models.OneToOneField(User_Extended, on_delete=models.CASCADE)
    instructor_id = models.IntegerField(null=True, blank=True)

    def gen_INSTRUCTOR_id():
        return uuid.uuid().hex.upper()

    def __str__(self):
        return self.instructor_id


@receiver(post_save, sender=Instructor)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'INSTRUCTOR':
        InstructorProfile.objects.create(user=instance)


class OwnerManager(BaseUserManager):
    """
        Filters all students
    """

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User_Extended.Roles.INSTRUCTOR)


class Owner(User_Extended):
    """
        Builds a owner profile
    """

    base_role = User_Extended.Roles.OWNER
    phone_number = models.IntegerField(blank=True, null=True)
    driving_school = models.ForeignKey(DrivingSchool, on_delete=models.CASCADE)

    owner = OwnerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Welcome new Driving school Owner"


class OwnerProfile(models.Model):
    """
        Creates a Owner profile
    """

    user = models.OneToOneField(User_Extended, on_delete=models.CASCADE)
    owner_id = models.IntegerField(null=True, blank=True)

    def gen_owner_id():
        return uuid.uuid().hex.upper()

    def __str__(self):
        return self.owner_id


@receiver(post_save, sender=Owner)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'OWNER':
        OwnerProfile.objects.create(user=instance)
