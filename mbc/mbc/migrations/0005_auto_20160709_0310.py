# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mbc', '0004_servicerecording'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerecording',
            old_name='service_data',
            new_name='service_date',
        ),
    ]
