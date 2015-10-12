Title: GIMP 2.8 Release Notes
Date: 2015-08-17T14:15:58-05:00
Modified: 2015-08-17T14:16:03-05:00
Authors: Pat David
Status: hidden

## Introduction

GIMP 2.8 is the result of three years of hard work and collaborative development. This version of GIMP is equipped with a wealth of new features, including some highly requested ones. Keep reading to find out exactly what GIMP 2.8 has to offer you in areas such as the user interface, tools, and plug-ins.

## User Interface

### Single-Window Mode

<figure>
<img src="{filename}images/2.8-single-window-mode.png" alt="Single-window mode screenshot" />
</figure>

GIMP 2.8 introduces an optional single-window mode. You can toggle between the default multi-window mode and the new single-window mode through the _Single-window mode_ checkbox in the _Windows_ menu. In single-window mode, GIMP will put dockable dialogs and images in a single, tabbed image window. The single-window mode setting is of course preserved if you quit and start GIMP again. Single-window mode removes the necessity for users of having to deal with multiple windows.  
**Developers:** Martin Nordholts, Michael Natterer  
**Interaction Architect:** Peter Sikking

### Multi-Column Dock Windows

<figure>
<img src="{filename}images/2.8-multi-column-dock-windows.png" alt="Multi-column dock windows screenshot" />
</figure>

GIMP 2.8 allows dockable dialogs in a dock window to be placed in multiple columns. To create a new column in a dock window, drag and drop a dockable dialog on the vertical edges of the dock window. This is an appealing feature for multi-monitor users where one screen can have a big dock window with all the dialogs and the tools, while all images are on other displays.  
**Developer:** Martin Nordholts  
**Interaction Architect:** Peter Sikking

### More Screen Real Estate For Dockable Dialogs

<figure>
<img src="{filename}images/2.8-removed-docking-bars.png" alt="Removed docking bars screenshot" />
</figure>

The docking bars have been removed and replaced with overlaid highlights. The dockable drag handle has been removed and the dockable menu button has been moved up to the tabs. A new Automatic tab style has been added which makes dockable tabs use the available space.  
**Developer:** Martin Nordholts

### Save And Export

<figure>
<img src="{filename}images/2.8-save-and-export.png" alt="Save and export screenshot" />
</figure>

A rather big conceptual change is that saving and exporting images now are clearly separated activities. Saving an image can only be done in the XCF format which is GIMP's native file format, able to save all kinds of information necessary for works in progress.

To export into other formats _File->Export..._ needs to be used. This distinction makes it clearer if all available information is stored in a file, or not. There are some optimizations for alternative workflows such as opening a jpg, polishing it, and quickly exporting back to the original file. This conceptual change has also allowed us to get rid of the annoying dialogs that warned about the flatting of images when saving to non-layered formats.  
**Developer:** Martin Nordholts  
**Interaction Architect:** Peter Sikking

### Layer Groups

<figure>
<img src="{filename}images/2.8-layer-groups.png" alt="Layer groups screenshot" />
</figure>

For complex compositions, a flat layer structure is very limiting. GIMP 2.8 lets users organize their compositions better through the introduction of layer groups which allow layers to be organized in tree-like structures. Layer groups are fully scriptable through the GIMP plug-in API.  
**Developer:** Michael Natterer

### Tools Drawn With Cairo

<figure>
<img src="{filename}images/2.8-tools-drawn-with-cairo.png" alt="Tools drawn with cairo screenshot" />
</figure>

All tools rendering on canvas have been ported to Cairo to provide smooth antialiased graphics and make GIMP's look and feel match modern users expectations. All but a few plug-ins have been ported over to Cairo as well. Additionally all tools now use an on-canvas progress indicator instead of the one in the statusbar.  
**Developer:** Michael Natterer

### On-Canvas Text Editing

<figure>
<img src="{filename}images/2.8-on-canvas-text-editing.png" alt="On-canvas text editing screenshot" />
</figure>

Text editing with the Text Tool is now performed on-canvas instead of in a separate window. The editing on-canvas is rather sophisticated: apart from the usual text formatting features like font family, style and size selectors you get numeric control over baseline offset and kerning, as well as the ability to change text color for a selection. You can also use a combination of Alt and arrow keys to change baseline offset and kerning. This feature was originally developed during Google Summer of Code 2008 and heavily improved since.  
**Developers:** Daniel Eddeland, Michael Natterer

### Keyboard Shortcut Changes

Since the keyboard shortcuts Ctrl+E and Ctrl+Shift+E have been repurposed for the image export mechanisms, new keyboard shortcuts have been setup for 'Shrink Wrap' and 'Fit in Window', namely Ctrl+J and Ctrl+Shift+J respectively.  
**Developer:** Martin Nordholts

### Simple Math In Size Entries

<figure>
<img src="{filename}images/2.8-math-in-size-entries.png" alt="Math in size entries screenshot" />
</figure>

Enhancements have also been made to the size entry widget, which is used for inputting most of the x, y, width, height parameters. For example, in the scale dialog it is now possible to write '50%' in the Width field to scale the image to 50% of the width. Expressions such as '30in + 40px' and '4 * 5.4in' work, too.  
**Developer:** Fredrik Alströmer

### Minor Changes

*   Added 'Windows→Hide docks' menu item that does what 'Tab' does and also displays its state, which is now persistent across sessions, too.
*   Added infrastructure allowing to embed user interface elements on the canvas. This is currently used for text styles in the text tool, and (experimentally) when a color correction tool is invoked while the canvas is in full-screen mode.
*   To make dock window titles manageable, only show the active dockable in the dock window title.
*   The layer modes have been rearranged into more logical and useful groups based on the effect they have on compositing of a layer. Layer modes that make the composite lighter are in one group, layer modes that make the composite darker in another group, and so forth.
*   You can now Alt+Click on layers in the Layers dialog to create a selection from it. Add, subtract and intersect modifiers Ctrl, Shift and Ctrl+Shift keys work too. This makes it easy to compose contents of a layer based on the contents of other layers, without detours.
*   New docks are created at the pointer position.
*   Removed Toolbox from list of Recently Closed Docks, handle that directly in the Windows menu.
*   Allow closing the toolbox without closing the whole application.
*   Default to non-fixed-aspect in Canvas Size dialog.
*   In the Preferences dialog, only have one setting for the window hint for both the toolbox and the docks.
*   Support arbitrary affine transforms of brushes.
*   Got rid of the Tools dockable and move toolbox configuration to Preferences.
*   A question that often arises is how to change the UI language in GIMP, which has traditionally been a bit cumbersome. Not any longer, it is now possible to change the language in Preferences.
*   Added 'Lock content' button to the layers, channels and paths dialogs, made the lock buttons more compact.
*   Allow renaming list items with F2.
*   Allow binding arbitrary actions to extra mouse buttons.

**Developers:** Michael Natterer, Martin Nordholts, Alexander Jones, Alexia Death, Sven Neumann

## Tools & Plug-ins

### Brush System Improvements

<figure>
<img src="{filename}images/2.8-brush-system-improvements.png" alt="Brush system improvements screenshot" />
</figure>

The brush dynamics engine has been expanded considerably, making almost all aspects of the brush engine drivable by a multitude of inputs, all of them configurable with their own response curve.

Because of the expansion, dynamics were separated from tool options and converted into a resource in their own right. The Google Summer of Code 2009 Advanced GUI for Brush Dynamics project was the start of its development.  
**Developers:** Alexia Death, Michael Natterer, Zhenfeng Zhao

### Tool Preset Improvements

You can now save existing state of any tool as a preset and give it a meaningful name. The presets are accessible from a new Tool Presets dockable dialog and additionally can be tagged so that you can easily manage a lot of presets.

This new feature completely replaces the previously existing tool presets system to a new level of accessibility. It also makes it possible to distribute tool presets just like any other resource because each preset is saved as an individual file.  
**Developers:** Michael Natterer, Alexia Death

### Cage Transform Tool

<figure>
<img src="{filename}images/2.8-cage-transform-tool.png" alt="Cage transform tool screenshot" />
</figure>

A completely new _Cage transform_ tool has been added thanks to the excellent work of one of our Google Summer of Code 2010 students. The tool implements an innovative approach to free transformation and makes it possible to easily warp parts of objects using an adjustable user-defined polygonal frame.  
**Developer:** Michael Muré

### File Plug-Ins

A plug-in for loading JPEG2000 images has been added, as well as plug-ins for X11 Mouse Cursor files and fundamental OpenRaster (.ora) import and export support. Added RGB565 support to the csource plug-in.  
**Developers:** Aurimas Juška, Takeshi Matsuyama

A Cairo based PDF exporter was implemented. While being somewhat simplistic the exporter saves text, embedding fonts into the final PDF file, and attempts to convert all flat filled areas to vector objects.  
**Developer:** Barak Itkin

Last, but not least, a Web-page plug-in was added to render any web page into an image using Webkit.  
**Developer:** Mukund Sivaraman

### For Tablet Users

<figure>
<img src="{filename}images/2.8-for-stylus-users.png" alt="For stylus users screenshot" />
</figure>

A new experimental widget was added to meet the requirements of graphic tablets users. The widget combines a slider, a label and a numeric value control which simplifies adjusting a value using a stylus, better visualizes the current value and provides a more compact UI. It is now used in the Tools Options dockable dialog for opacity control and most options of brush based tools.

Another useful feature for users of advanced input devices such as graphic tablets is a completely new dialog for input device configuration which allows configuring per-device pressure curves to compensate for hardware differences and personal per-pen preferences.

People with Intuos tablets and either Artpen or Airbrush styluses will be glad to find that Airbrush wheel and Artpen rotation are available for driving dynamics via the 'Wheel' input.  
**Developers:** Michael Natterer, Alexia Death

### Resource Tagging

<figure>
<img src="{filename}images/2.8-resource-tagging-brushes.png" alt="Resource tagging screenshot with brushes" />
</figure>

It is now possible to tag GIMP resources such as brushes and patterns to group them. The tagging is performed from the respective dockables e.g. the _Brushes_ dockable, and it is possible to filter resources based on these tags.

The tags are saved to an XML file, external to the data files themselves. It is possible to tag multiple resources simultaneously in the UI, but currently only while being viewed as a list. This feature was developed during Google Summer of Code 2008\.  
**Developer:** Aurimas Juška  
**Interaction Architect:** Peter Sikking

### Resources

We have started overhauling the default set of resources and in this version there have been some changes to the default set of brushes. The silly 'Untitled' title has been removed from unnamed palette entries. A wholly new set of brushes for painting has been added and makes use of the new tagging system.  
**Developer:** Martin Nordholts  
**Artists:** Johannes Engelhardt, Ramón Miranda, Guillermo Espertino

### Minor Changes

*   Allow specifying the written language in the Text Tool. This helps with choosing an appropriate font, or appropriate glyphs for the selected language.
*   Moved 'Text along path' from tool options to the text context menu.
*   Add diagonal guides to the Crop Tool.
*   Support rotating brushes.
*   The Smooth Stroke feature from GIMP Painter was ported to GIMP.
*   Added 'Rule of fifths' crop guide overlay.
*   Added an icon for the Desaturate tool.
*   Support loading 16bit (RGB565) raw data.
*   Added palette exporter for CSS, PHP, Python, txt and Java, accessed through the palette context menu.
*   Support printing crop marks for images.
*   Made the Pointer dockable show information about selection position and size.
*   Replaced the brush scale control in tool options by a brush size one that works in pixels, and does the right thing when the brush changes.
*   Improved the Free Select Tool on-canvas feedback.
*   Made it possible to use GEGL for scaling images.

**Developers:** Sven Neumann, Michael Natterer, Tim Jedlicka, Alexia Death, Nelson A. de Oliveira, Jakub Steiner, Nicholas Doyle, Barak Itkin, Martin Nordholts

## Miscellaneous

### Plug-in Development

GIMP 2.8 also further enhances its scripting abilities. For example, API changes to support layer groups have been made. Here is a [list of new symbols in GIMP 2.8](http://developer.gimp.org/api/2.0/libgimp/libgimp-index-new-in-2-8.html).

### API Changes

A lot of GIMP APIs have been refactored to simplify developing new scripts.

### License

The GIMP license has been changed to (L)GPLv3+.

### GEGL

The projection code which composes a single image from layers has been ported to GEGL. This includes the layer modes, as well as support for layer groups. Also, preparations have been made for better and more intuitive handling of the floating selection.  
**Developers:** Michael Natterer, Martin Nordholts

### Roadmap

The GIMP developers now maintain a roadmap for GIMP development found here: [http://wiki.gimp.org/index.php/Roadmap](http://wiki.gimp.org/index.php/Roadmap)

## GIMP 2.8 Screenshots

<figure>
<img src="{filename}../screenshots/1280x800-fresh-start.jpg" alt="First GIMP 2.8 startup" />
<figcaption>
First startup of GIMP 2.8 on a 1280x800 desktop.
</figcaption>
</figure>


</div>

## Known Regressions

GIMP 2.8 relies on a newer version of GTK+2 that unfortunately has partially broken support for graphics tablets such as Wacom. If your graphic tablet doesn't work in GIMP 2.8 as it should, we recommend downgrading to 2.6 until we release GIMP 3.0 that relies on GTK+3 which has fully functional support for advanced input devices.

To address the needs to migrate from the old tools presets system to the new one we provide a [script](http://wiki.gimp.org/index.php/Mindstorm:Preset_converter) in Python. However, the old tools presets are not 100% convertible to the new tool presets. For instance, brush scale from 2.6 can't be converted to brush size in 2.8.

## Download and install pre-made packages

GIMP can be downloaded directly from our [Downloads](/downloads/) section.

Please be very cautious when downloading from anywhere else - some sites use GIMP's popularity to lure unwary users into their traps by shipping modified installer packages.

## Building GIMP yourself from source

GIMP 2.8 must **not** be installed in the same prefix as other GIMP 2.x versions. If you want to keep your GIMP 2.6 installation in parallel to GIMP 2.8, you have to choose a separate installation prefix at compile-time and ensure that you use different library search paths for each version. If you do not set up your environment differently for each version, you will experience conflicts with the libraries and at least one version is likely to fail.

Also, do **not** install GIMP 2.8 to /usr/local because on most systems, its libraries would override the libraries of a stable GIMP 2.6 installed into /usr, breaking your distribution-installed GIMP from slightly to completely. The same applies to any prefix your system uses for the purpose or overriding things in /usr/lib.

You install the new version into a separate prefix, say /opt/gimp-2.8 by passing `--prefix=/opt/gimp-2.8` to the configure script. Then, in order to run the binary installed there, you change your environment to look for executables in /opt/gimp-2.8/bin by setting `PATH=/opt/gimp-2.8/bin` and you tell your linker to pick up libraries from /opt/gimp-2.8/lib by setting `LD_LIBRARY_PATH=/opt/gimp-2.8/lib`. Do not forget to `export` both variables.

You can use a tiny wrapper script called gimp-2.8 and place it into /usr/local/bin or elsewhere in your PATH. The script would look something like this:

    #!/bin/sh

    PATH=/opt/gimp-2.8/bin:$PATH
    export PATH
    LD_LIBRARY_PATH=/opt/gimp-2.8/lib
    export LD_LIBRARY_PATH

    /opt/gimp-2.8/bin/gimp-2.8 "$@"

## Bugs

If you think you found a bug in a development version, please make sure that it hasn't been already reported. Search [Bugzilla](http://bugzilla.gnome.org/) before filing a new bug-report. Here are some interesting Bugzilla queries:

*   [Open bugs with milestone 2.8](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&target_milestone=2.8&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED)
*   [Resolved bugs with milestone 2.8](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&target_milestone=2.8&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED)

## Contributing

We need your help to make GIMP 2.8 a success. If you want to join us hacking, show up in #gimp or introduce yourself on the gimp-developer mailing-list. We are also looking for people to look after the web-site and update the tutorials. Or you might want to join the [documentation team](http://docs.gimp.org/).
