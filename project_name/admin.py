from django.contrib import admin
from fluent_pages.admin import PageLayout

# Unregister the fluent layout model in favour of the ICEkit version.
admin.site.unregister(PageLayout)
