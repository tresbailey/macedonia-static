# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0017_auto_20161207_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgallery',
            name='group',
            field=models.ForeignKey(to='mbc.SmallGroup', null=True),
        ),
    ]
