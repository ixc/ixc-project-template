import os

os.environ['SITE_DOMAIN'] = '{{ project.name }}.lvh.me'

from ._base import *

SITE_PUBLIC_PORT = None  # Default: SITE_PORT

# DJANGO ######################################################################

CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

for k in CACHES:
    CACHES[k].update({
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211',
    })

LOGGING['handlers']['logfile']['backupCount'] = 100

MIDDLEWARE_CLASSES = (
    ('django.middleware.cache.UpdateCacheMiddleware', ) +
    MIDDLEWARE_CLASSES +
    ('django.middleware.cache.FetchFromCacheMiddleware', )
)

TEMPLATES_DJANGO['OPTIONS']['loaders'] = [
    (
        'django.template.loaders.cached.Loader',
        TEMPLATES_DJANGO['OPTIONS']['loaders'],
    ),
]

# CELERY EMAIL ################################################################

CELERY_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# NEW RELIC ###################################################################

SUPERVISOR['wsgi'] = 'newrelic-admin run-program %s' % SUPERVISOR['wsgi']
