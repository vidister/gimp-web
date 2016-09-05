Title: Making a Circle-Shaped Image
Date: 2016-09
Modified: 2016-09-04T20:54:21-05:00
Author: Ofnuts
Template: page_author

Making a circle-shaped image
============================

**Foreword:** There are no circular images. There are only rectangular images. 
But there can be images where corners are transparent, so that only a circle shows.

* First, make sure that your layer has an "alpha channel" (*Layer>Transparency>Add alpha channel*)(if it's grayed out, it means you already have one)
* Create a circular selection with the "Ellipse select tool (the 2nd one in the toolbox). 
Use the "Tool options" dialog (*Windows>Dockable dialogs>Tool options* (top of list)). 
    * If you want a true circle, use the *Fixed* option: select *Aspect ratio* and enter `1:1`. 
    * Depending on what kind of marks you have, you can use: 
        * The diagonal framing (default): click on one corner, drag across a full diagonal and release at the opposite corner, 
        * The radial framing (check *Expand from center* in the Tool options): click on the center, drag across a half diagonal release on a corner.
* If the selection isn't perfect on the first try, you can move it (click around the middle) or extend it (click inside, near a border or a corner).
* Once you have the required selection, invert the selection (*Select>Invert*, or Ctrl-I) so that everything is selected, except your circle
* Erase the selection (*Edit>Clear* or [Delete] key). You should have your central circle left, surrounded by a checkerboard pattern 
(this checkerboard is not part of the image, it just indicates the transparent parts of the image).
* You can reduce the checkerboard to the minimum by auto-cropping the image (*Image>Autocrop image*)
* Last, save the image in a format that supports transparency, like PNG (JPEG doesn't support transparent images...)
* If you are going to work further on the picture, save ist as XCF (Gimp native format).


<small>
<a href='http://creativecommons.org/licenses/by-sa/3.0/deed.en_US'>
<img class='cc-badge' src='http://i.creativecommons.org/l/by-sa/3.0/80x15.png' alt='Creative Commons By Share Alike'/>
</a>
<br/>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - Making a Circle-Shaped Image</span> by Ofnuts is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).</small>
