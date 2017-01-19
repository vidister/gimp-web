from pelican import signals, contents
import os
import os.path
from os.path import basename


'''
Random Header Background Image
It's been created by me, Pat David, to do what I need for wgo.
Don't try to make any sense of it.  I don't know what I'm doing.
I am not kidding.
'''

class UnexpectedException(Exception): pass

def do_headerimg(pelican):

    HEADER_IMG_STYLE = "#banner { background-image: linear-gradient(rgba(44,52,80,0.5), rgba(44,62,80,0.5)), url('"+ pelican.settings['HEADER_IMG']['file'] +"'); }"

    if os.path.exists('./output/theme/css/home.css'):
        print "Appending banner style to home.css..."
        with open('./output/theme/css/home.css', 'a') as cssfile:
            cssfile.write( HEADER_IMG_STYLE )
    #else:
    #    print "Appending banner style to home.css..." 
    #    print "The path doesn't exist? (possibly building i18n - just wait)"


def register():
    signals.finalized.connect(do_headerimg)

