"""
Settings for all deployments of this project. These should be defined when a
project is created from ``ixc-project-template``, and should not need to be
changed for each deployment of this project.

Includes settings like: custom apps, middleware classes and context processors;
optional generic apps that are not always useful for all projects; and Django
settings that frequently need to be changed per project.
"""
from .base import *

### IXC PROJECT ###############################################################

SITE_NAME = 'IC Site'

# Template constants are passed in as context offor template with
# `generic.context_processors.generic`.
TEMPLATE_CONSTANTS = {
    # 'GOOGLE_MAPS_API_KEY': '',
}

### DJANGO CORE ###############################################################

EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# Currently many apps are too tightly coupled. Below are the dependencies that
# are required for some of the apps. For now, you'll need to install all the
# requirements until we can decouple them.

# ixc-blog:
# feincmstools, feincms, ixc_assets, ixc_smartlinks_conf, smartlinks, oembed,
# adminboost, ixc_cms, feincms.module.medialibrary, ixc_pages,
# ixc_feincms_conf.

# ixc-home:
# singleton_models, feincmstools, feincms, mptt, ixc_smartlinks_conf,
# smartlinks, oembed, adminboost, ixc_cms, ixc_pages,
# feincms.module.medialibrary, ixc_feincms_conf.

INSTALLED_APPS += (
    # 'feincms',
    # 'feincms.module.medialibrary',
    # 'feincms.module.page', # Only used for template tags.
    # 'feincmstools',
    # 'mptt',
    # 'oembed',
    # 'redactor',
    # 'singleton_models',

    # 'adminboost',
    'ixc_accounts', # Also needs `AUTH_USER_MODEL = 'ixc_accounts.User'`.
    # 'ixc_assets',
    # 'ixc_assets.files',
    # 'ixc_assets.galleries', # You must provide a front-end if you enable galleries.
    # 'ixc_assets.images',
    # 'ixc_blog',
    # 'ixc_cms',
    # 'ixc_feincms_conf', # Must come after `feincms.*`.
    # 'ixc_home',
    # 'ixc_pages',
    # 'ixc_smartlinks_conf',
    # 'smartlinks',
)

### DJANGO AUTH ###############################################################

AUTH_USER_MODEL = 'ixc_accounts.User'

### BOWER #####################################################################

# BOWER_INSTALLED_APPS += ()

### SENTRY ####################################################################

# Get from: https://sentry.ixcsandbox.com
SENTRY_DSN = ''
