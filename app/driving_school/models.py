# from django.db import models

# # Create your models here.


# class DrivingSchool(models.Model):
#     """
#         Driving schools model
#     """

#     date_joined = models.DateField()
#     name = models.CharField()
#     school_email = models.EmailField()
#     phone_number = models.CharField()
#     website = models.CharField()
#     location = models.CharField()

#     franchise_fee = models.CharField()
#     lesson_types = models.CharField()

#     students = models.CharField()
#     instructors = models.CharField()
#     subscription_plan = models.CharField()

#     class Meta():
#         """
#             Setting Admin Names
#         """

#         verbose_name_plural = 'Driving School\'s'
#         verbose_name = 'Driving School'

#     def __str__(self):
#         return self.name
