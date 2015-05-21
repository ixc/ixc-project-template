from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from fluent_contents.models import ContentItem


@python_2_unicode_compatible
class SampleItem(ContentItem):
    sample = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Sample'

    def __str__(self):
        return self.sample
