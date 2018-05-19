
from __future__ import unicode_literals
from django.contrib import admin
from .models import Instrument, Project
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'TQ Instrument Administration'
    site_url = '/create_project'


class InstrumentAdmin(admin.ModelAdmin):
    list_display = ['__str__',
     'model', 'manufacturer', 'certificate_number', 'calibration_date', 'calibration_expiry_date']
    list_display_links = ['__str__']
    list_filter = ['calibration_expiry_date', 'certificate_number']
    search_fields = ['model', 'manufacturer', 'certificate_number', 'calibration_expiry_date']
    list_per_page = 10
    
    class Meta:
         model = Instrument

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'project_manag', 'project_id', 'expected_leaving_date', 'expected_return_date',]
    list_display_links = ['__str__']
    list_filter = ['project_manag', 'expected_return_date']
    search_fields = ['project_manag', 'project_id']
    list_per_page = 5

    class Meta:
         model = Project

admin_site = MyAdminSite(name='admin')
admin_site.register(Instrument, InstrumentAdmin)
admin_site.register(Project, ProjectAdmin)