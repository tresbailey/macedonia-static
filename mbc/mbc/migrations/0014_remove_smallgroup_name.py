# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0013_auto_20161202_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smallgroup',
            name='name',
        ),
    ]
