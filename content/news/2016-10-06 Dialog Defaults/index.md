Title: Dialog Defaults
Date: 2016-10-06
Category: News
Authors: Alexandre Prokoudine
Slug: dialog-defaults
Summary: FIXME

Until fairly recently GIMP didn't do a very good job of remembering all the settings. If you applied a filter to an image and liked the combination of options that you used, there was no way you could save that combination for a later use. If you carefully chose selection stroking options, the next time you had to stroke a selection, you had to define settings all over again.

Upcoming v2.10 has some major improvements in that department.

Early in the current development cycle we started porting existing GIMP filters to GEGL operations and using GEGL tool. This made it possible to . If you've been using v2.9.2 or v2.9.4, you most likely benefit from that already.

The second part of improvements started with reviewing a patch submitted by Benoit Touchette. The contributor came up with a clever idea to simplify adding new masks: clicking on layers' previews. Various modifier keys would additionally define whether you apply and remove the mask or just drop the mask entirely.

[patdavid screenshot]

The difficult part was to come up with a way to remember the last used mask initiation setting not just within one session, but across sessions. So instead of creating a special case for just the _Add Layer Mask_ dialog, Michael Natterer

A lot of the new code lives in app/config/gimpdialogconfig.c/h files, and settings are all stored in the _gimprc_ configuration file.

dialogs like New File, New Channel, Feather Selection, Stroke Path and others.

This also closed bugs [https://bugzilla.gnome.org/show_bug.cgi?id=63610](#63610), [https://bugzilla.gnome.org/show_bug.cgi?id=120829](#120829), and [https://bugzilla.gnome.org/show_bug.cgi?id=599573](#599573), filed in 2001, 2003, and 2009 respectively. We always get there, eventually :)

