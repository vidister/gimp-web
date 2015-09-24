Title: Image Map Tutorial
Date: 2002
Modified: 2015-09-24T11:21:06-05:00
Author: Carol Spears

<small>Text and images Copyright (C) 2002 [Carol Spears](mailto:carolNOSPAM@gimp.org) and may not be used without permission of the author.</small>

## Intention

<figure>
<img src="imap-table1-1-0.png" alt="imap-table1-1-0.png"/> <img src="dialog-imagemap-t.png" alt="dialog-imagemap-t.png"/>
</figure>

In my opinion, it is hard to come up with a good application for an image map. For many online applications, it is simply overkill. However, to emulate the behavior of a GIMP Dialog seems to be a perfect place for this powerful web tool.

The image to the left comes from a previous tutorial about how to use [perlotine](/tutorials/Perlotine/). The tutorial slices this image further, but since the GIMP Image Map Plug-in and image maps in general use coordinates, we can use a less complicated table for this.

Above is a screenshot of the GIMP Image Map Plug-in, it has been scaled down for a nicer page. It can be somewhat scary at first. I tried to arrow and number the few areas I am worried about for this tutorial. So, relax.

## 1\. Goodies->Create Guides

<figure>
<img src="dialog-createguides.png" alt="dialog-createguides.png"/> <img src="imagemap1-zoom.png" alt="imagemap1-zoom.png"/>
</figure>

This is a screenshot of the Create Guides Dialog (left image). We get to change every single option before we are done. Whee!

I came to this tutorial prepared with a perfectly wonderful colorpicker script that I stole from [Victor S. Engel](http://the-light.com/colclick.html). The only problem with his colorpicker is that it didn't look like GIMP. :) If you "View Source" of that page, you can see that there is a similar line to each image map coordinate area. So, into the "Base URL" box, put the stuff that will be the same on each. I am going to deal with the colors (256 of them, eek!) after I make the image map. So, put **javascript:GetClick()" onmouseover="GetColor('** into the bottom box. The Image Map Plug-in will put the href=" into the html for you.

Once I started to write this tutorial, I discovered that the Image Map Plug-in has the ability to do the zooming and such. Too late, for me, I guess as I used GIMPs tools for measuring to determine the information for the rest of the Create Guides information. The original image was still open, so it was hard not to think about using it. Here is a screen shot of <span class="filter"><Image> View -> Zoom -> 4:1</span>

I used GIMP's nifty measure tool to determine that the rectangles are all 10 pixels tall and 14 pixels wide. The black lines in between are only one pixel wide also.

You can do the math or count the squares, but the Visibone2 palette has 16 colors across and 16 colors down. I used the mouse on guides to determine the start point of the first image map area. That is all of the configurable things in this dialog. Time to click "Apply".

## 2\. Map Image

<figure>
<img src="dialog-guides-image.png" alt="dialog-guides-image.png"/>
</figure>

Once you hit "Apply" the guides will draw themselves on the image map preview window. You can see if you hit the right places on your image. This tutorial certainly makes it look like I got it right the first time ;)

At this point, for this project, you can jump right to "4\. File Save"as it is totally done for our use.

## 3\. Table Editor

<figure>
<img src="dialog-guides-urlset.png" alt="dialog-guides-urlset.png"/>
</figure>

Since 256 elements is way to much to edit by hand, so I ended up using a different way to finish the information at each point. However, I played with the editor a bit. It was easy to use and figure out. Highlight the text in the pictured portion of the Image Map Dialog area by clicking on the area in the image preview. (shown above). Honestly, I don't have that much experience with html renderers, if you have the experience and would like to fill this portion of the tutorial in with something smart about editing your image map elements, feel free. I fully admit that I only used a small small part of this great plug-ins ability. 256 elements was out of the reach of my short attention span.

## 4\. File->Save As

I am not going to bore you with the directions to <span class="filter">File->Save As</span>. Instead, check out my product [here](imap1.html). It needs the colors placed at the end of the lines. This information is already found in the GIMP Palette directory, usually located at ~/.gimp-1.2/palettes/. This was the [Visibone2](Visibone2) palette. I posed this problem to my friend Bex and went to sleep. When I awoke, she had solved my dilemma by writing the [bextruder shell script](bextruder.sh.txt).

This puppy takes each line from [Visibone2.txt](Visibone2.txt), gets a color from the [Visibone2](Visibone2) in your home directory and puts it on the end of the line. Then plops a ')> on the end of that, producing a file called [visibone.html](visibone.html). This didn't work. bex did exactly what I told her to do and I had forgotten a ". The plop at the end should have been a ')">. It was easy enough to fix with any editors global replace thingie .... My "working chunk of html" is called [bexcolored.html](bexcolored.html). The script should be easy to edit to use any palette. That is why I brought up the missing".

<form action="get" markdown='1'>
If all goes well, clicking on [this little pop-up](javascript:popup('bexcolorpicker-tutpop.html', document.forms[0].bg)) containing this [htmlized html of an online colorpicker](bexcolorpicker-tuthtml.html) should put your color choice into this box here --><input name="bg" size="8" type="text" value="#">.
</form>
