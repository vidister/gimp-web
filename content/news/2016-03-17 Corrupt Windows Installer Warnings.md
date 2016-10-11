Title: Corrupt Windows Installer Warnings
Date: 2016-03-17
Category: News
Authors: Michael Schumacher
Slug: corrupt-windows-installer-warnings
Summary: The Windows installer packages for GIMP 2.8.16 are reported as corrupt when downloaded with the Microsoft Edge or Internet Explorer 11 browsers. This is due to a policy by Microsoft.

For the past few weeks, we have been receiving reports that some users can't download our [installer packages](http://www.gimp.org/downloads/) for the Microsoft Windows platforms. Microsoft Edge and Internet Explorer 11 [mark them as corrupt](http://social.technet.microsoft.com/wiki/contents/articles/32288.windows-enforcement-of-authenticode-code-signing-and-timestamping.aspx#Signature_Verification_Failure_Experience) and discourage users from running them.

Turns out this is a policy change by Microsoft, gone into effect on January 1, 2016. The new policy affects all kinds of security certificates as of specific deadlines, and this includes code signing certificates. Jernej Simončič, who creates the Windows installer packages, signs them to make their authenticity verifiable. But the way this signature is done is no longer considered safe by Microsoft, and there are justified technical reasons for that.

Administrators and users of Microsoft Windows systems are well advised to make themselves familiar with the implications of this policy; the TechNet article on the subject is available at [Windows Enforcement of Authenticode Code Signing and Timestamping](http://social.technet.microsoft.com/wiki/contents/articles/32288.windows-enforcement-of-authenticode-code-signing-and-timestamping.aspx).

We are working to resolve the issue — this requires a more recent code-signing certificate and signing the installer packages with it. Stay tuned for updates.

As a temporary workaround, you can use other web browsers to download the installer packages.
