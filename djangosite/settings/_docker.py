from ._base import *

# Variable files. Logs, media, etc.
VAR_DIR = os.path.join(BASE_DIR, 'var')

# Create var directories that are expected to exist at runtime.
for dirname in ('logs', 'run'):
    try:
        os.makedirs(os.path.join(VAR_DIR, dirname))
    except OSError:
        pass

SECRET_FILE = os.path.join(VAR_DIR, 'secret.txt')

# DJANGO ######################################################################

DATABASES['default'].update({
    'NAME': os.environ['PGDATABASE'],
    'HOST': os.environ['PGHOST'],
    'PORT': os.environ['PGPORT'],
    'USER': os.environ['PGUSER'],
})

LOGGING['handlers']['logfile']['filename'] = \
    os.path.join(VAR_DIR, 'logs', '{{ project_name }}.log')

MEDIA_ROOT = os.path.join(VAR_DIR, 'media')
STATIC_ROOT = os.path.join(VAR_DIR, 'static')
