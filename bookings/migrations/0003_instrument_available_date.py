# Generated by Django 2.0.5 on 2018-05-18 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20180516_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='available_date',
            field=models.DateField(default=datetime.date(2018, 5, 18), verbose_name='Available Date'),
        ),
    ]