from django.contrib import admin
from .models import Support, SupportReason

# Register your models here.


class SupportAdmin(admin.ModelAdmin):
    """
        Admin support 
    """

    list_display = ('name', 'email', 'reason',)


class SupportReasonAdmin(admin.ModelAdmin):
    """"
        Support Reasons Admin
    """

    list_display = ('reason',)


admin.site.register(Support, SupportAdmin)
admin.site.register(SupportReason, SupportReasonAdmin)
