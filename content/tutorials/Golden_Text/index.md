Title: Golden Text Tutorial
Date: 2002
Modified: 2015-09-24T11:21:06-05:00
Author: Simon Budig 

<small>Text and images Copyright (C) 2002 [Simon Budig](mailto:Simon.BudigNOSPAM@unix-ag.org) and may not be used without permission of the author.</small>

## Intention

<figure>
<img src="title.gif" alt="title.gif"/>
</figure>

Doesn't the title look really valuable? To reproduce this effect you need the incredible "Lighting"-Plugin, created by Tom Bech and Federico Mena Quintero. It is not in the standard gimp-1.0 distribution, you have to install it yourself. It can be found at <span class="filter"><Image> Filters -> Light Effects -> Lighting Effects</span>. This Plugin does a very good Bump-Mapping. Additionally it can map an enviroment-map to the image.

## Part I

<figure>
<img src="envmap_gold.jpg" alt="envmap_gold.jpg"/>
</figure>

The trick is to use a good enviroment-map. I created it with <span class="filter"><Image> Filters -> Render -> Solid Noise</span> (X/Y-Size: 2.8, Detail: 1, Tileable). It is important for a good effect to get different grays in the top right corner. Then I did a <span class="filter"><Image> Image -> Colors -> Auto-Stretch Contrast</span> and a <span class="filter"><Image> Filters -> Blur -> Gaussian Blur (IIR)</span> with a radius of 5 to get the full range of gray. Then select the "Golden"-Gradient in <span class="filter"><Image> Dialogs -> Gradient Editor...</span> and <span class="filter"><Image> Filters -> Colors -> Gradient Map</span> it to the image.

<figure>
<img src="bumpmap1.gif" alt="bumpmap1.gif"/>
</figure>

The next step is to create a bumpmap for the text. Open a new grayscale image in the desired size, fill it black and paint the white text on it. To get a smooth transition do a Gaussian Blur on it.

<figure>
<img src="lighting_gui.gif" alt="lighting_gui.gif"/>
</figure>

Then open a new RGB-Image with exactly the same size and start the Lighting-Plugin. Select the "Enviroment-map"- and "Bumpmap"-Toggles and select the images in the appropriate notebook-pages. I prefer a lower value in the "Maximum height" Bumpmap option. I think 0.02 is good in most cases.

<figure>
<img src="render1.gif" alt="render1.gif"/>
</figure>

This is the result after a click on **Apply**. There is room for Improvements. Since the Lighting-Plugin doesn't support antialiasing yet it is a good idea to render the image in the double size and scale it down for the final image. Some other neat tricks can be found in the next part.

## Part II

<figure>
<img src="curves1_small.gif" alt="curves1_small.gif"/> <img src="bumpmap1_small.gif" alt="bumpmap1_small.gif"/> <img src="render1_small.gif" alt="render1_small.gif"/>
</figure>

<figure>
<img src="curves2_small.gif" alt="curves2_small.gif"/> <img src="bumpmap2_small.gif" alt="bumpmap2_small.gif"/> <img src="render2_small.gif" alt="render2_small.gif"/>
</figure>

<figure>
<img src="curves3_small.gif" alt="curves3_small.gif"/> <img src="bumpmap3_small.gif" alt="bumpmap3_small.gif"/> <img src="render3_small.gif" alt="render3_small.gif"/>
</figure>

<figure>
<img src="curves4_small.gif" alt="curves4_small.gif"/> <img src="bumpmap4_small.gif" alt="bumpmap4_small.gif"/> <img src="render4_small.gif" alt="render4_small.gif"/>
</figure>

At the Bumpmap-Options you can select different between four different Curves for Bumpmapping. So you can select between a linear, spherical, logarithmic and a sinusoidial Bumpmap.

There is a much more flexible way to specify the surface of the Bumpmap. The Key is the <span class="filter"><Image> Image -> Colors -> Curves-Dialog.</span> Create the text and blur it with a wider radius. Then select the Curves-Dialog and modify the text-profile. A little Blur (Radius 2) makes the Bumpmap a little bit smoother. See the examples above.

Another possibility is the use of a different gradient.

## Part III

<figure>
<img src="curves3_small.gif" alt="curves3_small.gif"/> <img src="bumpmap3_small.gif" alt="bumpmap3_small.gif"/> <img src="render3a_small.gif" alt="render3a_small.gif"/>
</figure>

<figure>
<img src="curves4_small.gif" alt="curves4_small.gif"/> <img src="bumpmap4_small.gif" alt="bumpmap4_small.gif"/> <img src="render4a_small.gif" alt="render4a_small.gif"/>
</figure>

To get Chrome-like effects try to use different enviroment-maps. Look at these examples.

That's it :-)

The original tutorial can be found [here](http://www.home.unix-ag.org/simon/gimp/golden.html).
