import os

from django.core.exceptions import ImproperlyConfigured

try:
    from .local import *
except ImportError:
    path = os.path.relpath(os.path.dirname(__file__))
    message = """
You MUST **review and uncomment** the appropriate environment specific
configuration in the local settings module:

    (venv)$ cp {path}/local.tmpl.py {path}/local.py
    (venv)$ $EDITOR {path}/local.py
"""
    raise ImproperlyConfigured(message.format(path=path))
