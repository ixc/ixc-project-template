"""
Core context processors for ``{{ project_name }}`` app.
"""

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
