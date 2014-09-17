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

# Check `requirements.txt` for a list of dependencies for each app below.

INSTALLED_APPS += (
    # 3rd party.
    # 'feincms',
    # 'feincms.module.medialibrary',
    # 'feincms.module.page', # Only used for template tags.
    # 'mptt',
    # 'oembed',
    # 'orm_fixtures',
    # 'redactor',
    # 'singleton_models',

    # IxC.
    # 'adminboost',
    # 'feincmstools',
    # 'generic',
    # 'ixc_accounts', # Also needs `AUTH_USER_MODEL = 'ixc_accounts.User'`.
    # 'ixc_blog',
    # 'ixc_cms',
    # 'ixc_content_types',
    # 'ixc_content_types.files',
    # 'ixc_content_types.galleries', # You must provide a front-end if you enable galleries.
    # 'ixc_content_types.images',
    'ixc_core',
    # 'ixc_feincms_conf', # Must come after `feincms.*`.
    'ixc_flatui',
    # 'ixc_home',
    # 'ixc_pages',
    # 'ixc_smartlinks_conf',
    # 'smartlinks',

    # This project.
    '{{ project_name }}',
)

### DJANGO AUTH ###############################################################

# AUTH_USER_MODEL = 'ixc_accounts.User'

### SENTRY ####################################################################

# Get from: https://sentry.ixcsandbox.com
SENTRY_DSN = ''

### CONTENT TYPES #############################################################
### Below is a sample of content types that may often be used in projects. If
### they are not used and ixc_content_types is installed it will fall back to
### some default choices

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
