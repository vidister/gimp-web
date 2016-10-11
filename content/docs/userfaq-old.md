Title: Frequency Asked Questions (Old)
Date: 2015-08-14T15:07:00-05:00
Author: Pat David



_This FAQ is still a work in progress. Some sections are very outdated, other sections should probably be removed, and some new questions and answers should be added. Please [contact us](/webmasters.html) if you can improve it._

[TOC]

## General Information

### What is this GIMP?

The “GNU Image Manipulation Program” (originally the General Image Manipulation Program) sired by Spencer Kimball & Peter Mattis.

In their own words, “GIMP is our answer to the current lack of free (or at least reasonably priced) image manipulation software for GNU/Linux and UNIX in general.”

It is a raster editor, which means that it performs operations directly on the pixels that make up the image, and not a vector editor. Other (proprietary) raster editors include Adobe Photoshop, Jasc Paintshop Pro and the humble Microsoft Paint. An alternative free editor is [Krita](http://www.krita.org/). Users wanting to edit photographs will certainly want a raster editor like GIMP. Graphic designers and illustrators may prefer a vector editor depending on their tastes.

### Where do I get it?

Most (if not all) GNU/Linux distributions will support GIMP through their package management systems and may even come with GIMP preinstalled. You can find the latest version for GNU/Linux, Microsoft Windows and Apple Mac OS X on [the download page](/downloads/). Of course, this is [free software](http://www.gnu.org/philosophy/free-sw.html) so the [source code](/source/) is available to, along with instruction on how to compile it.

### Why and when was GIMP changed from “general image manipulation program” to “GNU image manipulation program”?

One day (I believe it was in 1997) RMS visited Berkeley, and Spencer and Peter met with him. They asked if they could change General to GNU, and it was done.

### GIMP is a stupid name. Why can't you change it?

GIMP is comfortable with its name and thinks that you should apologise for your rudeness.

### Is GIMP a GNOME application?

Not really. It doesn't use the GNOME application framework. The only thing it has in common is GTK+. GIMP can optionally use gnome-vfs, allowing you to load and edit images from remote servers.

### Is GTK+ still under the aegis of GIMP? Was it ever?

GTK was developed solely for GIMP, initially. Towards the end of the 0.99 development cycle in 1998, GTK was split from being bundled with GIMP to being a separately available library. See [ancient history](/about/ancient_history.html) for some interesting tidbits from the GIMP perspective.

### Which version should I use?

You should use the latest stable release. See our [downloads page](/downloads/).

### Is there a user manual?

Yes. It is available in [HTML](http://docs.gimp.org/) form, and in [PDF](http://docs.gimp.org/download.html).

### What about a Windows version?

See [the download page](/downloads/).

### What about a Mac version?

See [the download page](/downloads/).

### Are there any Easter eggs in GIMP?

Yes.

### Is there a mailing list?

See our list of [Mailing Lists](/mail_lists.html).

### Is there an IRC channel?

See our list of [IRC channels](/irc.html).

### Why does GIMP complain about missing or wrong versions of libraries?

Probably because it can't find them.

_FIXME: some of the advice given here is incorrect and even dangerous._

There are a couple of solutions. The best one, if you have superuser access on your system, or a cooperative system administrator, is to add GIMP's library directory to the system library configuration. To do this, edit /etc/ld.so.conf to include /usr/local/lib and then type _ldconfig_ and things should work from then on.

If you can't do this, add the directory to your LD_LIBRARY_PATH environment variable. Be sure you do this in your shell's startup scripts as well.

If you have old versions of the libraries, you will probably need to remove them first, especially if they are in standard system locations such as /usr/lib . Don't just delete them, though; move them somewhere safe, install the new ones, and try again. Then make sure everything else still works; you may have other programs on your system which require the old versions. The ideal response in such a case is to rebuild all the programs to use the new libraries. Where this isn't possible, you will just have to experiment with trying them in different locations, or statically linking them to one or more programs.

### Is XInput support available?

Yes.

### Does GIMP support art tablets like the Wacom?

_FIXME: obsolete advice._

In the more recent releases of most distros, installing the wacom-tools package should make tablet support “just work”. Make sure that you enable the input devices in GIMP, too.

Otherwise, you have to do a little extra work to compile it in.

See [Intuos on Linux](http://www.levien.com/free/linux_intuos.html) by Terry Mackintosh, or this quick overview from Juergen Schlag:

1.  run GNU/Linux with a X11 server which supports the Xinput-Section (my old S3-Board running under the XFree-Server works well, but the XSuSE- Server for PERMEDIA2-Boards doesn't work :-(
2.  install the Xinput driver for the Artpad (see the docs). I used a patched driver for the PenPartner
3.  edit the Xinput-Section of your /etc/XF86Config to load the driver when X11 starts (see the man-pages for XF86Config and your X-server)
4.  recompile the GTK toolkit with the Xinput-support enabled. see the README and INSTALL file for the command switch to do this.
5.  restart your computer, start X11 and GIMP. if no error message occured your artpad should work well

### Does GIMP have scanner support?

Yes. It's available on Windows and uses TWAIN, and on GNU/Linux you even have a choice between XSane and gnome-scan — both can be used as GIMP plug-ins.

Further information is available at the [SANE project](http://www.sane-project.org/).

### Can GIMP install its own colormap?

Yes. In either the system-wide gimprc file or your personal gimprc file, uncomment the line that includes _install-colormap_.

### GIMP complains about MIT-SHM!

If GIMP gives you a message similar to either of these when you try to start it: _Xlib: extension “MIT-SHM” missing on display “198.51.29.58:0.0”._ or _* WARNING **: XShmAttach failed!_ then you need to run it with the --no-xshm option.

This happens for one of two reasons. Either your X display server does not have the shared memory option, or you are running GIMP on a different system than the one on which it is displaying. In the former case, you may wish to look into different X servers, because shared memory can give you MUCH better performance. In the latter case, you will just have to live with it, since different systems can't generally share the same memory space.

### What does “wire_read: unexpected EOF” mean?

This error message should say something like “the plug-in (or the main GIMP app) I was talking to has exited before returning any results, so I assume that it has crashed.”

### Do I need an X server to run in batch mode?

Yes, you have to have some form of X server (unless you're running Windows, of course). It needs an X server for image processing, and for font manipulation. However, if you wish to run in batch mode, you can run with a special, frame-buffer-less X server called Xvfb, which doesn't require a graphics card or mess with your screen:

_Xvfb :1 -screen 0 10x10x8 -pixdepths 1 & gimp --display :1.0 --no-interface --batch "commands" ... &_

The first command starts the special X server; the second is an example of how to invoke GIMP in batch mode. When you are done using GIMP this way for a while, kill off Xvfb so it doesn't waste system resources. If you expect to use GIMP this way a lot, you might want to leave Xvfb running for better response time.

You should check the man page for Xvfb(1) for other options, such as whether to use shared memory.

### What kind of system do I need to run GIMP?

Any system capable of running Gnome 2, KDE 3.2, Windows 2000, Mac OS X and later versions should be able to run GIMP. GIMP's biggest appetite is for memory and how much you will need will depend on the how many images you are working with, their resolution, size, the number of layers you use and so on. As a general rule, more is better, but 128MB should be enough to be getting started with.

### Is there a bug list somewhere?

See [Bugs](/bugs/) for a list of bugs and how to report them.

### Does/could GIMP use high-level graphics operations for its operations?

Not yet. GIMP does use MMX and SSE low-level instructions. The guess is that any gain from higher-level instructions would end up being swamped by having to push pixels back and forth to the graphics card, but we would love to be proved wrong :) The [GEGL project](http://www.gegl.org/) is a more logical place for this kind of thing.

### What does the future hold?

Version 2.8 may bring a combined Transform tool (Scale, Rotate, Shear, Flip and Perspective), more use of Cairo for beautiful antialiased graphics and more usability improvements. We will also make GIMP use more of [GEGL](http://www.gegl.org/), namely for projection (everything you see in a visible stack of layers). This will be another step to version 3.0, which will bring long requested features like support for 16+ bits per channel and adjustment layers, to name a few.

## Using GIMP

### How can I draw a straight line with GIMP?

See [Drawing a Straight Line](http://docs.gimp.org/en/gimp-using-simpleobjects.html#gimp-using-line) in the GIMP user manual or see our [nice tutorial](/tutorials/Straight_Line/).

### How can I draw a circle with GIMP?

The easiest way is to create a new selection with Ellipse Select tool and stroke it (Edit &rarr; Stroke Selection...). We welcome patches that add tools to draw geometric primitives on canvas.

### How can I create an outline around text?

Place some text somewhere. Then click “Create path from text” in the “Text tool option” window. Then use “Edit” &rarr; “Stroke path” and select the appropriate options in the following dialog. Please also see the [Paths](http://docs.gimp.org/en/gimp-concepts-paths.html) section in the user manual.

### What are layers?

The best analogy is to the way cartoons used to be animated. Each component of a scene would be painted on a transparent film, and then each film would be stacked or layered over the other to produce the complete composition. In this way, you could easily animate a person walking because his legs could be animated independantly of his body, for example. Similarly, complex images can be broken down to layers within GIMP and each layer can be processed independentlly of every other. See the [Layers](http://docs.gimp.org/en/gimp-image-combining.html#gimp-concepts-layers) section in the manual for more information.

### How do I save a selected sub-image to a file?

Use “Edit &rarr; Paste As &rarr; New Image” menu command or press Ctrl-Shift-V key combination, then save newly created image.

The script-fu-selection-to image can also be used to cut a selection out of an image and create a new image with it.

### How do I merge an image from a file to the current image?

Use "File &rarr; Open As Layers" menu command or just drag the file to a window and drop it there. The file will be added as a new layer on top of the layers stack.

### How do I get small fonts to look as nice as large ones?

Make sure you have "Hinting" and "Antialiasing" options enabled in Text tool options dialog.

### How do I bind keys to menus for shortcuts?

Make sure that "Use dynamic keyboard shortcuts" option in "Interface" tab of Preferences dialog is enabled, then go to the menu selection you are interested in. Keeping it selected (hold the mouse's menu selection down if necessary), press the key sequence you wish to assign to the menu. It will appear on the right of the menu. The new binding will be saved and used in future GIMP sessions. You can also use "Keyboard Shortcuts" dialog ("Edit &rarr; Keyboard Shortcuts") to assign keys to menus and functions.

### How do I select a layer "sitting" under the mouse cursor? I have more than 400 layers in my image and I cannot remember each layers name.

Please turn on "move-tool-changes-active" in the preferences dialog. Then (after you did a restart of GIMP) hold down the shift-key while you drag or click a layer in the image. The layer will now be selected (active).

### I hate switching between windows in GIMP. Isn't there an easier way?

You are probably using Windows or some GNU/Linux window manager that does not support the "Utility window" hint. Right now you can use list of currently opened images in "Windows" menu.

If you are using GNU/Linux or some free UNIX-like system and not willing to use GNOME and Metacity (its window manager) which does support "Utility window" hint, alternatively you can use a window manager like Fluxbox where you can apply this "always on top" property to the toolbox and layers dialogue. Window managers like Fluxbox also allow you to focus, or even raise, a window whenever you move the mouse over it (usually you have to click on a window before it will focus). Fluxbox allows you to stack windows together and the tab between them, much like Firefox can tab between web pages. Combined with focus-follows-mouse, this may increase one's workflow considerably. Fluxbox also requires very few resources meaning more memory for your images. Finally, don't forget about keyboard shortcuts and modifiers. Learning these means you rarely have to visit the toolbox.

In the mean time, during 2.7.x development cycle we will do our best to switch to tabbed user interface with docked palettes.

### Is there a macro recording interface?

Not at this time. With GIMP based on GEGL, so that all changes are non-destructive, it will be much easier to implement this feature by just remembering all nodes in given range and reapplying them to other images. This is something that can be part of a future release of GIMP like 3.0.

### How do I configure my X server to do global gamma correction?

Some servers have no facility for this; you may be able to adjust your monitor to correct somewhat. Later versions of XFree86 allow these server options:

*   -gamma f set gamma value (0.1 < f < 10.0) Default: 1.0 -rgamma f set gamma value for red phase -ggamma f set gamma value for green phase -bgamma f set gamma value for blue phase

### How do I fill with transparent?

If your image doesn't have an alpha channel, add one with Layers &rarr; Add Alpha Channel. Select the area you want to clear (if not the whole image). To change everything of a particular color transparent, pick Select &rarr; By Color... and click on the color in the image you want to replace. Then select Edit &rarr; Clear. That's it.

Any dithering, blurring, or related effects against the color you replace will be against the original color. This usually requires you to do some form of cleanup of the edge pixels. In cases likely to result in this, change the color to transparent as early as reasonably possible to preclude extra "cleanup" work.

### How do I draw in a different color?

At the bottom of the toolbar there is a box with two smaller boxes and an arrow. The uppermost box displays the current foreground color; the lowermost box displays the current background color. You can single-click on the arrow to switch these two. You can also double-click on either of the color boxes (or single-click if that box is already selected) to pop up a color selection tool, with which you can elect any color you like for that box. That color then becomes the new foreground or background color. Subsequent drawing operations (including text and color fill) will now use these colors.

### How can I export my path to SVG?

Open the dialog "paths", right click the path you want to export, click "Export path..." and save it as "yourpath.svg".

### How do I do something really simple like blur?

There are two methods, one for the current selection or current layer and one tool to blur using mouse. The tool looks like a waterdrop. Click it (or use shortcut V) and hold down the left mouse button while moving the mouse cursor over the desired area. Method two uses the blur filter (Filters &rarr; Blur filters &rarr; Blur) and as said it applies to the current selection and/or layer.

### I've tried to use GIMP but I just don't get it - what am I missing (and I know nothing about images so dont start about alpha channels and layers, etc).

There is plenty of documentation. See [http://docs.gimp.org/en/](http://docs.gimp.org/en/) If you need a complete course about photoediting, image manipulation etc. then a book would be the best to start with.  
 Example books:  
 "Beginning GIMP: From Novice to Professional" - Akkana Peck  
 "GIMP Pocket Reference" - Sven Neumann  
 "Gimp: The Official Handbook" - Karin Kylander, Olof S. Kylander  
 "GIMP Visual Quickstart Guide" - Phyllis Davis  
 "Guerrilla Guide to Great Graphics With the Gimp" - David D. Busch  
 and many many more! Check your local books-dealer!

### How can I paint easily an (OutLined) rectangle using GIMP?

Use "Rectangle Select" tool (see [http://docs.gimp.org/en/gimp-tools-selection.html](http://docs.gimp.org/en/gimp-tools-selection.html)) for making a selection in the form of a rectangle. Then use "Edit" &rarr; "Stroke Selection" (see [http://docs.gimp.org/en/gimp-selection-stroke.html](http://docs.gimp.org/en/gimp-selection-stroke.html)). The "Rectangle Select" tool has the shortcut "R".

### How do I edit properties of existing guides? How do I move existing guides?

Use the Move tool (Toolbox) or press M, then click and drag a guide. If the dragging moves the layer you have to switch modes (hold the shift-key while dragging or click "Pick a layer or guide" in the Move Tool options window). See "Grids and Guides" section of the online manual at [http://docs.gimp.org/](http://docs.gimp.org/)

### How do I select the layer currently shown under the mouse cursor? Is there a shortcut?

There isn't a context menu or shortcut. But you can move visible layers (not overlapped by another one) with the move tool (and holding down the shift key). Use the Move tool (Toolbox) or press M, then click and move a layer. If the dragging moves the currently selected layer you have to switch modes (hold the shift-key while dragging or click "Pick a layer or guide" in the Move Tool options window). This doesn't select the layer, it only moves it. See "Move tool" section of the online manual at [http://docs.gimp.org/](http://docs.gimp.org/)

### How can you wrap text using the Font tool? There are alignment buttons (including justified) but they have little effect since I can't work out how to make the text wrap.

Text cannot be wrapped automatically. But when you type some text in the text-editing dialog you can just hit enter for a new line. In that case the alignment buttons would apply.

### Why do I have to make my rectangular selection exactly right the first time? Why can't I move and resize a rectangular selection using handles?

You can, at least in version 2.3.10 of GIMP. (notice the small arrows at each edge of the rectangular selection.)

### I recently saw a project that specified files were to be saved in Photoshop "Save for Web &rarr; High (15K to 30K Optimized)" format. Is there an equivalent in GIMP?

Yes, there is a plug-in for GIMP which is called "Save for Web" and created by Aurimas Juška as a Google Summer of Code SOC project. It allows visual adjustment of various image parameters such as quality, number of colors, dimensions, etc to reach optimal file size.", see [http://registry.gimp.org/node/33](http://registry.gimp.org/node/33).

### How do I get GIMP to be by default image tool i.e. I installed another program & it is now associated to auto-opening them.

It depends on what operating system you are using.

*   **Windows**: Right-click on an image in explorer and select "Open with..." in the context menu. Select GIMP and mark "Use this program as standard for openening this filetype". Now the filetype of that image should be properly associated with GIMP.

*   **GNU/Linux (KDE)**: Right-click on an image in konqueror, select "Open with..." &rarr; "Other" in the context menu, select GIMP and check the box "Associate filetype with this program".

*   For all other operating systems check the manual of the os.

## Common Feature Requests

### When can we see layer groups?

GIMP 2.8 will have layer groups.

### When can we see 16-bit per channel support (or better)?

For some industries, especially photography, 24-bit colour depths (8 bits per channel) are a real barrier to entry. Once again, it's GEGL to the rescue. Work on integrating GEGL into GIMP began after 2.4 was released, and will span across several stable releases. This work will be completed in GIMP 3.0, which will have full support for high bit depths. If you need such support now and can't wait, [cinepaint](http://www.cinepaint.org/) and [Krita](http://www.krita.org/) support 16 bits per channel now.

The current development branch, GIMP 2.9.x, supports higher bit depths than the 2.8 and older 8-Bit-per-component...

### When can we see native CMYK support?

It is clear from the [product vision](http://gui.gimp.org/index.php/GIMP_UI_Redesign#product_vision) that GIMP eventually needs to support CMYK, but it is impossible to say when someone finds the free time and motivation to add it. In the meantime it is possible to work with CMYK to some extent using plug-ins, such as the [Separate+](http://cue.yellowmagic.info/softwares/separate-plus/index.html) plug-in.

### When will an MDI/nested windows be implemented?

GIMP will not get an MDI, but GIMP 2.8 will feature a single-window mode.

### How should I make feature requests?

The first thing to do is see if your request has already been made. It probably has; we get a lot of feature requests. Check the [user](https://lists.xcf.berkeley.edu/lists/gimp-user/) and [developer](https://lists.xcf.berkeley.edu/lists/gimp-developer/) mailing-list archives and search [bugzilla](https://bugzilla.gnome.org/query.cgi). If you find a discussion that seems relevant, feel free to add your two penneth.

If you are making a new feature request, please make it to the gimp-user or -developer mailing list first and _not_ bugzilla. Think about what it is you are trying to achieve with your request and not about what the underlying procedure is. We get a lot of requests from Photoshop users who simply ask for their favourite Photoshop tool without saying what it does and why it is useful to them. Once we understand what the tool is for, we may find that we can do it better, or that the way it works in Photoshop isn't suitable for GIMP's interface, or that GIMP already supports the feature, but in a different way.

Once the feature has been discussed on the mailing list, a bug report should be opened so that record can be kept on its progress.

Sven Neumann has this to say on the matter of a "polygon select" feature requests:

*   No tool should be written without doing a full specification beforehand and discussing this spec on the mailing-list(s). Bugzilla is the wrong place for such a discussion. If you want to do something to help, please make a list of usage scenarios that involve creating polygonal selections. Then analyze how these scenarios can be performed using the existing tools and identify problems.

    With the list of scenarios and problems, you are then able to analyze and to compare different possible solutions. These solutions might involve changing existing tools or adding new one(s). As soon as we have identified the best solution, it can be fully specified. Only then can someone can start to implement it.

## Plug-Ins

### What are plug-ins?

Plug-ins are external modules that actually do the nifty graphics transformations. There is a plug-in registry at [http://registry.gimp.org/](http://registry.gimp.org/) with the latest plug-ins, maintained by Ingo Lütkebohle. [Special thanks to Adam Moss for the original registry!]

### How do I add new plug-ins?

First, copy the plug-in[s] to your plug-in directory (typically /usr/local/lib/gimp/$VERSION/plug-ins/).

After copying the plug-in to its proper directory, just run GIMP. It should automatically find new plug-ins.

### How do I build new plug-ins?

You'll need a copy of the source directories. Build GIMP. Place the new plug-in in the plug-ins directory. The docs with the new plug-in hopefully identify any special libraries it needs. Look for a plug-in with similar libraries (if all else fails, look at xpm and whirlpinch).

With newer versions, if the plug-in is contained in a single source file, you should just have to run gimptool in the plug-in's directory :

*   gimptool --build plugin.c

For older versions, there are several methods. The first two walk you through a number of steps manually; these are the most thorough, but also require more work on your part. The last ones are scripts of one sort or another, and are easier on your part -- if they work with your system. Go ahead and try - you can always fall back on the first methods.

*   The best way to procede is to edit the Makefile. Pick a similar plug-in (such as whirlpinch). For the SRC and OBJ lines, just add entries similar to the others, but with the new plug-in's name. Now, find all the groups of lines with the other plug-in's name in them, duplicate them, and change the old name to the new name. The one exception is the huge set of lines that have a lot of paths that end in .h - do not bother with these. Now, just type

    *   make

        *   and it should build. Install it wherever your other plug-ins are installed.

*   A second choice for those who don't want to mess with the main Makefile is to build a file to create just the new plug-in. Start the same way - pick a similar plug-in. Now remove the binary and object files for the one you just picked. For instance, if you selected the whirlpinch plug-in, you will see the following files:

    *   whirlpinch whirlpinch.c whirlpinch.o

        *   In this case, you would remove the first and last files, leaving the whirlpinch.c file. Now type

        make

        *   to rebuild the old plug-in.

            Copy the output (cut and paste it!) into a file. Edit the file and change all occurances of "whirlpinch" (or whatever) to the name of the new plug-in. Execute the file you just edited. For instance, if the file is make_plug-in, just type

        make_plugin

        *   and it should work. The copy the plug-in to wherever the others are installed on your system.

*   A Makefile

    *   First, load Makefile-pi provided by Ciccio C. Simon . Change all occurances of the word sharpen in Makefile-pi to the name of the new plug-in. Then type

    *   make -f Makefile-pi

        *   and watch it (hopefully) work.

            If it doesn't work, try the next method.

*   A compile script

    *   First, load the compile-pi script provided by Jeremy Dinsel . Change the permissions on compile-pi as follows:

    *   chmod ugo+rx compile-pi

        *   and type

        compile-pi help

        *   for instructions. Follow those instructionms. If this one also fails, go back to the earlier, manual methods; you have too picky a configuration for the simple methods to work.

If you need more help, ask your system administrator or a handy programmer, or get a good book on make (such as O'Reilly's). You may want to join the GIMP developer's list as well (see the Developer FAQ).

### Is there a plug-in for ... ?

The plug-in registry referenced above is the place to check.

### Why did some plug-ins disappear for 0.99.19?

Some of the plug-ins have proven unstable. These have been moved into a separate download, which should be available wherever you got the GIMP, in the file gimp-plugins-unstable-VERSION.tar.gz or gimp-plugins-unstable-VERSION.tar.bz2 .

Since this list may change frequently, the unstable plug-ins are no longer listed here. Script-Fu

### What is Script-Fu?

In the words of S&P:

*   Script-Fu is the first GIMP scripting extension. Extensions are separate processes that communicate with the GIMP in the same way that plug-ins do. The distinction is that extensions don't require an active image to operate on, instead extending GIMP's functionality. GIMP internals for version 1.0 have been completely overhauled from version 0.54\. In particular, the plug-in API has been made far more general with the advent of the procedural database (PDB). The PDB allows GIMP and its plug-ins to register procedures which can then be called from anywhere: internally, from extensions, and from plug-ins. There are already over 200 internal GIMP procedures, and more being created all the time. Because all of these procedures can be easily invoked from extensions, the logical next step was to create a scripting facility; thus, Script-Fu was born.

### Where can I learn about Script-Fu?

As with plug-ins, web pages, COBOL, or anything else, one of the best things you can do is look at other peoples' code, and play with it. But it helps a lot if you know Scheme.

*   = S&P's Script-Fu pages at [http://www.xcf.berkeley.edu/~gimp/script-fu/script-fu.html](http://www.xcf.berkeley.edu/~gimp/script-fu/script-fu.html) = Mike Terry's Black Belt School of Script-Fu at [http://manual.gimp.org/manual/GUM/write_scriptfu3.html](http://manual.gimp.org/manual/GUM/write_scriptfu3.html)

### How do I call one script-fu script from another?

The trick to calling script-fu-scripts from another script is to just reference the main define for the script and not to try to use the pdb call. All the scripts in script-fu share a common name space; you call other scripts just like a regular function / define / whatever you call those those things in_scheme.

Ie, to call script-fu-predator in a script, just use

*   (script-fu-predator img drawable 2 TRUE 3 TRUE TRUE)

For examples, see

*   [http://adrian.gimp.org/scripts/test.scm](http://adrian.gimp.org/scripts/test.scm) .

### How do I call a plug-in from script-fu?

The following examples assume the plug-in name is "plug_in_randomize_hurl", and the plug-in has four parameters specific to it, the first two of which are floats, and the next two ints.

From the script-fu console, call a plug-in like this:

    (plug-in-name 1 0 0 100.0 1.0 10 0)

The first parameter should always be a "1". The next two are the image number and drawable. Anything following these numbers will be plug-in parameters, which depend on the plug-in.

Inside an actual script, call a plug-in like this:

    (define (script-fu-fred img drawable)

        (plug-in-randomize-hurl 1 img drawable 100.0 1.0 10 0)
        (gimp-displays-flush)

        )

        (script-fu-register "script-fu-fred" "<Image>/Script-Fu/fred"
        "Randomize test" "Miles O'Neal <meo@rru.com>" "Miles O'Neal"
        "1998/May/1" "RGB*, GRAY*, INDEXED*" SF-IMAGE "Image" 0 SF-DRAWABLE
        "Drawable" 0)

### How do I execute script-fu from batch mode?

Invoke the script as non-interactive and add a pair of escaped quotes around each string just like you do in (script-fu-register). You DO NOT need to replace '-' with '\_' in any names or registrations.

Example script:

    (define (script-fu-famhist-link text filename) ;; code ommitted
    for brevity (file-gif-save 1 img 0 filename "" FALSE FALSE 0 0))

    (script-fu-register "script-fu-famhist-link"
    "<Toolbox>/Xtns/Script-Fu/Family Historian/Link" "Family Historian
    Link" "John Johnson" "John Johnson" "1998" "" SF-VALUE "Text String"
    "\"Family Historian\"" SF-VALUE "Base filename" "\"foo\"")

    Example Invocation:

    ;; note the '1' as the first argument tell it to run non-interactivly ;;
    note the \" \" pairs around the strings

    gimp -n -b  '(script-fu-famhist-link 1 "\"Introduction\"" \
    "\"intro.gif\"")' '(gimp-quit 0)'

For a detailed, step by step explanation, check out Adrian's GIMP Batch Mode how-to at [http://adrian.gimp.org/batch/](http://adrian.gimp.org/batch/) .

### What does "procedural-database-error" in script-fu mean?

Normally it means that the script is trying to use a particular font that isn't available on your system - it's either not installed or not in your X server's FONTPATH. The base script-fu package makes extensive use of the freefont package, and at least one font (AlfredDrake) from the sharefont package.

### What is Net-Fu? Where is it?

Net-fu is a web-based interface to a script-fu server. The work is done at a remote site. To see Net-fu, point your web browser at [http://download.gimp.org/](http://download.gimp.org/) or one of the mirror sites, and then go to "pub/gimp/net-fu/". Any web browser can read net-fu pages; the browser must be Java-enabled to actually run Script-fu. Fonts

### Where can I get the fonts I'm missing?

The freefonts and sharefonts packages are both available from [ftp://ftp.funet.fi/pub/Linux/mirrors/metalab/X11/fonts/](ftp://ftp.funet.fi/pub/Linux/mirrors/metalab/X11/fonts/) or other metalab mirrors. If you get the sharefonts package, be sure and read the various licensing agreements, and abide by them.

### How can I change the GIMP font?

You need to copy the gtkrc file that comes with the GIMP source (in the top level directory) into $HOME/.gimp/gtkrc . As of 0.99.10, this should be recognized. You then go in and edit the default font style, the one that looks like this:

    style "default" { font =
    "-adobe-helvetica-medium-r-normal--*-100-*-*-*-*-*-*" }

I'm sure ther's a lot of clever stuff that can be done here, and I'll try to track it down soon, but in the meantime, just change that "100" to something larger, like "120" or "140". (The number is points= 10, so 100 is a 10 point font).

Obviously, you could stick in any font you have available.

### Why don't the Far Eastern fonts work?

These are 16 bit fonts, with thouousands and thouousands of characters. And the characters are more complex, which means (usually) more bits per character, which means more memory and more processing time.

This includes fonts such as kana, kanji, song ti, mincho and gothic. (If you look carefully at the fully qualified font name for gothic via xfontsel, you'll see clues. It's a daewoo font. The gothic name is misleading to western minds, but no doubt means something to its author[s].)

Check one of these out in a program that shows a font as pages (such as xfd).. You can keep hitting next page to see a new page of characters, almost forever.

### What about TrueType fonts?

If neither your X server nor your X font server supports you can try one of the TruType font servers: xfstt ([http://sunsite.unc.edu/pub/Linux/X11/fonts/](http://sunsite.unc.edu/pub/Linux/X11/fonts/)) or xfsft ([http://www.dcs.ed.ac.uk/home/jec/programs/xfsft/](http://www.dcs.ed.ac.uk/home/jec/programs/xfsft/) .

xfstt supposedly has limitations on the font size. File Formats

### What is GIMP's native graphics file format?

XCF is GIMP's "native" format. This will preserve all information about an image, including the layers.

### What other graphics file types are supported?

All the common formats, and many more as well, including GIF, TIFF, JPEG, XBM, XPM, PostScript, and BMP. Plug-ins are used to load and save files so adding new file types is very simple, compared to other graphics programs.

As of July 1, 1998, the list of supported types included BMP, CEL, FITS, FLI, GBR, Gicon, GIF, GIcon, HRZ, JPEG, PAT, PCX, PIX, PNG, PNM, PostScript, SGI, Sun Raster, TGA, TIFF, XPM, XWD and XCF. Bzipped, Gzipped and Xdelta'd files are understood, and URL support is provided.

Of course, plug-ins for other types may be available at the plug-in registry .

*   Why can't I save my image as a GIF (or whatever)?

The two most likely problems are related to image type and layers. For instance, your image type must be "Indexed" for GIF, but "RGB" for TIFF. Try a different image type (look under the "Image" menu). If you have more than 1 layer in your image, you probably need to merge the visible layers, and/or "flatten" the image. Both operations are available under the "Layers" menu or from the "Layers" dialog. Flattening will destroy any background transparency.

### Is there any way to keep the layers when I save?

Yes; GIMP has a file format just for this - the XCF format.

### Why can't I open or export JPEG / JPG files?  
 Why can't I open or export GIF files?  
 Why can't I open or export PNG files?  
 Why can't I open or export XPM files?  
 Why can't I open or export TIFF / TIF files?  
 Why can't I open or export PSD files?  
 Why can't I open or export SOME_FORMAT files?  

There are several possibilities.

1.  GIMP comes with full support for a few types built in. If the type you want doesn't appear in file type format of the Open and Export dialogs, you need to check the Plug-in registry to see whether you need to download an optional plug-in.
2.  Some of the file types, such as JPEG and TIFF, require extra libraries (described elsewhere). Make sure you have the correct versions of these on your system.

## Troubleshooting Unix Platforms

### Why can't I get JPEG to work on my Digital Alpha/UNIX (4.0d) box?

Even the jpeg libraries at the GIMP web site may not work for all versions. If their jpeg-shared-6.a.tar.gz package doesn't work for you, try:

*   [ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v6b.tar.gz](ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v6b.tar.gz)

### Why won't GIMP compile on 64-bit or IRIX (SGI) machines?

If you are using a 64-bit OS, you need to add the `-o32` option for the compiler, or use gcc.

With the SGI compiler, you may also need to play with optimization. 
Some modules may have exhibit problems unless compiled with `-O1` or even `-O0`.

### Script-Fu won't compile on IRIX (SGI)

Script-Fu requires the POSIX-compliant regex functions, which SGI only supports with IRIX 6.2 and later versions. The GNU version of regex should work just fine, though, and is available at:

*   [http://wuarchive.wustl.edu/systems/gnu/regex-0.12.tar.gz](http://wuarchive.wustl.edu/systems/gnu/regex-0.12.tar.gz)

### Why does GIMP complain about X Input Methods under Solaris?

GIMP is interacting in such a way with your system that it thinks you have XIM extensions when you don't. Run the configure script again, with the `--disable-xim` option, and recompile.

You can also try compiling with `--disable-shared`.

Or you can install a version of X11R6\. 8^)

### How do I add fonts with Solaris?

If you just want to use freefonts or sharefonts, you can copy these files into the appropriate directory (such as /usr/openwin/lib/fonts/freefonts/ or /usr/openwin/lib/fonts/sharefonts/), or merge them with the appropriate fonts.dir and fonts.scale files if you mixed in freefonts and sharefonts with existing fonts:

*   freefonts fonts.dir

*   freefonts fonts.scale

*   sharefonts fonts.dir

*   sharefonts fonts.scale

Or just try using fontadmin instead of mkfontdir .

I've never run into a Solaris system missing this, but according to Neil Corlett:

*   The 'fontadmin' tool is a openwin demo program and sometimes does not exist. To properly add fonts the finagled directory requires fonts.dir, fonts.scale files to exist. mkfontdir does the first of these OK. For the second I built groff and downloaded type1inst-0.6.1 from an X contrib archive. type1inst (which needs groff) will build the fonts.scale file from the pfb files automatically.

Solaris 2.6 is supposed to include better font editor and admin tools.

### How do I add fonts with SunOS?

SunOS ships with an X11R4 server, which does not handle either scaleable fonts or communications with the X font server. If you want to use the freefonts (or any scalable fonts) on SunOS, you need to install your own, newer X server, preferably X11R6.4 (which will be much faster than the server shipped with SunOS).

If you do this, you will no longer have PostScript capability directly in your X server; you will need to use ghostscript. You may well want to keep both servers around, and use each when you need its features.

Of course, you could always try to find a PS version of the font you need and make a bitmap for the size you need and add that to the X11R4 server's font path, but if you need more than one or two font/size combinations over all the time you use GIMP, this is an obnoxious solution.

### What is the gimp.wmconfig file?

*   It's a Red Hat RPM-related file, related to their desktop and window manager.

#### Why does my RedHat system get <span class="u">register_? errors when I run GIMP? ####
This is due to incompaitble RPMS. If (for example) gtk was compiled with egcs, GIMP must be compiled with egcs. There is no easy way to tell what is compiled with what, so getting both GIMP and gtk off a GIMP mirror would be a good idea.</span>

Another possibility is for this error (far less common) is that there is an old library compiled with the other hanging around somewhere on the system. Remove old copies of libgimp.

### Why don't GIF and JPEG work on Slackware Linux?

*   You need to manually get libgif and libjpeg and compile and install them on your system. They will install by default in /usr/local/lib, so once they're installed, you have to make sure that LD_LIBRARY_PATH=/usr/local/lib or put /usr/local/lib in your ld.so configuration file. In addition, you also have to remove libgif.* and libjpeg.* from your /usr/lib directory, as these will be found first (and even if you finagle ld.so to find the other libs first, they're still broken so remove them anyway).

### I get make errors on {Solaris, HP/UX, whatever}.

You are probably not using the GNU make. Most, if not all, non-GNU makes will fail on the GIMP makefiles. Get the GNU make package.

### Why do I see weird things when I use GIMP with AcceleratedX?

It's a bug in AcceleratedX with shared memory. Turn off shared memory when you start GIMP (--no-xshm) or pick up the patch to AcceleratedX's X server from [ftp://ftp.xinside.com/pub/update/](ftp://ftp.xinside.com/pub/update/) .

At least one person has found this bug (or another one with the same symptoms) to still be present in 4.1 .

### What's this beavis.jpg image used in several scripts?

(/usr/local/share/gimp/scripts/beavis.jpg is the B/W image in question.)

The image (of a kitten playing with Gumby) is used as "sorta random, sorta not" data to generate (for example) the crystal bands, or other texture maps. There are other ways to produce this data as well, but the author stuck with this one, found in a tutorial somewhere. 

#### What lucky human does this adorable cat own?

One of the original GIMP authors, Spencer Kimball or Peter Mattis, we forgot which.

## Footnotes

Portions of this FAQ have been taken from [http://www.rru.com/~meo/gimp/faq-user.html](http://www.rru.com/~meo/gimp/faq-user.html)
