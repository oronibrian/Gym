# Generated by Django 2.0.3 on 2018-04-27 05:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0021_member_medical_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='dob',
            field=models.DateField(default=datetime.datetime(2018, 4, 27, 11, 2, 3, 303759)),
        ),
    ]