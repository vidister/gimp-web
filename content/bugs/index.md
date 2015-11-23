Title: Bugs 
Date: 2015-08-17T11:09:31-05:00
Modified: 2015-08-17T11:09:40-05:00
Authors: Pat David
Status: hidden


Making good bug reports is a great way to help increase the software quality of GIMP. A good bug report is a bug report that provides unambigous step-by-step instructions on how to reproduce the bug, what result that is expected, and what the actual result it. Good bug reports makes it easy for the developers to reproduce and fix the bug.

Related to bug reports are enhancement requests. An enhancement request should never be filed without prior discussion on the gimp-developer [mailing list](/mail_lists.html). This is to make sure that the enhancement requests that are filed are well-specified and aligned with the overall goals the developers have for GIMP.

More information about Bugzilla, and bug hunting in general, can be found at [http://wiki.gimp.org/](http://wiki.gimp.org/). See also [why we are using Bugzilla](why_bugzilla.html) to handle bug reports. The rest of this page contains more detailed information regarding bug reports.

## Bug How Tos

Since correctly submitting a bug report requires you to use tools you may have not used previously, we have created two documents. The first helps you to learn Bugzilla, which is the bug system used by GIMP developers to track bug reports. If you are fixing a problem yourself, the second document shows you how to properly create and submit a patch.

*   [How To Bugzilla](/bugs/howtos/bugzilla.html)
*   [How To Create and Submit a Patch](/bugs/howtos/submit-patch.html)

## Bug Lists

Below are different links into Bugzilla which show you lists of open and closed bugs. You can also search manually, but these links are often more convienient. With the help of the lists below you should be able to see if the bug you have found has already been reported. If it has been reported, and you have additional information, please add a comment with the additional information!

### GIMP bugs

*   [List of open bugs (all)](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED)
*   [List of open bugs (all excluding enhancement requests)](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_severity=blocker&bug_severity=critical&bug_severity=major&bug_severity=normal&bug_severity=minor&bug_severity=trivial)

*   [List of bugs that are easy to fix](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=UNCONFIRMED&bug_status=NEEDINFO&keywords=gnome-love)

*   [List of closed bugs (The past week)](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&bug_status=RESOLVED&bug_status=CLOSED&changedin=7)
*   [List of fixed bugs since last release](https://bugzilla.gnome.org/buglist.cgi?chfieldto=Now;query_format=advanced;order=Importance;chfieldfrom=2013-11-28;bug_status=RESOLVED;resolution=FIXED;product=GIMP;classification=Other)

#### By severity

*   [List of open bugs (blocker and critical)](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_severity=blocker&bug_severity=critical)
*   [List of open bugs (major)](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_severity=major)
*   [List of open bugs (normal)](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_severity=normal)
*   [List of open bugs (minor and trivial)](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_severity=minor&bug_severity=trivial)
*   [List of open enhancement proposals](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=UNCONFIRMED&bug_status=NEEDINFO&bug_severity=enhancement)

#### By operating system

*   [List of open GIMP on Linux bugs](https://bugzilla.gnome.org/buglist.cgi?order=Importance;classification=Other;op_sys=Linux;query_format=advanced;bug_status=UNCONFIRMED;bug_status=NEW;bug_status=ASSIGNED;bug_status=REOPENED;bug_status=NEEDINFO;product=GIMP)
*   [List of open GIMP on OS X bugs](https://bugzilla.gnome.org/buglist.cgi?order=Importance&classification=Other&op_sys=Mac%20OS&query_format=advanced&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=NEEDINFO&product=GIMP)
*   [List of open GIMP on Windows bugs](https://bugzilla.gnome.org/buglist.cgi?order=Importance;classification=Other;op_sys=Windows;query_format=advanced;bug_status=UNCONFIRMED;bug_status=NEW;bug_status=ASSIGNED;bug_status=REOPENED;bug_status=NEEDINFO;product=GIMP)
*   [List of open GIMP bugs, failing on all platforms](https://bugzilla.gnome.org/buglist.cgi?order=Importance;classification=Other;op_sys=All;query_format=advanced;bug_status=UNCONFIRMED;bug_status=NEW;bug_status=ASSIGNED;bug_status=REOPENED;bug_status=NEEDINFO;product=GIMP)

*   [Submit a new GIMP bug report](https://bugzilla.gnome.org/enter_bug.cgi?product=GIMP)

### GIMP Help bugs

*   [List of open bugs (all)](https://bugzilla.gnome.org/buglist.cgi?product=GIMP-manual&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED)
*   [List of open bugs (all excluding enhancement requests)](https://bugzilla.gnome.org/buglist.cgi?product=GIMP-manual&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_severity=blocker&bug_severity=critical&bug_severity=major&bug_severity=normal&bug_severity=minor&bug_severity=trivial)

*   [List of bugs that are easy to fix](https://bugzilla.gnome.org/buglist.cgi?product=GIMP-manual&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=UNCONFIRMED&bug_status=NEEDINFO&keywords=gnome-love)

*   [List of closed bugs (The past week)](https://bugzilla.gnome.org/buglist.cgi?product=GIMP-manual&bug_status=RESOLVED&bug_status=CLOSED&changedin=7)
*   [List of fixed bugs since last release](https://bugzilla.gnome.org/buglist.cgi?chfieldto=Now;query_format=advanced;order=Importance;chfieldfrom=2013-11-28;bug_status=RESOLVED;resolution=FIXED;product=GIMP-manual;classification=Other)

*   [Submit a new GIMP Help bug report](https://bugzilla.gnome.org/enter_bug.cgi?product=GIMP-manual)

### GIMP Website bugs

*   [List of open bugs (all)](https://bugzilla.gnome.org/buglist.cgi?product=gimp-web&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED)
*   [List of open bugs (all excluding enhancement requests)](https://bugzilla.gnome.org/buglist.cgi?product=gimp-web&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_severity=blocker&bug_severity=critical&bug_severity=major&bug_severity=normal&bug_severity=minor&bug_severity=trivial)

*   [List of bugs that are easy to fix](https://bugzilla.gnome.org/buglist.cgi?product=gimp-web&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=UNCONFIRMED&bug_status=NEEDINFO&keywords=gnome-love)

*   [List of closed bugs (The past week)](https://bugzilla.gnome.org/buglist.cgi?product=gimp-web&bug_status=RESOLVED&bug_status=CLOSED&changedin=7)

*   [Submit a new GIMP Website bug report](https://bugzilla.gnome.org/enter_bug.cgi?product=gimp-web)

## Security bugs

Some bug reports may be related to security issues. For example, a file plug-in may be vulnerable to a buffer overflow allowing arbitrary code execution when loading an image. We believe that the best way to report these vulnerabilities is through Bugzilla, as described above. This will ensure that the bug is reviewed and handled quickly (if necessary, a developer may decide to hide a sensitive bug report from other users until it is fixed). But if you really do not want to use Bugzilla for security reports and you do not mind some extra delay, you can also contact a limited set of GIMP developers by mail @gimp.org, using the special alias "security". What will happen next is that a developer will review the issue and submit it in Bugzilla, usually as a hidden bug report only visible to developers. This will take a bit longer than if you directly submit the bug yourself, but we know that some people have a policy of not disclosing security vulnerabilities publicly, so we provide that address for their convenience.
