from fluent_contents.extensions import plugin_pool, ContentPlugin

from . import models


@plugin_pool.register
class SamplePlugin(ContentPlugin):
    model = models.SampleItem
    render_template = 'sfmoma/plugins/sample/default.html'
