Title: GIMP 2.9.4 Released
Date: 2016-12-31
Category: News
Authors: Alexandre Prokoudine
Slug: gimp-2-9-4-released
Status: draft
Summary: We have just released the second development version of GIMP in the 2.9.x series. GIMP 2.9.4 features revamped look and feel, major improvements in color management, as well as production-ready MyPaint Brush tool, symmetric painting, and split preview for GEGL-based filters.

We have just released the second development version of GIMP in the 2.9.x series. After half a year in the works, GIMP 2.9.4 delivers a massive update: revamped look and feel, major improvements in color management, as well as production-ready MyPaint Brush tool, symmetric painting, and split preview for GEGL-based filters. Additionally, XX bugs have been fixed, and numerous small improvements have been applied.

GIMP 2.9.4 is quite reliable for production work, but there are still loose ends to tie, which is why releasing stable v2.10 will take a while. Please refer to the [Roadmap](http://wiki.gimp.org/wiki/Roadmap#GIMP_2.10) for the list of major pending changes.

## Revamped User Interface and Usability Changes

The new version features several new themes by Benoit Touchette in various shades of grey: Lighter, Light, Gray, Dark, Darker. System theme has been preserved for users who prefer completely consistent look of user interfaces across all desktop applications.

Note that we still consider this feature a work in progress, as dark themes still need some fine-tuning (especially regarding the color of inactive menu items).

The new UI themes are accompanied by symbolic icons originally created by Barbara Muraus, Jakub Steiner, and heavily updated and completed by Klaus Staedtler. The existing icon theme from past releases of GIMP has also been preserved, and users can freely switch between available icon themes and easily add their own ones.

Note that themes and icon themes are now separate: you can easily mix your favorite UI with various icon sets. Also since most 2.8 themes would end up broken in 2.9.x, themes are not migrated anymore. Users who want custom themes will have to install ones specifically made for GIMP 2.9.x/2.10.

All work on icons by Klaus Staedtler is made on vector (SVG) images, which should allow better support for HiDPI displays (also commonly known as Retina) soon. Vector icons are an experimental feature, available after using '--enable-vector-icons' build configure option. Note that this option does not allow HiDPI support at this time.

We cleaned the Preferences dialog a little and reordered options in a  more logical manner. The Color Management page was redesigned following both internal and user-visible changes in relevant parts of GIMP (see below), and _Snap Distance_ options have been moved to a dedicated _Snapping_ page.

Additionally, it is now possible to configure the size of undo step previews in the Undo dialog via the Preferences dialog, which was only possible by manually editing GIMP's configuration file before, by a complete oversight on our part.

The startup splash screen now features a pulsing progress bar to indicate that GIMP is not frozen. This, as well as initializing fontconfig in the background (also a new feature in 2.9.4), is meant to address a common issue where rebuilding fonts cache (or building it for the first time) can take a lot of time hence making an impression that GIMP freezes at startup. We acknowledge that this is a workaround. Fixing the actual reason involves hacking on fontconfig. If you are interested, there is a [bug report](https://bugs.freedesktop.org/show_bug.cgi?id=64766) on that.

## Color Management Improvements

Color Management implementation got a complete overhaul in this version of GIMP. Instead of being a pluggable module, it's a core feature now. Moreover, we added an abstraction layer that makes GIMP less dependent on LittleCMS. This means that in the future GIMP could use native APIs on Windows and OS X, and/or use [OCIO](http://opencolorio.org/).

Since GIMP currently relies on sRGB (this is bound to change in future versions of GIMP), we decided to expose that in the user interface.

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

GIMP now keeps track of GEGL-based filters that you used within one session and allows re-running them via `Filters > Recently` used submenu, just like old GIMP plug-ins.

_Posterize_ and _Desaturate_ color tools have been converted to regular GEGL-based filters, and both _Tile_ and _Pagecurl_ filters have been converted to use GEGL buffers. A quite popular "photographic" _Highpass_ filter commonly used for enhancing details was added to the `Filters > Enhance` submenu.

A way more noticeable new feature, however, is split preview for GEGL-based filters. You can compare before/after versions right on canvas and move a "curtain" around to see more of "before" or "after" and swap their position. You can also switch between vertical and horizontal division.

## darktable as RAW processing plugin

On Linux, GIMP is now capable of using darktable for pre-processing raw images from DSLRs (Canon CR2, Nikon NEF etc.). darktable is an amazing project whose developers stick around at our IRC channel and even contribute to GIMP (most recently, they added reading various metadata from EXR files).

Note that the file-darktable plug-in is activated only when darktable is built with Lua support. Make sure your build of darktable for Linux is feature-complete.

It is still possible to use other raw development plug-ins like UFRaw. For cases when multiple plug-ins are installed in your system, we intend to add a preference option.

## Screenshots

The code for capturing screenshots has undergone a major reorganization. It's now split into a back-end and several front-ends specific for Windows, OS X, Wayland and X.org (Linux and UNIX systems).

While there are no immediate user-visible changes, this reorganizations greatly simplifies improving user experience for different operating systems.

## Painting

The new MyPaint Brush tool is now enabled by default. Daniel Sabo and Michael Natterer improved its performance and made MyPaint brushes available via an aready familiar dockable dialog interface, with previews and tagging.

Jehan Pagès collaborated with the MyPaint team: he ported libmypaint to autotools, allowing in particular standard builds on all platforms, and work is being done to turn default brushes into a separately shipped package.

Another major new feature is symmetric painting mode, also developed by Jehan Pagès with financial support from the GIMP community. It can be activated through the new "Symmetry Painting" dock, and allows to use all paint tools with various symmetries (mirrors, central and rotational symmetry, tiling…).

Additionally, it is now possible to assign a combination like **Shift + Mousewheel** for changing brush size.

## Selections

For cases when your selection has a lot of small unselected regions, you can now use `Select > Remove Holes` command.

(FIXME SCREENSHOT)

The `Select > Border...` dialog now provides several border style options: hard, smooth, and feathered. _Feathered_ creates a selection that goes gradually from 1 to 0 the farther you get from the middle of the border. _Smooth_ preserves partial selection (antialiasing) along the edges of the selection.

## Better Tools

_Fuzzy Select_ and _Bucket Fill_ tools got a new feature for selecting/filling diagonally neighboring pixels.

(FIXME SCREENSHOT)

The _Blend_ tool got shapeburst fills resurrected, and allows to place their handles on the canvas. Additionally the Blend tool displays progress indication now thanks to a new GEGL feature available in several GEGL operations including `gegl:distance-transform`.

The _Text_ tool now fully supports advanced input methods for CJK and other non-western languages. Minimal support already existed but the preedit text was displayed in a floating popup instead of inline within the text tool box, and without any preview styling. It is now displayed just as expected depending on your platform and Input Method Engine. Several input method-related bugs and crashes have also been fixed in the same time.

(FIXME SCREENSHOT)

## Batch processing on command line

A new macro `with-files` is now available in order to easily process multiple files through GIMP, on command line, which was a much awaited feature.

## Email plugin back from the dead

The `File > Send by email…` dialog will open your default email client with an attached copy of your current image, to share your work-in-progress in a single click. This is available only on operating systems with `xdg-email` (likely GNU/Linux, BSD only).

The original implementation using `sendmail` is also available, yet since it requires a properly configured sendmail, which is not common on desktop machines, the explicit `--with-sendmail` option has to be set at build time to replace the `xdg-email` implementation.

## Debugging Facilities for Windows

Windows builds can now generate backtrace logs upon a crash with Dr.MinGW's ExcHndl library, which must be available at build time. The logs will be available in `%APPDATA%\GIMP\2.9\CrashLog\`.

## Misc

* Bug 109161 * Improve Histogram with Luminance Channel

## What's Left To Do for GIMP 2.10

(FIXME ADD CONTENT)

## Downloads

FIXME ADD CONTENT
