# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0014_remove_smallgroup_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smallgroup',
            options={},
        ),
        migrations.RemoveField(
            model_name='smallgroup',
            name='page_ptr',
        ),
        migrations.AddField(
            model_name='smallgroup',
            name='description',
            field=mezzanine.core.fields.RichTextField(default='Group description', verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smallgroup',
            name='id',
            field=models.BigIntegerField(default=0, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smallgroup',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Group Name', blank=True),
        ),
    ]
