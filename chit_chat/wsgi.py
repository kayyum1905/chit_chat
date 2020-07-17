"""
WSGI config for chit_chat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import sensitive_file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ['MANAGE.PY_SETTINGS'])

application = get_wsgi_application()
