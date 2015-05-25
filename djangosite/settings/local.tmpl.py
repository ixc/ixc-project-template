"""
Settings that apply to a single deployment.

Rename to ``local.py`` and uncomment or edit to suite the local environment.
"""

import django

from .base import *

# GLOBAL ######################################################################

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

# DEVELOPMENT #################################################################

# Settings you might want to enable for development.

# DEBUG = True  # Show detailed error pages when exceptions are raised
# TEMPLATE_DEBUG = True  # Show details when exceptions are raised in templates

# CSRF_COOKIE_SECURE = False  # Don't require HTTPS for CSRF cookie
# SESSION_COOKIE_SECURE = False  # Don't require HTTPS for session cookie

# MASTER_PASSWORDS.update({
#     'abc123': lambda u: DEBUG,  # Only when `DEBUG=True`.
# })

# STAGING #####################################################################

# Settings you might want to enable for staging.

# URLOPEN_AUTH_CACHE = {
#     'realm@%s' % host: ('username', 'password') for host in ALLOWED_HOSTS
# }

# PRODUCTION ##################################################################

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
#         'NAME': '{{ project_name }}',
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
# TEMPLATE_DJANGO['OPTIONS']['loaders'] = [
#     ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
# ]

# GENERIC #####################################################################

# Enable view profiling. Add `prof` key to querystring to see profiling results
# in your browser.
# if DEBUG:
#     MIDDLEWARE_CLASSES += ('generic.middleware.ProfileMiddleware', )

# TEMPLATE_CONSTANTS.update({
#     'SITE_DOMAIN': SITE_DOMAIN,
#     'SITE_PORT': SITE_PORT,
# })

# HOSTS #######################################################################

# PARENT_HOST = SITE_DOMAIN

# MASTER PASSWORD #############################################################

# Only use clear text passwords for local development. Use the `make_password
# management command to generated hashed passwords for production and staging.

MASTER_PASSWORDS.update({
    # 'abc123': lambda u: DEBUG,  # Only when `DEBUG=True`.
})

# SENTRY ######################################################################

# See: https://sentry.ixcsandbox.com
SENTRY_DSN = ''

# SUPERVISOR ##################################################################

SUPERVISOR.update({
    'GUNICORN_ADDRESS': '127.0.0.1:%s' % SITE_PORT,  # Default: 127.0.0.1:8000
    # 'GUNICORN_WORKERS': N,  # Default: 2x CPU cores + 1
})

# CALCULATED ##################################################################

# Settings that are calculated from the value of other settings.

# De-dupe installed apps.
_seen = set()
INSTALLED_APPS = [
    app for app in INSTALLED_APPS if app not in _seen and not _seen.add(app)
]

# Enable template backends.
TEMPLATES = [TEMPLATES_DJANGO, TEMPLATES_JINJA2]

# OLDER DJANGO ################################################################

# Calculate settings that are required for older versions of Django.

if django.VERSION[:2] == (1, 7):

    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
    MIDDLEWARE_CLASSES.remove('django.middleware.security.SecurityMiddleware')

    SILENCED_SYSTEM_CHECKS = (
        '1_6.W002',
    )

    TEMPLATE_DIRS = TEMPLATES_DJANGO['DIRS']

    TEMPLATE_CONTEXT_PROCESSORS = []
    for cp in TEMPLATES_DJANGO['OPTIONS']['context_processors']:
        TEMPLATE_CONTEXT_PROCESSORS.append(
            cp.replace('django.template', 'django.core'))

    TEMPLATE_LOADERS = TEMPLATES_DJANGO['OPTIONS']['loaders']
