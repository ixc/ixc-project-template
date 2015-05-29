"""
PostgreSQL test settings for ``{{ project_name }}`` project.
"""

from {{ project_name }}.tests.settings import *

DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
    }
}
