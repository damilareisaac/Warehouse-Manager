from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from .models import Instrument, Project
import datetime
from time import sleep
import dateutil.parser as parser

def coming_soon(request):
    if request.user.is_authenticated:
        context = {
            'current_user': request.user,
            'page_title': 'Coming Soon'
            }
        return render(request, 'coming_soon.html', context)
    else:
        return redirect('/accounts/login')  

def dashboard(request):
    if request.user.is_authenticated:
        context = {
            'current_user': request.user,
            'page_title': 'Dashboard'
            }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/accounts/login')  

def create_project(request):
    if request.user.is_authenticated:
        crypt = get_random_string(length=12)
        project_key = 'PRJ_' + crypt.upper()
        if request.method == 'POST':
            project = dict(request.POST)
            
            new_project = Project(
                project_id = project['project_id'][-1],
                project_manag = project['project_manager'][-1],
                expected_leaving_date = parser.parse(project['expected_leaving_date'][-1]),
                expected_return_date = parser.parse(project['expected return date'][-1]))
            request.session['project id'] = request.POST['project_id']
            new_project.save()
            return redirect('/book_instruments')
        context = {
        'page_title': 'Create Project',
        'form_title': 'Create New Project',
        'current_user': request.user,
        'project_id': project_key
        }
        return render(request, 'bookings/project.html', context)
    else:
        return redirect('/accounts/login')

def book_instruments (request):
    if request.user.is_authenticated:
        project_id = request.session.get('project id')
        post_to_DB = False
        if project_id:
            current_project = Project.objects.get(project_id=project_id)
            instrument_list = Instrument.objects.all()
            today = datetime.datetime.today()
            instrument_list = instrument_list.filter(calibration_expiry_date__gt=today)
            instrument_list = instrument_list.filter(available_date__lte=today)
            query = request.GET.get('q')
            if query:
                instrument_list = instrument_list.filter(
                    Q(instrument_id__icontains=query) |
                    Q(model__icontains=query) |
                    Q(manufacturer__icontains=query) |
                    Q(certificate_number__icontains=query)
                )
            if request.method == 'POST':
                if 'booked' in dict(request.POST):
                    instrument_selected = dict(request.POST)['booked']
                    for i in instrument_selected:
                        instrument = Instrument.objects.get(instrument_id=i)
                        current_project.instruments.add(instrument)
                        instrument.available_date = current_project.expected_return_date
                    # request.session['project id'] = ''
                    post_to_DB = True
            context = {
            'instrument': instrument_list,
            'page_title': 'Book Instruments',
            'form_title': 'Book Instruments for Project',
            'current_project': current_project,
            'current_user': request.user,
            'post_to_DB': post_to_DB,
            'sucess_message': '... Instrument(s) is sucessful added to project.....'
            }
        else:
            return redirect('/create_project')
        return render(request, 'bookings/instruments.html', context)
    else:
        return redirect('/accounts/login')

def edit_bookings(request):
    if request.user.is_authenticated:
        project_id = request.session.get('project id')
        post_to_DB = False
        if project_id:
            all_projects = Project.objects.all()
            current_project = Project.objects.get(project_id=project_id)
            booked_instruments = current_project.instruments.all()

            if request.method == 'POST':
                if 'selected_project' in dict(request.POST):
                    selected_project = dict(request.POST)['selected_project'][0]
                    print(selected_project)
                    current_project = Project.objects.get(project_id=selected_project)
                    request.session['project id'] = request.POST['selected_project']
            booked_instruments = current_project.instruments.all()

            query = request.GET.get('q')
            if query:
                booked_instruments = booked_instruments.filter(
                    Q(instrument_id__icontains=query) |
                    Q(model__icontains=query) |
                    Q(manufacturer__icontains=query) |
                    Q(certificate_number__icontains=query)
                )
            if request.method == 'POST':
                if 'booked' in dict(request.POST):
                    instrument_selected = dict(request.POST)['booked']
                    for i in instrument_selected:
                        instrument = Instrument.objects.get(instrument_id=i)
                        current_project.instruments.remove(instrument)
                    post_to_DB = True
            context = {
            'instrument': booked_instruments,
            'page_title': 'Edit Booked Instruments',
            'form_title': 'Edit Booked Instruments',
            'current_project': current_project,
            'all_projects': all_projects,
            'current_user': request.user,
            'post_to_DB': post_to_DB,
            'sucess_message': '... Delete Successful.....'
            }
        else:
            return redirect('/create_project')
        return render(request, 'bookings/instruments.html', context)
    else:
        return redirect('/accounts/login')