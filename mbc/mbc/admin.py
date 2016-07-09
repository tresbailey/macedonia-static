from django.contrib import admin

from mezzanine.pages.admin import PageAdmin
from mbc.models import EventGallery, ServiceRecording

admin.site.register(EventGallery, PageAdmin)
admin.site.register(ServiceRecording, PageAdmin)
