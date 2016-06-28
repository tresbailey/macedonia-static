from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import RichTextField
from mezzanine.galleries.models import Gallery, GalleryImage
from mezzanine.pages.models import Page


class EventGallery(Page):
    event_date = models.DateTimeField(verbose_name=_("Date of Event"))
    content = RichTextField(_("Content"))
   

class Giving(models.Model):
    full_name = models.CharField(_('Full Name'), max_length=50, blank=True, null=True)
    envelope_number = models.CharField(_("Tithe Envelope Number"), max_length=4, blank=True, null=True)
    amount = models.IntegerField(_('Amount to Give'))
    transaction_id = models.CharField(_('Card Transaction ID'), max_length=50, blank=True, null=True)

