from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def add_css(value, arg):
  '''
  http://stackoverflow.com/a/18962481
  '''
  return value.as_widget(attrs={'class': arg})

@register.filter(name='replace_linebr')
@stringfilter
def replace_linebr(value):
    """Replaces all values of line break from the given string with a line space."""
    return value.replace("<p>", '').replace('</p>', '')
