# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0019_auto_20161207_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventgallery',
            name='scheduled_time',
            field=models.TimeField(default=datetime.datetime(2016, 12, 7, 21, 22, 18, 249462, tzinfo=utc), verbose_name='Weekly Scheduled Time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventgallery',
            name='group',
            field=models.ForeignKey(blank=True, to='mbc.SmallGroup', null=True),
        ),
    ]
