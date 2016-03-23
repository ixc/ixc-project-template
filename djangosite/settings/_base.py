"""
Safe settings by default, based on Django 1.8 project template.

Prevent accidentally leaking sensitive information, connecting to a production
database, sending live emails, etc.

Uncomment or edit settings that apply to all deployments. Override settings for
each deployed environment in ``local.py``.
"""

import hashlib
import multiprocessing
import os
import posixpath


# Uniquely identify this settings module on the file system, so we can avoid
# conflicts with other projects running on the same system.
SETTINGS_MODULE_HASH = hashlib.md5(__file__).hexdigest()

SITE_NAME = '{{ project_name }}'

SITE_DOMAIN = os.environ.get('SITE_DOMAIN', 'localhost')
SITE_PORT = 8000

# FILE SYSTEM PATHS ###########################################################

# Working copy root. Contains `manage.py`.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Variable files. Logs, media, etc.
VAR_DIR = os.path.join(BASE_DIR, 'var')

# DJANGO CHECKLIST ############################################################

# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

#
# CRITICAL
#

SECRET_FILE = os.path.join(VAR_DIR, 'secret.txt')

DEBUG = False  # Don't show detailed error pages when exceptions are raised

#
# ENVIRONMENT SPECIFIC
#

# Only allow `SITE_DOMAIN`, including subdomains and full qualified domains.
ALLOWED_HOSTS = (
    '.%s' % SITE_DOMAIN,
    '.%s.' % SITE_DOMAIN,
)

# Use dummy caching, so we don't get confused because a change is not taking
# effect when we expect it to.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'KEY_PREFIX': 'default-%s' % SETTINGS_MODULE_HASH,
    }
}

DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('PGDATABASE', '{{ project_name }}'),
        'HOST': os.environ.get('PGHOST'),
        'PORT': os.environ.get('PGPORT'),
        'USER': os.environ.get('PGUSER'),
        'PASSWORD': os.environ.get('PGPASSWORD'),
    },
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(VAR_DIR, 'media')
MEDIA_URL = '/media/'

#
# HTTPS
#

# CSRF_COOKIE_SECURE = True  # Require HTTPS for CSRF cookie
# SESSION_COOKIE_SECURE = True  # Require HTTPS for session cookie

#
# PERFORMANCE
#

# Enable persistent database connections.
CONN_MAX_AGE = 60  # Default: 0

#
# ERROR REPORTING
#

# Add a root logger and change level for console handler to `DEBUG`.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'logfile': {
            'format': (
                '%(asctime)s %(levelname)s (%(module)s.%(funcName)s) '
                '%(message)s'),
        },
    },
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
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(
                VAR_DIR, 'logs', '{{ project_name }}.log'),
            'backupCount': 30,
            'when': 'midnight',
            'formatter': 'logfile',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'logfile'],
        },
    },
}

ADMINS = (
    ('Interaction Consortium', 'admins@interaction.net.au'),
)
MANAGERS = ADMINS

# DJANGO ######################################################################

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Default
)

# Enable cross-subdomain cookies, only if `SITE_DOMAIN` is not a TLD.
if '.' in SITE_DOMAIN:
    CSRF_COOKIE_DOMAIN = LANGUAGE_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN = \
        '.%s' % SITE_DOMAIN

DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'noreply@%s' % SITE_DOMAIN

EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# FILE_UPLOAD_PERMISSIONS = 0755  # Default: None

# Optional contrib and 3rd party apps that require additional configuration can
# be enabled and configured in app-specific sections further below.
INSTALLED_APPS = (
    # Default.
    'django.contrib.admin',
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

# Fix HTTPS redirect behind proxy.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

# Avoid session conflicts when running multiple projects on the same domain.
SESSION_COOKIE_NAME = 'sessionid-%s' % SETTINGS_MODULE_HASH

# Every write to the cache will also be written to the database. Session reads
# only use the database if the data is not already in the cache.
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

SILENCED_SYSTEM_CHECKS = (
    '1_6.W001',
    '1_6.W002',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'djangosite', 'static'),
    os.path.join(BASE_DIR, 'bower_components'),
)

STATICFILES_FINDERS = (
    # Defaults.
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

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
        'loaders': [
            # Default.
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ],
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

# CELERY ######################################################################

BROKER_URL = CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

# CELERY EMAIL ################################################################

CELERY_EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
INSTALLED_APPS += ("djcelery_email",)

# COMPRESSOR ##################################################################

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',  # Default
    # 'compressor.filters.cssmin.CSSMinFilter',
)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', os.path.join(
        BASE_DIR, 'node_modules/.bin/node-sass {infile} {outfile}')),
)

INSTALLED_APPS += ('compressor', )
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder', )

# DYNAMIC FIXTURES ############################################################

DDF_FILL_NULLABLE_FIELDS = False

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

# Must come after `admin_tools` apps.
INSTALLED_APPS = tuple(
    app for app in INSTALLED_APPS if app != 'django.contrib.admin')

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
    'django.contrib.admin',
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

    # Page type and content plugin dependencies.
    'any_urlfield',
    'django_wysiwyg',
    'micawber',
)

TEMPLATES_DJANGO['OPTIONS']['loaders'] += [
    'admin_tools.template_loaders.Loader']

# GENERIC #####################################################################

# INSTALLED_APPS += ('generic', )

# TEMPLATES_DJANGO['OPTIONS']['context_processors'].append(
#     'generic.context_processors.generic')

# TEMPLATE_CONSTANTS = {
#     'SITE_NAME': SITE_NAME,
# }

# GUARDIAN ####################################################################

# INSTALLED_APPS += ('guardian', )
# AUTHENTICATION_BACKENDS += ('guardian.backends.ObjectPermissionBackend', )

# HOSTS #######################################################################

# INSTALLED_APPS += ('django_hosts', )
# MIDDLEWARE_CLASSES += ('django_hosts.middleware.HostsMiddleware', )

# DEFAULT_HOST = 'www'
# ROOT_HOSTCONF = 'djangosite.hosts'

# ICEKIT ######################################################################

# INSTALLED_APPS += (
#     'icekit',
#     'icekit.plugins.brightcove',
#     'icekit.plugins.child_pages',
#     'icekit.plugins.faq',
#     'icekit.plugins.horizontal_rule',
#     'icekit.plugins.image',
#     'icekit.plugins.instagram_embed',
#     'icekit.plugins.reusable_form',
#     'icekit.plugins.slideshow',
#     'icekit.plugins.twitter_embed',
#     'icekit.response_pages',
#     'notifications',
# )

# MASTER PASSWORD #############################################################

AUTHENTICATION_BACKENDS = \
    ('master_password.auth.ModelBackend', ) + AUTHENTICATION_BACKENDS

INSTALLED_APPS += ('master_password', )
MASTER_PASSWORD = os.environ.get('MASTER_PASSWORD')
MASTER_PASSWORDS = {}

# MODEL SETTINGS ##############################################################

INSTALLED_APPS += ('model_settings', 'polymorphic')

TEMPLATES_DJANGO['OPTIONS']['context_processors'].append(
    'model_settings.context_processors.settings')

# NEW RELIC ###################################################################

# This environment variable is read by the `newrelic-admin` subprocess started
# by supervisor.
os.environ['NEW_RELIC_CONFIG_FILE'] = 'newrelic.ini'

# NOSE ########################################################################

INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'  # Default: django.test.runner.DiscoverRunner

NOSE_ARGS = [
    '--logging-clear-handlers',  # Clear all other logging handlers
    '--nocapture',  # Don't capture stdout
    '--nologcapture',  # Disable logging capture plugin
    # '--processes=-1',  # Automatically set to the number of cores
    '--with-progressive',  # See https://github.com/erikrose/nose-progressive
]

# POLYMORPHIC AUTH ############################################################

AUTH_USER_MODEL = 'polymorphic_auth.User'

INSTALLED_APPS += (
    'polymorphic',
    'polymorphic_auth',
    'polymorphic_auth.usertypes.email',
    # 'polymorphic_auth.usertypes.username',
)

POLYMORPHIC_AUTH = {
    'DEFAULT_CHILD_MODEL': 'polymorphic_auth_email.EmailUser',
    # 'DEFAULT_CHILD_MODEL': 'polymorphic_auth_username.UsernameUser',
}

# POST OFFICE #################################################################

EMAIL_BACKEND = 'post_office.EmailBackend'
INSTALLED_APPS += ('post_office', )

POST_OFFICE = {
    'BACKENDS': {
        'default': 'djcelery_email.backends.CeleryEmailBackend',
    },
    'DEFAULT_PRIORITY': 'now',
}

# SENTRY ######################################################################

RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN'),
}

# SUPERVISOR ##################################################################

INSTALLED_APPS += ('djsupervisor', )

WSGI_ADDRESS = '127.0.0.1'
WSGI_WORKERS = multiprocessing.cpu_count() * 2 + 1
WSGI_TIMEOUT = 30

SUPERVISOR = {
    # Config.
    'childlogdir': os.path.join(VAR_DIR, 'logs'),
    'logfile': os.path.join(VAR_DIR, 'logs', 'supervisord.log'),
    'pidfile': os.path.join(VAR_DIR, 'run', 'supervisord.pid'),

    # Programs.
    'celery': 'celery -A djangosite worker -l info',
    'wsgi': (
        'gunicorn '
        '-b {WSGI_ADDRESS}:{SITE_PORT} '
        '-w {WSGI_WORKERS} '
        '-t {WSGI_TIMEOUT} '
        'djangosite.wsgi:application'
    ),

    # Exclude programs.
    'exclude_autoreload': True,
    'exclude_celery': False,
    'exclude_wsgi': False,
}

# TEST WITHOUT MIGRATIONS #####################################################

INSTALLED_APPS = ('test_without_migrations', ) + INSTALLED_APPS

# Default: django.core.management.commands.test.Command
TEST_WITHOUT_MIGRATIONS_COMMAND = \
    'django_nose.management.commands.test.Command'

# WHITENOISE ##################################################################

# See: http://whitenoise.evans.io/en/latest/#quickstart-for-django-apps
_index = MIDDLEWARE_CLASSES.index(
    'django.middleware.security.SecurityMiddleware') + 1
MIDDLEWARE_CLASSES = (
    MIDDLEWARE_CLASSES[:_index] +
    ('djangosite.middleware.WhiteNoiseMediaMiddleware', ) +
    MIDDLEWARE_CLASSES[_index:]
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

WHITENOISE_AUTOREFRESH = True
WHITENOISE_USE_FINDERS = True

WHITENOISE_ROOT = os.path.join(BASE_DIR, 'staticroot')
