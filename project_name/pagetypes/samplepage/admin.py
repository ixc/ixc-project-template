from fluent_pages.integration.fluent_contents.admin import \
    FluentContentsPageAdmin


class SamplePageAdmin(FluentContentsPageAdmin):
    # A fixed template, from which the placeholder data can be read. The
    # placeholder_layout will be read automatically from the template.
    placeholder_layout_template = \
        'sfmoma/pagetypes/samplepage/default.html'
