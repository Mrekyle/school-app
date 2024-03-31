# Generated by Django 4.2.9 on 2024-03-31 16:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrivingSchool',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('school_email', models.EmailField(blank=True, max_length=30, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('website', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('franchise_fee', models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True)),
            ],
            options={
                'verbose_name': 'Driving School',
                'verbose_name_plural': "Driving School's",
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=25, null=True)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='driving_school.drivingschool')),
            ],
            options={
                'verbose_name_plural': 'School Locations',
            },
        ),
        migrations.CreateModel(
            name='LessonTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='driving_school.drivingschool')),
            ],
            options={
                'verbose_name': 'Lesson Type',
                'verbose_name_plural': "Lesson Type's",
            },
        ),
    ]
