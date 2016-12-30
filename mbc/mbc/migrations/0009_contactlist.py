# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0008_newsletter_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mailing_list', models.CharField(max_length=50, null=True, verbose_name='Mailing List Name', blank=True)),
                ('email_alias', models.EmailField(max_length=254, verbose_name='Email Alias')),
                ('upload', models.FileField(null=True, upload_to=b'news', blank=True)),
            ],
        ),
    ]
