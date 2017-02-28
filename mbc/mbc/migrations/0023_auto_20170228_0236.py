# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0022_auto_20170224_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='leftimageblock',
            name='image_link',
            field=models.URLField(null=True, verbose_name='Image Link', blank=True),
        ),
        migrations.AddField(
            model_name='rightimageblock',
            name='image_link',
            field=models.URLField(null=True, verbose_name='Image Link', blank=True),
        ),
        migrations.AlterField(
            model_name='leftimageblock',
            name='file',
            field=mezzanine.core.fields.FileField(max_length=200, null=True, verbose_name='File', blank=True),
        ),
        migrations.AlterField(
            model_name='rightimageblock',
            name='file',
            field=mezzanine.core.fields.FileField(max_length=200, null=True, verbose_name='File', blank=True),
        ),
    ]
