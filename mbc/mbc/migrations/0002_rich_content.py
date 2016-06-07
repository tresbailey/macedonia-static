# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventgallery',
            name='content',
            field=mezzanine.core.fields.RichTextField(default='', verbose_name='Content'),
            preserve_default=False,
        ),
    ]
