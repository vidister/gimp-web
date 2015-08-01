Title: Gimp-Perl release candidate ready for testing
Date: 2014-06-12
Category: News
Authors: Wilber Gimp

It's been possible to use various scripting languages to automate GIMP for a long time. But until recently [Perl bindings for GIMP](https://git.gnome.org/browse/gimp-perl) were considerably out of date due to lack of interest from contributors. Fortunately, a while ago Ed J started working on updating those, and now a release candidate is available for testing.

[Gimp-Perl version 2.30_05](https://metacpan.org/release/ETJ/Gimp-2.30_05) is on CPAN now. It supports GIMP 2.8 and provides the following features:

*   An autosave script (not installed by default, `examples/autosave2`) will save in its own directory files that were opened and changed, then reopen them on GIMP startup; if installed, will start along with GIMP.
*   A plugin registry viewer, installed by default to `Filters/Browse Plug-in Registry`.
*   A Perl console, installed by default to `Filters/Perl/Console`.

The way to install the release candidate on Linux is:

`perl -MCPAN -e "install 'ETJ/Gimp-2.30_05.tar.gz'"`

If you encounter any bugs, please report them on [bugzilla.gnome.org](https://bugzilla.gnome.org/enter_bug.cgi?product=gimp-perl).
