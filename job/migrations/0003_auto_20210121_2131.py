# Generated by Django 3.1.5 on 2021-01-21 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_jobapplication_location'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='jobapplication',
            table='JobApplication',
        ),
    ]