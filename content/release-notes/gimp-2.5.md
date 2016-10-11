Title: GIMP 2.5 Release Notes
Date: 2015-08-17T14:15:58-05:00
Modified: 2015-08-17T14:16:03-05:00
Authors: Pat David
Status: hidden



This is an unstable development version of the **GNU Image Manipulation Program**. Please realize that this is just a snapshot of the development tree. We are working hard towards GIMP 2.6, the next stable release. GIMP 2.5 is in no way a final product. A lot of new features are incomplete and some things may even be completely broken. If you need to get work done, please use the stable version, GIMP 2.4.

## What's New in GIMP 2.5

### UI changes

GIMP has several UI changes in this version, many of them offering relief to long standing issues.

A major change is the appearance of an "empty image window". This window is a placeholder where your image will eventually open, also a drop zone into which you can drag-and-drop your file and start working. You will also notice that the Toolbox menu is gone: it has been merged into the image window menu. Toolbox and docks are treated as utility windows, so if your window manager supports it, then your problems with docks and toolbox getting lost under other windows are over. Unfortunately, at this moment utility window hints only work correctly in metacity, the Gnome default window manager.

There are also a couple of nice usability changes concerning docks. Have you ever been aggravated to no end because you accidentally closed your neatly set up dock and had to build it from scratch again? That is no longer a source of stress, because the Window menu now holds a list of recently closed docks, and just one click can bring your carefully constructed setup back to you. Another common annoyance is incidentally dragging tabs out of docks. Now GIMP lets you lock your tabs to make sure that does not happen.

One of the most desired changes over the years has been "overpanning": the ability to pull those pesky corners, that are so hard to reach with just the right point of the brush, to the front and center. This is now finally available. Panning does not have to stop when the image edge reaches the window edge. You can go on panning, and position the area you work on where it is comfortable for you.

### Improved Freehand select tool

The freehand select tool has been enhanced to support polygon segments in selections. Selection segments are all independently adjustable. This significant improvement fills the need for making polygonal selections without creating yet another tool.

### Improved help system

Ever been bothered by the fact that you need a single page of help but can't get it because you don't have the whole large help docs package installed? Despair no more. GIMP now supports online help. All you need is a network connection and that particular page opens in your browser when you ask for help anywhere in GIMP.

### Brush dynamics

Brush dynamics let you map different brush parameters, commonly at least size and opacity, to one or more of three input dynamics: pressure, velocity and random. Velocity and random are usable with a mouse. The Ink tool, that supported velocity before, has been overhauled and now handles velocity-dependent painting much better.

Brush dynamics have enabled a new feature in stroking paths. There is now a check box under the "paint tool" option, for emulating brush dynamics if you stroke using a paint tool. What this means is that when your stroke is being painted by GIMP, it tells the brush that its pressure and velocity are varying along the length of the stroke. Pressure starts with zero, ramps up to full pressure and then ramps down again to no pressure. Velocity starts from zero and ramps up to full speed by the end of the stroke.

### Preset saving for color tools

Now you can save presets in all color tools for color adjustments you use frequently.

### Under the hood

Most notable of under-the-hood changes are the first steps of [GEGL](http://gegl.org) integration. Right now the effect on user experience is minimal, but it is an important development for the future. Once GEGL integration is complete, GIMP will finally get support for higher color depths, more color spaces and eventually non-destructive editing.

Peeking out from under the hood are subtle differences in the way the UI draws its elements. These changes are due to internally making use of the Cairo library to draw UI elements. This is visible for example in the drawing of Layers and Paths docks and Curves dialog.

Please see the [NEWS](https://git.gnome.org/browse/gimp/plain/NEWS?id=GIMP_2_5_0) file for a more detailed list of changes. [Screenshots](http://developer.gimp.org/screenshots.html) of the development version can also be found there.

## Download

The development snapshots of GIMP can be downloaded as source code from ftp.gimp.org or from one of the mirrors listed in the [Downloads](/downloads/#mirrors) section.

Distribution of binary packages of the development version is discouraged unless it is made clear that this is an early development snapshot. Users should be referred to these release notes or similar information.

## Installation

GIMP 2.5 must **not** be installed in the same prefix as other GIMP 2.x versions. If you want to keep your GIMP 2.4 installation in parallel to GIMP 2.5, you have to choose a separate installation prefix at compile-time and ensure that you use different library search paths for each version. If you do not set up your environment differently for each version, you will experience conflicts with the libraries and at least one version is likely to fail.

You install the new version into a separate prefix, say /opt/gimp-2.5 by passing `--prefix=/opt/gimp-2.5` to the configure script. Then, in order to run the binary installed there, you change your environment to look for executables in /opt/gimp-2.5/bin by setting `PATH=/opt/gimp-2.5/bin` and you tell your linker to pick up libraries from /opt/gimp-2.5/lib by setting `LD_LIBRARY_PATH=/opt/gimp-2.5/lib`. Do not forget to `export` both variables.

You can use a tiny wrapper script called gimp-2.5 and place it into /usr/local/bin or elsewhere in your PATH. The script would look something like this:

    #!/bin/sh

    PATH=/opt/gimp-2.5/bin:$PATH
    export PATH
    LD_LIBRARY_PATH=/opt/gimp-2.5/lib
    export LD_LIBRARY_PATH

    /opt/gimp-2.5/bin/gimp-2.5 "$@"

## Bugs

If you think you found a bug in a development version, please make sure that it hasn't been already reported. Search [Bugzilla](http://bugzilla.gnome.org/) before filing a new bug-report. Here are some interesting Bugzilla queries:

*   [Open bugs with milestone 2.6](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&target_milestone=2.6&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED)
*   [Resolved bugs with milestone 2.6](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&target_milestone=2.6&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED)

## Contributing

We need your help to make GIMP 2.6 a success. There's still a lot to do. If you want to join us hacking, show up in #gimp or introduce yourself on the gimp-developer mailing-list. We are also looking for people to look after the web-site and update the tutorials. Or you might want to join the [documentation team](http://docs.gimp.org/).
