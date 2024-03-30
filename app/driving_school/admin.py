from django.contrib import admin

from .models import DrivingSchool, Locations, LessonTypes

# Register your models here.


class SchoolAdmin(admin.ModelAdmin):
    """
        Driving school Admin
    """

    list_display = ('date_joined', 'name', 'school_email', 'phone_number')


class LocationAdmin(admin.ModelAdmin):
    """
        School Locations Admin
    """

    list_display = ('school', 'location',)


class lessonTypeAdmin(admin.ModelAdmin):
    """
        Lesson Types Admin
    """

    list_display = ('school',)


admin.site.register(DrivingSchool, SchoolAdmin)
admin.site.register(Locations, LocationAdmin)
admin.site.register(LessonTypes, lessonTypeAdmin)
