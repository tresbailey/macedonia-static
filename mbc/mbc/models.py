from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import RichTextField
from mezzanine.galleries.models import Gallery, GalleryImage
from mezzanine.pages.models import Page


class EventGallery(Page):
    event_date = models.DateTimeField(verbose_name=_("Date of Event"))
    content = RichTextField(_("Content"))
    

