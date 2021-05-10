"""
WSGI config for penetrance_platform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.abspath(__file__ + '/..'))
sys.path.append(os.path.abspath(__file__ + '/../..'))
sys.path.append(os.path.abspath(__file__ + '/../../..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'penetrance_platform.config.settings')

application = get_wsgi_application()
