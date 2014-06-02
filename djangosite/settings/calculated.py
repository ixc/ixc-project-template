"""
Settings that are automatically calculated from other settings.
"""
from .local import *

### IXC PROJECT ###############################################################

SITE_URL = 'http://%s' % SITE_DOMAIN

TEMPLATE_CONSTANTS.update({
    'SITE_URL': SITE_URL,
    'SITE_NAME': SITE_NAME,
})

### DJANGO CORE ###############################################################

ALLOWED_HOSTS += (SITE_DOMAIN, )
TEMPLATE_DEBUG = DEBUG

### DEBUG TOOLBAR #############################################################

DEBUG_TOOLS = DEBUG # Use debug toolbar.

if DEBUG:
    INSTALLED_APPS += ('debug_toolbar', )

    # You should include the Debug Toolbar middleware as early as possible in
    # the list. However, it must come after any other middleware that encodes
    # the response's content, such as GZipMiddleware.
    MIDDLEWARE_CLASSES = \
        ('debug_toolbar.middleware.DebugToolbarMiddleware', ) + \
        MIDDLEWARE_CLASSES

### EASY THUMBNAILS ###########################################################

THUMBNAIL_DEBUG = DEBUG

### SENTRY ####################################################################

if DEBUG:
    RAVEN_CONFIG = {}

### SUIT ######################################################################

SUIT_CONFIG['ADMIN_NAME'] = '%s Admin' % SITE_NAME
