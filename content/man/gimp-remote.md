Title: GIMP-REMOTE Man Page
Date: 2015-08-17T11:31:37-05:00
Modified: 2015-08-17T11:31:42-05:00
Authors: Pat David
Status: hidden


[Table of Contents](#toc)

## [Name](#toc0)

gimp-remote - tells a running GIMP to open a (local or remote) image file.

## [Synopsis](#toc1)

<span class="man" markdown="1">
**gimp&#8209;remote** [&#8209;h] [&#8209;&#8209;help] [&#8209;v] [&#8209;&#8209;version] [&#8209;&#8209;display _display_] [&#8209;e] [&#8209;&#8209;existing] [&#8209;q] [&#8209;&#8209;query] [&#8209;s] [&#8209;&#8209;no&#8209;splash] [&#8209;p] [&#8209;&#8209;print&#8209;xid] _filename_ ...
</span>

## [Description](#toc2)

_gimp-remote_ is a small utility that tells a running GIMP to open one or more (local or remote) image files. It does so by searching for a GIMP toolbox on the active display. If it can find a GIMP toolbox, a synthetic drop event is created which makes GIMP think the files would have been dropped onto the toolbox. More than one filename or URL can be specified on the commandline.

If no GIMP window is found, _gimp-remote_ will start a new GIMP instance and ask it to load the specified images. If no filename or URL is given, _gimp-remote_ will start a new GIMP. This behaviour can be altered using the command-line options described below.

If you are using GIMP on Linux or another platform with the D-Bus message bus system, chances are good that this functionality is already built into the main GIMP executable and that you will not need to use _gimp-remote_.

## [Options](#toc3)

_gimp-remote_ accepts the following options:

<dl class='man'>

<dt>-h, --help</dt>

<dd>Display a list of all commandline options.</dd>

<dt>-v, --version</dt>

<dd>Output the version info.</dd>

<dt>--display _display_</dt>

<dd>Use the designated X display.</dd>

<dt>-e, --existing</dt>

<dd>If no running GIMP instance is found, don’t start a new one but exit.</dd>

<dt>-q, --query</dt>

<dd>Check if GIMP is running and exit. A status code of 0 indicates that a GIMP toolbox window has been found on this display.</dd>

<dt>-p, --print-xid</dt>

<dd>Like -q, but print the X Window ID of the toolbox window if GIMP is already running. If no such window exists nothing is printed.</dd>

<dt>-s, --no-splash</dt>

<dd>When starting GIMP, do not show the splash screen.</dd>

</dl>

## [Examples](#toc4)

<dl>

<dt>gimp-remote <a href="http://www.gimp.org/images/wilber_the_gimp.png">http://www.gimp.org/images/wilber_the_gimp.png</a></dt>

<dd>Loads the image from the GIMP website into a running GIMP or starts a new one.</dd>

<dt>gimp-remote wilber.xcf wilma.xcf</dt>

<dd>Loads the local files wilber.xcf and wilma.xcf into a running GIMP or starts a new one.</dd>

</dl>

## [Environment](#toc5)

<dl>

<dt>DISPLAY</dt>

<dd>to get the default host and display number.</dd>

</dl>

## [Authors](#toc6)

Sven Neumann and Simon Budig.

## [See Also](#toc7)

[**gimp**(1)](gimp.html) , [**gimprc**(5)](gimprc.html) , [**gimptool**(1)](gimptool.html)

* * *

<a name="toc">Table of Contents</a>

*   [Name](#sect0)
*   [Synopsis](#sect1)
*   [Description](#sect2)
*   [Options](#sect3)
*   [Examples](#sect4)
*   [Environment](#sect5)
*   [Authors](#sect6)
*   [See Also](#sect7)
