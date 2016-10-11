Title: GIMP 2.3.3 Simplifies the Extraction of Foreground Objects
Date: 2015-08-17T14:15:58-05:00
Modified: 2015-08-17T14:16:03-05:00
Authors: Pat David
Status: hidden


The new development release 2.3.3 of the free image manipulation software GIMP now contains a preliminary version of a new selection tool called SIOX. Until now, creating a selection mask for an object was mostly equivalent to either a slow step-by-step approximation to a certain shape or a tedious manual drawing of the selection. SIOX ("Simple Interactive Object eXtraction") allows a semi-automatic pixel-accurate selection of typical foreground objects like portraits of humans, animals, or plants with only a few mouse clicks. The user only encloses the object with a rough outline and uses a foreground brush to mark representative foreground regions. GIMP then answers with the extraction of the object. The selection can be refined by incrementally adding further foreground brush strokes or by subtracting regions with background brush strokes. SIOX is being developed at the Center for Digital Media at the computer science department at Freie Universitaet Berlin and roots from video processing applications.

GIMP Version 2.3.3 represents the current state of development. There are still features missing that are planned for the stable 2.4 release. Some work has already been done on the color management that had been announced for the 2.4 release. Using the preferences dialog a color profile for the screen can already be specified that GIMP 2.3 uses to correct the display. In the final release of GIMP 2.4, pictures containing embedded color profiles will also be handled.

Work is also being done on the user interface: The script-fu menu does not exist any more because most of the scripts have been integrated into the filter menu. There will be further changes - some of them have already been discussed in the Bugtracker. In addition to the SIOX tool there are several other new tools: A new rectangle selection tool allows to change the rectangle even after selecting. The alignment of layers is simplified by another tool.

There were also some changes behind the scenes: Users of G4 processors will enjoy the speed improvement that results from supporting the Altivec instruction set. GIMP also reacted to the trend of using Hyperthreading and Dualcore CPUs. In order to utilize multiple processors at a time several internal functions were parallelized.

A detailed list of all changes since GIMP 2.2 is available [here](https://git.gnome.org/browse/gimp/plain/NEWS?id=GIMP_2_3_3). It will take a little more time until the GIMP developers will present the next stable release. Those who do not want to wait are free to try GIMP 2.3.3\. For those who yearn for a faster release: Help is always welcome! Not only programmers are needed but also web designers, documentation authors and translators are desperately needed.

[GIMP Homepage](http://www.gimp.org)  
[GIMP User Manual](http://docs.gimp.org)  
[SIOX Algorithm](http://www.siox.org)

