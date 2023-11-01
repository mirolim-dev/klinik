# Generated by Django 4.2.6 on 2023-11-01 14:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_room_roomstuff'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomstuff',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roomstuff',
            name='name',
            field=models.CharField(default='name', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roomstuff',
            name='quantity',
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roomstuff',
            name='room',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='departments.room'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(default='Room 5-45A', max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_beds', models.PositiveBigIntegerField(default=1)),
                ('price_for_one_day', models.DecimalField(decimal_places=2, default=0.0, max_digits=25)),
                ('status', models.IntegerField(choices=[(0, 'Available'), (1, 'Occupied')], default=1)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='departments.department')),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='departments.room')),
            ],
            options={
                'ordering': ['status'],
            },
        ),
    ]
