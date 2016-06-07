from django.contrib import admin

from mezzanine.pages.admin import PageAdmin
from mbc.models import EventGallery

admin.site.register(EventGallery, PageAdmin)
