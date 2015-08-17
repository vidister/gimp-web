Title: gimptool Man Page
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

gimptool-2.0 - script to perform various GIMPy functions

## [Synopsis](#toc1)

<span style="font-family: monospace;" markdown="1">
**gimptool&#8209;2.0** [&#8209;&#8209;prefix_[=DIR]_] [&#8209;&#8209;exec&#8209;prefix_[=DIR]_] [&#8209;&#8209;version] [&#8209;&#8209;help] [&#8209;&#8209;quiet] [&#8209;&#8209;silent] [&#8209;n] [&#8209;&#8209;just&#8209;print] [&#8209;&#8209;dry&#8209;run] [&#8209;&#8209;recon] [&#8209;&#8209;msvc&#8209;syntax] [&#8209;&#8209;bindir] [&#8209;&#8209;sbindir] [&#8209;&#8209;libexecdir] [&#8209;&#8209;datadir] [&#8209;&#8209;sysconfdir] [&#8209;&#8209;sharedstatedir] [&#8209;&#8209;localstatedir] [&#8209;&#8209;libdir] [&#8209;&#8209;infodir] [&#8209;&#8209;mandir] [&#8209;&#8209;includedir] [&#8209;&#8209;gimpplugindir] [&#8209;&#8209;gimpdatadir] [&#8209;&#8209;libs] [&#8209;&#8209;libs&#8209;noui] [&#8209;&#8209;cflags] [&#8209;&#8209;cflags&#8209;noi] [&#8209;&#8209;build&nbsp;_plug&#8209;in.c_] [&#8209;&#8209;build&#8209;strip&nbsp;_plug&#8209;in.c_] [&#8209;&#8209;install&nbsp;_plug&#8209;in.c_] [&#8209;&#8209;install&#8209;strip&nbsp;_plug&#8209;in.c_] [&#8209;&#8209;install&#8209;admin&nbsp;_plug&#8209;in.c_] [&#8209;&#8209;install&#8209;bin&nbsp;_plug&#8209;in_] [&#8209;&#8209;install&#8209;admin&#8209;strip&nbsp;_plug&#8209;in.c_] [&#8209;&#8209;install&#8209;bin&#8209;strip&nbsp;_plug&#8209;in_] [&#8209;&#8209;install&#8209;admin&#8209;bin&nbsp;_plug&#8209;in_] [&#8209;&#8209;install&#8209;script&nbsp;_script.scm_] [&#8209;&#8209;install&#8209;admin&#8209;script&nbsp;_script.scm_] [&#8209;&#8209;uninstall&#8209;bin&nbsp;_plug&#8209;in_] [&#8209;&#8209;uninstall&#8209;admin&#8209;bin&nbsp;_plug&#8209;in_] [&#8209;&#8209;uninstall&#8209;script&nbsp;_script.scm_] [&#8209;&#8209;uninstall&#8209;admin&#8209;script&nbsp;_script.scm_]
</span>

## [Description](#toc2)

<em>gimptool-2.0</em> is a tool that can, among other things, build plug-ins or scripts and install them if they are distributed in one source file.

<em>gimptool-2.0</em> can also be used by programs that need to know what libraries and include-paths <em>GIMP</em> was compiled with. <em>gimptool-2.0</em> uses _pkg-config_ for this task. For use in Makefiles, it is recommended that you use _pkg-config_ directly instead of calling <em>gimptool-2.0</em>.

## [Options](#toc3)

<em>gimptool-2.0</em> accepts the following options:

<dl>

<dt>--version</dt>

<dd>Print the currently installed version of <em>GIMP</em> on the standard output.</dd>

<dt>--help</dt>

<dd>Print out the help blurb, showing commonly used commandline options.</dd>

<dt>--quiet</dt>

<dd>Run quietly without echoing any of the build commands.</dd>

<dt>--silent</dt>

<dd>Run silently without echoing any of the build commands. Same as --quiet.</dd>

<dt>-n</dt>

<dd>Test mode. Print the commands but don’t actually execute them. Useful for making dry runs for testing.</dd>

<dt>--just-print</dt>

<dd>Test mode. Print the commands but don’t actually execute them. Same as -n.</dd>

<dt>--dry-run</dt>

<dd>Test mode. Print the commands but don’t actually execute them. Same as -n.</dd>

<dt>--recon</dt>

<dd>Test mode. Print the commands but don’t actually execute them. Same as -n.</dd>

<dt>--msvc-syntax</dt>

<dd>Useful on Windows. Outputs the compiler and linker flags in the syntax used by Microsoft’s toolchain. Passed to the pkg-config command that does most of <em>gimptool-2.0</em>’s work.</dd>

<dt>--bindir</dt>

<dd>Outputs the bindir used to install the <em>GIMP</em>.</dd>

<dt>--sbindir</dt>

<dd>Outputs the sbindir used to install the <em>GIMP</em>.</dd>

<dt>--libexecdir</dt>

<dd>Outputs the libexecdir used to install the <em>GIMP</em>.</dd>

<dt>--datadir</dt>

<dd>Outputs the datadir used to install the <em>GIMP</em>.</dd>

<dt>--sysconfdir</dt>

<dd>Outputs the sysconfdir used to install the <em>GIMP</em>.</dd>

<dt>--sharedstatedir</dt>

<dd>Outputs the sharedstatedir used to install the <em>GIMP</em>.</dd>

<dt>--localstatedir</dt>

<dd>Outputs the localstatedir used to install the <em>GIMP</em>.</dd>

<dt>--libdir</dt>

<dd>Outputs the libdir used to install the <em>GIMP</em>.</dd>

<dt>--infodir</dt>

<dd>Outputs the infodir used to install the <em>GIMP</em>.</dd>

<dt>--mandir</dt>

<dd>Outputs the mandir used to install the <em>GIMP</em>.</dd>

<dt>--includedir</dt>

<dd>Outputs the includedir used to install the <em>GIMP</em>.</dd>

<dt>--gimpdatadir</dt>

<dd>Outputs the actual directory where the <em>GIMP</em> data files were installed.</dd>

<dt>--gimpplugindir</dt>

<dd>Outputs the actual directory where the <em>GIMP</em> plug-ins were installed.</dd>

<dt>--build <em>plug-in.c</em></dt>

<dd>Compile and link <em>plug-in.c</em> into a <em>GIMP</em> plug-in.</dd>

<dt>--build-strip <em>plug-in.c</em></dt>

<dd>Compile,link, and strip <em>plug-in.c</em> into a <em>GIMP</em> plug-in.</dd>

<dt>--install <em>plug-in.c</em></dt>

<dd>Compile, link, and install <em>plug-in.c</em> into the user’s personal <em>GIMP</em> plug-in directory (<strong>$HOME</strong>/.gimp-2.6/plug-ins)</dd>

<dt>--install-strip <em>plug-in.c</em></dt>

<dd>Compile, link,strip, and install <em>plug-in.c</em> into the user’s personal <em>GIMP</em> plug-in directory (<strong>$HOME</strong>/.gimp-2.6/plug-ins)</dd>

<dt>--install-admin <em>plug-in.c</em></dt>

<dd>Compile, link, and install <em>plug-in.c</em> into the system-wide <em>GIMP</em> plug-in directory (/usr/lib64/gimp/2.0/plug-ins)</dd>

<dt>--install-bin <em>plug-in</em></dt>

<dd>Install <em>plug-in</em> into the user’s personal <em>GIMP</em> plug-in directory (<strong>$HOME</strong>/.gimp-2.6/plug-ins)</dd>

<dt>--install-admin-bin <em>plug-in</em></dt>

<dd>Install <em>plug-in</em> into the system-wide <em>GIMP</em> plug-in directory (/usr/lib64/gimp/2.0/plug-ins)</dd>

<dt>--install-bin-strip <em>plug-in</em></dt>

<dd>Install stripped <em>plug-in</em> into the user’s personal <em>GIMP</em> plug-in directory (<strong>$HOME</strong>/.gimp-2.6/plug-ins)</dd>

<dt>--install-admin-bin-strip <em>plug-in</em></dt>

<dd>Install stripped <em>plug-in</em> into the system-wide <em>GIMP</em> plug-in directory (/usr/lib64/gimp/2.0/plug-ins)</dd>

<dt>--install-script <em>script.scm</em></dt>

<dd>Install <em>script.scm</em> into the user’s personal <em>GIMP</em> script directory (<strong>$HOME</strong>/.gimp-2.6/scripts)</dd>

<dt>--install-admin-script <em>script.scm</em></dt>

<dd>Install <em>script.scm</em> into the system-wide <em>GIMP</em> script directory (/usr/share/gimp/2.0/scripts)</dd>

<dt>--uninstall-bin <em>plug-in</em></dt>

<dd>Uninstall <em>plug-in</em> from the user’s personal <em>GIMP</em> plug-in directory (<strong>$HOME</strong>/.gimp-2.6/plug-ins)</dd>

<dt>--uninstall-admin-bin <em>plug-in</em></dt>

<dd>Uninstall <em>plug-in</em> from the system-wide <em>GIMP</em> plug-in directory (/usr/lib64/gimp/2.0/plug-ins)</dd>

<dt>--uninstall-script <em>script.scm</em></dt>

<dd>Uninstall <em>script.scm</em> from the user’s personal <em>GIMP</em> script directory (<strong>$HOME</strong>/.gimp-2.6/scripts)</dd>

<dt>--uninstall-admin-script <em>script.scm</em></dt>

<dd>Uninstall <em>script.scm</em> from the system-wide <em>GIMP</em> script directory (/usr/share/gimp/2.0/scripts)</dd>

<dt>--libs</dt>

<dd>Print the linker flags that are necessary to link a <em>GIMP</em> plug-in.</dd>

<dt>--libs-noui</dt>

<dd>Print the linker flags that are necessary to link a <em>GIMP</em> plug-in, for plug-ins that do not require the GTK+ libraries.</dd>

<dt>--cflags</dt>

<dd>Print the compiler flags that are necessary to compile a <em>GIMP</em> plug-in.</dd>

<dt>--clags-noui</dt>

<dd>Print the compiler flags that are necessary to compile a <em>GIMP</em> plug-in for plug-ins that do not require the GTK+ libraries.</dd>

<dt>--prefix=PREFIX</dt>

<dd>If specified, use PREFIX instead of the installation prefix that <em>GIMP</em> was built with when computing the output for the --cflags and --libs options. This option is also used for the exec prefix if --exec-prefix was not specified. This option must be specified before any --libs or --cflags options.</dd>

<dt>--exec-prefix=PREFIX</dt>

<dd>If specified, use PREFIX instead of the installation exec prefix that <em>GIMP</em> was built with when computing the output for the --cflags and --libs options. This option must be specified before any --libs or --cflags options.</dd>

</dl>

## [Environment](#toc4)

<dl>

<dt>CC</dt>

<dd>to get the name of the desired C compiler.</dd>

<dt>CFLAGS</dt>

<dd>to get the preferred flags to pass to the C compiler for plug-in building.</dd>

<dt>DESTDIR</dt>

<dd>to add a prefix to the install/uninstall path.</dd>

<dt>LDFLAGS</dt>

<dd>to get the preferred flags for passing to the linker.</dd>

<dt>LIBS</dt>

<dd>for passing extra libs that may be needed in the build process. For example, LIBS=-lintl .</dd>

<dt>PKG_CONFIG</dt>

<dd>to get the location of the <em>pkg-config</em> program that is used to determine details about your glib, pango, gtk+ and gimp installation.</dd>

</dl>

## [See Also](#toc5)

[**gimp**(1)](gimp.html) , [**gimprc**(5)](gimprc.html) , [**pkg-config**(1)](pkg-config.html)

## [Authors](#toc6)

gimptool was written by Manish Singh (yosh@gimp.org) and is based on gtk-config by Owen Taylor (owen@gtk.org).

This man page was written by Ben Gertzfield (che@debian.org), and tweaked by Manish Singh (yosh@gimp.org), Adrian Likins (adrian@gimp.org) and Marc Lehmann (pcg@goof.com>).

* * *

<a name="toc">Table of Contents</a>

*   [Name](#sect0)
*   [Synopsis](#sect1)
*   [Description](#sect2)
*   [Options](#sect3)
*   [Environment](#sect4)
*   [See Also](#sect5)
*   [Authors](#sect6)
