from django.contrib import admin
import base64
import requests
import os

from mezzanine.core.admin import BaseTranslationModelAdmin
from mezzanine.pages.admin import PageAdmin, PageAdminForm
from mbc.models import EventGallery, ServiceRecording, Newsletter

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

admin.site.register(EventGallery, PageAdmin)
admin.site.register(ServiceRecording, PageAdmin)

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
        API_KEY = 'kLMCS5fYlOSnPhzTYsqe8Vb79glWL9c9Wiqzubci'
        url = 'https://pgmas4i5zb.execute-api.us-east-1.amazonaws.com/prod/apps/MBC/buckets/macedonia-static-site/items/newsletters/%s.b64' % obj.file_name
        resp = requests.put(url, data=base64.b64encode(obj.upload.read()), headers={'X-API-KEY': API_KEY})
        logging.debug('Response was %s' % resp.text)



admin.site.register(Newsletter, NewsletterAdmin)

