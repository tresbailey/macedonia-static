from collections import defaultdict
from datetime import date, timedelta, datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from json import dumps
from mezzanine.utils.views import render, set_cookie, paginate
from mbc import paypal_views, utils
from mbc.forms import GivingForm
from mbc.models import Giving, EventGallery

import logging
import pytz
logging.basicConfig(filename='example.log',level=logging.DEBUG)

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


class DailyEventListView(ListView):

    template_name='pages/events.html'

    def get_queryset(self):
        return EventGallery.daily.all()

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        logging.debug("Object list: %s" % self.object_list)
        context = self.get_context_data()
        return self.render_to_response(context)


class WeeklyEventListView(ListView):
    template_name='pages/about/service-times.html'

    def get_queryset(self):
        return EventGallery.weekly.all()

    def get(self, request, *args, **kwargs):
        event_groups = defaultdict(list)
        days = dict(utils.DAY_OF_WEEK)
        for event in self.get_queryset():
            event_groups[days[event.weekly_day]].append(event)
        self.object_list = dict(event_groups)
        logging.debug("Object list: %s" % self.object_list)
        context = self.get_context_data()
        return self.render_to_response(context)


