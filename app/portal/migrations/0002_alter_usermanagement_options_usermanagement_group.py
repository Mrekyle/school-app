# Generated by Django 4.2.9 on 2024-04-01 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermanagement',
            options={'verbose_name_plural': 'User Management'},
        ),
        migrations.AddField(
            model_name='usermanagement',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group'),
        ),
    ]