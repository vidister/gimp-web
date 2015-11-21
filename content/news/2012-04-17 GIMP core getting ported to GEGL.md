Title: GIMP's Core Getting Ported to GEGL
Date: 2012-04-17
Category: News
Authors: Alexandre Prokoudine

In late 2007 we launched smooth transition to GEGL—a new advanced image processing core incepted by a team of Rhythm & Hues developers.

For v2.6 we made an optional GEGL-based implementation of color adjustment tools, and for upcoming v2.8 we implemented optional projection rendering via GEGL. But nobody really had evaluated the amount of the work to be done in order to finalize this transition. Until just now.

Five weeks ago Michael Natterer and Øyvind Kolås decided to finally work out the migration strategy. While working on that they found themselves [doing the actual porting](http://gimpfoo.de/2012/04/17/goat-invasion-in-gimp/). So now about 90% of the GIMP application’s core has been [ported to GEGL](http://git.gnome.org/browse/gimp/log/?h=goat-invasion). When finished, this will be released as GIMP 2.10 along with some other improvements yet to be decided on.

GEGL is quite an exciting project that will make it possible to implement some long anticipated features in a clean, non-sloppy way: high bit depth image processing and deep painting, non-destructive editing, a wider choice of color spaces to work in, mipmaps processing for faster perceived editing etc. This will be the focus of our future work after release of v2.10, along with further user interface improvements thanks to collaboration with Peter Sikking and his team at Man+Machine Works.

Now that we passed the point of no return with regards to GIMP and GEGL, we encourage you to join us and help porting the rest of GIMP. We'd really like to finish the boring part as soon as possible and start new exciting developments where we'd also need your support.

We also encourage you to [support](http://pledgie.com/campaigns/16614) Libre Graphics Meeting 2012 where developers of GIMP and other teams such as Scribus, Inkscape and Blender meet to align development strategies.