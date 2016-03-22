from djangosite.settings.calculated import *

# DJANGO ######################################################################

# Always use the same database, not only when running tests.
DATABASES['default'].update({
    'NAME': 'test_{{ project_name }}',
    'TEST': {
        'NAME': 'test_{{ project_name }}',
        'SERIALIZE': False,  # Don't serialize the database to speed up tests.
    },
})

INSTALLED_APPS += ('{{ project_name }}.tests', )

# Use fast/insecure password hasher to speed up tests.
PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher', )

# Use cached template loader to speed up tests.
TEMPLATES_DJANGO['OPTIONS']['loaders'] = [(
    'django.template.loaders.cached.Loader',
    TEMPLATES_DJANGO['OPTIONS']['loaders']
)]

# COMPRESSOR ##################################################################

# Don't compile compress CSS and JS to speed up tests.
COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = ()

# TRAVIS ######################################################################

if 'TRAVIS' in os.environ:
    DATABASES['default']['USER'] = 'postgres'

    # Disable progressive plugin, which doesn't work properly on Travis.
    NOSE_ARGS.remove('--with-progressive')
