"""
WSGI config for warehouse_manager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "warehouse_manager.settings")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
application = get_wsgi_application()
