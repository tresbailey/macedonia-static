from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView
from json import dumps
from mezzanine.utils.views import render, set_cookie, paginate
from mbc import paypal_views
from mbc.forms import GivingForm
from mbc.models import Giving


def online_giving(request, template='giving.html', form_class=GivingForm, extra_context=None):
    model = Giving
    initial_data = {'full_name': '',
        'envelope_number': '',
        'amount': 0}
    begin_giving = form_class(request.POST or None, initial=initial_data)
    context = {
        'editable_obj': model,
        'begin_giving': begin_giving
    }
    if 'POST' == request.method:
        if begin_giving.is_valid():
            model = begin_giving.save()
            return paypal_views.client_token(request, extra_content={'giving_id': model.id, 'amount': model.amount, 'giver': model.full_name})
    return render(request, template, context)
