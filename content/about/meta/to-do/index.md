Title: To Do (Meta)
Date: 2015-08-06T16:01:03-05:00
Modified: 2015-08-06T16:01:12-05:00
Author: Pat David
Summary: Stuff to fix still.


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

## Combine and minimize assets

Probably run a grunt task (or whatever the equivalent is in Python) to combine and minimize assets like CSS and JS.


## <strike>Test Nested Folders</strike>

<strike>This To-Do page actually represents a test of nested content folders being created as expected for output.

That is, folder nested with an `index.md` file for the contents will work correctly.
If you're reading this in a browser, and the url looks like: `/about/meta/to-do/`, then it works! :)
</strike>  
2015-08-06T16:24:26-05:00


[FontAwesome]: http://fortawesome.github.io/Font-Awesome/
