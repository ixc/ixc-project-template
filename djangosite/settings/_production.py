import os

os.environ.setdefault('SITE_DOMAIN', '{{ project_name }}-prd.ixcsandbox.com')

from ._base import *

SITE_PUBLIC_PORT = None  # Default: SITE_PORT

# DJANGO ######################################################################

ALLOWED_HOSTS = (
    '.%s' % SITE_DOMAIN,
    '.%s.' % SITE_DOMAIN,
)

for i, k in enumerate(CACHES, 1):
    CACHES[k].update({
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/%s' % i,
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
