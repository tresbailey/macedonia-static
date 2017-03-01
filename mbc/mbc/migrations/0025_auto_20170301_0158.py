# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('mbc', '0024_auto_20170228_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoBlock',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('sub_header', models.CharField(max_length=50, null=True, verbose_name='Block Sub-Header', blank=True)),
                ('file', mezzanine.core.fields.FileField(max_length=200, null=True, verbose_name='File', blank=True)),
                ('video_link', models.URLField(null=True, verbose_name='Image Link', blank=True)),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
    ]
