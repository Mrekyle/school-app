from django.db import models

# Create your models here.


class Support(models.Model):
    """
        Support message model
    """

    name = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    driving_school = models.TextField(max_length=25, blank=True, null=True)
    reason = models.ForeignKey(
        'SupportReason', on_delete=models.SET_NULL, null=True, blank=True)
    text_field = models.TextField()

    class Meta():
        verbose_name_plural = 'Support Message\'s'
        verbose_name = 'Support Message'

    def __str__(self):
        return self.name


class SupportReason(models.Model):
    """
        Support Reasons
    """

    reason = models.CharField(max_length=50, blank=True, null=True)
    friendly_reason = models.CharField(max_length=50, blank=True, null=True)

    class Meta():
        verbose_name_plural = 'Support Reason\'s'

    def get_friendly(self):
        return self.friendly_reason

    def __str__(self):
        return self.reason
