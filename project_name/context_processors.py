"""
Context processors for ``{{ project_name }}`` app.
"""

from django.conf import settings


def environment(request):
    """
    Add ``COMPRESS_ENABLED`` to the context.
    """
    context = {
        'COMPRESS_ENABLED': settings.COMPRESS_ENABLED,
        'GOOGLE_ANALYTICS_CODE': getattr(settings, 'GOOGLE_ANALYTICS_CODE', None),
        'GOOGLE_ANALYTICS_ADDRESS': getattr(settings, 'GOOGLE_ANALYTICS_ADDRESS', None),
    }
    return context
