#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Plugins
PLUGIN_PATHS = ["plugins"]
#PLUGINS = ["page_hierarchy_gimp"]
PLUGINS = ["mimic_hierarchy"]

AUTHOR = u'Pat David'
SITENAME = u'GIMP'
SITEURL = 'http://static.gimp.org'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Pat David changes while building/testing

# This will copy over these folders w/o modification
STATIC_PATHS = ['images', 'pages', 'tutorials', 'about', 'books', 'develop', 'docs', 'donating', 'downloads', 'features', 'bugs', 'links', 'man', 'release-notes', 'screenshots', 'source', 'unix']

# This sets which directories will be parsed as pages (vs. news/articles)
PAGE_PATHS = ['about', 'pages', 'tutorials', 'books', 'develop', 'docs', 'donating', 'downloads', 'features', 'bugs', 'links', 'man', 'release-notes', 'screenshots', 'source', 'unix']

ARTICLE_PATHS = ['news']

THEME = "./themes/newgimp"

PAGE_URL = "{slug}/"
#PAGE_SAVE_AS = "{slug}/index.html"
PAGE_SAVE_AS = "{slug}/{filename}"

ARTICLE_URL = "news/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "news/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

# This redirects the old standard output of blog/news/articles post
# summaries on the front page.  It will now appear at the location
# below instead.
# The _actual_ index.html page is located at:
# content/pages/index.md -> which simply calls the home.html template
# See: http://docs.getpelican.com/en/3.6.3/faq.html#how-can-i-use-a-static-page-as-my-home-page
INDEX_SAVE_AS = "/news/index.html"

TYPOGRIFY = True
TYPOGRIFY_IGNORE_TAGS = ['title']

DELETE_OUTPUT_DIRECTORY = True

MD_EXTENSIONS = ['fenced_code', 'codehilite(css_class=codehilite)', 'extra', 'headerid', 'toc']


# Pagination testing stuff

DEFAULT_ORPHANS = 0
DEFAULT_PAGINATION = 5

