from datetime import datetime
from django.db import models
from django.forms.fields import ChoiceField
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import RichTextField
from mezzanine.galleries.models import Gallery, GalleryImage
from mezzanine.pages.models import Page

import logging
import pytz
logging.basicConfig(filename='mbc.log',level=logging.DEBUG)


GROUP_SCHEDULE_CHOICES = (
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('semiweekly', 'Semi-Weekly'),
    ('monthly', 'Monthly'),
    ('semimonthly', 'Semi-Monthly'),
    ('quarterly', 'Quarterly'),
    ('yearly', 'Yearly'),
    ('adhoc', 'Ad Hoc')
)

GROUP_GENDERS = (
    ('men', 'Men'),
    ('women', 'Women'),
    ('all', 'Everyone')
)

class SmallGroup(models.Model):
    meeting_schedule = models.CharField(_("Meeting Schedule"), 
        choices=GROUP_SCHEDULE_CHOICES,
        default='weekly',
        max_length=25)
    name = models.CharField(_("Group Name"), max_length=50, blank=True, null=True)
    description = RichTextField(_("description"))
    gender = models.CharField(_("Group Gender"), 
        choices=GROUP_GENDERS,
        default='all',
        max_length=10)
    owner = models.OneToOneField("auth.User")



DAY_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday')
)


class DailyManager(models.Manager):
  def get_queryset(self):
    items = super(DailyManager, self).get_queryset().filter(weekly_worship=False, event_date__gte=datetime.now()).order_by('event_date')
    logging.debug('not_weekly are: %s' % str(items))
    return items


class WeeklyManager(models.Manager):
  def get_queryset(self):
    items = super(WeeklyManager, self).get_queryset().filter(weekly_worship=True).order_by('event_date')
    logging.debug('weekly are: %s' % str(items))
    return items


class EventGallery(Page):

    objects = models.Manager()
    daily = DailyManager()
    weekly = WeeklyManager()

    event_date = models.DateTimeField(verbose_name=_("Date of Event"))
    content = RichTextField(_("Content"))
    weekly_worship = models.NullBooleanField(verbose_name=_("Weekly Worship Event"))
    weekly_day = models.IntegerField(_("Weekly Day"), 
        choices=DAY_OF_WEEK,
        default=0,
        null=True,
        blank=True)
    scheduled_time = models.TimeField(verbose_name=_("Weekly Scheduled Time"), null=True)
    group = models.ForeignKey(SmallGroup, on_delete=models.CASCADE, null=True, blank=True)

class ServiceRecording(Page):
    service_date = models.DateTimeField(verbose_name=_("Date of Service"))
    preacher_name = models.CharField(_("Preacher of the Service"), max_length=50, blank=True, null=True)
    mp3_location = models.URLField()
    ogg_location = models.URLField()
    overview = RichTextField(_("Overview"), blank=True, null=True)
    mp3_upload = models.FileField(upload_to='recordings', blank=True, null=True)
    ogg_upload = models.FileField(upload_to='recordings', blank=True, null=True)
   

class Giving(models.Model):
    full_name = models.CharField(_('Full Name'), max_length=50, blank=True, null=True)
    envelope_number = models.CharField(_("Tithe Envelope Number"), max_length=4, blank=True, null=True)
    amount = models.IntegerField(_('Amount to Give'))
    transaction_id = models.CharField(_('Card Transaction ID'), max_length=50, blank=True, null=True)


class Newsletter(models.Model):
    newsletter_date = models.DateTimeField(verbose_name=_("Date of Newsletter"))
    file_name = models.CharField(_('Newsletter File Name'), max_length=50, blank=True, null=True)
    upload = models.FileField(upload_to='news', blank=True, null=True)


class ContactList(models.Model):
    mailing_list = models.CharField(_('Mailing List Name'), max_length=50, blank=True, null=True)
    email_alias = models.EmailField(_('Email Alias'))
    upload = models.FileField(upload_to='contacts', blank=True, null=True)


class Bulletin(models.Model):
    service_date = models.DateTimeField(verbose_name=_("Date of Service"))
    upload = models.FileField(upload_to='bulletins', blank=True, null=True)

