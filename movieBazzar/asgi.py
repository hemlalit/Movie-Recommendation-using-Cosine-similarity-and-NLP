"""
ASGI config for movieBazzar project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieBazzar.settings')

port = os.environ.get('PORT', '8000')  # default to 8000 if not set
application = get_asgi_application()
