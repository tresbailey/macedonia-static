# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0023_auto_20170228_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='leftimageblock',
            name='image_width',
            field=models.IntegerField(default=25, verbose_name='Image Width'),
        ),
        migrations.AddField(
            model_name='rightimageblock',
            name='image_width',
            field=models.IntegerField(default=25, verbose_name='Image Width'),
        ),
    ]
