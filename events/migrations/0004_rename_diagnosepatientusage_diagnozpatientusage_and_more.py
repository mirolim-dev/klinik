# Generated by Django 4.2.6 on 2023-11-02 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_management', '0010_alter_availabletime_from_time_alter_availabletime_to'),
        ('events', '0003_diagnoz_description_diagnoz_name_diagnoz_price_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DiagnosePatientUsage',
            new_name='DiagnozPatientUsage',
        ),
        migrations.RenameModel(
            old_name='DiagnoseProductUsage',
            new_name='DiagnozProductUsage',
        ),
        migrations.AlterModelOptions(
            name='diagnoz',
            options={'verbose_name_plural': 'Diagnoses'},
        ),
    ]
