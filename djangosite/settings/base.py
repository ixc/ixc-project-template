"""
Base settings. These should be OK for most projects with very few changes.

Includes settings like: static file and template directories; generic apps,
middleware classes and context processors that are useful for all projects; and
Django settings that rarely need to be changed per project.

Extends an ``ixc-settings`` settings module, determined by the local hostname
or ``IXC_SETTINGS_MODULE`` variable in your environ. See `ixc-settings`_.

.. _`ixc-settings`: https://github.com/ixc/ixc-settings/
"""
import ixc_settings, os, tempfile

### IXC-SETTINGS ##############################################################

# Add IXC settings to the local scope as defaults. Define `IXC_SETTINGS_MODULE`
# in your environ, otherwise it will be derived from your current hostname.
locals().update(ixc_settings.as_dict())

### FILE SYSTEM PATHS #########################################################

# Working copy root. Contains `manage.py`.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Directory that will be served by front-end server. Should contain media and
# static directories.
PUBLIC_DIR = os.path.join(BASE_DIR, 'public')

### DJANGO CORE ###############################################################

# Use sqlite3 by default for simplicity. Override in `local.py` for postgresql.
DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

FILE_UPLOAD_PERMISSIONS = 0755

# Must come before `django.contrib.admin`.
INSTALLED_APPS = ('suit', ) + INSTALLED_APPS

INSTALLED_APPS += (
    # Contrib.
    'django.contrib.admindocs',
    'django.contrib.redirects',
    'django.contrib.sites',

    # 3rd party.
    'compressor',
    'django_extensions',
    'djsupervisor',
    'easy_thumbnails',
    'reversion',
    'south',
)

MEDIA_ROOT = os.path.join(PUBLIC_DIR, 'media')
MEDIA_URL = '/media/'

MIDDLEWARE_CLASSES += (
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

ROOT_URLCONF = 'djangosite.urls'

# Get the secret key from a hidden file that should never be committed to
# version control. If it doesn't exist, create it.
SECRET_FILE = os.path.join(BASE_DIR, 'secret.txt')
try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
    try:
        import string, random
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

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'generic.context_processors.generic',

    # TODO: Don't rely on URL fragments to apply styles. Use URL names or hard
    # coded variables in section base templates.
    '{{ project_name }}.context_processors.site_section',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'djangosite', 'templates'),
)

USE_ETAGS = True # Django default: False
WSGI_APPLICATION = 'djangosite.wsgi.application'

### DJANGO AUTH ###############################################################

LOGIN_REDIRECT_URL = '/' # Django default: '/accounts/profile/'
# LOGIN_URL = '/accounts/signin/'
# LOGOUT_URL = '/accounts/signout/'

### DJANGO SITES ##############################################################

SITE_ID = 1

### DJANGO STATICFILES ########################################################

STATIC_ROOT = os.path.join(PUBLIC_DIR, 'static')

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(BASE_DIR, 'djangosite', 'static')),
)

### BOWER #####################################################################

BOWER_COMPONENTS_ROOT = BASE_DIR

BOWER_INSTALLED_APPS = (
    'bootstrap',
    'jquery',
    'jquery.placeholder',
)

INSTALLED_APPS += ('djangobower', )
STATICFILES_FINDERS += ('djangobower.finders.BowerFinder', )

### COMPRESSOR ################################################################

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', os.path.join(os.getenv('VIRTUAL_ENV'), 'bin', 'pyscss') +
        ' --load-path={inpath} {infile}'),
)

COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder', )

### EASY THUMBNAILS ###########################################################

THUMBNAIL_BASEDIR = 'thumbs'
THUMBNAIL_HIGH_RESOLUTION = True

### FEINCMS ###################################################################

FEINCMS_JQUERY_NO_CONFLICT = True
FEINCMS_TREE_EDITOR_INCLUDE_ANCESTORS = True
FEINCMS_USE_PAGE_ADMIN = False
TEMP_FOLDER = os.path.join(tempfile.gettempdir(), '{{ project_name }}')
TMP_UPLOAD_FOLDER = os.path.join(TEMP_FOLDER, 'uploads')

### GUARDIAN ##################################################################

# ANONYMOUS_USER_ID = -1 # Syncdb to create the user
# INSTALLED_APPS += ('guardian', )
# AUTHENTICATION_BACKENDS += ('guardian.backends.ObjectPermissionBackend', )

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

### SOUTH #####################################################################

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
    'ixc_accounts': 'ixc_accounts.south_migrations',
    'page': 'ixc_feincms_conf.feincms_page_migrations',
}

### SUIT ######################################################################

SUIT_CONFIG = {
    # Header.
    'ADMIN_NAME': 'Admin',
    'HEADER_DATE_FORMAT': 'l, j. F Y', # Saturday, 16th March 2013
    'HEADER_TIME_FORMAT': 'P', # 6:42pm, 10am, midnight, etc.

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
            'icon':'icon-pencil',
            'models': (
                'ixc_pages.page',
                'ixc_home.homepage',
                'redirects.redirect',
                # 'smartlinks.customsmartlink',
            ),
        },
        {
            'label': 'Media',
            'icon':'icon-play',
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

### SUPERVISOR ################################################################

SUPERVISOR.update({
    'NAME': '{{ project_name }}',
})
