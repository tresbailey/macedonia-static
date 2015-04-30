#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tres Bailey'
SITENAME = u'Macedonia Baptist Church'

PATH = 'content'

THEME = 'twenty-pelican-html5up'
THEME_STATIC_DIR = 'theme'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

CATEGORY_URL = 'category/{slug}'

ARTICLE_ORDER_BY = 'Order'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

def sidebar(value):
  if value.startswith('archives') or value.startswith('category'):
    return 'right-sidebar'
  elif value == 'index':
    return 'index'
  else:
    return 'no-sidebar'

JINJA_FILTERS = {'sidebar': sidebar}

JINJA_EXTENSIONS = ['jinja2.ext.with_']

STATIC_PATHS = ['images',
                'fonts',
                'css',
                'js',
                ]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = False
