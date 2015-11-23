Title: Install Help
Date: 2015-08-14T14:18:56-05:00
Author: Pat David
Status: hidden



**Note for Windows Users:** This page is for installation help for the Unix version of GIMP. If you need help with the installation of Windows GIMP, see the [GIMP for Windows](/windows/) page.

*   [Requirements](#requirements)
*   [GIMP Compilation and Installation](#gimp-compilation-and-installation)
*   [Other Packages](#other-packages)

## Requirements

### Main Requirements

Well, it is necessary to have a C compiler and related tools to compile and install the source package. For the most part, GCC is recommended, but a lot of effort has gone into making GIMP compile with as many compilers as possible.

A fair amount of disk space is needed too. For a full build with debugging, at least 200 megs free is recomended. Without debugging and with static libs turned off, GIMP can be compiled in 20-30 megs of space. This will vary depending on architecture of course. A full GIMP install including all the gimp-data packs can be 20 megs or more.

A full compile of the stable version takes 1-2 hours on a PPro 200 or K-6 200 with 64 megs of RAM. On a P4 or Athlon with 256 megs of RAM, a build can take 20-30 minutes. In general, expect about 3-4 times as long as a Linux kernel 2.2 compile (for GNU/Linux systems of course). In other words, its a long compile. That's what 300,000+ lines of code get you.

### Stable version (2.2.x)

*   A recent version of **pkg-config** is needed and you can grab them at [http://www.freedesktop.org/software/pkgconfig/](http://www.freedesktop.org/software/pkgconfig/)
*   **GTK+ 2.4.4** or better (Gimp Toolkit). The GIMP toolkit can be found at [ftp://ftp.gtk.org/](ftp://ftp.gtk.org/) GTK+ 2.4.4 also needs the following packages. (Either the version listed or newer)
    *   **GLib 2.4.5**
    *   **Pango 1.4.0**
    *   **ATK**
*   **PangoFT2** a Pango backend that uses **FreeType2** (Make sure you have FreeType2 installed before installing Pango). Downloads can be found at [http://www.freetype.org/](http://www.freetype.org/)
*   **libart2** Grab the module libart_lgpl out of GNOME CVS or fetch the tarball from [ftp://ftp.gnome.org/pub/gnome/sources/libart_lgpl/](ftp://ftp.gnome.org/pub/gnome/sources/libart_lgpl/)



## GIMP Compilation and Installation


After grabbing the GIMP distribution, you are ready to compile and install. The main site for the latest offical GIMP distribution is [http://download.gimp.org/pub/gimp/](//download.gimp.org/pub/gimp/) but you should consider using one of the mirrors listed on the [download page](./).

GIMP makes use of the Gimp Toolkit (GTK+) and other libraries that must be installed first. Look in Requirements above to find out more.

Compile as a normal user using: <kbd>./configure && make</kbd> and then as root <kbd>make install</kbd>

If all goes well, a good while later, you will have a brand spanking new GIMP to play with. Unfortunately, it has been rumored that it isn't always that easy. So, here are a few common problems and some solutions ...

For some more specific info, you may want to read the [INSTALL](INSTALL) file from the main GIMP distribution.


## Other Packages


### Print plug-in does not compile

Starting with version 1.2.4, the print plug-in depends on libgimpprint, which is now distributed as a separate package. The previous versions of GIMP (up to 1.2.3) included all files as part of the GIMP distribution, but you should now download and install libgimpprint 4.2.6 separately from the Gimp-Print site:

[http://gimp-print.sourceforge.net/](http://gimp-print.sourceforge.net/)

Once the lib is compiled and installed, run <kbd>ldconfig</kbd> as root and the print plug-in should compile.

### JPEG plug-in does not compile

The jpeg plug-in requires the jpeg library. If you don't have it installed or you have a very old version, then you need to get a recent jpeg library. The places to look are:

[ftp://ftp.uu.net/graphics/jpeg/](ftp://ftp.uu.net/graphics/jpeg/)

Once the lib is compiled and installed, run <kbd>ldconfig</kbd> as root and the jpeg plug-in should compile.

### TIFF plug-in does not compile

The tiff plug-in requires the tiff library. See the jpeg problem mentioned above. Same deal, different lib. The places to look are at:

[ftp://ftp.sgi.com/graphics/tiff/](ftp://ftp.sgi.com/graphics/tiff/)

Once the lib is compiled and installed, run <kbd>ldconfig</kbd> as root and the tiff plug-in should compile.

### PNG plug-in does not compile

The png plug-in requires libpng and libz (zlib). See the jpeg problem mentioned above. Same deal, different lib. The places to look are at:

[ftp://ftp.uu.net/graphics/png/src/](ftp://ftp.uu.net/graphics/png/src/)

Once the lib is compiled and installed, run <kbd>ldconfig</kbd> as root and the png plug-in should compile.

### XPM plug-in does not compile

The xpm plug-in requires the xpm library. See the jpeg problem above. Same deal, different lib. The places to look are at:

[ftp://ftp.x.org/contrib/libraries/](ftp://ftp.x.org/contrib/libraries/)

### I have no SVG support

SVG support requires at least version 2.2 of the rsvg library from gnome.org. This can be found at:

[ftp://ftp.gnome.org/mirror/gnome.org/sources/librsvg/](ftp://ftp.gnome.org/mirror/gnome.org/sources/librsvg/2.6/)

