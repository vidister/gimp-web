Title: To Do (Meta)
Date: 2015-08-06T16:01:03-05:00
Modified: 2015-08-06T16:01:12-05:00
Author: Pat David
Summary: Stuff to fix still.

In no particular order, just general notes on stuff that should be addressed...

## Showcase pages

Per Americo's suggestion - consider some pages that we can use to showcase artwork and contributions from the community.
Possibly expand news/articles posts to include interviews and other outreach to the community at large?  I like it!

## Download Page Auto-Detect OS

The general consensus is that everyone likes the auto-detection of OS.
I'll have a deeper look at a good way to do this (hopefully without having to link in all of jquery as dependency).

I'm going to start by styling the page assuming no scripts at all, then progressively enhance it to auto-detect and display.

I'm using [platform.js](https://github.com/bestiejs/platform.js/) to do the detecting.
It currently provides more than we likely need but we'll roll with it (it's much less than pulling in jquery).

At the moment, the OS will be detected as one of the following:

    var os = getOS([
      'Windows Phone ',
      'Android',
      'CentOS',
      'Debian',
      'Fedora',
      'FreeBSD',
      'Gentoo',
      'Haiku',
      'Kubuntu',
      'Linux Mint',
      'Red Hat',
      'SuSE',
      'Ubuntu',
      'Xubuntu',
      'Cygwin',
      'Symbian OS',
      'hpwOS',
      'webOS ',
      'webOS',
      'Tablet OS',
      'Linux',
      'Mac OS X',
      'Macintosh',
      'Mac',
      'Windows 98;',
      'Windows '
    ]);


## Link Order in Nav bar

Sort these items by *importance*.
Not sure *what* is most important, so check with the team to clarify the best order of items here.

A general feeling is around possibly having screenshots be first/more prominent, then a little bit about the page, then download.

Should screenshots be integrated into the main front page in some way as opposed to a separate page?  I'm going to ping the ML on this.


## Check/Add Support for Other Input Filetypes

I used Markdown by default, but per Marco's suggestions, get support for asciidoc working!

We already have restructuredtext (rest) by default with Pelican, but having other types can help further lower the 
barrier to entry/contributions.  I'll have to see what it'll take to get asciidoc working.


## <del>Test/Port News Items</del>

<del>2015-08-19T14:25:29-05:00</del>

<del>
Test that news items are permalinked and generated correctly.
Also test that they are properly aggregated on an index page, and that the 
pagination is working correctly.</del>

<del>
The actual number of news posts over the years makes me think it shouldn't be too much of a problem,
but I'd rather have it all working for a ton of posts and not need it (vs. the other way around...).
</del>

2015-08-27T14:59:29-05:00

## SVG Spritesheet

I am using [FontAwesome] at the moment for some small icons as I flesh things out.
This is not ideal, I think.
It may be smarter to combine any icons we may use as an SVG spritesheet and call it as needed.
It could certainly be more lightweight I'd imagine.


## Get Fonts in Order

Collect all the final font decisions and get them saved in the correct directories.
Also link them with @font-face correctly in the css for the site.
Consider Google Fonts as an option for font hosting?
Check with the others to see what the general consensus would be.

<small>2015-08-11T11:46:08-05:00</small>  
Temporarily set to using Google fonts to hopefully leverage any caching for clients.
Current font faces include:

* League Gothic<sup>1</sup>
* Ostrich Sans<sup>1</sup>
* Open Sans (body fonts)
* Lato (navigation font)
* Questrial (body headings)

<small>1: These are only used on the front page currently (in the header).</small>

<small>2015-08-14T13:11:17-05:00</small>  
drc has reported some issues with hinting the navigation bar font (Lato) at its current size.
I cannot reproduce his results exactly.
Looking into either increasing the weight of that font to 400 (from 300), or to swap it for a different typeface.
Possibly Roboto, Ostrich Sans (GNU Image Manipulation Program)?

<small>2015-09-03T09:05:44-05:00</small>  
There are still rendering issues for akk and drc for the navigation item font, Lato.

I'm switching it to Josefin Sans for the time being to see if it renders nicer.
Don't forget to host the font files from wgo before going live (or asap after).


## Combine and minimize assets

Probably run a grunt task (or whatever the equivalent is in Python) to combine and minimize assets like CSS and JS.


## <strike>Test Nested Folders</strike>

<strike>This To-Do page actually represents a test of nested content folders being created as expected for output.

That is, folder nested with an `index.md` file for the contents will work correctly.
If you're reading this in a browser, and the url looks like: `/about/meta/to-do/`, then it works! :)
</strike>  
2015-08-06T16:24:26-05:00


[FontAwesome]: http://fortawesome.github.io/Font-Awesome/
