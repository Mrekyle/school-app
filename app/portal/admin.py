from django.contrib import admin

from .models import UserManagement, Owner, Instructors, Students

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    """
        User admin
    """

    list_display = ('username',)


admin.site.register(UserManagement, UserAdmin)
