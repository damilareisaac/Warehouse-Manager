from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import (dashboard, create_project, book_instruments,
 edit_bookings, coming_soon)

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^accounts/login/', login, {'template_name':'account/login.html'}, name='login'),
    url(r'^accounts/logout/', logout, {'template_name':'account/login.html'}, name='logout'),
    url(r'^create_project/', create_project, name='create project'),
    url(r'^book_instruments', book_instruments, name='book instruments'),
    url(r'^edit_bookings', edit_bookings, name='edit_bookings'),
    url(r'^coming_soon', coming_soon, name='coming_soon')
]
