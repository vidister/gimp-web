Title: Using Pelican
Date: 2015-08-10T14:43:06-05:00
Modified: 2015-08-10T14:43:11-05:00
Author: Pat David
Summary: Using Pelican

These are some meta notes about using the Pelican build system, including any idiosyncrasies I come across while testing it.

## Project Directory Structure

This project (the entire site) is housed under a single directory.
The important files and directories look like this:

```
gimp-web-static/
    - pelicanconf.py
    - Makefile
    - content/
        - about/
            - index.md
            - meta/
                - index.md
                - wtf-pelican.md
                - fluffle-puff.jpg
                - using-pelican/
                    - index.md
                - to-do/
                    - index.md
        - tutorials/
            - index.md
            - GIMP_Quickies/
                - index.md
                - ...
        - news/
            - 2015-08-10 An Update.md
            - 2015-07-28 Other Stuff.md
            - ...
    - plugins/
    - themes/
    - output/
```


## pelicanconf.py

This file contains settings for Pelican to generate the site.
Don't play with this file unless you're feeling comfortable about what things do.


## Content

There are two main types of content as far as Pelican is concerned: **pages** and **articles**.


### Pages

Pages are simply static page content that doesn't change often in general.
**About**, **Downloads**, or even this **Meta** page are all considered *page* content.

Almost *all* of the old site could be considered *page* content.


#### In Pelican

The way that Pelican is told to parse content as *pages* rather than *articles* is through the `pelicanconf.py` file in the root of the project directory.
There is a particular setting in that file that describes the path to *page* content (relative to the `content` directory):

`PAGE_PATHS = ['about', 'tutorials']`

As you can see, two directories of content will be parsed as *pages*, `about` and `tutorials`.

The modification of the [Page Hierarchy]({filename}../wtf-pelican.md) plugin means that any sub-folders of `page` directories will be parsed and nested just as they are in the `content` directory.


#### Tutorials

A good example of *page* content are the tutorials from the old site.
The modified Page Hierarchy plugin is handy here, as it allows the tutorials to be stand-alone discrete directories full of assets + the tutorial written as a Markdown file.
This makes things much more portable in the event the user wants to re-use the tutorials somewhere else, or if the site infrastructure changes for some reason.



### Articles

*Articles* to Pelican are dated content being published in the context of time.
They are usually permalinked based on their date/title and are often displayed on a page as an archival series of posts.


#### News Items (and Blog Posts?)

The most natural fit for this type of content would be *News* posts and similarly *Blog* posts.
There's really no difference, the posts are all *Articles* as far as Pelican is concerned.
The nice difference from the past is that each post now gets it's own permalinked page.

<del>Any content *not* explicitly inside of a `PAGE_PATHS` location will be parsed as an *Article* by Pelican.</del>
For keeping things tidy, I've created a sub-directory called *news* to keep those posts organized.

The `pelicanconf.py` file has a setting for explicitly setting the location of *Articles*:

    ARTICLES_PATHS = ['news']

This will tell Pelican to look for articles only under the listed path(s).

---
## Pelican Notes

### Hide Page on Navigation

To hide a page from being included on the navigation elements, add to the pages metadata:

`status: hidden`

At the moment, with the addition of the *Page Hierarchy* plugin, each page also gets extra metadata
that describes the pages parents and children.
While testing, I assumed I would *not* want sub-pages to be listed in the navigation (ie: only top-level pages should be listed).

So, in the `themes/newgimp/templates/base.html` base template file, I did this to the navigation element:

    {% for p in PAGES %}
        {% if p.parents|length == 1 %}
          <li{% if p == page %} class="active"{% endif %}>
            <a href="{{ SITEURL }}/{{ p.url }}">{{ p.title }}</a>
          </li>
        {% endif %}
    {% endfor %}

That is, if page.parents length is "1", then it must be a top-level page, and list it in the navigation.
Note that the `status: hidden` metadata on the page will override this behavior if desired.


### Python SimpleHTTPServer & SVG

Apparently the python (2.7.x) built-in http server doesn't serve .svg files correctly for use as images in html.
To fix this, either run a different http server to test with, or from [this blog post](http://gotmetoo.blogspot.com/2013/07/python-simple-http-server-with-svg.html) you can do this:

    :::python
    #!/usr/bin/python 
    import SimpleHTTPServer
    import SocketServer
    import mimetypes
    
    PORT = 8000
    
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    
    Handler.extensions_map['.svg']='image/svg+xml'
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    
    print "serving at port", PORT
    httpd.serve_forever()

Or just be aware that any SVG elements used as images will not display correctly on the page (but *should* display fine when being served from wgo).
Honestly, if you're not working on showing/linking SVG elements as images, you can safely ignore this.
