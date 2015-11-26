Title: All GSoC 2012 Students Passed Midterm Evaluation
Date: 2012-07-20
Category: News
Authors: Alexandre Prokoudine

We are glad to announce that all of our Google Summer of Code 2012 students passed the midterm evaluation last week.

All projects are coming along nicely. The unified transform is already quite functional, the experimental GEGL editor is maturing, more filters were rewritten into GEGL operations, and more parts of GEGL were adapted for the new image processing core.

There's also substantial progress with the Seamless Clone tool that was part of Google Summer of Code 2011 program. The tool relies on Poly2tri — a C++ library for generating constrained Delaunay triangulations. You can read more about this project in [the developer's blog](http://lightningismyname.blogspot.com/).

The Poly2tri library is likely to be used by the next generation of the Cage Transform tool (available since v2.8). This is expected to simplify and hence speed up calculations which are currently slow when used on large images.
