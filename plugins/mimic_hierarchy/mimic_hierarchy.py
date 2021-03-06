from pelican import signals, contents
import os.path
from os.path import basename
from copy import copy
from itertools import chain

'''
This plugin creates a URL hierarchy for pages that matches the
directory hierarchy of their sources.
'''

'''
It's been modified by me, Pat David, to do what I need for wgo
don't try to make any sense of it.  I don't know what I'm doing.
'''

class UnexpectedException(Exception): pass

def get_path(page, settings):
    ''' Return the dirname relative to PAGE_PATHS prefix. '''
    path = os.path.split(page.get_relative_source_path())[0] + '/'
    path = path.replace( os.path.sep, '/' )
    # Try to lstrip the longest prefix first
    for prefix in sorted(settings['PAGE_PATHS'], key=len, reverse=True):
        if not prefix.endswith('/'): prefix += '/'
        if path.startswith(prefix):
            return path[len(prefix):-1]
    raise UnexpectedException('Page outside of PAGE_PATHS ?!?')

def in_default_lang(page):
    # page.in_default_lang property is undocumented (=unstable) interface
    return page.lang == page.settings['DEFAULT_LANG']

def mimic_page_hierarchy(content_object):
    if type(content_object) is not contents.Page:
        return
    page = content_object

    #print( " " )
    #print( page )

    path = os.path.split(page.get_relative_source_path())[0]
    path = path.replace( os.path.sep, '/' )
    #print( "path: " + path )

    def _override_value(page, key):
        metadata = copy(page.metadata)

        #if hasattr(page, key):
        #    print("*_override_value, key: " + key +" - "+ getattr(page, key ) )
        #else:
        #    print("*_override_value, key: " + key +" - NONE" )

        #if hasattr(page, 'save_as') and key == 'save_as':
        #    print("HAS SAVE_AS..................................")
        #    metadata['SAVE_AS'] = page.url
        #    #setattr( page, 'override_save_as', page.override_url )

        # We override the slug to include the path up to the filename
        metadata['slug'] = os.path.join(path, page.slug)


        metadata['filename'] = os.path.split(page.get_relative_source_path())[1]
        metadata['filename'] = os.path.splitext( metadata['filename'])[0] + '.html'

        # PLD: This is a stupid hack.
        # I'm basically stripping the 'fr.' off of
        # translation files, and letting the i18n_subsite engine
        # take care of things from here.  I hope nobody reads this...
        fn = metadata['filename']
        metadata['filename'] = fn.replace('fr.', '')


        #print("#### filename: " + metadata['filename'] )
        #if 'index' in metadata['filename'] and 'about/meta' in metadata['slug']:
            #print('slug: ' + metadata['slug'] + '  filename: ' + metadata['filename'] )

        # PLD: this is my doing, sorry...
        # ok, if path is empty, use page.slug
        # if path is not empty, use path
        # still need to test if lang works properly after this
        if path:
            #print( "path: " + path )
            metadata['slug'] = path
        else:
            #print( "path empty! " + page.slug )
            metadata['slug'] = page.slug


        if metadata['filename'] != 'index.html':
            setattr(page, 'override_url', metadata['slug'] +'/'+ metadata['filename'] )
            if hasattr( page, 'save_as' ) and key == 'save_as':
                #setattr(page, 'override_save_as', page.override_url )
                #metadata['override_save_as'] = page.override_url
                return page.override_url
        
        #if hasattr(page, 'override_url'):
        #    print( "page.override_url: " + page.override_url )
        #if hasattr(page, 'override_save_as'):
        #    print( "page.override_save_as: " + page.override_save_as )

        #print("***** PAGE.SETTINGS *****")
        #for setting in page.settings:
        #    print( setting )

        # We have to account for non-default language and format either,
        # e.g., PAGE_SAVE_AS or PAGE_LANG_SAVE_AS
        infix = '' if in_default_lang(page) else 'LANG_'
        #if 'index' in metadata['filename'] and 'about/meta' in metadata['slug']:
            #print( "infix: " + infix + " key: " + key.upper() )
            #print( "RETURNING: " + page.settings['PAGE_' + infix + key.upper()].format(**metadata) )
        return page.settings['PAGE_' + infix + key.upper()].format(**metadata)



    for key in ('save_as', 'url'):
        #if hasattr(page, 'override_save_as'):
        #    print("FOR (override_save_as): " + getattr(page, 'override_save_as'))
        #if hasattr(page, 'override_url'):
        #    print("FOR (override_url): " + getattr(page, 'override_url'))
        if not hasattr(page, 'override_' + key):
            setattr(page, 'override_' + key, _override_value(page, key))
        

def set_relationships(generator):
    def _all_pages():
        return chain(generator.pages, generator.translations)

    # initialize parents and children lists
    for page in _all_pages():
        page.parent = None
        page.parents = []
        page.children = []

    # set immediate parents and children
    for page in _all_pages():
        # Parent of /a/b/ is /a/, parent of /a/b.html is /a/
        parent_url = os.path.dirname(page.url[:-1])
        if parent_url: parent_url += '/'
        for page2 in _all_pages():
            if page2.url == parent_url and page2 != page:
                page.parent = page2
                page2.children.append(page)
        # If no parent found, try the parent of the default language page
        if not page.parent and not in_default_lang(page):
            for page2 in generator.pages:
                if (page.slug == page2.slug and
                    os.path.dirname(page.source_path) ==
                    os.path.dirname(page2.source_path)):
                    # Only set the parent but not the children, obviously
                    page.parent = page2.parent

    # set all parents (ancestors)
    for page in _all_pages():
        p = page
        while p.parent:
            page.parents.insert(0, p.parent)
            p = p.parent


def register():
    signals.content_object_init.connect(mimic_page_hierarchy)
    signals.page_generator_finalized.connect(set_relationships)

