"""
Safe settings by default, based on Django 1.8 project template.

Prevent accidentally leaking sensitive information, connecting to a production
database, sending live emails, etc.

Uncomment or edit settings that apply to all deployments. Override settings for
each deployed environment in ``local.py``.
"""

import multiprocessing
import os
import posixpath
import sys

from django.utils import six
from django.utils.functional import lazy


SITE_NAME = '{{ project_name }}'

# FILE SYSTEM PATHS ###########################################################

# Working copy root. Contains `manage.py`.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Directory that will be served by front-end server. Should contain media and
# static directories.
PUBLIC_DIR = os.path.join(BASE_DIR, 'public')

# DJANGO CHECKLIST ############################################################

# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

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

# Use SQLite, because a real database will need to be provisioned and will
# require credentials and should be configured in `local.py`.
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

# DJANGO ######################################################################

EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# FILE_UPLOAD_PERMISSIONS = 0755  # Default: None

# Optional contrib and 3rd party apps that require additional configuration can
# be enabled and configured in app-specific sections further below.
INSTALLED_APPS = (
    # Default.
    # 'django.contrib.admin',  # Must come after `admin_tools` apps, below.
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Contrib.
    'django.contrib.admindocs',
    'django.contrib.sitemaps',

    # 3rd party.
    'django_extensions',
    'reversion',

    # IC.
    'django_frontend_compiler',

    # Project.
    '{{ project_name }}',
)

LANGUAGE_CODE = 'en-au'  # Default: en-us

LOGIN_REDIRECT_URL = '/'  # Default: '/accounts/profile/'
# LOGIN_URL = '/accounts/signin/'
# LOGOUT_URL = '/accounts/signout/'

MIDDLEWARE_CLASSES = (
    # Default.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    # Contrib.
    'django.contrib.admindocs.middleware.XViewMiddleware',
)

ROOT_URLCONF = 'djangosite.urls'

SILENCED_SYSTEM_CHECKS = (
    '1_6.W001',
    '1_6.W002',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'bower_components'),
    os.path.join(BASE_DIR, 'djangosite', 'static'),
)

STATICFILES_FINDERS = (
    # Defaults.
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Deprecated, but we still use in calculated settings.
TEMPLATE_LOADERS = [
    # Default.
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

# Define template backends separately. Backends will be added to `TEMPLATES` in
# `local.py`. This makes it easier to update for specific environments.

# Django templates backend.
TEMPLATES_DJANGO = {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [  # Default: empty
        os.path.join(BASE_DIR, 'djangosite', 'templates'),
    ],
    # 'APP_DIRS': True,  # Must not be set when `loaders` is defined
    'OPTIONS': {
        'context_processors': [
            # Default.
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',

            # Extra.
            'django.core.context_processors.i18n',
            'django.core.context_processors.media',
            'django.core.context_processors.static',
            'django.core.context_processors.tz',

            # Project.
            '{{ project_name }}.context_processors.environment',
        ],
        'loaders': TEMPLATE_LOADERS,
    },
}

# Jinja2 template backend.
TEMPLATES_JINJA2 = {
    'BACKEND': 'django.template.backends.jinja2.Jinja2',
    'DIRS': [
        os.path.join(BASE_DIR, 'djangosite', 'jinja2'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'environment': '{{ project_name }}.jinja2.environment',
    }
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'  # Default: django.test.runner.DiscoverRunner

TIME_ZONE = 'Australia/Sydney'  # Default: America/Chicago

USE_ETAGS = True  # Default: False
# USE_I18N = False  # Default: True
USE_L10N = True  # Default: False
USE_TZ = True  # Default: False

WSGI_APPLICATION = 'djangosite.wsgi.application'

# DJANGO REDIRECTS ############################################################

# Requires: django.contrib.sites

INSTALLED_APPS += ('django.contrib.redirects', )

MIDDLEWARE_CLASSES += (
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

# DJANGO SITES ################################################################

INSTALLED_APPS += ('django.contrib.sites', )
SITE_ID = 1

# COMPRESSOR ##################################################################

COMPRESS_CSS_FILTERS = [
    'django_frontend_compiler.filters.clean_css.CleanCSSFilter',
]

COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL
INSTALLED_APPS += ('compressor', )
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder', )

# EASY THUMBNAILS #############################################################

INSTALLED_APPS += ('easy_thumbnails', )
THUMBNAIL_BASEDIR = 'thumbs'
THUMBNAIL_HIGH_RESOLUTION = True

# FLUENT ######################################################################

ADMIN_TOOLS_APP_INDEX_DASHBOARD = \
    'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

DJANGO_WYSIWYG_FLAVOR = 'redactor'
DJANGO_WYSIWYG_MEDIA_URL = posixpath.join(STATIC_URL, 'redactor/')

FLUENT_CONTENTS_PLACEHOLDER_CONFIG = {
    # 'home': {
    #     'plugins': ('...', ),
    # },
    'main': {
        'plugins': (
            # 'CodePlugin',
            # 'CommentsAreaPlugin',
            # 'DisqusCommentsPlugin',
            # 'FormDesignerLinkPlugin',
            # 'GistPlugin',
            # 'GoogleDocsViewerPlugin',
            'IframePlugin',
            'MarkupPluginBase',
            'OEmbedPlugin',
            'PicturePlugin',
            'RawHtmlPlugin',
            'SharedContentPlugin',
            'TextPlugin',
            # 'TwitterRecentEntriesPlugin',
            # 'TwitterSearchPlugin',
        ),
    },
    # 'sidebar': {
    #     'plugins': ('...', ),
    # },
}

FLUENT_DASHBOARD_DEFAULT_MODULE = 'ModelList'

# FLUENT_MARKUP_LANGUAGES = ['restructuredtext', 'markdown', 'textile']
# FLUENT_MARKUP_MARKDOWN_EXTRAS = []

FLUENT_PAGES_TEMPLATE_DIR = os.path.join(
    BASE_DIR, '{{ project_name }}', 'layouts', 'templates')

# FLUENT_TEXT_CLEAN_HTML = True  # Default: False
# FLUENT_TEXT_SANITIZE_HTML = True  # Default: False

INSTALLED_APPS += (
    # Fluent.
    'fluent_contents',
    'fluent_dashboard',
    'fluent_pages',

    # Dependencies.
    'admin_tools',
    'admin_tools.dashboard',
    'admin_tools.menu',
    'admin_tools.theming',
    'django.contrib.admin',  # Must come after `admin_tools` apps.
    'mptt',
    'parler',
    'polymorphic',
    'polymorphic_tree',

    # Page types.
    'fluent_pages.pagetypes.flatpage',
    'fluent_pages.pagetypes.fluentpage',
    'fluent_pages.pagetypes.redirectnode',

    # Content plugins.
    # 'fluent_contents.plugins.code',
    # 'fluent_contents.plugins.commentsarea',
    # 'fluent_contents.plugins.disquswidgets',
    # 'fluent_contents.plugins.formdesignerlink',
    # 'fluent_contents.plugins.gist',
    # 'fluent_contents.plugins.googledocsviewer',
    'fluent_contents.plugins.iframe',
    'fluent_contents.plugins.markup',
    'fluent_contents.plugins.oembeditem',
    'fluent_contents.plugins.picture',
    'fluent_contents.plugins.rawhtml',
    'fluent_contents.plugins.sharedcontent',
    'fluent_contents.plugins.text',
    # 'fluent_contents.plugins.twitterfeed',

    # Project.
    '{{ project_name }}.layouts',
    # '{{ project_name }}.pagetypes.samplepage',
    # '{{ project_name }}.plugins.sample',

    # Page type and content plugin dependencies.
    'any_urlfield',
    'django_wysiwyg',
    'micawber',
)

# GENERIC #####################################################################

# INSTALLED_APPS += ('generic', )

# TEMPLATES_DJANGO['OPTIONS']['context_processors'].append(
#     'generic.context_processors.generic')

# TEMPLATE_CONSTANTS = {
#     'SITE_NAME': SITE_NAME,
# }

# GUARDIAN ####################################################################

# ANONYMOUS_USER_ID = -1  # Migrate to create the user
# INSTALLED_APPS += ('guardian', )
# AUTHENTICATION_BACKENDS += ('guardian.backends.ObjectPermissionBackend', )

# HOSTS #######################################################################

# INSTALLED_APPS += ('django_hosts', )
# MIDDLEWARE_CLASSES += ('django_hosts.middleware.HostsMiddleware', )

# DEFAULT_HOST = 'www'
# ROOT_HOSTCONF = 'djangosite.hosts'

# MASTER PASSWORD #############################################################

AUTHENTICATION_BACKENDS = ('master_password.auth.ModelBackend', )
INSTALLED_APPS += ('master_password', )
MASTER_PASSWORDS = {}

# MODEL SETTINGS ##############################################################

INSTALLED_APPS += ('model_settings', 'polymorphic')

TEMPLATES_DJANGO['OPTIONS']['context_processors'].append(
    'model_settings.context_processors.settings')

# POLYMORPHIC AUTH ############################################################

AUTH_USER_MODEL = 'email.EmailUser'
# AUTH_USER_MODEL = 'username.UsernameUser'

INSTALLED_APPS += (
    'polymorphic',
    'polymorphic_auth',
    'polymorphic_auth.usertypes.email',
    # 'polymorphic_auth.usertypes.username',
)

# SORL THUMBNAIL ##############################################################

# INSTALLED_APPS += ('sorl.thumbnail', )
# THUMBNAIL_DEBUG = False

# SUPERVISOR ##################################################################

INSTALLED_APPS += ('djsupervisor', )

GUNICORN_ADDRESS = '127.0.0.1'
GUNICORN_WORKERS = multiprocessing.cpu_count() * 2 + 1

def get_gunicorn_command():
    from django.conf import settings
    gunicorn = os.path.join(sys.prefix, 'bin', 'gunicorn')
    command = (
        '{gunicorn} -b {address}:{port} -w {workers} '
        'djangosite.wsgi:application'.format(
            gunicorn=gunicorn,
            address=settings.GUNICORN_ADDRESS,
            port=settings.SITE_PORT,
            workers=settings.GUNICORN_WORKERS,
        ))
    return command

# Lazily evaluate so we can override just the address, port, or number of
# workers in the `local` settings module.
get_gunicorn_command = lazy(get_gunicorn_command, six.text_type)

SUPERVISOR = {
    'wsgi': get_gunicorn_command(),
}
