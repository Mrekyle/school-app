from django.contrib import admin
from .models import Student, Instructor, Owner

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    """
        Student profile management
    """

    # fields = ('username', 'first_name', 'last_name',)


class InstructorAdmin(admin.ModelAdmin):
    """
        Driving Instructor profile management
    """

    fields = ('username', 'first_name', 'last_name',)


class OwnerAdmin(admin.ModelAdmin):
    """
        Owner profile management
    """

    fields = ('username', 'first_name', 'last_name',)


admin.site.register(Student, StudentAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Owner, OwnerAdmin)
