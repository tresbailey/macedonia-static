from django import template
from django.template.defaultfilters import stringfilter
from datetime import datetime
from mbc.models import EventGallery

register = template.Library()

@register.filter
def add_css(value, arg):
  '''
  http://stackoverflow.com/a/18962481
  '''
  return value.as_widget(attrs={'class': arg})

@register.filter
def help_text(value, arg):
    return value.as_widget(attrs={'aria-describedby': arg +'Help'})

@register.filter(name='replace_linebr')
@stringfilter
def replace_linebr(value):
    """Replaces all values of line break from the given string with a line space."""
    return value.replace("<p>", '').replace('</p>', '')


@register.filter
def future_dates_only(the_date):
   '''
   http://stackoverflow.com/a/4493818
   '''
   if the_date.replace(tzinfo=None) > datetime.now():
       return the_date
   else:
       return None


@register.inclusion_tag('pages/coming-sunday.html')
def coming_sunday(takes_context=False):
    return {'object_list': EventGallery.sunday.all()}
