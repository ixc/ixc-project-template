"""
Root URLconf for ``{{ project_name }}`` project.
"""

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView
from generic.views import relative_view_on_site_urls

admin.autodiscover()
handler500 = 'generic.views.server_error'
sitemaps = {}

# Create a sitemap that is automatically populated with all pages in the
# FeinCMS site.
# from feincms.module.page.sitemap import PageSitemap
# sitemaps.update({'pages' : PageSitemap})

urlpatterns = patterns(
    '',
    # Make "view on site" links use relative URLs.
    relative_view_on_site_urls,

    url(r'^sitemap\.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),

    # Test templates.
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html')),

    # Optional.
    # url(r'^$', include('ixc_home.urls', namespace='home')),
    # url(r'^ajax_delete/(?P<uuid>.*)/$',
    #     'ixc_cms.views.admin_media_delete',
    #     name='ajax_delete'),
    # url(r'^ajax_upload/$',
    #     'ixc_cms.views.admin_media_upload',
    #     name='ajax_upload'),
    # url(r'^blog/',
    #     include('ixc_blog.urls', app_name='blogtools', namespace='blog')),

    # Included apps.
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include('adminboost.urls')),
    url(r'^redactor/', include('redactor.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Catch all, project URLs.
urlpatterns += patterns(
    '',
    url(r'^', include('{{ project_name }}.urls')),
)
