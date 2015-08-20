Title: Editing the Front Page
Date: 2015-08-20T09:42:26-05:00
Author: Pat David
Summary: How to edit the main landing page of the site.

So you'd like to modify the main landing page of this site?
Check with someone first.
Seriously.  Get on [irc]({filename}../../about/irc.md), and get someone to get support for what you want to do.


The reason I say this is that it's likely going to be a bit of work, and I'd hate for you
to get too far down the rabbit hole before finding out it may not be something that will be implemented.

Ok, still on track to fiddle with the front page?  Read on! Or just jump straight to the [TL;DR](#tldr).



## The Front Page

The way that [Pelican] is normally handling the front page of a site is to consider it a listing of
blog posts.  This means that a normal "front page" for a Pelican site usually has a list of all of the 
*Article* posts on the site.

This is not what we're doing here.

We still want a listing of *Article* posts, but in a different location than the front page
(I will be referring to the Pelican idea of *Article* as *News* items from now on).
Really, we want a (*relatively*) static front page, and we'd like to move the list of news items
to it's own page (and each news item gets it's own permalink as well).

So, the default way this works in Pelican is that the main front page for the site is auto-generated
from a template file:

    themes/themename/templates/index.html


### Modifying Default Behavior

We only need to modify two things to get the behavior we want.
From a high-level perspective:

1. Move the current news-indexed main page to a different location
2. Put a new static page at the old location (gimp.org/index.html).


#### Move old index.html to new location

We want the auto-generated page that indexes all of the *News* items to live in a different location.
Preferably, at: `www.gimp.org/news/index.html`.
This way, getting a list of the latest news can be found at the url: `www.gimp.org/news/`.

This is accomplished through a setting in `pelicanconf.py`:

    INDEX_SAVE_AS = "/news/index.html"

This setting will redirect what *was* the front page to a new location `/news/index.html`.
Note that the template to produce this page is still the `/themes/themename/tempates/index.html` file,
all we've done is redirected it's output to a new location.


#### Create new index.html

With the old front page redirected to a new location, we now need a new file to replace it.
This only requires that we create a new index file and give it an explicit override for some metadata.

I created a new folder just for this one file, `/content/frontpage/`.
In that folder, there is a file, `index.md` whose contents look like this:

    Title: GIMP
    Date: 2015-08-20T10:23:31-05:00
    URL:
    save_as: index.html
    Template: home

This is only a placeholder file to trigger the use of a new template.
It has two important pieces of metadata to get this behavior:

    save_as: index.html

Tells Pelican to save this file as the new main page, `gimp.org/index.html`.

    Template: home

This tells Pelican to use a custom template for this page, called "home", which is located here:

    themes/themename/templates/home.html

**Which**, *finally* gives us the file you'll need to modify to change the front page!

### TL;DR

To modify the front page, modify the file located at `/themes/themename/templates/home.html`.



## Editing Notes

In Pelican, all template will receive some [common variables](http://docs.getpelican.com/en/3.6.2/themes.html#common-variables) for parsing.  Something that we may want to include for example is the latest news post.

This can be accessed in the template through the `article` variable.  For instance, some common properties (from the most recent news post):
    
    articles[0].title
    articles[0].url
    articles[0].summary
    articles[0].author
    articles[0].date
    
The way it might actually be used in the template:

    <h3>Articles Object</h3>
        <div>
            <a href="{{ articles[0].url }}">{{ articles[0].title }}</a>
        </div>
        <div>
            {{ articles[0].summary }}
        </div>
        <div>
            {{ articles[0].author }}
        </div>
        <div>
            {{ articles[0].date }}
        </div>

