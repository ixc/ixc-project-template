"""
URLconf for ``{{ project_name }}`` app.
"""

from django.conf.urls import include, patterns, url


urlpatterns = patterns(
    '{{ project_name }}.views',
    url(r'^$', 'index', name='{{ project_name }}_index'),
    url(r'^', include('fluent_pages.urls')),
)
