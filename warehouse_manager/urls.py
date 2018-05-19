from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
from bookings.admin import admin_site


urlpatterns = [
    url(r'^admin/', admin_site.urls),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'', RedirectView.as_view(url='/accounts/login'), name='bookings'),
    url(r'', include("bookings.urls"), name='bookings'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
