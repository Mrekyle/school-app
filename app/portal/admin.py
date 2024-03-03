from django.contrib import admin
from .models import Student, Instructor, Owner, DrivingSchool, SchoolLocation

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    """
        Student profile management
    """

    fields = ('username', 'first_name', 'last_name', 'driving_school',)


class InstructorAdmin(admin.ModelAdmin):
    """
        Driving Instructor profile management
    """

    fields = ('username', 'first_name', 'last_name', 'driving_school',)


class OwnerAdmin(admin.ModelAdmin):
    """
        Owner profile management
    """

    fields = ('username', 'first_name', 'last_name', 'driving_school',)


class SchoolAdmin(admin.ModelAdmin):
    """
        Driving school management
    """

    fields = ('school_name', 'school_email', 'school_number', 'school_owner')


class LocationAdmin(admin.ModelAdmin):
    """
        School Location management
    """

    fields = ('base_location', 'driving_school',)


admin.site.register(Student, StudentAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(DrivingSchool, SchoolAdmin)
admin.site.register(SchoolLocation, LocationAdmin)
