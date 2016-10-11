Title: GIMP 2.3 Release Notes
Date: 2015-08-17T14:15:58-05:00
Modified: 2015-08-17T14:16:03-05:00
Authors: Pat David
Status: hidden


# GIMP 2.3 Release Notes

This is an unstable development version of the **GNU Image Manipulation Program**. Please realize that this is just a snapshot of the development tree. We are about halfway up the hill to GIMP 2.4, the next stable release. GIMP 2.3 is in no way a final product. A lot of new features are incomplete and some things may even be completely broken. If you need to get work done, please use the stable version, GIMP 2.2.

## What's New in GIMP 2.3

Please see the [NEWS](https://git.gnome.org/browse/gimp/plain/NEWS?h=gimp-2-4&id=GIMP_2_3_0) file for a list of changes. [Screenshots](http://developer.gimp.org/screenshots.html) of the development version can also be found there.

## Download

The development snapshots of GIMP can be downloaded as source code from ftp.gimp.org or from one of the mirrors listed in the [Downloads](/downloads/#mirrors) section.

Distribution of binary packages of the development version is discouraged unless it is made clear that this is an early development snapshot. Users should be referred to these release notes or similar information.

## Installation

GIMP 2.3 must **not** be installed in the same prefix as other GIMP 2.x versions. If you want to keep your GIMP 2.2 or GIMP 2.0 installation in parallel to GIMP 2.3, you have to choose a separate installation prefix at compile-time and ensure that you use different library search paths for each version. If you do not set up your environment differently for each version, you will experience conflicts with the libraries and at least one version is likely to fail.

You install the new version into a separate prefix, say /opt/gimp-2.3 by passing `--prefix=/opt/gimp-2.3` to the configure script. Then, in order to run the binary installed there, you change your environment to look for executables in /opt/gimp-2.3/bin by setting `PATH=/opt/gimp-2.3/bin` and you tell your linker to pick up libraries from /opt/gimp-2.3/lib by setting `LD_LIBRARY_PATH=/opt/gimp-2.3/lib`. Do not forget to `export` both variables.

You can use a tiny wrapper script called gimp-2.3 and place it into /usr/local/bin or elsewhere in your PATH. The script would look something like this:

    #!/bin/sh

    PATH=/opt/gimp-2.3/bin:$PATH
    export PATH
    LD_LIBRARY_PATH=/opt/gimp-2.3/lib
    export LD_LIBRARY_PATH

    /opt/gimp-2.3/bin/gimp-2.3 "$@"

## Bugs

If you think you found a bug in a development version, please make sure that it hasn't been reported earlier. Search [Bugzilla](http://bugzilla.gnome.org/) before filing a new bug-report. Here are some interesting Bugzilla queries:

*   [Open bugs with milestone 2.4](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&target_milestone=2.4&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED)
*   [Resolved bugs with milestone 2.4](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&target_milestone=2.4&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED)

## Contributing

We need your help to make GIMP 2.4 a success. There's still a lot to do in all areas. If you want to join us hacking, show up in #gimp or introduce yourself on the gimp-developer mailing-list. We are also looking for people to look after the web-site and update the tutorials. Or you might want to join the [documentation team](http://docs.gimp.org/).

