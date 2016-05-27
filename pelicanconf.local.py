#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["mimic_hierarchy", "i18n_subsites", "sitemap", "gimp_mirrors", "tipue_search"]

# sitemap plugin settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 1
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'weekly'
    }
}

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
        'fr': {
            'SITENAME': 'GIMP FR',
            },
        }

AUTHOR = u'Pat David'
SITENAME = u'GIMP'
SITEURL = '//www.gimp.org'
SITEMAP_SITEURL = 'https://www.gimp.org'
GIMP_VERSION = u'2.8.16'

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

# Feed generation is usually not desired when developing
#FEED_DOMAIN = SITEURL
#FEED_ATOM = 'feeds/atom.xml'
#FEED_RSS = 'feeds/rss.xml'
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#TRANSLATION_FEED_ATOM = 'feeds/all-%s.atom.xml'
#TRANSLATION_FEED_RSS = 'feeds/all-%s.rss.xml'
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

#  # Blogroll
#  LINKS = (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)
#  
#  # Social widget
#  SOCIAL = (('You can add links in your config file', '#'),
#            ('Another social link', '#'),)

DEFAULT_PAGINATION = False



# Pat David changes while building/testing
READERS = {'html': None}

# This will copy over these folders w/o modification
STATIC_PATHS = ['images', 'js', 'pages', 'tutorials', 'about', 'books', 'develop', 'docs', 'donating', 'downloads', 'features', 'bugs', 'links', 'man', 'release-notes', 'screenshots', 'source', 'unix', 'robots.txt', 'COPYING', 'GNUGPLv2', 'GNUGPLv3', 'news']

# This sets which directories will be parsed as pages (vs. news/articles)
# If a new directory is to be added under content/, make sure it gets added here.
PAGE_PATHS = ['about', 'frontpage', 'tutorials', 'books', 'develop', 'docs', 'donating', 'downloads', 'features', 'bugs', 'links', 'man', 'release-notes', 'screenshots', 'source', 'unix', 'search.md']

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
# This sets the "old" index.html page to be saved to /news/index.html.
INDEX_SAVE_AS = "/news/index.html"


TYPOGRIFY = True
TYPOGRIFY_IGNORE_TAGS = ['title']

DELETE_OUTPUT_DIRECTORY = True

MD_EXTENSIONS = ['fenced_code', 'codehilite(css_class=codehilite)', 'extra', 'headerid', 'toc(permalink=True)']

# Pagination testing stuff

DEFAULT_ORPHANS = 0
DEFAULT_PAGINATION = 10

# Debug output on pages
# Seting to 'True' will show child/parent pages at bottom of pages
PAGES_DEBUG = False

# When developing, you probably want document relative URLs - so set this to True
# When publishing, set to False
RELATIVE_URLS = True
