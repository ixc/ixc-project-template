"""
Local settings for this deployment. Sample values should be defined when a
project is created from ``ixc-project-template``, and will need to be updated
every time this project is deployed.

Includes things like: the primary domain name where this deployment will be
accessed from; database credentials and secret keys; settings that are derived
from other settings; and settings that frequently need to be toggled during
development.
"""
from .project import *

### IXC PROJECT  ##############################################################

SITE_DOMAIN = 'localhost'

### DJANGO CORE ###############################################################

# Uncomment if you don't want the default, sqlite3.
DATABASES['default'].update({
    # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
    # 'NAME': '',
    # 'USER': '',
    # 'PASSWORD': '',
})

# DEBUG = False

DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'noreply@%s' % SITE_DOMAIN

# Enable site-wide caching.
# MIDDLEWARE_CLASSES = (
#     ('django.middleware.cache.UpdateCacheMiddleware', ) +
#     MIDDLEWARE_CLASSES +
#     ('django.middleware.cache.FetchFromCacheMiddleware', ))

# Enable cached template loader.
# TEMPLATE_LOADERS = (
#     ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
# )

### GENERIC ###################################################################

# Enable view profiling. Add `prof` key to querystring to see profiling results
# in your browser.
# MIDDLEWARE_CLASSES += ('generic.middleware.ProfileMiddleware', )
