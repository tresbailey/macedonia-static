# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0016_auto_20161205_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgallery',
            name='group',
            field=models.ForeignKey(blank=True, to='mbc.SmallGroup', null=True),
        ),
        migrations.AlterField(
            model_name='smallgroup',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
