# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0007_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='upload',
            field=models.FileField(null=True, upload_to=b'news', blank=True),
        ),
    ]
