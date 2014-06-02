"""
Core URLs for ``{{ project_name }}`` app.
"""

from django.conf.urls import include, patterns, url

urlpatterns = patterns('{{ project_name }}.views',
    # url(r'^$', 'index', name='{{ project_name }}_index'),

    # Catch all, pages app.
    # url(r'^', include('ixc_pages.urls', namespace='pages')),
)
