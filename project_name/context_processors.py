"""
Core context processors for ``{{ project_name }}`` app.
"""

from django.conf import settings

SITE_SECTION_OVERRIDES = {
    'history': 'about',  # etc.
}


def site_section(request):
    """
    Populates a tuple in the context called 'site_section' which indicates the
    current section (and subsection) of the site. This can be used, for
    example, to highlight menu items in templates.
    """
    # TODO: Don't rely on URL fragments to apply styles. Use URL names or hard
    # coded variables in section base templates.

    # Define your rules here. Strip leading and trailing slashes.
    url_based = request.get_full_path().split("/")[1:-1]

    if url_based == []:
        url_based = ["home"]

    url_based = [SITE_SECTION_OVERRIDES.get(x, x) for x in url_based]
    return {'site_section': url_based}


def django_environment(request):
    """
    Return `DEBUG` and `COMPRESS_ENABLED` settings as context.
    """
    # TODO: Make a generic context processor in `ixc-core` for this, which gets
    # the list of settings to be included as context from a setting.
    return {
        'DEBUG': settings.DEBUG,
        'COMPRESS_ENABLED': settings.COMPRESS_ENABLED,
    }
