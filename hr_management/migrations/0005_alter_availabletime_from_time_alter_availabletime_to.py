# Generated by Django 4.2.6 on 2023-10-31 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_management', '0004_rename_postion_doctor_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='from_time',
            field=models.TimeField(default=datetime.time(16, 32, 50, 200639)),
        ),
        migrations.AlterField(
            model_name='availabletime',
            name='to',
            field=models.TimeField(default=datetime.time(16, 32, 50, 200639)),
        ),
    ]