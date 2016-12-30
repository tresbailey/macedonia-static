# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('mbc', '0012_auto_20161202_2039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smallgroup',
            options={'ordering': ('_order',)},
        ),
        migrations.RemoveField(
            model_name='smallgroup',
            name='description',
        ),
        migrations.RemoveField(
            model_name='smallgroup',
            name='id',
        ),
        migrations.AddField(
            model_name='smallgroup',
            name='page_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=-1, serialize=False, to='pages.Page'),
            preserve_default=False,
        ),
    ]
