Title: GIMP 2.6 Release Notes
Date: 2015-08-17T14:15:58-05:00
Modified: 2015-08-17T14:16:03-05:00
Authors: Pat David
Status: hidden



## Introduction

GIMP 2.6 is an important release from a development point of view. It features changes to the user interface addressing some often received complaints, and a tentative integration of GEGL, the graph based image processing library that will eventually bring high bit-depth and non-destructive editing to GIMP.

## User Interface

### Toolbox Menubar Removed

<figure>
<img src="{filename}images/2.6-empty-image-window.png" alt="Empty Image Window screenshot"/>
</figure>

The toolbox menubar has been removed and merged with the image window menubar. To be able to do this a window called the _empty image window_ has been introduced. It hosts the menubar and keeps the application instance alive when no images are opened. It also acts as a drag and drop target. When opening the first image the empty image window is transformed into a normal image window, and when closing the last image, that window becomes the empty image window.

### Toolbox and Docks are Utility windows

With the empty image window acting as a natural main window, the default window hints for the Toolbox and Docks have been changed to _Utility window_. This enables window managers to do a much better job of managing the GIMP windows, including omitting the Toolbox and Docks from the taskbar and ensuring that the Toolbox and Docks always are above image windows.

### Ability to Pan Beyond Image Border

<figure>
<img src="{filename}images/2.6-scroll-beyond-border.png" alt="Scroll Beyond Border illustration"/>
</figure>

It is now possible to pan beyond the image border, making image window navigation much less constrained. It is no longer a problem to use the edge of a brush on the edge of an image while being zoomed in, and one can adapt the canvas to any utility windows covering parts of the image window.

### Minor Changes

*   Renamed Dialogs menu to Windows.
*   Keep a list of recently closed Docks and allow reopening them.
*   Make opening images in already running GIMP instances work better on Windows.
*   You can now enter the image zoom ratio directly in the status bar.
*   Added support for using online help instead of a locally installed GIMP Help package.
*   Make it possible to lock tabs in docks to prevent accidental moving.

## Tools, Filters & Plug-ins

### Improved Free Select Tool

<figure>
<img src="{filename}images/2.6-new-free-select-tool.png" alt="New Free Select Tool in action"/>
</figure>

The freehand select tool has been enhanced to support polygonal selections. It also allows mixing free hand segments with polygonal segments, editing of existing segments, applying angle-constraints to segments, and of course the normal selection tool operations like add and subtract. Altoghether this ends up making the Free Select Tool a very versatile, powerful and easy-to-use selection tool.

### Brush Dynamics

<figure>
<img src="{filename}images/2.6-brush-dynamics.jpg" alt="Brush Dynamics illustration"/>
</figure>

Brush dynamics let you map different brush parameters, commonly at least size and opacity, to one or more of three input dynamics: pressure, velocity and random. Velocity and random are usable with a mouse. The Ink tool, that supported velocity before, has been overhauled and now handles velocity-dependent painting much better.

Brush dynamics have enabled a new feature in stroking paths. There is now a check box under the "paint tool" option, for emulating brush dynamics if you stroke using a paint tool. What this means is that when your stroke is being painted by GIMP, it tells the brush that its pressure and velocity are varying along the length of the stroke. Pressure starts with zero, ramps up to full pressure and then ramps down again to no pressure. Velocity starts from zero and ramps up to full speed by the end of the stroke.

### Minor Changes

<figure>
<img src="{filename}images/2.6-text-tool-and-rectangle-handles.png" alt="Text Tool bounding box and outside rectangle handles screenshot"/>
</figure>

*   Added a bounding box for the Text Tool that supports automatic wrapping of text within that bounding box.
*   Move handles for rectangle based tools like Crop and Rectangle Select to the outside of the rectangle when the rectangle is narrow.
*   Added motion constraints to the Move Tool.
*   Improved event smoothing for paint tools.
*   Mark the center of rectangles while they are moved, and snap the center to grid and rulers.
*   Enable brush scaling for the Smudge tool.
*   Added ability to save presets in all color tools for color adjustments you use frequently.
*   Allow to transfer settings from _Brightness-Contrast_ to _Levels_, and from _Levels_ to _Curves_.
*   Allow changing opacity on transform tool previews.
*   The Screenshot plug-in has been given the ability to capture the mouse cursor (using Xfixes).
*   Display aspect ratio of the Crop and Rectangle Select Tool rectangles in the status bar.
*   Desaturate has been given an on-canvas preview.
*   The Flame plug-in has been extended with 22 new variations.
*   Data file folders like brush folders are searched recursively for files.
*   Replaced the PSD import plug-in with a rewritten version that does what the old version did plus some other things, for example reading of ICC color profiles.

## Under the Hood

### GEGL

Important progress towards high bit-depth and non-destructive editing in GIMP has been made. Most color operations in GIMP are now ported to the powerful graph based image processing framework [GEGL](http://www.gegl.org/), meaning that the internal processing is being done in 32bit floating point linear light RGBA. By default the legacy 8bit code paths are still used, but a curious user can turn on the use of GEGL for the color operations with _Colors / Use GEGL_.

<figure>
<img src="{filename}images/2.6-experimental-gegl-tool.png" alt="Experimental GEGL tool screenshot"/>
</figure>

In addition to porting color operations to GEGL, an experimental _GEGL Operation_ tool has been added, found in the _Tools_ menu. It enables applying GEGL operations to an image and it gives on-canvas previews of the results. The screenshot to the right shows this for a Gaussian Blur.

### Minor Changes

*   Ported many widgets to use the 2D graphics library [cairo](http://www.cairographics.org/) for drawing. See this [comparison](images/gimp-curves-tool-2-4-vs-2-6.png) for an example of how much better this looks.

## Miscellaneous

### Plug-in Development

There are new things for a plug-in developer to enjoy as well. For example, procedures can now give a detailed error description in case of an error, and the error can be propagated to the user.

GIMP 2.6 also further enhances its scripting abilities. In particular there is now a much richer API for the creation and manipulation of text layers. Here is a [list of new symbols in GIMP 2.6](//developer.gimp.org/api/2.0/libgimp/libgimp-index-new-in-2-6.html).

### Backwards Compatibility

Script-Fu has undergone some clean up and includes several bug fixes. One important bug fix, for [bug #508020](https://bugzilla.gnome.org/show_bug.cgi?id=512105), prevents a possible crash of Script-Fu. A side effect of the fix will break any script which does not provide an initial value for a variable in the binding portion of a _let_, _let*_, or _letrec_ block.

An initial value for a variable is required as stated in the [R5RS Scheme standard document](http://www.schemers.org/Documents/Standards/R5RS/r5rs.pdf). The initial value can be provided as a simple constant, or as the result of a function call. The following examples will illustrate the problem and show a simple change that will fix a broken script.

This example shows a _let*_ block with incorrect syntax that will no longer work in Script-Fu.

    (let* (
          (four (+ 2 2))
          (this-is-wrong)
          )

This example shows a _let*_ block with the correct syntax.

    (let* (
          (four (+ 2 2))
          (this-is-correct 0)
          )

### Known Problems

*   The _Utility window_ hint is currently only known to work well in the Linux GNOME desktop environment and on Windows starting with GIMP 2.6.1.
*   Using the Text Tool is currently not an optimal experience. Making it work better is a goal for GIMP 2.8.
*   If you build GIMP yourself and don't have [GVfs](http://en.wikipedia.org/wiki/GVFS) support on your platform you need to explicitly pass <kbd>--without-gvfs</kbd> to configure, otherwise opening remote files will not work properly.

### What's Planned

For the interested, here is roughly what is planned for GIMP 2.8, the next stable release:

*   Merging Google Summer of Code 2008 projects to trunk, namely on-canvas text editing, tagging of GIMP resources and Python scripting enhancements.
*   Continue integration of GEGL.
*   And of course many other improvements...

## GIMP 2.6 Screenshots

<figure>
<a href="../screenshots/gnome-1280x800-fresh-start.jpg"><img src="{filename}../screenshots/gnome-1280x800-fresh-start.jpg" alt="First GIMP 2.6 startup"/></a>
<figcaption>
First startup of GIMP 2.6 on a 1280x800 GNOME desktop.
</figcaption>
</figure>


<figure>
<a href="../screenshots/alternative-2-6-ui-layout-example-one.jpg"><img src="{filename}../screenshots/alternative-2-6-ui-layout-example-one.jpg" alt="Alternative UI example"/></a>
<figcaption>
UI layout example: Tool Options moved out of the toolbox.
</figcaption>
</figure>


<figure>
<a href="../screenshots/alternative-2-6-ui-layout-example-two.jpg"><img src="{filename}../screenshots/alternative-2-6-ui-layout-example-two.jpg" alt="Another alternative UI example"/></a>
<figcaption>
UI layout example: Using the image window as a background window.
</figcaption>
</figure>


<figure>
<a href="../screenshots/2.6-brush-dynamics-example.jpg"><img src="{filename}../screenshots/2.6-brush-dynamics-example.jpg" alt="Brush Dynamics at use"/></a>
<figcaption>
Demonstrating the kind of effects the new Brush Dynamics can create.
</figcaption>
</figure>


<figure>
<a href="../screenshots/on-canvas-preview-of-gaussian-blur-in-2-6.jpg"><img src="{filename}../screenshots/on-canvas-preview-of-gaussian-blur-in-2-6.jpg" alt="On-canvas Gaussian Blur"/></a>
<figcaption>
Full screenshot of on-canvas preview of Gaussian Blur using the experimental GEGL Operation tool.
</figcaption>
</figure>



## We Hope You Enjoy GIMP 2.6!

<figure markdown="span">
<img src="{filename}images/2.6-lgm-2008-groupshot.jpg" alt="LGM 2008 shot of the GIMP team"/>
<figcaption>
A picture of (mostly) GIMP developers, taken by [Garrett LeSage](http://www.flickr.com/photos/garrett/2733807768/) at [Libre Graphics Meeting 2008](http://www.libregraphicsmeeting.org/2008/), licenced under [CC-By](http://creativecommons.org/licenses/by/2.0/deed.en)
</figcaption>
</figure>
