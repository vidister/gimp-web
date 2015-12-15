Title: How to Create and Submit a Patch
Date: 2015-08-17T11:09:31-05:00
Modified: 2015-08-17T11:09:40-05:00
Authors: Pat David
Status: hidden


## Introduction

A patch is exactly what the word says: a small piece of code used to repair a breach. It is normally a plain text file containing only the differences between the current version of the code and the fixed version.

## Generating a Patch

### With git

The preferred way of creating a patch is to create it against current git. The ensures that the patches works with the latest edition of the source code and makes it easier for the developers to apply the patch.

Clone the git repository which is  

    git clone git://git.gnome.org/gimp

 Create commits that fixes the problem. For small problems it will only be a single commit. Be sure to provide your name and email in the commits - you can [set up your git repository](http://live.gnome.org/Git/Developers#head-2ad4a3239be27d5312d1be06debb39d4550baaf8) to do this for you. Please make sure to provide useful commit messages; you may refer to [GNOME's guidelines](http://live.gnome.org/Git/CommitMessages).

Now that you have commits that fixes the problem, create patches by doing  

    git format-patch origin/master

 This will give you patch files in the form of git commits with names like  

    0001-plug-ins-Use-string-literal-as-format-in-metadata-p.patch

 We prefer to have the patches attached to bug reports in Bugzilla (see below) but it is also fine to send them to the mailing list if they are reasonably small.

### Against the Latest Release

If you do not have access to git you can generate the patch against the latest release.

To generate the patch you will need two copies of the source code: one that is unmodified and one containing your changes to the source. Start by downloading the source code of the latest release, extract it and make a copy of the entire source directory. After you have made your changes to one of the source directories and made sure it compiles and works as expected, you can create the patch file using the command:  

`diff -rup /path/to/unmodified/source /path/to/modified/source > patchfile.patch`

To summarize the steps:

*   Download the source code of the latest release
*   Extract the source code
*   Make a copy of the source code directory
*   Apply your changes to the copy of the source code
*   Re-compile and make sure it works as expected
*   Do a `make clean` to remove files generated during build
*   Generate the patch file using  
    `diff -rup /path/to/unmodified/source /path/to/modified/source > patchfile.patch`
*   Examine the resulting .patch file to make sure it contains only the intended changes
*   Submit the patch using Bugzilla, see below

## Using Bugzilla

### Closing a bug patch

The best way to submit a patch to the GIMP development is to send it to Bugzilla and inform the rest of the team what the patch is doing:

*   Is it closing bugs?
*   Is it a enhancement?
*   What are the changes in the code?
*   Are there any know problems with the patch?

If you have a patch that is closing bugs then you can attach the patch to the bug/bugs explaining what the patch is doing. You can also inform the gimp-developer mailing list about the closed bug but avoid to attach the patch to the mail sent to the list, instead put the bug links in the mail where the attached patch is located.

1.  Test the patch locally on your own machine and look if it closes the bug there.
2.  Find the bug it is closing in the [Open bugs](https://bugzilla.gnome.org/buglist.cgi?product=GIMP&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED) list.
3.  Attach the patch to the bug report.
4.  Explain what the patch is doing and if there might be any problems with the patch.
5.  If you want to send a mail to the gimp-developer list and explain it there also. Remember to have the bug number or even better the link to the bug in the mail. Avoid attaching the patch to the mail.

Now you just have to wait for the developers and maintainers to look at the patch and see if this is really closing the bug and if it might open new bugs. If everything is fine it will be implemented in a release done soon either stable or development version.

#### How about enhancements?

Start a new bug report, mark it as enhancement and put the patch in that report on Bugzilla. This will give developers a good explanation of why you did the patch and how the patch changes GIMP source or adds new things to it. The only thing you need to add to the report is that it is an enhancement and explain the patch a little bit. A simple way to this is to:

1.  Go to [Submit a new bug report](https://bugzilla.gnome.org/enter_bug.cgi?product=GIMP).
2.  Start a new report and select _enhancement_ as a _Severity_ option.
3.  Attach the patch and explain what you wanted to get going with the help of this patch.
4.  Remember to explain the purpose of the patch and who might want to use this enhancement.

Thats it! You have done a patch reporting enhancement all that is left is for the developers to look at the report and the patch. They might get even better ideas of how to implement this with the help of the patch you sent.

### Remember to

*   use the same coding style, see file HACKING
*   avoid sending the patch as an attachment to the mailing lists.
*   explain what the patch is doing to GIMP.
*   report the bugs that the patch is closing.
*   always test the patch before submitting it.
*   write what version it is tested on. stable? development?

