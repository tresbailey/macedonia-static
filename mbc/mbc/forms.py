from copy import deepcopy
from decimal import Decimal
from django import forms
from django import template
from django.db.models.fields import Field
from django.forms.models import BaseInlineFormSet, ModelFormMetaclass
from django.forms.models import inlineformset_factory
from django.forms.forms import BoundField
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.encoding import smart_text, force_text

from mezzanine.conf import settings
from mbc.models import Giving

class GivingForm(forms.ModelForm):
    """
    """

    class Meta:
        model=Giving
        fields=('full_name', 'envelope_number', 'amount')
        exclude=('transaction_id',)

    def __init__(self, data, giving=None, template='', *args, **kwargs):
        super(GivingForm, self).__init__(data)
        self.fields['full_name'] = forms.CharField(label=_('Full Name'))
        self.fields['envelope_number'] == forms.CharField(label=_('Tithe Envelope Number'))
        self.fields['amount'] = forms.CharField(label=_('Amount to Give'))
        print 'Fields: %s' % self.fields
