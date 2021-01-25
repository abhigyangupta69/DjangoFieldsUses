# Generated by Django 3.1.5 on 2021-01-21 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0007_auto_20210121_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='user',
            field=models.OneToOneField(default=False, limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
