from any_imagefield.models import AnyImageField
from django.db import models
from fluent_pages.integration.fluent_contents import FluentContentsPage


class SamplePage(FluentContentsPage):
    name = models.CharField(max_length=255)
    sample_image = AnyImageField(upload_to='sample_images')

    class Meta:
        verbose_name = 'Sample'
