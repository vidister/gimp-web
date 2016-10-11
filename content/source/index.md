Title: GIMP From Source
Date: 2015-08-17T15:38:06-05:00
Modified: 2015-08-17T15:38:12-05:00
Authors: Pat David
Status: hidden


The official distribution of GIMP is the source code, distributed in tar files from the GIMP FTP site and its [mirrors](/downloads/#mirrors). The same source code can be compiled to create binaries for different platforms such as [GNU/Linux](/unix/), [Microsoft Windows](/windows/), [Mac OS X](/macintosh/), [Solaris](/unix/) and many others.

*   [GIMP Source Code](#gimp-source-code)
*   [GIMP Requirements](#gimp-requirements)
*   [GIMP from Git](#gimp-from-git)
*   [Optional packages](#optional-packages)

### Stable releases

Is recommended for most users. Pre-compiled binaries of the stable GIMP are usually available for many platforms (see the platform-specific pages for more details), so you do not even have to compile the code yourself.

### Development releases

For those who want to check the progress towards the next stable release, and who want to help the developers by testing the code and reporting bugs. The development version contains more features than the stable version but it may crash from time to time so be sure to save your work often. If you are using this version, it is a good idea to subscribe to some of the GIMP [mailing lists](/mail_lists.html) (gimp-user or gimp-developer) so that you can follow the discussions about new features and known bugs.

### Git repository

This is for those who want to live on the bleeding edge. This will give you the latest version of the source code with the latest features, but also with the latest bugs (eeek!). The repository contains several versions of the code called "branches" so you can fetch the latest version ("trunk") or a stable version from a maintenance branch. If you intend to [contribute](/develop/) to the development of GIMP, then you should try using Git. As the code is constantly evolving and features are added (or removed) every day, you should have a look at the [developers' site](http://wiki.gimp.org/) and subscribe to the gimp-developer mailing list if you compile the code from Git.

## GIMP Source Code

The GIMP source code is distributed as tarballs. It is available from the GIMP FTP site and its [mirrors](/downloads/#mirrors).

## GIMP Requirements

All requirements below must be met to be able compiling GIMP from source. This list might change depending on the releases being worked on during development of GIMP. Look at the files INSTALL and README in the tarballs for details.

### Stable version 2.8.x

<table markdown='span' class='gimpfromsrc'>
<tbody>
<tr>
<th>Package</th>
<th>Version</th>
<th>FTP</th>
<th>HTTP</th>
<th>Description</th>
</tr>
<tr>
<td>pkg-config</td>
<td>0.16.0 or newer</td>
<td>-</td>
<td>[Download](http://www.freedesktop.org/software/pkgconfig/)</td>
<td>A system for managing library compile/link flags</td>
</tr>
<tr>
<td>GTK+</td>
<td>2.24.10 or newer</td>
<td>[Download](ftp://ftp.gnome.org/pub/GNOME/sources/gtk+/)</td>
<td>-</td>
<td>The GIMP toolkit</td>
</tr>
<tr>
<td>GLib</td>
<td>2.30.2 or newer</td>
<td>[Download](ftp://ftp.gnome.org/pub/GNOME/sources/glib/)</td>
<td>-</td>
<td>Glib Convenience Library</td>
</tr>
<tr>
<td>Pango</td>
<td>1.29.4 or newer</td>
<td>[Download](ftp://ftp.gnome.org/pub/GNOME/sources/pango/)</td>
<td>-</td>
<td>Text layout engine, GIMP also requires PangoCairo — a Pango backend using Cairo</td>
</tr>
<tr>
<td>Fontconfig</td>
<td>2.2.0 or newer</td>
<td>-</td>
<td>[Download](http://freedesktop.org/fontconfig/release/)</td>
<td>Font Configuration</td>
</tr>
<tr>
<td>babl</td>
<td>0.1.10 or newer</td>
<td>[Download](http://download.gimp.org/pub/babl/)</td>
<td>-</td>
<td>Pixel format translation library</td>
</tr>
<tr>
<td>GEGL</td>
<td>0.2.0 or newer</td>
<td>[Download](http://download.gimp.org/pub/gegl/)</td>
<td>-</td>
<td>Generic Graphics Library</td>
</tr>
</tbody>
</table>


## GIMP from Git

The source code of GIMP is maintained in the GNOME Git repository. Besides offering version tracking, branching, avanced diff support and else, this repository grants everyone access to the latest revision of the GIMP source code.  
 Follow this guide and you will have the most recent GIMP in no time:

*   [Best way to keep up with GIMP from git](/source/howtos/gimp-git-build.html)

To find out more about GIMP development, [http://wiki.gimp.org/](http://wiki.gimp.org/) should answer the questions you have.

## <a name="optional_packages">Optional packages</a>

To make it easy for you to understand how to get GIMP and what is required to run GIMP, the list of packages has been done below. Not only is the list for the required packages but also for the packages that can be added to support other things like fileformats etc.

<table markdown="span" class='gimpfromsrc'>
<tbody>
<tr>
<th>Package</th>
<th>FTP</th>
<th>HTTP</th>
<th>Description</th>
<th>Dependency</th>
</tr>
<tr>
<td>aalib</td>
<td>-</td>
<td>[Download](http://aa-project.sourceforge.net/aalib/)</td>
<td>ASCII art library</td>
<td>Optional</td>
</tr>
<tr>
<td>libexif</td>
<td>-</td>
<td>[Download](http://sourceforge.net/projects/libexif)</td>
<td>EXIF tag support for JPEGs</td>
<td>Optional</td>
</tr>
<tr>
<td>libjpeg</td>
<td>[Download](ftp://ftp.uu.net/graphics/jpeg/)</td>
<td>-</td>
<td>JPEG support</td>
<td>Optional (explicit disable)</td>
</tr>
<tr>
<td>libpng</td>
<td>-</td>
<td>[Download](http://www.libpng.org/)</td>
<td>PNG support</td>
<td>Optional (explicit disable)</td>
</tr>
<tr>
<td>libtiff</td>
<td>-</td>
<td>[Download](http://www.remotesensing.org/libtiff/)</td>
<td>TIFF support</td>
<td>Optional (explicit disable)</td>
</tr>
<tr>
<td>libmng</td>
<td>-</td>
<td>[Download](http://www.libmng.com/)</td>
<td>MNG support</td>
<td>Optional (plugin won't be built)</td>
</tr>
<tr>
<td>libxpm</td>
<td>[Download](ftp://ftp.x.org/contrib/libraries/)</td>
<td>[Download](http://koala.ilog.fr/ftp/pub/xpm/)</td>
<td>XPM support</td>
<td>Optional</td>
</tr>
<tr>
<td>librsvg</td>
<td>[Download](ftp://ftp.gnome.org/mirror/gnome.org/sources/librsvg/)</td>
<td>[Download](http://librsvg.sourceforge.net/)</td>
<td>Scalable Vector Graphics</td>
<td>Optional (plugin won't be built)</td>
</tr>
<tr>
<td>libwmf</td>
<td>-</td>
<td>[Download](http://wvware.sourceforge.net/libwmf.html)</td>
<td>Library to convert wmf files</td>
<td>Optional (plugin won't be built)</td>
</tr>
<tr>
<td>webkit</td>
<td>-</td>
<td>[Download](http://live.gnome.org/WebKitGtk)</td>
<td>HTML renderer and web content engine</td>
<td>Optional (Help Browser won't be built)</td>
</tr>
<tr>
<td>zlib</td>
<td>-</td>
<td>[Download](http://www.gzip.org/zlib/)</td>
<td>Compression routines</td>
<td>Optional</td>
</tr>
<tr>
<td>Python</td>
<td>[Download](ftp://ftp.python.org/pub/python/)</td>
<td>[Download](http://www.python.org/)</td>
<td>Python support</td>
<td>Optional</td>
</tr>
</tbody>
</table>

