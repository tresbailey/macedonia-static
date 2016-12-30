# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0010_auto_20161117_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventgallery',
            name='weekly_worship',
            field=models.NullBooleanField(verbose_name='Weekly Worship Event'),
        ),
    ]
