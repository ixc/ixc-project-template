"""
Settings that apply to a single deployment.

Rename to ``local.py`` and uncomment or edit to suite the local environment.
"""

from .base import *

### GLOBAL ####################################################################

# Settings you will probably want to change for all environments.

SITE_DOMAIN = 'localhost'
SITE_PORT = 8000

ADMINS = (
    ('Interaction Consortium', 'admins@interaction.net.au'),
)

ALLOWED_HOSTS += (
    SITE_DOMAIN,
)

DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'noreply@%s' % SITE_DOMAIN

### DEVELOPMENT ###############################################################

# Settings you might want to enable for development.

# DEBUG = True  # Show detailed error pages when exceptions are raised
# TEMPLATE_DEBUG = True  # Show details when exceptions are raised in templates

# CSRF_COOKIE_SECURE = False  # Don't require HTTPS for CSRF cookie
# SESSION_COOKIE_SECURE = False  # Don't require HTTPS for session cookie

### STAGING ###################################################################

# Settings you might want to enable for staging.

# URLOPEN_AUTH_CACHE = {
#     'realm@%s' % host: ('username', 'password') for host in ALLOWED_HOSTS
# }

### PRODUCTION ################################################################

# Settings you might want to enable for production.

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#     }
# }

# CONN_MAX_AGE = 60  # Enable persistent database connections

# DATABASES = {
#     'default': {
#         'ATOMIC_REQUESTS': True,
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'nsw-health',
#         'HOST': '',
#         'PORT': '',
#         'USER': '',
#         'PASSWORD': '',
#     }
# }

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Send emails

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'noreply@%s' % SITE_DOMAIN
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# Enable site-wide caching middleware.
# MIDDLEWARE_CLASSES = (
#     ('django.middleware.cache.UpdateCacheMiddleware', ) +
#     MIDDLEWARE_CLASSES +
#     ('django.middleware.cache.FetchFromCacheMiddleware', )
# )

# Enable cached template loader.
# TEMPLATE_LOADERS = (
#     ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
# )

### GENERIC ###################################################################

# Enable view profiling. Add `prof` key to querystring to see profiling results
# in your browser.
if DEBUG:
    MIDDLEWARE_CLASSES += ('generic.middleware.ProfileMiddleware', )

TEMPLATE_CONSTANTS.update({
    'SITE_DOMAIN': SITE_DOMAIN,
    'SITE_PORT': SITE_PORT,
})

### HOSTS #####################################################################

# PARENT_HOST = SITE_DOMAIN

### SENTRY ####################################################################

# See: https://sentry.ixcsandbox.com
SENTRY_DSN = ''
