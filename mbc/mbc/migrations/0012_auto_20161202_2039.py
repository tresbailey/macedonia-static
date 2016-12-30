# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0011_eventgallery_weekly_worship'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventgallery',
            name='group',
            field=models.ForeignKey(to='mbc.SmallGroup', null=True),
        ),
        migrations.AddField(
            model_name='eventgallery',
            name='scheduled_day',
            field=models.CharField(default=b'sun', max_length=10, verbose_name='Weekly Scheduled Day', choices=[(b'mon', b'Monday'), (b'tue', b'Tuesday'), (b'wed', b'Wednesday'), (b'thu', b'Thursday'), (b'fri', b'Friday'), (b'sat', b'Saturday'), (b'sun', b'Sunday')]),
        ),
    ]
