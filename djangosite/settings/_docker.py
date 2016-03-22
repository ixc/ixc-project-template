from ._base import *

# DJANGO ######################################################################

DATABASES['default'].update({
    'NAME': os.environ['PGDATABASE'],
    'HOST': os.environ['PGHOST'],
    'PORT': os.environ['PGPORT'],
    'USER': os.environ['PGUSER'],
})
