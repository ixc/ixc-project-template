"""
Root URLconf for ``{{ project_name }}`` project.

Only include and override URLs for installed apps here. ``{{ project_name }}``
URLs should go in ``{{ project_name }}.urls`` instead (included below).
"""

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from fluent_pages.sitemaps import PageSitemap

admin.autodiscover()

sitemaps = {
    'pages': PageSitemap,
}

urlpatterns = patterns(
    '',

    # Sitemap.
    url(r'^sitemap\.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),

    # Test templates.
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html')),

    # URLs for `admin/*` must come before `admin/`.
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/util/tools/', include('admin_tools.urls')),

    # URLs for installed apps.
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^forms/', include('forms_builder.forms.urls')),
)

# Catch all, project URLs.
urlpatterns += patterns(
    '',
    url(r'^', include('{{ project_name }}.urls')),
)
