# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0020_auto_20161207_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventgallery',
            name='weekly_day',
            field=models.IntegerField(default=0, choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b'Sunday')], max_length=10, blank=True, null=True, verbose_name='Weekly Day'),
        ),
        migrations.AlterField(
            model_name='eventgallery',
            name='scheduled_time',
            field=models.TimeField(null=True, verbose_name='Weekly Scheduled Time'),
        ),
    ]
