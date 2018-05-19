# Generated by Django 2.0.5 on 2018-05-16 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument_id', models.CharField(max_length=65, verbose_name='Instrument ID')),
                ('item_id', models.CharField(max_length=65, null=True, verbose_name='Item ID')),
                ('description', models.TextField(max_length=100, null=True, verbose_name='Description')),
                ('manufacturer', models.CharField(max_length=65, null=True, verbose_name='Manufacturer')),
                ('model', models.CharField(max_length=65, null=True, verbose_name='Model')),
                ('serial_number', models.CharField(max_length=65, null=True, verbose_name='Serial Number')),
                ('certificate_number', models.CharField(max_length=65, null=True, verbose_name='Certificate Number')),
                ('min_operating_range', models.PositiveIntegerField(null=True, verbose_name='Minimum Operating Range')),
                ('max_operating_range', models.PositiveIntegerField(null=True, verbose_name='Maximum Operating Range')),
                ('tolerance', models.PositiveIntegerField(null=True, verbose_name='Tolerance')),
                ('calibration_date', models.DateField(null=True, verbose_name='Calibration Date')),
                ('calibration_expiry_date', models.DateField(null=True, verbose_name='Calibration Expiry Date')),
                ('location', models.CharField(max_length=100, null=True, verbose_name='Location')),
                ('value', models.PositiveIntegerField(null=True, verbose_name='Value')),
                ('calibration_cost', models.PositiveIntegerField(null=True, verbose_name='Calibration Cost')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=45, verbose_name='Project ID')),
                ('project_manag', models.CharField(max_length=80, verbose_name='Project Manager')),
                ('expected_leaving_date', models.DateField(verbose_name='Expected Leaving Date')),
                ('expected_return_date', models.DateField(verbose_name='Expected Return Date')),
                ('instruments', models.ManyToManyField(to='bookings.Instrument')),
            ],
        ),
    ]
