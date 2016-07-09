# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('mbc', '0003_giving'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRecording',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('service_data', models.DateTimeField(verbose_name='Date of Service')),
                ('preacher_name', models.CharField(max_length=50, null=True, verbose_name='Preacher of the Service', blank=True)),
                ('mp3_location', models.URLField()),
                ('ogg_location', models.URLField()),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
    ]
