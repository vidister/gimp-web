Title: High Bit Depth Processing Available Now
Date: 2012-05-04
Category: News
Authors: Alexandre Prokoudine

Today at [Libre Graphics Meeting 2012](http://libre-graphics-meeting.org/2012/) in Vienna we announced that the development version of GIMP is now capable of processing images in 16bit and 32bit modes, integer or float at your preference.

Transformation, painting and color adjustment tools will just work in higher bit depth precision modes. More than that, GIMP can load and save 16bit PNG images and save EXR and HDR files now. We also improved support for indexed images, so that you could finally paint over them with the Smudge tool or apply filters.

There is still a lot of work left to do, and this is a great chance for potential contributors to step up and begin improving the application. Low-hanging fruits include porting of file loaders and savers, filters and other small bits of GIMP that don't require a lot of familiarity with the internal structure. Please contact us in the gimp-developer mailing list.

Decision on the final feature set in 2.10 is yet to be made, no time-based schedule is available either. However we fully intend to make development cycles much shorter.