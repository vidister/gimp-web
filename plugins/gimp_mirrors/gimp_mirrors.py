from pelican import signals, contents
import os.path
from os.path import basename

'''
This is a skeleton for testing the parsing of a MIRRORS file
to show a list on /downloads/
'''

'''
It's been created by me, Pat David, to do what I need for wgo
don't try to make any sense of it.  I don't know what I'm doing.
I am not kidding.
'''

class UnexpectedException(Exception): pass

def do_mirrors(content_object):
    if type(content_object) is not contents.Page:
        return
    
    print "##########"
    print "%s" % content_object.metadata
    

def register():
    signals.content_object_init.connect(do_mirrors)
