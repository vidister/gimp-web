Title: GIMP 2.9.4 Released
Date: 2016-12-31
Category: News
Authors: Alexandre Prokoudine
Slug: gimp-2-9-4-released
Status: draft
Summary: We have just released the second development version of GIMP in the 2.9.x series. GIMP 2.9.4 features revamped look and feel, major improvements in color management, as well as production-ready MyPaint Brush tool, symmetric painting, and split preview for GEGL-based filters.

We have just released the second development version of GIMP in the 2.9.x series. GIMP 2.9.4 features revamped look and feel, major improvements in color management, as well as production-ready MyPaint Brush tool, symmetric painting, and split preview for GEGL-based filters. Additionally, XX bugs have been fixed, and numerous small improvements have been applied.

## Revamped User Interface

* new themes (Benoit Touchette)
* symbolic icon theme and switching icon themes (Barbara Muraus, Benoit Touchette and Klaus Staedtler)
* vector icons for HiDPI displays (--enable-vector-icons)
* app: enable a pulsing progress bar in the splash
* Reordered Preferences dialog
* Configurable undo preview size (no more manual config file editing)

## Color Management Improvements

* Color-managing grayscale images
* app: prepare the color profile dialog for doing RGB <-> GRAY conversion
* Bug 765176 * ICC profile conversions between grayscale and RGB images
* Bug 478528 * Layer and Image previews are not color managed
* app: implement GimpColorManaged in GimpDrawable
* pygimp: add GimpColorConfig object
* pygimp: add type definition for GimpColorManaged
* libgimpcolor: add gimp_color_profile_save_to_file()
* app: add Image -> Color Management -> Save Color Profile to File...
* libgimpwidgets: update OS X code to get display profile to new API (Kris)
* libgimpwidgets: Mac OS X: read ICC profile from the correct buffer
* app: add a per-image "is color managed" switch
* app: pass the right color profile around in gimp_selection_float()
* app: show the image's "is color managed" state in the window title string
* app: add basic support for creating images with color profiles
* app: clean up Preferences -> Color Management
* Bug 320447 * fast switching between "color managed display" and "softproof"
* app: add tooltips that mention that disabling color management == sRGB
* Bug 748749 * picked colors don't match image colors...
* libgimpwidgets: add gimp_preview_area_set_color_config()
* libgimpcolor: add new object GimpColorTransform: which encapsulates a cmsHTRANSFORM and does all the pixel format conversion magic. It has API to create transforms and proofing transforms, and to convert pixels arrays and GeglBuffers. Before, each place which has a transform had to keep around the transform and its input and output Babl formats, and had to implement lots of stuff itself. Now all that lives in GimpColorTransform, removing lots of logic from many places, and pretty much removing lcms from the public API entirely. This removes including <lcms2.h>, LCMS_LIBS and LCMS_CFLAGS from almost all directories and potentially allows to replace lcms by something else.
* libgimpwidgets: set the color config on GimpColorSelection's color areas
* libgimpwidgets: set the color config on the "GIMP" page of color selectors
* app: color manage the color buttons of GimpColorHistory
* app: color manage GimpFgBgEditor, as used e.g. in the toolbox
* libgimpcolor: add CMYK formats to gimp_color_profile_get_format()
* Bug 467930 * color selectors are not color managed
* app: make all GimpViewRenderers color manage themselves, color manage palette and gradient previews (patterns, gradients, swatches)
* app: set a color config on color areas created from menu actions
* Bug 766988 * Colors applied to images are not color managed
* app: color manage the color DND icon widget
* app: color manage GimpColorPanel and its color dialog (gegl tool dialogs etc.)
* app: set the color config on the color picker tool dialog's color area
* libgimpwidgets: always ask the toplevel window for its color profile
* libgimpwidgets, app: have all previews track the monitor they are on

## GEGL

* Bug 759316 * "Recently used" menu not updated with gegl filters
* app: turn the posterize tool into an ordinary GEGL filter
* app: turn the desaturate tool into a normal GEGL filter
* menus: move "Desaturate" to Colors -> Desaturate
* app: add gegl:saturation as Colors -> Saturation
* app: add gegl:high-pass as Filters > Enhance > High Pass
* Bug 759316 * "Recently used" menu not updated with gegl filters
* Bug 758915 * port Tile to gegl
* app: add a "split preview" feature to GEGL ops that can be dragged around
* app: add gegl:gegl to Filters -> Generic
* pagecurl: do a pretty basic port to the gegl API. Still 8 bit though.

## darktable as RAW processing plugin

* plug-ins: add new plug-in file-darktable
* plug-ins: Read comment, XMP, and Exif data from EXR files
* plug-ins: use the right magic for Canon CR2 files
* plug-ins: use the right magic for EXR files
* plug-ins: add a magic for Nikon NEF files to file-darktable
* plug-ins: Add a bunch of formats for file-darktable

## Screenshots

The code for capturing screenshots has undergone a major reorganization. It's now split into a backend and several front-ends specific for Windows, OS X, Wayland and X.org (Linux and UNIX systems).

While there are no immediate user-visible changes, this reorganizations greatly simplifies improving user experience for different operating systems.

## Painting

The new MyPaint Brush tool is now enabled by default. Daniel Sabo and Michael Natterer improved its performance and made MyPaint brushes available via an aready familiar dockable dialog interface, with previews and tagging.

Jehan Pagès collaborated with the MyPaint team: he ported libmypaint to autotools and turned default brushes into a separately shipped package.

Another major new feature is symmetric painting mode, also developed by Jehan Pagès with financial support from the GIMP community. (FIXME MORE CONTENT)

Additionally, it is now possible to assign a combination like **Shift + Mousewheel** for changing brush size.

## Selections

* app: Add "Flood" select action
* app: add gimpdrawable-fill.[ch]
* app: add "style" and "antialias" setters to GimpFillOptions
* app: add menu items and a dialog for GimpItem::fill()
* app: Add "Border style" combo to the "Select -> Border..." dialog (Ell)

## Better Tools

* app: Add "Diagonal neighbors" option to the fuzzy select tool
* app: Add "Diagonal neighbors" option to the bucket fill tool
* operations: Use input for the shapeburst distance map in Blend.
* app: Add shapeburst handles to the blend tool.
* app: use gegl:distance-transform in the blend tool, it has a progress now
* Bug 755005 * Align Tool > Distribute * vertical offset is missing
* app: IM preedit displayed as expected.

## Misc

* Bug 109161 * Improve Histogram with Luminance Channel

## What's Left To Do for GIMP 2.10

FIXME ADD CONTENT

## Downloads

FIXME ADD CONTENT