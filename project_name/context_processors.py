"""
Core context processors for ``{{ project_name }}`` app.
"""

from django.conf import settings


SITE_SECTION_OVERRIDES = {
    'history': 'about', #etc.
}


def site_section(request):
    """
    Populates a tuple in the context called 'site_section' which indicates the
    current section (and subsection) of the site. This can be used, for example,
    to highlight menu items in templates.
    """
    # TODO: Don't rely on URL fragments to apply styles. Use URL names or hard
    # coded variables in section base templates.

    #Define your rules here
    url_based = request.get_full_path().split("/")[1:-1] #leading and trailing slashes

    if url_based == []:
        url_based = ["home"]

    url_based = [SITE_SECTION_OVERRIDES.get(x, x) for x in url_based]
    return {'site_section': url_based }


def django_environment(request):
    return {
        'DEBUG': settings.DEBUG,
        'COMPRESS_ENABLED': settings.COMPRESS_ENABLED,
    }


def main_nav(request):
    url = request.get_full_path()

    return {
        'main_nav': [
            {
                'title': 'Home',
                'url': '/',
                'is_active': url == '/',
            },
            {
                'title': 'Admin',
                'url': '/admin/',
                'is_active': url.startswith('/admin/'),
            },
            # {
            #     'title': 'Foo App',
            #     'url': reverse('foo-app-index'),
            #     'is_active': url.startswith(reverse('foo-app-index')),
            # },
        ]
    }
