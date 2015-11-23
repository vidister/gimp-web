Title: GIMP Man Page
Date: 2015-08-17T11:31:37-05:00
Modified: 2015-08-17T11:31:42-05:00
Authors: Pat David
Status: hidden

<style>
dt {
    font-family: monospace;
}
</style>


[Table of Contents](#toc)

## [Name](#toc0)

gimp - an image manipulation and paint program.

## [Synopsis](#toc1)

<span style="font-family: monospace;" markdown="1">
**gimp** [&#8209;h] [&#8209;&#8209;help] [&#8209;&#8209;help&#8209;all] [&#8209;&#8209;help&#8209;gtk] [&#8209;v] [&#8209;&#8209;version] [&#8209;&#8209;license] [&#8209;&#8209;verbose] [&#8209;n] [&#8209;&#8209;new&#8209;instance] [&#8209;a] [&#8209;&#8209;as&#8209;new] [&#8209;i] [&#8209;&#8209;no&#8209;interface] [&#8209;d] [&#8209;&#8209;no&#8209;data] [&#8209;f] [&#8209;&#8209;no&#8209;fonts] [&#8209;s] [&#8209;&#8209;no&#8209;splash] [&#8209;&#8209;no&#8209;shm] [&#8209;&#8209;no&#8209;cpu&#8209;accel] [&#8209;&#8209;display&nbsp;_display_] [&#8209;&#8209;session&nbsp;_&lt;name&gt;_] [&#8209;g] [&#8209;&#8209;gimprc&nbsp;_&lt;gimprc&gt;_] [&#8209;&#8209;system&#8209;gimprc&nbsp;_&lt;gimprc&gt;_] [&#8209;&#8209;dump&#8209;gimprc] [&#8209;&#8209;console&#8209;messages] [&#8209;&#8209;debug&#8209;handlers] [&#8209;&#8209;stack&#8209;trace&#8209;mode&nbsp;_&lt;mode&gt;_] [&#8209;&#8209;pdb&#8209;compat&#8209;mode&nbsp;_&lt;mode&gt;_] [&#8209;&#8209;batch&#8209;interpreter&nbsp;_&lt;procedure&gt;_] [&#8209;b] [&#8209;&#8209;batch&nbsp;_&lt;command&gt;_] [_filename_] ...
</span>
<!--
If you're reading this, I'm sorry for what you see above.  It's a man page formatting.  HTML makes a mess of it.
And raw man pages suck, imo.  Here's what I did:
1. Wrap it in a span, set the font family to mono.
2. escape all brackets (not sure I need this).
3. replace all "<" and ">" with &lt; and &gt;
4. replace all hyphens/dashes with the non-breaking version: &#8209;
5. replace all spaces inside brackets with non-breaking version: &nbsp;
-->

## [Description](#toc2)

GIMP is the _GNU Image Manipulation Program_. It is used to edit and manipulate images. It can load and save a variety of image formats and can be used to convert between formats.

GIMP can also be used as a paint program. It features a set of drawing and painting tools such as airbrush, clone, pencil, and paint brush. Painting and drawing tools can be applied to an image with a variety of paint modes. It also offers an extensive array of selection tools like rectangle, ellipse, fuzzy select, bezier select, intelligent scissors, and select by color.

GIMP offers a variety of plug-ins that perform a variety of image manipulations. Examples include bumpmap, edge detect, gaussian blur, and many others. In addition, GIMP has several scripting extension which allow for advanced non-interactive processing and creation of images.

GIMP ships with a second binary called _gimp-console_. This binary is a console-only version and behaves as if _gimp_ was called with the --no-interface command-line option.

On platforms with the D-Bus message bus system, GIMP will by default check if an instance is already running in this user session. If it detects that, it will pass all filenames given on the command-line to the already running GIMP instance and quit.

## [Options](#toc3)

GIMP accepts the following options:

<dl>

<dt>-h, --help</dt>

<dd>Show GIMP command-line options.</dd>

<dt>--help-all</dt>

<dd>Show all command-line options.</dd>

<dt>--help-gtk</dt>

<dd>Show GTK+ command-line options.</dd>

<dt>--help-gegl</dt>

<dd>Show GEGL command-line options.</dd>

<dt>-v, --version</dt>

<dd>Output version information and exit. When combined with the --verbose option, version information about libraries used by GIMP is shown as well.</dd>

<dt>--license</dt>

<dd>Output license information and exit.</dd>

<dt>--verbose</dt>

<dd>Be verbose and create information on standard output.</dd>

<dt>-n, --new-instance</dt>

<dd>Do not attempt to reuse an already running GIMP instance. Always start a new one.</dd>

<dt>-a, --as-new</dt>

<dd>Open filenames passed on the command-line as new images, don’t set the filename on them.</dd>

<dt>-i, --no-interface</dt>

<dd>Run without a user interface.</dd>

<dt>-d, --no-data</dt>

<dd>Do not load patterns, gradients, palettes, or brushes. Often useful in non-interactive situations where startup time is to be minimized.</dd>

<dt>-f, --no-fonts</dt>

<dd>Do not load any fonts. No text functionality will be available if this option is used.</dd>

<dt>--display _display_</dt>

<dd>Use the designated X display.</dd>

<dt>-s, --no-splash</dt>

<dd>Do not show the splash screen.</dd>

<dt>--no-shm</dt>

<dd>Do not use shared memory between GIMP and its plug-ins. Instead of using shared memory, GIMP will send the data via pipe. This will result in slower performance than using shared memory.</dd>

<dt>--no-cpu-accel</dt>

<dd>Do not use CPU accelerations such as MMX or SSE even if GIMP detects that your CPU provides this functionality.</dd>

<dt>--session <em>&lt;name&gt;</em></dt>

<dd>Use a different sessionrc for this GIMP session. The given session name is appended to the default sessionrc filename.</dd>

<dt>-g, --gimprc <em>&lt;gimprc&gt;</em></dt>

<dd>Use an alternative gimprc instead of the default one. Useful in cases where plug-in paths or machine specs may be different.</dd>

<dt>--system-gimprc <em>&lt;gimprc&gt;</em></dt>

<dd>Use an alternate system gimprc file.</dd>

<dt>--dump-gimprc</dt>

<dd>Output a gimprc file with default settings.</dd>

<dt>--debug-handlers</dt>

<dd>Enable debugging signal handlers.</dd>

<dt>-c, --console-messages</dt>

<dd>Do not popup dialog boxes on errors or warnings. Print the messages on the console instead.</dd>

<dt>--stack-trace-mode <em>{never|query|always}</em></dt>

<dd>If a stack-trace should be generated in case of fatal signals.</dd>

<dt>--pdb-compat-mode <em>{off|on|warn}</em></dt>

<dd>If the PDB should provide aliases for deprecated functions.</dd>

<dt>--batch-interpreter <em>&lt;procedure&gt;</em></dt>

<dd>Specifies the procedure to use to process batch events. The default is to let Script-Fu evaluate the commands.</dd>

<dt>-b, --batch <em>&lt;command&gt;</em></dt>

<dd>Execute <em>&lt;command&gt;</em> non-interactively. This option may appear multiple times. The <em>&lt;command&gt;</em> is passed to the batch interpreter. When <em>&lt;command&gt;</em> is <strong>-</strong> the commands are read from standard input.</dd>

</dl>

## [Environment](#toc4)

GIMP respects a number of environment variables.

<dl>

<dt>DISPLAY</dt>

<dd>to get the default host and display number.</dd>

<dt>GIMP2_DIRECTORY</dt>

<dd>to get the name of the personal GIMP directory. If unset .gimp-2.6 is used. If this is an absolute path, it is used as is. If it is a relative path, it is taken to be a subdirectory of the home directory.</dd>

<dt>GIMP2_DATADIR</dt>

<dd>to get the base location for data files such as brushes and patterns. If unset /usr/share/gimp/2.0 is used.</dd>

<dt>GIMP2_LOCALEDIR</dt>

<dd>to get the base location for translations. If unset /usr/share/locale is used.</dd>

<dt>GIMP2_PLUGINDIR</dt>

<dd>to get the base location for plug-ins and modules. If unset /usr/lib64/gimp/2.0 is used.</dd>

<dt>GIMP2_SYSCONFDIR</dt>

<dd>to get the location of configuration files. If unset /etc/gimp/2.0 is used.

On Linux GIMP can be compiled with support for binary relocatibility. This will cause data, plug-ins and configuration files to be searched relative to the location of the gimp executable file unless overridden by the environment variables mentioned above.

</dd>

</dl>

## [Files](#toc5)

GIMP’s data files are stored in /usr/share/gimp/2.0, where ${datarootdir} is set on install, but is typically /usr/share. GIMP’s system-wide configuration files are stored in /etc/gimp/2.0, where ${prefix} is typically /usr.

Most GIMP configuration is read in from the user’s init file, **$HOME**/.gimp-2.6/gimprc. The system wide equivalent is in /etc/gimprc. The system wide file is parsed first and the user gimprc can override the system settings. /etc/gimprc_user is the default gimprc placed in users’ home directories the first time GIMP is run.

**$HOME**/.gimp-2.6/devicerc - holds settings for input devices together with the tool, colors, brush, pattern and gradient associated to that device.

**$HOME**/.gimp-2.6/gtkrc - users set of GIMP-specific GTK+ config settings. Options such as widget color and fonts sizes can be set here.

/etc/gimp/2.0/gtkrc - sytem wide default set of GIMP-specific GTK+ config settings.

**$HOME**/.gimp-2.6/menurc - user’s set of keybindings.

**$HOME**/.gimp-2.6/parasiterc - Stores all persistent GIMP parasites. This file will be rewritten every time you quit GIMP.

**$HOME**/.gimp-2.6/sessionrc - This file takes session-specific info (that is info, you want to keep between two GIMP sessions). You are not supposed to edit it manually, but of course you can do. This file will be entirely rewritten every time you quit GIMP. If this file isn’t found, defaults are used.

**$HOME**/.gimp-2.6/templaterc - Image templates are kept in this file. New images can conveniently created from these templates. If this file isn’t found, defaults are used.

/etc/gimp/2.0/unitrc - default user unit database. It contains the unit definitions for centimeters, meters, feet, yards, typographic points and typographic picas and is placed in users home directories the first time GIMP is ran. If this file isn’t found, defaults are used.

**$HOME**/.gimp-2.6/unitrc - This file contains your user unit database. You can modify this list with the unit editor. You are not supposed to edit it manually, but of course you can do. This file will be entirely rewritten every time you quit GIMP.

**$HOME**/.gimp-2.6/plug-ins - location of user installed plug-ins.

**$HOME**/.gimp-2.6/pluginrc - plug-in initialization values are stored here. This file is parsed on startup and regenerated if need be.

**$HOME**/.gimp-2.6/modules - location of user installed modules.

**$HOME**/.gimp-2.6/tmp - default location that GIMP uses as temporary space.

/usr/share/gimp/2.0/brushes - system wide brush files.

**$HOME**/.gimp-2.6/brushes - user created and installed brush files. These files are in the .gbr, .gih or .vbr file formats.

**$HOME**/.gimp-2.6/curves - Curve profiles and presets as saved from the Curves tool.

**$HOME**/.gimp-2.6/gimpressionist - Presets and user created brushes and papers are stored here.

**$HOME**/.gimp-2.6/levels - Level profiles and presets as saved from the Levels tool.

/usr/share/gimp/2.0/palettes - the system wide palette files.

**$HOME**/.gimp-2.6/palettes - user created and modified palette files. This files are in the .gpl format.

/usr/share/gimp/2.0/patterns - basic set of patterns for use in GIMP.

**$HOME**/.gimp-2.6/patterns - user created and installed gimp pattern files. This files are in the .pat format.

/usr/share/gimp/2.0/gradients - standard system wide set of gradient files.

**$HOME**/.gimp-2.6/gradients - user created and installed gradient files.

/usr/share/gimp/2.0/scripts - system wide directory of scripts used in Script-Fu and other scripting extensions.

**$HOME**/.gimp-2.6/scripts - user created and installed scripts.

/usr/share/gimp/2.0/gflares - system wide directory used by the gflare plug-in.

**$HOME**/.gimp-2.6/gflares - user created and installed gflare files.

/usr/share/gimp/2.0/gfig - system wide directory used by the gfig plug-in.

**$HOME**/.gimp-2.6/gfig - user created and installed gfig files.

/usr/share/gimp/2.0/images/gimp-splash.png - the default image used for the GIMP splash screen.

/usr/share/gimp/2.0/images/gimp-logo.png - image used in the GIMP about dialog.

/usr/share/gimp/2.0/tips/gimp-tips.xml - tips as displayed in the "Tip of the Day" dialog box.

## [Splash Images](#toc6)

GIMP comes with a default image for the splash screen but it allows system administrators and users to customize the splash screen by providing other images. The image to be used with the splash screen is chosen as follows:


1. GIMP tries to load a random splash screen from the directory **$HOME**/.gimp-2.6/splashes.

2. It then falls back to using **$HOME**/.gimp-2.6/gimp-splash.png.

3. If the user didn’t install any custom splash images, a random image is picked from /usr/share/gimp/2.0/splashes.

4. As a last resort, GIMP uses the default splash image located at /usr/share/gimp/2.0/images/gimp-splash.png.

## [Suggestions and Bug Reports](#toc7)

Any bugs found should be reported to the online bug-tracking system available on the web at [http://bugzilla.gnome.org/.](http://bugzilla.gnome.org/.) Before reporting bugs, please check to see if the bug has already been reported.

When reporting GIMP bugs, it is important to include a reliable way to reproduce the bug, version number of GIMP (and probably GTK+), OS name and version, and any relevant hardware specs. If a bug is causing a crash, it is very useful if a stack trace can be provided. And of course, patches to rectify the bug are even better.

## [Other Info](#toc8)

The canonical place to find GIMP info is at [http://www.gimp.org/.](//www.gimp.org/.) Here you can find links to just about many other GIMP sites, tutorials, data sets, mailing list archives, and more.

There is also a GIMP User Manual available at [http://docs.gimp.org/](http://docs.gimp.org/) that goes into much more detail about the interactive use of GIMP.

The latest version of GIMP and the GTK+ libs is always available at http://download.gimp.org/.

## [Authors](#toc9)

Spencer Kimball, Peter Mattis and the GIMP Development Team.

With patches, fixes, plug-ins, extensions, scripts, translations, documentation and more from lots and lots of people all over the world.

## [See Also](#toc10)

[**gimprc**(5)](gimprc.html) , [**gimptool**(1)](gimptool.html) ,

* * *

<a name="toc">**Table of Contents**</a>

*   [Name](#sect0)
*   [Synopsis](#sect1)
*   [Description](#sect2)
*   [Options](#sect3)
*   [Environment](#sect4)
*   [Files](#sect5)
*   [Splash Images](#sect6)
*   [Suggestions and Bug Reports](#sect7)
*   [Other Info](#sect8)
*   [Authors](#sect9)
*   [See Also](#sect10)
