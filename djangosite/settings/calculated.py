"""
Import base settings module and calculate derived settings.
"""

import django
import importlib
import os
import sys

from icekit.utils.sequences import dedupe_and_sort

BASE_SETTINGS_MODULE = os.environ.setdefault('BASE_SETTINGS_MODULE', 'base')

print '# Importing BASE_SETTINGS_MODULE: %s' % BASE_SETTINGS_MODULE

# Emulate `from ... import *` with base settings module from environment.
locals().update(
    importlib.import_module('djangosite.settings._%s' % BASE_SETTINGS_MODULE)
    .__dict__)

# Create missing runtime directories.
runtime_dirs = STATICFILES_DIRS + (
    os.path.dirname(LOGGING['handlers']['logfile']['filename']),
    os.path.dirname(SUPERVISOR['logfile']),
    os.path.dirname(SUPERVISOR['pidfile']),
    SUPERVISOR['childlogdir'],
)
for dirname in runtime_dirs:
    try:
        os.makedirs(dirname)
    except OSError:
        pass

# DJANGO ######################################################################

AUTHENTICATION_BACKENDS = dedupe_and_sort(AUTHENTICATION_BACKENDS, [
    'master_password.auth.ModelBackend',
])

# Sort installed apps to override collect static and template load order.
INSTALLED_APPS = dedupe_and_sort(INSTALLED_APPS, [
    # First the project.
    '{{ project_name }}',

    # Then 1st party apps.
    'icekit',
    'icekit.dashboard',
    'icekit.integration.reversion',

    # Then 3rd party apps.
    'fluent_suit',
    'suit',
    'flat',
    'test_without_migrations',
])

# Sort middleware according to documentation.
MIDDLEWARE_CLASSES = dedupe_and_sort(MIDDLEWARE_CLASSES, [
    # See: http://whitenoise.evans.io/en/latest/#quickstart-for-django-apps
    'django.middleware.security.SecurityMiddleware',
    'ixc_whitenoise.WhiteNoiseMiddleware',

    # See: https://docs.djangoproject.com/en/1.8/ref/middleware/#middleware-ordering
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',  # See: https://docs.djangoproject.com/en/1.8/ref/middleware/#django.contrib.auth.middleware.SessionAuthenticationMiddleware
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
])

# Get the secret key from a file that should never be committed to version
# control. If it doesn't exist, create it.
try:
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        open(SECRET_FILE).read().strip()
except IOError:
    try:
        import random
        import string
        SECRET_CHARSET = ''.join([
            string.digits, string.ascii_letters, string.punctuation])
        SECRET_KEY = ''.join(random.choice(SECRET_CHARSET) for i in range(50))
        secret = open(SECRET_FILE, 'w')
        secret.write(SECRET_KEY)
        secret.close()
        os.chmod(SECRET_FILE, 0400)
    except IOError:
        raise Exception(
            'Please create a %s file with 50 random characters to set your '
            'secret key.' % SECRET_FILE)

# Enable template backends.
TEMPLATES = [TEMPLATES_DJANGO, TEMPLATES_JINJA2]

# ENVIRONMENT #################################################################

# Add the virtualenv bin directory to the PATH environment variable.
VENV_BIN = os.path.join(sys.prefix, 'bin')
if VENV_BIN not in os.environ['PATH'].split(':'):
    os.environ['PATH'] = '%s:%s' % (VENV_BIN, os.environ['PATH'])

# COMPRESSOR ##################################################################

# Trick `compress` management command into combining files, regardless of
# `DEBUG` and `COMPRESS_ENABLED` settings.
#
# See: https://github.com/django-compressor/django-compressor/issues/258

if 'compress' in sys.argv:
    COMPRESS_ENABLED = True

# MASTER PASSWORDS ############################################################

if MASTER_PASSWORD:
    MASTER_PASSWORDS[MASTER_PASSWORD] = None

# SENTRY ######################################################################

if RAVEN_CONFIG.get('dsn'):
    INSTALLED_APPS += ('raven.contrib.django.raven_compat', )

# STORAGES ####################################################################

if ENABLE_S3_MEDIA:
    AWS_S3_CUSTOM_DOMAIN = 's3-us-west-2.amazonaws.com/%s' % \
        AWS_STORAGE_BUCKET_NAME
    MEDIA_URL = 'https://%s/media/' % AWS_S3_CUSTOM_DOMAIN

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE

# SUPERVISOR ##################################################################

SUPERVISOR.update({
    'wsgi': SUPERVISOR['wsgi'].format(**locals()),
})

# DJANGO 1.7 ##################################################################

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
