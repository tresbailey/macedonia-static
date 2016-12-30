# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mbc', '0009_contactlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_date', models.DateTimeField(verbose_name='Date of Service')),
                ('upload', models.FileField(null=True, upload_to=b'bulletins', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SmallGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meeting_schedule', models.CharField(default=b'weekly', max_length=25, verbose_name='Meeting Schedule', choices=[(b'daily', b'Daily'), (b'weekly', b'Weekly'), (b'semiweekly', b'Semi-Weekly'), (b'monthly', b'Monthly'), (b'semimonthly', b'Semi-Monthly'), (b'quarterly', b'Quarterly'), (b'yearly', b'Yearly'), (b'adhoc', b'Ad Hoc')])),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Group Name', blank=True)),
                ('description', mezzanine.core.fields.RichTextField(verbose_name='description')),
                ('gender', models.CharField(default=b'all', max_length=10, verbose_name='Group Gender', choices=[(b'men', b'Men'), (b'women', b'Women'), (b'all', b'Everyone')])),
                ('owner', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='servicerecording',
            name='mp3_upload',
            field=models.FileField(null=True, upload_to=b'recordings', blank=True),
        ),
        migrations.AddField(
            model_name='servicerecording',
            name='ogg_upload',
            field=models.FileField(null=True, upload_to=b'recordings', blank=True),
        ),
        migrations.AlterField(
            model_name='contactlist',
            name='upload',
            field=models.FileField(null=True, upload_to=b'contacts', blank=True),
        ),
    ]
