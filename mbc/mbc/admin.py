from datetime import date, timedelta, datetime
from django.contrib import admin
import base64
import csv
import json
import pytz
import requests
import os

from mezzanine.core.admin import BaseTranslationModelAdmin, TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin, PageAdminForm
from mezzanine.galleries.admin import GalleryAdmin
from mbc.models import EventGallery, ServiceRecording, \
    Newsletter, ContactList, SmallGroup, BlockyPage, LeftImageBlock, RightImageBlock
from mbc import utils

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)


API_KEY = 'kLMCS5fYlOSnPhzTYsqe8Vb79glWL9c9Wiqzubci'


def send_to_s3_gateway(prefix, file_name, data, bucket='macedonia-static-site', b64_encoded=True):
    url = 'https://pgmas4i5zb.execute-api.us-east-1.amazonaws.com/prod/apps/MBC/buckets/%s/items/%s/%s' % (bucket, prefix, file_name)
    if b64_encoded:
        url = url + '.b64'
        data = base64.b64encode(data)
    resp = requests.put(url, data=data, headers={'X-API-KEY': API_KEY})
    logging.debug('Response was %s' % resp.text)
    return 'https://s3.amazonaws.com/%s/%s/%s' % (bucket, prefix, file_name)


class NewsletterAdminForm(PageAdminForm):
  def save(self, force_insert=False, force_update=False, commit=True):
      print "SAVING!!!!"

class NewsletterAdmin(BaseTranslationModelAdmin):
    ordering = ('newsletter_date', )
    list_display = ('file_name',)
    
    def get_fields(self, request, obj=None):
        '''
        Returns the fields for the Admin page.
        Removes the file_name field, so that it is hidden, and only updated by code
        '''
        fields = super(BaseTranslationModelAdmin, self).get_fields(request, obj)
        fields.remove("file_name")
        return fields

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.file_name = os.path.basename(obj.upload.path)
        obj.save()
        bucket = 'macedonia-static-site'
        prefix = 'newsletters'
        send_to_s3_gateway(prefix, obj.file_name, obj.upload.read())



admin.site.register(Newsletter, NewsletterAdmin)

class ContactListAdmin(BaseTranslationModelAdmin):
    ordering = ('mailing_list', )
    list_display = ('mailing_list', 'email_alias')

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.save()
        bucket = 'macedonia-static-site'
        prefix = 'contact-lists'
        file_name = os.path.basename(obj.upload.path)
        send_to_s3_gateway(prefix, file_name, obj.upload.read())
        contact_list = csv.reader(obj.upload)
        contact_list = [{'address': cont[2], 'name': '%s %s' % (cont[0], cont[1])} 
            for cont in contact_list]
        logging.debug("Contact list: " + str(contact_list))
        resp = requests.post(
            "https://api.mailgun.net/v3/lists/%s/members.json" % obj.email_alias,
            auth=("api", "key-43c6c3d0cc532cf009ad7e90861352a4"),
            data={"members": json.dumps(contact_list),
                "upsert": "yes"})
        logging.debug("Response: "+ resp.text)
         



admin.site.register(ContactList, ContactListAdmin)

class SmallGroupAdmin(BaseTranslationModelAdmin):
    ordering = ('name', )
    list_display = ('name', 'description')

admin.site.register(SmallGroup, SmallGroupAdmin)

class ServiceRecordingAdmin(PageAdmin):
    def save_model(self, request, obj, form, change):
        super(PageAdmin, self).save_model(request, obj, form, change)
        bucket = 'macedonia-static-site'
        prefix = 'recordings'
        if obj.mp3_upload:
            file_name = os.path.basename(obj.mp3_upload.path)
            obj.mp3_location = send_to_s3_gateway(prefix, file_name, obj.mp3_upload.read())
        if obj.ogg_upload:
            file_name = os.path.basename(obj.ogg_upload.path)
            obj.ogg_location = send_to_s3_gateway(prefix, file_name, obj.ogg_upload.read())
        obj.save()
        

admin.site.register(ServiceRecording, ServiceRecordingAdmin)


def weekly_individuals(weekly, new_date, weekly_id):
    individual = weekly
    individual.id = None
    individual.parent_id = weekly_id
    individual.page_ptr_id = None
    individual.event_date = new_date
    individual.weekly_worship = False
    individual.save()
    return individual


class EventGalleryAdmin(PageAdmin):
    ordering = ('event_date', )

    def save_model(self, request, obj, form, change):
        super(EventGalleryAdmin, self).save_model(request, obj, form, change)
        if obj.weekly_worship:
            parent_id = obj.id
            individuals = [weekly_individuals(obj, cal_week, parent_id)
                for cal_week in utils.all_of_days(obj.weekly_day, obj.scheduled_time)
                if cal_week >= datetime.now(pytz.utc)]
                

admin.site.register(EventGallery, EventGalleryAdmin)

admin.site.register(BlockyPage, PageAdmin)
admin.site.register(LeftImageBlock, PageAdmin)
admin.site.register(RightImageBlock, PageAdmin)
