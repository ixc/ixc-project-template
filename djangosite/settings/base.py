"""
Safe settings by default.

Prevent accidentally leaking sensitive information, connecting to a production
database, sending live emails, etc.

Uncomment or edit settings that apply to all deployments. Override settings for
each deployed environment in ``local.py``.
"""

import os
import sys
import tempfile

SITE_NAME = '{{ project_name }}'

### FILE SYSTEM PATHS #########################################################

# Working copy root. Contains `manage.py`.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Directory that will be served by front-end server. Should contain media and
# static directories.
PUBLIC_DIR = os.path.join(BASE_DIR, 'public')

### DJANGO CHECKLIST ##########################################################

# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

#
# CRITICAL
#

# Get the secret key from a file that should never be committed to version
# control. If it doesn't exist, create it.
SECRET_FILE = os.path.join(BASE_DIR, 'secret.txt')
try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
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

DEBUG = False  # Don't show detailed error pages when exceptions are raised

#
# ENVIRONMENT SPECIFIC
#

# Only allow requests to loopback interfaces.
ALLOWED_HOSTS = (
    '127.0.0.1',
    'localhost',
)

# Use dummy caching, so we don't get confused because a change is not taking
# effect when we expect it to.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Use SQLite, because a real database will require credentials and should be
# configured in `local.py`.
DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Don't send emails, just in case we're testing locally with a copy of the
# production database.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = os.path.join(PUBLIC_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PUBLIC_DIR, 'media')
MEDIA_URL = '/media/'

#
# HTTPS
#

CSRF_COOKIE_SECURE = True  # Require HTTPS for CSRF cookie
SESSION_COOKIE_SECURE = True  # Require HTTPS for session cookie

#
# PERFORMANCE
#

CONN_MAX_AGE = 0  # Disable persistent database connections

#
# ERROR REPORTING
#

# Add a root logger and change level for console handler to `DEBUG`.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
        },
    },
}

ADMINS = (
    ('Interaction Consortium', 'admins@interaction.net.au'),
)
MANAGERS = ADMINS

### DJANGO ####################################################################

EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# FILE_UPLOAD_PERMISSIONS = 0755  # Default: None

# Optional contrib and 3rd party apps that require additional configuration can
# be enabled and configured in app-specific sections further below.
INSTALLED_APPS = (
    # Defaults.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Contrib.
    'django.contrib.admindocs',

    # Check `requirements.txt` for a list of dependencies for the 3rd party and
    # IxC apps below.

    # 3rd party.
    'django_extensions',
    'reversion',
    # 'feincms',
    # 'feincms.module.medialibrary',
    # 'feincms.module.page',  # Only used for template tags
    # 'mptt',
    # 'oembed',
    # 'orm_fixtures',
    # 'redactor',
    # 'singleton_models',

    # IxC.
    # 'adminboost',
    'django_frontend_compiler',
    # 'feincmstools',
    # 'generic',
    # 'ixc_blog',
    # 'ixc_cms',
    'ixc_core',
    # 'ixc_feincms_conf',  # Must come after `feincms.*`
    'ixc_flatui',
    # 'ixc_home',
    # 'ixc_pages',
    # 'ixc_smartlinks_conf',
    # 'smartlinks',

    # Local.
    '{{ project_name }}',
)

LANGUAGE_CODE = 'en-au'  # Default: en-us

LOGIN_REDIRECT_URL = '/'  # Default: '/accounts/profile/'
# LOGIN_URL = '/accounts/signin/'
# LOGOUT_URL = '/accounts/signout/'

MIDDLEWARE_CLASSES = (
    # Defaults.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Extras.
    'django.contrib.admindocs.middleware.XViewMiddleware',
)

MIGRATION_MODULES = {
    'ixc_blog': 'djangosite.migrations.ixc_blog',
    'ixc_home': 'djangosite.migrations.ixc_home',
    'ixc_pages': 'djangosite.migrations.ixc_pages',
    'page': 'ixc_feincms_conf.feincms_page_migrations',
}

ROOT_URLCONF = 'djangosite.urls'

# Django will think this settings module was created by Django 1.5 or earlier
# if `MANAGERS`, `SITE_ID` and `TEMPLATE_LOADERS` settings are defined. Ignore
# the resulting backward incompatibility warnings.
# See: https://code.djangoproject.com/ticket/22454
SILENCED_SYSTEM_CHECKS = (
    '1_6.W001',
    '1_6.W002',
)

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(BASE_DIR, 'bower_components')),
    os.path.abspath(os.path.join(BASE_DIR, 'djangosite', 'static')),
)

STATICFILES_FINDERS = (
    # Defaults.
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # Defaults.
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages'

    # Extras.
    'django.core.context_processors.request',

    # TODO: Don't rely on URL fragments to apply styles. Use URL names or hard
    # coded variables in section base templates.
    '{{ project_name }}.context_processors.site_section',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'djangosite', 'templates'),
)

TEMPLATE_LOADERS = (
    # Defaults.
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TIME_ZONE = 'Australia/Sydney'  # Default: America/Chicago

USE_ETAGS = True  # Default: False
# USE_I18N = False  # Default: True
USE_L10N = True  # Default: False
USE_TZ = True  # Default: False

WSGI_APPLICATION = 'djangosite.wsgi.application'

### DJANGO REDIRECTS ##########################################################

# Requires `django.contrib.sites`.

INSTALLED_APPS += ('django.contrib.redirects', )

MIDDLEWARE_CLASSES += (
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

### DJANGO SITES ##############################################################

INSTALLED_APPS += ('django.contrib.sites', )
SITE_ID = 1

### COMPRESSOR ################################################################

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', '%s --load-path={inpath} {infile}' %
        os.path.join(sys.prefix, 'bin', 'pyscss')),
)

COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL
INSTALLED_APPS += ('compressor', )
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder', )

### EASY THUMBNAILS ###########################################################

INSTALLED_APPS += ('easy_thumbnails', )
THUMBNAIL_BASEDIR = 'thumbs'
THUMBNAIL_HIGH_RESOLUTION = True

### FEINCMS ###################################################################

FEINCMS_JQUERY_NO_CONFLICT = True
FEINCMS_TREE_EDITOR_INCLUDE_ANCESTORS = True
FEINCMS_USE_PAGE_ADMIN = False
TEMP_FOLDER = os.path.join(tempfile.gettempdir(), '{{ project_name }}')
TMP_UPLOAD_FOLDER = os.path.join(TEMP_FOLDER, 'uploads')

### GENERIC ###################################################################

TEMPLATE_CONTEXT_PROCESSORS += ('generic.context_processors.generic', )

TEMPLATE_CONSTANTS = {
    'SITE_NAME': SITE_NAME,
}

### GUARDIAN ##################################################################

# ANONYMOUS_USER_ID = -1  # Syncdb to create the user
# INSTALLED_APPS += ('guardian', )
# AUTHENTICATION_BACKENDS += ('guardian.backends.ObjectPermissionBackend', )

### HOSTS #####################################################################

# INSTALLED_APPS += ('django_hosts', )
# MIDDLEWARE_CLASSES += ('django_hosts.middleware.HostsMiddleware', )

# DEFAULT_HOST = 'www'
# ROOT_HOSTCONF = 'djangosite.hosts'

### IXC-ACCOUNTS ##############################################################

# AUTH_USER_MODEL = 'ixc_accounts.User'
# INSTALLED_APPS += ('ixc_accounts', )

### IXC-CONTENT-TYPES #########################################################

# Below is a sample of content types that may often be used in projects. If
# they are not used and ixc_content_types is installed it will fall back to
# some default choices.

# If you choose to use GalleryContent or GalleryContentWithDimensions, remember
# to run `bower install -S colorbox`.

# DEFAULT_CONTENT_TYPES = {
#     (
#         'Images',
#         (
#             'ixc_content_types.images.content_types.OneOffImageContent',
#             'ixc_content_types.images.content_types.OneOffImageContentWithStyles',
#             'ixc_content_types.images.content_types.ReusableImageContent',
#             'ixc_content_types.images.content_types.ReusableImageContentWithStyles',
#             'ixc_content_types.images.content_types.GalleryContent',
#             'ixc_content_types.images.content_types.GalleryContentWithDimensions',
#             'ixc_content_types.images.content_types.CarouselContent',
#             'ixc_content_types.images.content_types.CarouselContentWithDimensions',
#         ),
#     ),
#     (
#         'Files',
#         (
#             'ixc_content_types.files.content_types.OneOffFileContent',
#             'ixc_content_types.files.content_types.ReusableFileContent',
#             'ixc_content_types.files.content_types.OEmbedContent',
#         ),
#     ),
#     (
#         None,
#         (
#             'redactor.content_types.RedactorContent',
#             'ixc_content_types.textual.content_types.QuoteContent',
#             'ixc_content_types.textual.content_types.RawHTMLContent',
#         ),
#     ),
# }

# INSTALLED_APPS += (
#     'ixc_content_types',
#     'ixc_content_types.files',
#     'ixc_content_types.galleries',  # You must provide a front-end
#     'ixc_content_types.images',
# )

### MODEL SETTINGS ############################################################

INSTALLED_APPS += ('model_settings', 'polymorphic')
TEMPLATE_CONTEXT_PROCESSORS += ('model_settings.context_processors.settings', )

### REDACTOR ##################################################################

REDACTOR_OPTIONS = {
    'autoResize': True,
    'buttons': (
        'html', '|', 'formatting', '|', 'bold', 'italic', 'deleted', '|',
        'unorderedlist', 'orderedlist', 'outdent', 'indent', '|',
        # Uncomment if you want to support uploads within the editor.
        # 'image', 'video', 'file',
        'table', 'link', '|', 'alignment', '|',
        'horizontalrule'
    ),
    'lang': 'en',
    'observeLinks': True,
    'tabFocus': True,
    'wym': True,
}

REDACTOR_UPLOAD = 'uploads/redactor/'

### SUIT ######################################################################

# Must come before `django.contrib.admin`
INSTALLED_APPS = ('suit', ) + INSTALLED_APPS

SUIT_CONFIG = {
    # Header.
    'ADMIN_NAME': '%s Admin' % SITE_NAME,
    'HEADER_DATE_FORMAT': 'l, j. F Y',  # Saturday, 16th March 2013
    'HEADER_TIME_FORMAT': 'P',  # 6:42pm, 10am, midnight, etc.

    # Forms.
    # 'CONFIRM_UNSAVED_CHANGES': True,
    # 'SHOW_REQUIRED_ASTERISK': True,

    # Menu. Icons at http://getbootstrap.com/components/
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #     'sites': 'icon-leaf',
    #     'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True,
    # 'MENU_ICONS': {
    #     'sites': 'icon-leaf',
    #     'auth': 'icon-lock',
    # },
    # 'MENU_EXCLUDE': ('auth.group', ),
    'MENU': (
        # 'sites',
        # {
        #     'app': 'auth',
        #     'icon': 'icon-lock',
        #     'models': (
        #         'user',
        #         'group',
        #     ),
        # },
        '-',
        {
            'label': 'Content',
            'icon': 'icon-pencil',
            'models': (
                'ixc_pages.page',
                'ixc_home.homepage',
                'redirects.redirect',
                # 'smartlinks.customsmartlink',
            ),
        },
        {
            'label': 'Media',
            'icon': 'icon-play',
            'models': (
                'ixc_content_types.assetcategory',
                {
                    'label': 'Media file category',
                    'model': 'medialibrary.category',
                },
                'medialibrary.mediafile',
                'images.image',
                'files.file',
            ),
        },
        '-',
        {
            'label': 'Configuration',
            'icon': 'icon-cog',
            'models': (
                'model_settings.setting',
                'ixc_accounts.user',
                'auth.group',
                'oembed.providerrule',
                'oembed.storedoembed',
                'sites.site',
            ),
        },
        # {
        #     'label': 'Support',
        #     'icon': 'icon-question-sign',
        #     'url': '/support/',
        # },
    ),

    # Misc.
    'LIST_PER_PAGE': 100,
}

### SORL THUMBNAIL ############################################################

# INSTALLED_APPS += ('sorl.thumbnail', )
# THUMBNAIL_DEBUG = False

### SUPERVISOR ################################################################

INSTALLED_APPS += ('djsupervisor', )

SUPERVISOR = {
    'ADDRESS': '127.0.0.1:8000',  # Bind to loopback interface
    'NAME': '{{ project_name }}',
    'PREFIX': sys.prefix,
}
