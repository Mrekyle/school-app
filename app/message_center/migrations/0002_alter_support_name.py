# Generated by Django 4.2.9 on 2024-03-27 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_center', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
