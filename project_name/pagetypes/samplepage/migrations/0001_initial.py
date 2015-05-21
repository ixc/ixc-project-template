# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import any_imagefield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fluent_pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SamplePage',
            fields=[
                ('urlnode_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fluent_pages.UrlNode')),
                ('name', models.CharField(max_length=255)),
                ('sample_image', any_imagefield.models.fields.AnyImageField(upload_to=b'sample_images')),
            ],
            options={
                'db_table': 'pagetype_samplepage_samplepage',
                'verbose_name': 'Sample',
            },
            bases=('fluent_pages.htmlpage',),
        ),
    ]
