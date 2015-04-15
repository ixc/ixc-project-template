"""
Context processors for ``{{ project_name }}`` app.
"""

from django.conf import settings


def environment(request):
    """
    Return `COMPRESS_ENABLED` setting as context.
    """
    # TODO: Make a generic context processor in `ixc-core` for this, which gets
    # the list of settings to be included as context from a setting.
    return {
        'COMPRESS_ENABLED': settings.COMPRESS_ENABLED,
    }
