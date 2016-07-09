# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0005_auto_20160709_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerecording',
            name='overview',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Overview', blank=True),
        ),
    ]
