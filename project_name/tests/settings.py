"""
Test settings for ``{{ project_name }}`` project.
"""

from djangosite.settings.local_sample import *

DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS += (
    '{{ project_name }}.tests',
)
