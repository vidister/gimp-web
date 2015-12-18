from pelican import signals, contents
import os.path
from os.path import basename
#import geoip2.database
import socket
import json
import pygeoip


'''
This is a skeleton for testing the parsing of a MIRRORS file
to show a list on /downloads/
'''

'''
It's been created by me, Pat David, to do what I need for wgo.
This is based heavily on stuff the LoTR was doing already...
Don't try to make any sense of it.  I don't know what I'm doing.
I am not kidding.
'''

class UnexpectedException(Exception): pass

def do_mirrors(content_object):
    # Not 'Page' object?  Quit.
    if type(content_object) is not contents.Page:
        return
    
    # normalize OS path separators to fwd slash
    page = content_object
    path = content_object.source_path.replace( os.path.sep, '/' )

    #print "##########"
    #print "%s" % content_object
    #print "path: %s" % path
    #print dir(page)

    # if we are on a downloads page
    if '/downloads/index.md' in path:

        # create mirrors dict
        mirrors = {}
        # instantiate geoip object, load db 
        gi = pygeoip.GeoIP('./plugins/gimp_mirrors/GeoIP.dat')

        # load mirrors2.json file from content
        with open('./content/downloads/mirrors2.json') as data_file:
            data = json.load(data_file)

        for record in data:
            print "####"
            print record

            try:
                country = gi.country_name_by_name( record )
                print country

                if country in mirrors:
                    mirrors[ country ] += data[ record ]
                else:
                    mirrors[ country ] = data[ record ]

            except:
                print "cannot resolve record: ", record

        print( mirrors )

        page._content = page.content.replace(u"<!-- MIRRORS -->", u"<h2>Mirrors Test</h2>")



    

def register():
    signals.content_object_init.connect(do_mirrors)
