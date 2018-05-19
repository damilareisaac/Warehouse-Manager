from __future__ import unicode_literals
from django.db import models
import datetime

class Instrument(models.Model):
    instrument_id = models.CharField('Instrument ID', max_length=65, unique=True)
    item_id = models.CharField('Item ID', null=True, blank=True, max_length=65)
    description = models.TextField('Description', null=True, blank=True,max_length=100)
    manufacturer = models.CharField('Manufacturer', null=True, blank=True, max_length=65)
    model = models.CharField('Model', null=True, blank=True, max_length=65)
    serial_number = models.CharField('Serial Number',null=True, blank=True, max_length=65)
    certificate_number = models.CharField('Certificate Number', null=True, blank=True,  max_length=65)
    min_operating_range = models.PositiveIntegerField('Minimum Operating Range',null=True, blank=True)
    max_operating_range = models.PositiveIntegerField('Maximum Operating Range', null=True, blank=True)
    tolerance = models.PositiveIntegerField('Tolerance', null=True, blank=True)
    calibration_date = models.DateField('Calibration Date', null=True, blank=True)
    calibration_expiry_date = models.DateField('Calibration Expiry Date', null=True, blank=True)
    available_date = models.DateField('Available Date', default=datetime.date.today())
    location = models.CharField('Location',null=True, blank=True, max_length=100)
    value = models.PositiveIntegerField('Value',null=True, blank=True)
    calibration_cost = models.PositiveIntegerField('Calibration Cost', null=True, blank=True)
    # python 3.x
    def __str__(self):
        return self.instrument_id




class Project(models.Model):
    instruments = models.ManyToManyField(Instrument)
    project_id = models.CharField('Project ID', max_length=45, unique=True)
    project_manag = models.CharField('Project Manager', max_length=80)
    expected_leaving_date = models.DateField('Expected Leaving Date')
    expected_return_date = models.DateField('Expected Return Date')

    # @classmethod
    # def add_instrument(cls, current_project, instrument):
    #     instrument, created = cls.objects.get_or_create(instrument_id=instrument_id)
    
     # python 3.x
    def __str__(self):
        return self.project_id

    

