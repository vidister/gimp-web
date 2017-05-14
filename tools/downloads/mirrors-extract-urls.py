#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import json
import urllib
import urlparse
from collections import OrderedDict

with open('../../content/downloads/mirrors2.json') as data:
    MIRRORS = json.load(data, object_pairs_hook=OrderedDict)

    for mirror, urls in MIRRORS.iteritems() :
        for url in urls:
            u = urlparse.urlparse(url)
            print u.scheme + '\t: ' +  u.hostname

    
