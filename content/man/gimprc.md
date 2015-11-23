Title: gimprc Man Page
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

gimprc - gimp configuration file

## [Description](#toc1)

The **gimprc** file is a configuration file read by GIMP when it starts up. There are two of these: one system-wide one stored in /etc/gimp/2.0/gimprc and a per-user **$HOME**/.gimp-2.6/gimprc which may override system settings.

Comments are introduced by a hash sign (#), and continue until the end of the line. Blank lines are ignored.

The **gimprc** file associates values with properties. These properties may be set by lisp-like assignments of the form:

<dl>

<dt><em><strong>(property-name value)</strong></em></dt>

<dt>where:</dt>

<dt><em>property-name</em></dt>

<dd>is one of the property names described below.</dd>

<dt><em>value</em></dt>

<dd>is the value the property is to be set to.</dd>

</dl>

Either spaces or tabs may be used to separate the name from the value.

## [Properties](#toc2)

Valid properties and their default values are:

<dl>

<dt>(temp-path "${gimp_dir}/tmp")</dt>

<dd>

Sets the folder for temporary storage. Files will appear here during the course of running GIMP. Most files will disappear when GIMP exits, but some files are likely to remain, so it is best if this folder not be one that is shared by other users. This is a single folder.

</dd>

<dt>(swap-path "${gimp_dir}")</dt>

<dd>

Sets the swap file location. GIMP uses a tile based memory allocation scheme. The swap file is used to quickly and easily swap tiles out to disk and back in. Be aware that the swap file can easily get very large if GIMP is used with large images. Also, things can get horribly slow if the swap file is created on a folder that is mounted over NFS. For these reasons, it may be desirable to put your swap file in "/tmp". This is a single folder.

</dd>

<dt>(num-processors 1)</dt>

<dd>

Sets how many processors GIMP should try to use simultaneously. This is an integer value.

</dd>

<dt>(tile-cache-size 1024M)</dt>

<dd>

When the amount of pixel data exceeds this limit, GIMP will start to swap tiles to disk. This is a lot slower but it makes it possible to work on images that wouldn’t fit into memory otherwise. If you have a lot of RAM, you may want to set this to a higher value. The integer size can contain a suffix of ’B’, ’K’, ’M’ or ’G’ which makes GIMP interpret the size as being specified in bytes, kilobytes, megabytes or gigabytes. If no suffix is specified the size defaults to being specified in kilobytes.

</dd>

<dt>(interpolation-type cubic)</dt>

<dd>

Sets the level of interpolation used for scaling and other transformations. Possible values are none, linear, cubic and lanczos.

</dd>

<dt>(plug-in-path "${gimp_dir}/plug-ins:${gimp_plug_in_dir}/plug-ins")</dt>

<dd>

Sets the plug-in search path. This is a colon-separated list of folders to search.

</dd>

<dt>(module-path "${gimp_dir}/modules:${gimp_plug_in_dir}/modules")</dt>

<dd>

Sets the module search path. This is a colon-separated list of folders to search.

</dd>

<dt>(interpreter-path "${gimp_dir}/interpreters:${gimp_plug_in_dir}/interpreters")</dt>

<dd>

Sets the interpreter search path. This is a colon-separated list of folders to search.

</dd>

<dt>(environ-path "${gimp_dir}/environ:${gimp_plug_in_dir}/environ")</dt>

<dd>

Sets the environ search path. This is a colon-separated list of folders to search.

</dd>

<dt>(brush-path "${gimp_dir}/brushes:${gimp_data_dir}/brushes")</dt>

<dd>

Sets the brush search path. This is a colon-separated list of folders to search.

</dd>

<dt>(brush-path-writable "${gimp_dir}/brushes")</dt>

<dd>

This is a colon-separated list of folders to search.  

</dd>

<dt>(pattern-path "${gimp_dir}/patterns:${gimp_data_dir}/patterns")</dt>

<dd>

Sets the pattern search path. This is a colon-separated list of folders to search.

</dd>

<dt>(pattern-path-writable "${gimp_dir}/patterns")</dt>

<dd>

This is a colon-separated list of folders to search.  

</dd>

<dt>(palette-path "${gimp_dir}/palettes:${gimp_data_dir}/palettes")</dt>

<dd>

Sets the palette search path. This is a colon-separated list of folders to search.

</dd>

<dt>(palette-path-writable "${gimp_dir}/palettes")</dt>

<dd>

This is a colon-separated list of folders to search.  

</dd>

<dt>(gradient-path "${gimp_dir}/gradients:${gimp_data_dir}/gradients")</dt>

<dd>

Sets the gradient search path. This is a colon-separated list of folders to search.

</dd>

<dt>(gradient-path-writable "${gimp_dir}/gradients")</dt>

<dd>

This is a colon-separated list of folders to search.  

</dd>

<dt>(font-path "${gimp_dir}/fonts:${gimp_data_dir}/fonts")</dt>

<dd>

Where to look for fonts in addition to the system-wide installed fonts. This is a colon-separated list of folders to search.

</dd>

<dt>(default-brush "Circle (11)")</dt>

<dd>

Specify a default brush. The brush is searched for in the specified brush path. This is a string value.

</dd>

<dt>(default-pattern "Pine")</dt>

<dd>

Specify a default pattern. This is a string value.

</dd>

<dt>(default-palette "Default")</dt>

<dd>

Specify a default palette. This is a string value.

</dd>

<dt>(default-gradient "FG to BG (RGB)")</dt>

<dd>

Specify a default gradient. This is a string value.

</dd>

<dt>(default-font "Sans")</dt>

<dd>

Specify a default font. This is a string value.

</dd>

<dt>(global-brush yes)</dt>

<dd>

When enabled, the selected brush will be used for all tools. Possible values are yes and no.

</dd>

<dt>(global-pattern yes)</dt>

<dd>

When enabled, the selected pattern will be used for all tools. Possible values are yes and no.

</dd>

<dt>(global-palette yes)</dt>

<dd>

When enabled, the selected palette will be used for all tools. Possible values are yes and no.

</dd>

<dt>(global-gradient yes)</dt>

<dd>

When enabled, the selected gradient will be used for all tools. Possible values are yes and no.

</dd>

<dt>(global-font yes)</dt>

<dd>

When enabled, the selected font will be used for all tools. Possible values are yes and no.

</dd>

<dt>(default-image</dt>

<dd>
<pre style="font-size: 0.85rem;">
    (width 640)  
    (height 400)  
    (unit pixels)  
    (xresolution 72.000000)  
    (yresolution 72.000000)  
    (resolution-unit inches)  
    (image-type rgb)  
    (fill-type background-fill)  
    (comment "Created with GIMP"))  
</pre>

Sets the default image in the "File/New" dialog. This is a parameter list.

</dd>

<dt>(default-grid</dt>

<dd><pre style="font-size: 0.85rem;">
(style solid)  
 (fgcolor (color-rgba 0.000000 0.000000 0.000000 1.000000))  
 (bgcolor (color-rgba 1.000000 1.000000 1.000000 1.000000))  
 (xspacing 10.000000)  
 (yspacing 10.000000)  
 (spacing-unit inches)  
 (xoffset 0.000000)  
 (yoffset 0.000000)  
 (offset-unit inches))  
</pre>

Specify a default image grid. This is a parameter list.

</dd>

<dt>(undo-levels 5)</dt>

<dd>

Sets the minimal number of operations that can be undone. More undo levels are kept available until the undo-size limit is reached. This is an integer value.

</dd>

<dt>(undo-size 64M)</dt>

<dd>

Sets an upper limit to the memory that is used per image to keep operations on the undo stack. Regardless of this setting, at least as many undo-levels as configured can be undone. The integer size can contain a suffix of ’B’, ’K’, ’M’ or ’G’ which makes GIMP interpret the size as being specified in bytes, kilobytes, megabytes or gigabytes. If no suffix is specified the size defaults to being specified in kilobytes.

</dd>

<dt>(undo-preview-size large)</dt>

<dd>

Sets the size of the previews in the Undo History. Possible values are tiny, extra-small, small, medium, large, extra-large, huge, enormous and gigantic.

</dd>

<dt>(plug-in-history-size 10)</dt>

<dd>

How many recently used plug-ins to keep on the Filters menu. This is an integer value.

</dd>

<dt>(pluginrc-path "${gimp_dir}/pluginrc")</dt>

<dd>

Sets the pluginrc search path. This is a single filename.

</dd>

<dt>(layer-previews yes)</dt>

<dd>

Sets whether GIMP should create previews of layers and channels. Previews in the layers and channels dialog are nice to have but they can slow things down when working with large images. Possible values are yes and no.

</dd>

<dt>(layer-preview-size medium)</dt>

<dd>

Sets the preview size used for layers and channel previews in newly created dialogs. Possible values are tiny, extra-small, small, medium, large, extra-large, huge, enormous and gigantic.

</dd>

<dt>(thumbnail-size normal)</dt>

<dd>

Sets the size of the thumbnail shown in the Open dialog. Possible values are none, normal and large.

</dd>

<dt>(thumbnail-filesize-limit 4M)</dt>

<dd>

The thumbnail in the Open dialog will be automatically updated if the file being previewed is smaller than the size set here. The integer size can contain a suffix of ’B’, ’K’, ’M’ or ’G’ which makes GIMP interpret the size as being specified in bytes, kilobytes, megabytes or gigabytes. If no suffix is specified the size defaults to being specified in kilobytes.

</dd>

<dt>(install-colormap no)</dt>

<dd>

Install a private colormap; might be useful on 8-bit (256 colors) displays. Possible values are yes and no.

</dd>

<dt>(min-colors 144)</dt>

<dd>

Generally only a concern for 8-bit displays, this sets the minimum number of system colors allocated for GIMP. This is an integer value.

</dd>

<dt>(color-management</dt>

<dd><pre style="font-size:0.85rem;">
(mode display)  
 (display-profile-from-gdk no)  
 (display-rendering-intent perceptual)  
 (simulation-rendering-intent perceptual)  
 (simulation-gamut-check no)  
 (out-of-gamut-color (color-rgb 0.501961 0.501961 0.501961))  
 (display-module "CdisplayLcms"))  
</pre>

Defines the color management behavior. This is a parameter list.

</dd>

<dt>(color-profile-policy ask)</dt>

<dd>

How to handle embedded color profiles when opening a file. Possible values are ask, keep and convert.

</dd>

<dt>(save-document-history yes)</dt>

<dd>

Keep a permanent record of all opened and saved files in the Recent Documents list. Possible values are yes and no.

</dd>

<dt>(transparency-size medium-checks)</dt>

<dd>

Sets the size of the checkerboard used to display transparency. Possible values are small-checks, medium-checks and large-checks.

</dd>

<dt>(transparency-type gray-checks)</dt>

<dd>

Sets the manner in which transparency is displayed in images. Possible values are light-checks, gray-checks, dark-checks, white-only, gray-only and black-only.

</dd>

<dt>(snap-distance 8)</dt>

<dd>

This is the distance in pixels where Guide and Grid snapping activates. This is an integer value.

</dd>

<dt>(marching-ants-speed 200)</dt>

<dd>

Speed of marching ants in the selection outline. This value is in milliseconds (less time indicates faster marching). This is an integer value.

</dd>

<dt>(resize-windows-on-zoom no)</dt>

<dd>

When enabled, the image window will automatically resize itself when zooming into and out of images. Possible values are yes and no.

</dd>

<dt>(resize-windows-on-resize no)</dt>

<dd>

When enabled, the image window will automatically resize itself whenever the physical image size changes. Possible values are yes and no.

</dd>

<dt>(default-dot-for-dot yes)</dt>

<dd>

When enabled, this will ensure that each pixel of an image gets mapped to a pixel on the screen. Possible values are yes and no.

</dd>

<dt>(initial-zoom-to-fit yes)</dt>

<dd>

When enabled, this will ensure that the full image is visible after a file is opened, otherwise it will be displayed with a scale of 1:1\. Possible values are yes and no.

</dd>

<dt>(perfect-mouse yes)</dt>

<dd>

When enabled, the X server is queried for the mouse’s current position on each motion event, rather than relying on the position hint. This means painting with large brushes should be more accurate, but it may be slower. Perversely, on some X servers enabling this option results in faster painting. Possible values are yes and no.

</dd>

<dt>(cursor-mode tool-icon)</dt>

<dd>

Sets the type of mouse pointers to use. Possible values are tool-icon, tool-crosshair and crosshair.

</dd>

<dt>(cursor-updating yes)</dt>

<dd>

Context-dependent mouse pointers are helpful. They are enabled by default. However, they require overhead that you may want to do without. Possible values are yes and no.

</dd>

<dt>(show-brush-outline yes)</dt>

<dd>

When enabled, all paint tools will show a preview of the current brush’s outline. Possible values are yes and no.

</dd>

<dt>(show-paint-tool-cursor yes)</dt>

<dd>

When enabled, the mouse pointer will be shown over the image while using a paint tool. Possible values are yes and no.

</dd>

<dt>(image-title-format "%D&#42;%f-%p.%i (%t, %L) %wx%h")</dt>

<dd>

Sets the text to appear in image window titles. This is a format string; certain % character sequences are recognised and expanded as follows:  

<pre style="font-size: 0.85rem;">
    %% literal percent sign   
    %f bare filename, or "Untitled"   
    %F full path to file, or "Untitled"   
    %p PDB image id   
    %i view instance number   
    %t image type (RGB, grayscale, indexed)   
    %z zoom factor as a percentage   
    %s source scale factor   
    %d destination scale factor   
    %Dx expands to x if the image is dirty, the empty string otherwise   
    %Cx expands to x if the image is clean, the empty string otherwise   
    %B expands to (modified) if the image is dirty, the empty string otherwise   
    %A expands to (clean) if the image is clean, the empty string otherwise   
    %l the number of layers   
    %L the number of layers (long form)   
    %m memory used by the image   
    %n the name of the active layer/channel   
    %P the PDB id of the active layer/channel   
    %w image width in pixels   
    %W image width in real-world units   
    %h image height in pixels   
    %H image height in real-world units   
    %u unit symbol   
    %U unit abbreviation  

</pre>
</dd>

<dt>(image-status-format "%n (%m)")</dt>

<dd>

Sets the text to appear in image window status bars. This is a format string; certain % character sequences are recognised and expanded as follows:  

<pre style="font-size:0.85rem;">
%% literal percent sign   
%f bare filename, or "Untitled"   
%F full path to file, or "Untitled"   
%p PDB image id   
%i view instance number   
%t image type (RGB, grayscale, indexed)   
%z zoom factor as a percentage   
%s source scale factor   
%d destination scale factor   
%Dx expands to x if the image is dirty, the empty string otherwise   
%Cx expands to x if the image is clean, the empty string otherwise   
%B expands to (modified) if the image is dirty, the empty string otherwise   
%A expands to (clean) if the image is clean, the empty string otherwise   
%l the number of layers   
%L the number of layers (long form)   
%m memory used by the image   
%n the name of the active layer/channel   
%P the PDB id of the active layer/channel   
%w image width in pixels   
%W image width in real-world units   
%h image height in pixels   
%H image height in real-world units   
%u unit symbol   
%U unit abbreviation  
</pre>

</dd>

<dt>(confirm-on-close yes)</dt>

<dd>

Ask for confirmation before closing an image without saving. Possible values are yes and no.

</dd>

<dt>(monitor-xresolution 96.000000)</dt>

<dd>

Sets the monitor’s horizontal resolution, in dots per inch. If set to 0, forces the X server to be queried for both horizontal and vertical resolution information. This is a float value.

</dd>

<dt>(monitor-yresolution 96.000000)</dt>

<dd>

Sets the monitor’s vertical resolution, in dots per inch. If set to 0, forces the X server to be queried for both horizontal and vertical resolution information. This is a float value.

</dd>

<dt>(monitor-resolution-from-windowing-system yes)</dt>

<dd>

When enabled, GIMP will use the monitor resolution from the windowing system. Possible values are yes and no.

</dd>

<dt>(navigation-preview-size medium)</dt>

<dd>

Sets the size of the navigation preview available in the lower right corner of the image window. Possible values are tiny, extra-small, small, medium, large, extra-large, huge, enormous and gigantic.

</dd>

<dt>(default-view</dt>

<dd>
<pre style="font-size: 0.85rem;">
(show-menubar yes)  
 (show-rulers yes)  
 (show-scrollbars yes)  
 (show-statusbar yes)  
 (show-selection yes)  
 (show-layer-boundary yes)  
 (show-guides yes)  
 (show-grid no)  
 (show-sample-points yes)  
 (padding-mode default)  
 (padding-color (color-rgb 1.000000 1.000000 1.000000)))  
</pre>

Sets the default settings for the image view. This is a parameter list.

</dd>

<dt>(default-fullscreen-view</dt>

<dd>
<pre style="font-size: 0.85rem;">>
(show-menubar yes)  
 (show-rulers yes)  
 (show-scrollbars yes)  
 (show-statusbar yes)  
 (show-selection yes)  
 (show-layer-boundary yes)  
 (show-guides yes)  
 (show-grid no)  
 (show-sample-points yes)  
 (padding-mode default)  
 (padding-color (color-rgb 1.000000 1.000000 1.000000)))  
</pre>

Sets the default settings used when an image is viewed in fullscreen mode. This is a parameter list.

</dd>

<dt>(activate-on-focus yes)</dt>

<dd>

When enabled, an image will become the active image when its image window receives the focus. This is useful for window managers using "click to focus". Possible values are yes and no.  

</dd>

<dt>(space-bar-action pan)</dt>

<dd>

What to do when the space bar is pressed in the image window. Possible values are none, pan and move.

</dd>

<dt>(xor-color (color-rgb 0.501961 1.000000 0.501961))</dt>

<dd>

Sets the color that is used for XOR drawing. This setting only exists as a workaround for buggy display drivers. If lines on the canvas are not correctly undrawn, try to set this to white. The color is specified in the form (color-rgb red green blue) with channel values as floats in the range of 0.0 to 1.0\.

</dd>

<dt>(zoom-quality high)</dt>

<dd>

There’s a tradeoff between speed and quality of the zoomed-out display. Possible values are low and high.

</dd>

<dt>(default-threshold 15)</dt>

<dd>

Tools such as fuzzy-select and bucket fill find regions based on a seed-fill algorithm. The seed fill starts at the initially selected pixel and progresses in all directions until the difference of pixel intensity from the original is greater than a specified threshold. This value represents the default threshold. This is an integer value.

</dd>

<dt>(move-tool-changes-active no)</dt>

<dd>

If enabled, the move tool sets the edited layer or path as active. This used to be the default behaviour in older versions. Possible values are yes and no.

</dd>

<dt>(trust-dirty-flag yes)</dt>

<dd>

When enabled, GIMP will not save an image if it has not been changed since it was opened. Possible values are yes and no.

</dd>

<dt>(save-device-status no)</dt>

<dd>

Remember the current tool, pattern, color, and brush across GIMP sessions. Possible values are yes and no.

</dd>

<dt>(save-session-info yes)</dt>

<dd>

Save the positions and sizes of the main dialogs when GIMP exits. Possible values are yes and no.

</dd>

<dt>(restore-session yes)</dt>

<dd>

Let GIMP try to restore your last saved session on each startup. Possible values are yes and no.

</dd>

<dt>(save-tool-options no)</dt>

<dd>

Save the tool options when GIMP exits. Possible values are yes and no.

</dd>

<dt>(show-tooltips yes)</dt>

<dd>

Show a tooltip when the pointer hovers over an item. Possible values are yes and no.

</dd>

<dt>(tearoff-menus yes)</dt>

<dd>

When enabled, menus can be torn off. Possible values are yes and no.

</dd>

<dt>(can-change-accels no)</dt>

<dd>

When enabled, you can change keyboard shortcuts for menu items by hitting a key combination while the menu item is highlighted. Possible values are yes and no.

</dd>

<dt>(save-accels yes)</dt>

<dd>

Save changed keyboard shortcuts when GIMP exits. Possible values are yes and no.

</dd>

<dt>(restore-accels yes)</dt>

<dd>

Restore saved keyboard shortcuts on each GIMP startup. Possible values are yes and no.

</dd>

<dt>(menu-mnemonics yes)</dt>

<dd>

When enabled, GIMP will show mnemonics in menus. Possible values are yes and no.

</dd>

<dt>(last-opened-size 10)</dt>

<dd>

How many recently opened image filenames to keep on the File menu. This is an integer value.

</dd>

<dt>(max-new-image-size 128M)</dt>

<dd>

GIMP will warn the user if an attempt is made to create an image that would take more memory than the size specified here. The integer size can contain a suffix of ’B’, ’K’, ’M’ or ’G’ which makes GIMP interpret the size as being specified in bytes, kilobytes, megabytes or gigabytes. If no suffix is specified the size defaults to being specified in kilobytes.

</dd>

<dt>(toolbox-color-area yes)</dt>

<dd>

Show the current foreground and background colors in the toolbox. Possible values are yes and no.

</dd>

<dt>(toolbox-foo-area no)</dt>

<dd>

Show the currently selected brush, pattern and gradient in the toolbox. Possible values are yes and no.

</dd>

<dt>(toolbox-image-area no)</dt>

<dd>

Show the currently active image in the toolbox. Possible values are yes and no.

</dd>

<dt>(toolbox-wilber yes)</dt>

<dd>

Show the GIMP mascot at the top of the toolbox. Possible values are yes and no.

</dd>

<dt>(theme-path "${gimp_dir}/themes:${gimp_data_dir}/themes")</dt>

<dd>

Sets the theme search path. This is a colon-separated list of folders to search.

</dd>

<dt>(theme "Default")</dt>

<dd>

The name of the theme to use. This is a string value.

</dd>

<dt>(use-help yes)</dt>

<dd>

When enabled, pressing F1 will open the help browser. Possible values are yes and no.

</dd>

<dt>(show-help-button yes)</dt>

<dd>

When enabled, dialogs will show a help button that gives access to the related help page. Without this button, the help page can still be reached by pressing F1\. Possible values are yes and no.

</dd>

<dt>(help-locales "")</dt>

<dd>

Specifies the language preferences used by the help system. This is a colon-separated list of language identifiers with decreasing priority. If empty, the language is taken from the user’s locale setting. This is a string value.

</dd>

<dt>(help-browser gimp)</dt>

<dd>

Sets the browser used by the help system. Possible values are gimp and web-browser.

</dd>

<dt>(web-browser "firefox %s")</dt>

<dd>

Sets the external web browser to be used. This can be an absolute path or the name of an executable to search for in the user’s PATH. If the command contains ’%s’ it will be replaced with the URL, else the URL will be appended to the command with a space separating the two. This is a single filename.

</dd>

<dt>(user-manual-online no)</dt>

<dd>

When enabled, the online user manual will be used by the help system. Otherwise the locally installed copy is used. Possible values are yes and no.

</dd>

<dt>(user-manual-online-uri "http://docs.gimp.org/2.6")</dt>

<dd>

The location of the online user manual. This is used if ’user-manual-online’ is enabled. This is a string value.

</dd>

<dt>(toolbox-window-hint utility)</dt>

<dd>

The window type hint that is set on the toolbox. This may affect how your window manager decorates and handles the toolbox window. Possible values are normal, utility and keep-above.

</dd>

<dt>(dock-window-hint utility)</dt>

<dd>

The window type hint that is set on dock windows. This may affect the way your window manager decorates and handles dock windows. Possible values are normal, utility and keep-above.

</dd>

<dt>(transient-docks no)</dt>

<dd>

When enabled, dock windows (the toolbox and palettes) are set to be transient to the active image window. Most window managers will keep the dock windows above the image window then, but it may also have other effects. Possible values are yes and no.

</dd>

<dt>(cursor-format pixbuf)</dt>

<dd>

Sets the pixel format to use for mouse pointers. Possible values are bitmap and pixbuf.

</dd>

<dt>(fractalexplorer-path "${gimp_dir}/fractalexplorer:${gimp_data_dir}/fractalexplorer")</dt>

<dd>

Where to search for fractals used by the Fractal Explorer plug-in. This is a colon-separated list of folders to search.

</dd>

<dt>(gfig-path "${gimp_dir}/gfig:${gimp_data_dir}/gfig")</dt>

<dd>

Where to search for Gfig figures used by the Gfig plug-in. This is a colon-separated list of folders to search.

</dd>

<dt>(gflare-path "${gimp_dir}/gflare:${gimp_data_dir}/gflare")</dt>

<dd>

Where to search for gflares used by the GFlare plug-in. This is a colon-separated list of folders to search.

</dd>

<dt>(gimpressionist-path "${gimp_dir}/gimpressionist:${gimp_data_dir}/gimpressionist")</dt>

<dd>

Where to search for data used by the Gimpressionist plug-in. This is a colon-separated list of folders to search.

</dd>

<dt>(script-fu-path "${gimp_dir}/scripts:${gimp_data_dir}/scripts")</dt>

<dd>

This path will be searched for scripts when the Script-Fu plug-in is run. This is a colon-separated list of folders to search.

</dd>

</dl>

## [Path Expansion](#toc3)

Strings of type PATH are expanded in a manner similar to [**bash**(1)](bash.html) . Specifically: tilde (~) is expanded to the user’s home directory. Note that the bash feature of being able to refer to other user’s home directories by writing ~userid/ is not valid in this file.

${variable} is expanded to the current value of an environment variable. There are a few variables that are pre-defined:

<dl>

<dt><em>gimp_dir</em></dt>

<dd>The personal gimp directory which is set to the value of the environment variable GIMP2_DIRECTORY or to ~/.gimp-2.6\.</dd>

<dt><em>gimp_data_dir</em></dt>

<dd>Base for paths to shareable data, which is set to the value of the environment variable GIMP2_DATADIR or to the compiled-in default value /usr/share/gimp/2.0\.</dd>

<dt><em>gimp_plug_in_dir</em></dt>

<dd>Base to paths for architecture-specific plugins and modules, which is set to the value of the environment variable GIMP2_PLUGINDIR or to the compiled-in default value /usr/lib64/gimp/2.0\.</dd>

<dt><em>gimp_sysconf_dir</em></dt>

<dd>Path to configuration files, which is set to the value of the environment variable GIMP2_SYSCONFDIR or to the compiled-in default value /etc/gimp/2.0\.</dd>

</dl>

## [Files](#toc4)

<dl>

<dt><em>/etc/gimp/2.0/gimprc</em></dt>

<dd>System-wide configuration file</dd>

<dt><em><strong>$HOME</strong>/.gimp-2.6/gimprc</em></dt>

<dd>Per-user configuration file

</dd>

</dl>

## [See Also](#toc5)

[**gimp**(1)](gimp.html) , [**gimptool**(1)](gimptool.html) , [**gimp-remote**(1)](gimp-remote.html)

* * *

<a name="toc">**Table of Contents**</a>

*   [Name](#sect0)
*   [Description](#sect1)
*   [Properties](#sect2)
*   [Path Expansion](#sect3)
*   [Files](#sect4)
*   [See Also](#sect5)
