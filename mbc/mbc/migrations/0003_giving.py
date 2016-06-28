# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0002_rich_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Giving',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=50, null=True, verbose_name='Full Name', blank=True)),
                ('envelope_number', models.CharField(max_length=4, null=True, verbose_name='Tithe Envelope Number', blank=True)),
                ('amount', models.IntegerField(verbose_name='Amount to Give')),
                ('transaction_id', models.CharField(max_length=50, null=True, verbose_name='Card Transaction ID', blank=True)),
            ],
        ),
    ]
