Title: GIMP Splash Archive
Date: 2015-08-13T13:34:55-05:00
Modified: 2016-05-30T23:35:01+00:00
Author: Pat David


The splash screens archives shows us some of the history behind GIMP and how it has developed through the years. As a gratitude to all people doing splash screens for GIMP, this page has been setup to show everyone the good art from people contributing.

## Splash Screen galleries (image archives)

*   [Stable GIMP Splash Screens](stable.html)
*   [GIMP 2.9 Development Splash Screens](unstable-2.9.html)
*   [GIMP 2.7 Development Splash Screens](unstable-2.7.html)
*   [GIMP 2.5 Development Splash Screens](unstable-2.5.html)
*   [GIMP 2.3 Development Splash Screens](unstable-2.3.html)
*   [GIMP 2.1 Development Splash Screens](unstable-2.1.html)
*   [GIMP 1.3 Development Splash Screens](unstable-1.3.html)
*   [GIMP 1.1 Development Splash Screens](unstable-1.1.html)

# Create your own splash screen

GIMP allows you to make your own splash screen and have that as startup splash instead of the one that comes with the archive. To do this you can simply follow the guidelines below.

*   Make the splash **300x200** or more. (Smaller splashs will make text being cut off)
*   Go to your personal GIMP directory. For UNIX users, this is usually in **/home/username/.gimp-2.6/**. For Windows, this is usually in **C:\Documents and Settings\username\.gimp-2.6\** (you may have to enable the option "Show Hidden Files" in your file browser).
*   Create a "splashes" directory if it does not exist.
*   Save your image in the "splashes" directory.

Restart GIMP and your splash screen should be the one being used by GIMP instead of the one from the archive. If you have more than one splash screen, then GIMP will pick one at random. More information is available in the [gimp manual page](/man/gimp.html).

If there are multiple users on your system and you want to make a single splash screen available for all of them, then you can save your image in **$PREFIX/gimp/2.0/images/gimp-splash.png**.

Note that older older GIMP versions (2.0.x) used **gimp_splash.png** instead of **gimp-splash.png** and did not look for them in your personal GIMP directory.
