from ._base import *

# DJANGO ######################################################################

ALLOWED_HOSTS = ('*', )  # Allow connections on any host name

CSRF_COOKIE_SECURE = False  # Don't require HTTPS for CSRF cookie
SESSION_COOKIE_SECURE = False  # Don't require HTTPS for session cookie

DEBUG = True  # Show detailed error pages when exceptions are raised

# MASTER PASSWORD #############################################################

MASTER_PASSWORD = 'abc123'

# SUPERVISOR ##################################################################

WSGI_ADDRESS = '0.0.0.0'  # Default: 127.0.0.1
WSGI_WORKERS = 2  # Default: 2x CPU cores + 1
SUPERVISOR.update({
    'exclude_autoreload': False,
})
