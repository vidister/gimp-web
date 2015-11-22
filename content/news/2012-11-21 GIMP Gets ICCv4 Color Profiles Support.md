Title: GIMP Gets ICC v4 Color Profiles Support 
Date: 2012-11-21
Category: News
Authors: Alexandre Prokoudine

For the last few weeks GIMP has been capable of using ICC v4 color profiles thanks to a patch by [Laurent Martelli](http://www.laurentmartelli.com/) who ported the color management plug-in to use LittleCMS v2.

There is also an ongoing work by [Elle Stone](http://ninedegreesbelow.com/) to adapt that plug-in to the new GEGL-based architecture and make color space conversions just work between various bit depth precision levels — from 8-bit to 32-bit floating point.

Once it's done, GIMP will be capable of converting images between different color spaces with little to no loss of color fidelity. In fact, it already works, with some caveats.

Meanwhile Michael Natterer is busy porting plug-ins for loading and saving files to GEGL and GIO. The latter means that GIMP doesn't create temporary files anymore when loading files from remote locations, and previews in the Open File dialog 100% match actual images.

There is still a lot of work to do before GEGL-based version of GIMP is completely functional. We encourage you to join the team and help making the future closer.