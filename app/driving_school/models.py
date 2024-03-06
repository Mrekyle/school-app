# from django.db import models

# from portal.models import Student, Instructor, Owner

# # Create your models here.

# """

#     SCHOOL LOCATIONS

# """


# class SchoolLocation(models.Model):
#     """
#         Driving school locations
#     """

#     base_location = models.CharField(max_length=50, blank=True, null=True)
#     sub_location1 = models.CharField(max_length=50, blank=True, null=True)
#     sub_location2 = models.CharField(max_length=50, blank=True, null=True)
#     sub_location3 = models.CharField(max_length=50, blank=True, null=True)


# """

#     DRIVING SCHOOL MODEL

# """


# class DrivingSchool(models.Model):
#     """
#         Setting a driving school

#         Add finances onto the model or foreign key to another
#         model in a separate app

#         add students
#     """

#     date_created = models.DateField(blank=True, null=True)
#     school_name = models.CharField(max_length=100, blank=True, null=True)
#     school_website = models.CharField(max_length=100, blank=True, null=True)
#     school_number = models.IntegerField(blank=True, null=True)
#     school_email = models.EmailField(max_length=50, blank=True, null=True)
#     school_location = models.ForeignKey(
#         SchoolLocation, on_delete=models.CASCADE)
#     school_bio = models.TextField()
#     school_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
#     instructors = models.ForeignKey(Instructor, on_delete=models.CASCADE)
