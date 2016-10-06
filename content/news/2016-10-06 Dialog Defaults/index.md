Title: Making settings persistent in GIMP
Date: 2016-10-06
Category: News
Authors: Alexandre Prokoudine
Slug: dialog-defaults
Summary: Until fairly recently GIMP didn't do a very good job of remembering all the kinds of customizations. Upcoming v2.10 has some major improvements in that department.

Until fairly recently GIMP didn't do a very good job of remembering all the kinds of customizations. If you applied a filter to an image and liked the combination of options that you used, there was no way you could save that combination for a later use. If you carefully chose selection stroking options, the next time you had to stroke a selection, you had to define settings all over again.

Upcoming v2.10 has some major improvements in that department.

<figure>
    <img src="{filename}gimp-2-9-5-filter-named-presets.jpg" alt="Adding a named preset for the Unsharp Mask filter in GIMP" width='975' height='442' />
</figure>

Early in the current development cycle we started porting existing GIMP filters to GEGL operations and using GEGL tool. This made it possible to automatically save each used combination as preset with a timestamp for a name, or manually&mdash;as a named preset. If you've been using v2.9.2 or v2.9.4, you most likely benefit from that already.

<figure>
    <img src="{filename}gimp-2-9-5-masks-in-xcf.jpg" alt="Using masks for digital photrography in GIMP" width='975' height='596' />
</figure>

The second part of improvements started with reviewing a [patch](https://bugzilla.gnome.org/show_bug.cgi?id=759601) submitted by Benoit Touchette. The contributor came up with a clever idea to simplify adding new masks: clicking on layers' previews. Various modifier keys would additionally define whether you apply and remove the mask or just drop the mask entirely.

<figure>
    <img src="{filename}gimp-2-9-5-easy-mask-create-tooltip.jpg" alt="Tooltips for handling masks quickly in GIMP" width='975' height='536' />
</figure>

The difficult part was to come up with a way to remember the last used mask initiation setting not just within one session, but across sessions. So instead of creating a special case for just the _Add Layer Mask_ dialog, Michael Natterer added a whole new infrastructure to automatically save and load settings of dialogs.

All the dialog defaults are stored in the _gimprc_ configuration file. To give you idea, these is how stroking options are saved in _gimprc_:

	(stroke-options
    	(style solid)
	    (antialias yes)
	    (method line)
	    (width 6.000000)
	    (unit pixels)
	    (cap-style butt)
	    (join-style miter)
	    (miter-limit 10.000000)
	    (dash-offset 0.000000)
	    (dash-info 0)
	    (emulate-brush-dynamics no))

The options are preserved for dialogs like _New File_, _New Channel_, _Feather Selection_, _Stroke Path_ and others. To give you visual control over the settings, Michael created a new page in the _Preferences_ dialog called _Dialog Defaults_.

<figure>
    <img src="{filename}gimp-2-9-5-prefs-dialog-defaults.png" alt="Dialog Defaults preferences page in GIMP 2.9.5" width='805' height='638' />
</figure>

You may have noticed a few more new things about the _Preferences_ dialog. There is now a scrollbar on large pages, to make the dialog fit small screens like the still popular 1366x768 on lower-end laptops. Additionally, some pages now feature a reset button that restores default settings.

The dialog defaults feature will be available in GIMP 2.9.6 and, eventually, in GIMP 2.10.

The introduction of filter presets and dialog defaults gets us closer to resolving [#63610](https://bugzilla.gnome.org/show_bug.cgi?id=63610), [#120829](https://bugzilla.gnome.org/show_bug.cgi?id=120829), and [#599573](https://bugzilla.gnome.org/show_bug.cgi?id=599573), filed in 2001, 2003, and 2009 respectively. If you think that more dialogs could benefit from either saving their settings as defaults or getting named presets, please drop by on [IRC](https://www.gimp.org/irc.html) or the [mailing list](https://www.gimp.org/mail_lists.html) for developers and tell us.

If you are interested in helping out with getting GIMP 2.10 released, please check out the [TODO](http://wiki.gimp.org/wiki/Hacking:TODO#2.10) page.