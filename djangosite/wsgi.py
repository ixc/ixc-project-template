"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Serve static files from installed app `static` directories when `DEBUG=True`.
# Avoids the need to run the `collectstatic` management command.
from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler

if settings.DEBUG:
    application = StaticFilesHandler(application)
