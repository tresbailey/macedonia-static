# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0006_servicerecording_overview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('newsletter_date', models.DateTimeField(verbose_name='Date of Newsletter')),
                ('file_name', models.CharField(max_length=50, null=True, verbose_name='Newsletter File Name', blank=True)),
            ],
        ),
    ]
