Title: EEK! A Bug!
Date: 2004
Modified: 2015-10-05T10:19:55-05:00
Author: Pat David


## or How To Report GIMP Bugs

If you find a bug or think you find a bug, it is very important to report it. If the developers don't know it is broken (or might be broken), they can't fix it. So there you are at your computer trying to do something with GIMP and it freaks out at you. It can be a frightening experience at times.

### First, Next, Third

First: Get out a piece of paper or open a text file and scribble down everything you can remember about what you were doing when it happened. Also write down the exact wording of any error messages you received.

Next: Go away and yell and scream and do whatever you need to do to relax again. Your next step will be to brave bugzilla, the GNOME bug tracker. It is used to track bug reports and requests for enhancements for GIMP and GTK+).

Third: Check to see if your bug has been reported yet. Go to the [Current Bug List](http://bugzilla.gnome.org/buglist.cgi?product=GIMP&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=NEEDINFO&form_name=query) to see if something that looks like your bug has been reported yet. Don't worry if it has, you can still help. See the section: [Enhancing Bug Reports](#enhance). If you can't find something that sounds like your bug there, you will need to report it.

## Getting Ready to Report and Reporting a Bug

The goal of the following is to give the developers as much information about what goes wrong as possible. This helps them find out what needs to be fixed.

### The Steps

1.  Use <kbd>gimp --version</kbd> or the about dialog to check your GIMP version. Next check with [www.gimp.org](http://www.gimp.org) to see what the most recent GIMP release is. If your GIMP is old, update then try to to reproduce the bug. Your bug may have been fixed in the most recent release. If you are running GIMP from CVS, update your CVS and recompile.

2.  Attempt to reproduce the problem. Go do what you were doing when it happened and see if you can do it again.

    If using GIMP for GNU/Linux, start the program from a terminal with the command <kbd>gimp</kbd>. Sometimes the program will output error messages that can help. This is especially important if GIMP crashes completely without warning. After reproducing the bug, copy the error messages from your terminal into somewhere where you can save them for the bug report. It is better to give too much information than not enough.

    To narrow down the exact cause of the problem, attempt to reproduce it in other ways. Prepare yourself to explain how to reproduce it in your bug report. If you are running GIMP in another language, try switching your GIMP to English so you can report menu items exactly with the English menu item name. It helps. (Developers generally understand English) If you cannot reproduce the bug, assume it was some weird freak event and don't report it. If it recurs, consult with your appropriate [user mailing list](/mail_lists.html). Perhaps someone else can find the key to reproducing it.

3.  Prepare to face the horror. Go to [bugzilla.gnome.org](https://bugzilla.gnome.org/). If you don't have a login yet, follow the directions to create one. The reason to do this and report a bug with your e-mail address is so the developers can contact you if they have any questions (see also [why we are using Bugzilla](/bugs/why_bugzilla.html)). That way if we miss some useful tidbit of debugging information, they can tell you what to do to get it. Log in.

4.  Select "Enter a New Bug Report". From the list of products provided, select GIMP. This opens the actual entry form.

5.  Here you have to tell the developers everything about your system, your version of GIMP, and your bug. Just do your best to tell them about it. A crappy bug report is better than no report at all, but if you write down everything you can clearly, you will create a decent bug report.

1.  Select the "version" that corresponds with the GIMP version in which you found the bug. It is the information you got with <kbd>gimp --version</kbd> or by looking in Help -> About.

2.  Select the appropriate "component". If you don't know what component it is, submit the bug under General. Descriptions of the components are [available](http://bugzilla.gnome.org/describecomponents.cgi?product=GIMP).

3.  Classify the "severity" of your bug. If the bug causes GIMP to crash totally or do other really ucky things so you can't use the program at all, classify it as critical. If it completely disables some part of GIMP, classify it as major (for example, keeps you from using a tool). Most bugs are "normal". If you don't know what severity to use, call it "normal". Trivial bugs are annoying but don't really keep you from using the program. Cosmetic bugs are things like spelling errors or UI (User Interface, "the look and feel") issues. If you are requesting a new feature, choose "enhancement". Don't worry if you choose the wrong severity. The people getting your bug report will adjust it. Don't mark it higher than it really is just to get their attention.

4.  Select your "operating system". Bugs in [GIMP for Windows](wgo:wingimp) and [GIMP for GNU/Linux](wgo:gimp-unix) are not always identical. It would be annoying to get a Linux GIMP developer trying to reproduce a Windows-specific bug. Do not select "All" for the operating system unless you have verified yourself that the bug affects more than one. The developers who will take care of your bug may change that later, once the bug is confirmed.

5.  Leave "Assigned to:" blank. Bugzilla will do that automatically. Only worry about CC: if you want to send a copy of your bug report to someone else.

6.  For "Summary", write a brief description of your bug. This summary will help other users see if their bug might be like your bug. Write something that would help you if you were looking for a bug like yours.

7.  "Description" is the hard part. It is the actual bug report. First provide the detailed description of your bug: a brief overview of when it happened and exactly what went wrong (including error messages). Next, describe step-by-step how to reproduce the bug. Use the exact name of menu items. Describe tools, windows, and clicks as precisely as possible. If they can't reproduce the bug, it will be very hard for them to fix it. Last, tell them anything else you can think of that might be relevant. This could include recently installed programs or hardware that might interfere with GIMP.

## Enhancing Bug Reports

If someone has already reported a bug like yours, read the bug report carefully. Read through all the additional comments. Make sure every bit of information you know about the bug is in there. If your version is different or you had a slightly different experience with the bug, add a comment providing your information. Check the status of the bug carefully. If it is marked "NEEDINFO", see if you can provide the information needed. Do not add a "me too" comment unless your comment provides additional information that might be helpful for the developer.

If you have provided a bug report and later get more information (like a more specific error message or fancy stuff like a trace), add a comment to your original bug with that information. It is especially important to add a comment if you somehow resolve your bug. For example, you update something else on your system and the bug no longer appears. In that case, add a comment describing what you updated from what version to what version that resolved the bug.

## The Wait Patiently Part

<cite>Whee!!</cite> You survived! If you managed to get through all this and submit your bug report, be happy. Be proud. You will later get e-mails about your bug. It might include a request for more information. If you get something that says your bug is not a bug, do not be discouraged from reporting in the future. Next time it might be. Submitting careful bug reports and providing additional information where possible helps make GIMP better. The day will come where you submit a bug and later get an e-mail that says your bug is "FIXED" or "RESOLVED". Then you will know that some developer out there found your bug, reproduced it, and fixed it.

