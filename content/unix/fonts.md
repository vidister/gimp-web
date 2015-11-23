Title: Fonts in GIMP 2.X
Date: 2015-08-17T16:18:41-05:00
Modified: 2015-08-17T16:18:45-05:00
Author: Pat David
Status: hidden


GIMP 2.x handles a variety of font formats, most notably TrueType, OpenType and Type1.

## Adding Fonts for GIMP 2.x

### System-Wide

Most distributions will propose a large choice of fonts in their package manager. The easier is usually to install them this way.

In case you want to manually add third-party fonts (commercial, downloaded...), adding fonts is usually just a matter of moving font files into a directory that is searched by the font system. Have a look at <tt>/etc/fonts/fonts.conf</tt> (and perhaps <tt>/etc/fonts/local.conf</tt>) to find out which directories are searched, or look for your operating system documentation. After copying the fonts there, you should run **fc-cache** to regenerate the fonts cache.

Some distributions also propose a graphical tool allowing to install fonts from third-party without bothering about the specifics.

Fonts added this way will be available to all applications using the Fontconfig system (such as GIMP).

### For GIMP only

You might want to install fonts for use with GIMP only or you might not have permissions to install fonts system-wide. For such cases, GIMP 2.x also looks for fonts in a GIMP specific font search path. The default place where GIMP will look for user fonts is <tt>~/.gimp-2.8/fonts/</tt> but you can change it or add other directories by modifying your <tt>gimprc</tt> or in _Edit -> Preferences -> Folders -> Fonts_. Then press the _Refresh_ button in the _Fonts_ dialog and start using your new fonts.

## Internal Mechanics

_This section is mostly informational, for users or developers who want to know more about under-the-hood font handling in GIMP 2.x. In nearly no case would you have to understand and know any of this in order to have font support in GIMP 2.x. See above for adding fonts simply._

Starting with GIMP version 2.0, font rendering is handled significantly differently from the way it was done in GIMP 1.0 and 1.2\. GIMP no longer uses the X server to render the fonts. Instead it uses [Pango](http://www.pango.org/) and the [FreeType](http://www.freetype.org/) library. Font configuration is handled by [Fontconfig](http://www.fontconfig.org/). As a result you get much better font rendering with real antialiasing, support for bidirectional text and various scripts.

Fontconfig can nowadays be considered a de-facto standard on Linux and other Unix operating systems as the simple way to list and share the same fonts accross all application. Most modern graphical programs with text support now uses this library. And desktop environments (GNOME or KDE for instance) use it too. Therefore it is likely already installed and properly set up out of the box in most Unix/Linux machines and you have probably nothing to do in particular to have fonts working in GIMP 2.x.

If you use a very raw operating system though, or if you simply want to know more, you may want to have a look at the [Fontconfig User Manual](http://www.fontconfig.org/fontconfig-user.html) to create or edit your font configuration file. Note though that since it is such a widespread system, modern desktops environments such as GNOME or KDE, or other distribution software, may overwrite your font configuration file. They sometimes provide an easier interface to manage your fonts instead. For this reason, you are advised to search the specific documentation of your operating system distribution before updating your font configuration.

## Known Problems

<dl>

<dt>GIMP crashes when scanning fonts</dt>

<dd>There have been reports of crashes at startup when GIMP scans your font directories. These crashes should go away as soon as you update to a newer version of fontconfig (>= 2.2.0). As a quick workaround you can start gimp with the <kbd>--no-fonts</kbd> command-line option but of course you will not be able to use the text tool then.</dd>

<dt>GIMP cannot see my X fonts</dt>

<dd>GIMP does not use the X server or any X font server, so don't be surprised if GIMP doesn't see the fonts you configured in your X11 setup. If you wish to add fonts, see the instructions above.</dd>

</dl>

