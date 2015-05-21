from fluent_pages.extensions import page_type_pool
from fluent_pages.integration.fluent_contents.page_type_plugins import \
    FluentContentsPagePlugin

from . import admin, models


@page_type_pool.register
class SamplePageTypePlugin(FluentContentsPagePlugin):
    model = models.SamplePage
    model_admin = admin.SamplePageAdmin
    render_template = 'sfmoma/pagetypes/samplepage/default.html'
