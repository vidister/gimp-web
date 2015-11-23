Title: Anti-Aliased Threshold Tutorial
Date: 2015-08-17T16:49:18-05:00
Modified: 2015-08-17T16:49:23-05:00
Author: Ville Pätsi 


<small>
Text and images Copyright (C) 2002 [Ville Pätsi](mailto:drcNOSPAM@gimp.org) and may not be used without permission of the author.
</small>

## Intention

The threshold plug-in works by dividing the image into two parts, dark and light, producing a 2 color image. This is often not the desired result, for some images anti-aliasing is needed, but the threshold plug-in cannot provide that. With a little utilization of the curves plug-in, we get nice results.

## Problems with the threshold

<figure>
<img src="{filename}original.jpg" alt="Antialiased Threshold Tutorial" />
<img src="{filename}threshold.jpg" alt="Antialiased Threshold Tutorial" />
</figure>


On the left you we see the original image that is about to be thresholded, and on the right side we see the result. The default settings for the Threshold plug-in were used (<span class="filter"><Image> Layers -> Colors -> Threshold</span>). The resulting image is very blocky and aliased.

## The Curves Trick

<figure>
<img src="{filename}curves.png" alt="Antialiased Threshold Tutorial" />
<img src="{filename}finished.jpg" alt="Antialiased Threshold Tutorial" />
</figure>

First duplicate the image layer by going to the layers dialog, making sure the image layer is selected, and clicking the duplicate button (fourth from the left). We can use the original layer for some color tricks later. Now the next thing is to desaturate the image (<span class="filter"><Image> Layers -> Colors -> Desaturate</span>). This way the colors will not interfere with the fake thresholding. When the layer is grayscale, select the curves editor (<span class="filter"><Image> Layers -> Colors -> Curves</span>). Now we can play with the Value "channel". The image on the left displays the settings used for the example image. The space between the two dots determines how much aa the resulting image will have. The wider the gap, the more grayscale values it will have, and vice versa. The resulting image can be seen on the right.

## A neat addition

<figure>
<img src="{filename}effect.jpg" alt="Antialiased Threshold Tutorial" />
</figure>

If you now take the original image layer, move it over the new one (make sure it has an alpha channel), and change its mode to "Color" in the layers dialog, you get nice results displayed above.

The original tutorial can be found [here](http://drc.gimp.org/).

<small>
Text and images Copyright (C) 2002 [Ville Pätsi](mailto:drcNOSPAM@gimp.org) and may not be used without permission of the author.
</small>
