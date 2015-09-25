Title: Quickmask Tutorial
Date: 2002
Modified: 2015-09-25T13:33:27-05:00
Author: Zach Beane

<small>
Text and images Copyright (C) 2002 [Zach Beane](mailto:xachNOSPAM@gimp.org) and may not be used without permission of the author.
</small>

## Intention

<figure>
<img src="blur-15.jpg" alt="blur-15.jpg"/>
</figure>

This tutorial shows how you can do vignette effects using a feature of GIMP called QuickMask. QuickMask is a convenient way to modify selections using pixel-changing tools such as the paintbrush, eraser, or any plug-in filter. It lets you make very precise adjustments to your selections. This tutorial doesn't use QuickMask for complex masking; it's intended to show how you can use it to create quick and easy vignette effects.

## Step 1

<figure>
<img src="image.1.jpg" alt="image.1.jpg"/>
</figure>

For your first step, load up an image. Any image will do. GIMP 1.1.7, a development version of GIMP, introduced QuickMask. The QuickMask control button is located at the lower-left side of the image.

## Step 2

<figure>
<img src="image.2.jpg" alt="image.2.jpg"/>
</figure>

First, make a rectangular selection around the edge of the image. Then click on the red-bordered QuickMask icon in the lower-left corner of your image.

## Step 3

<figure>
<img src="image.3.jpg" alt="image.3.jpg"/>
</figure>

After you click the red QuickMask button, a translucent red mask appears around your selection. This red mask represents the outside of your selection. When you click the dashed QuickMask button to go back into normal selection mode, anything red will not be selected, and anything clear will be. So, let's start playing with this mask. First, right click on the image and select 

<div class="MenuCmd"><span>Filters &rarr; Distorts &rarr; Waves</span></div>

from the menu. Apply the filter, and watch what happens to the mask.

## Step 4

<figure>
<img src="image.4.jpg" alt="image.4.jpg"/>
</figure>

The mask gets all wavy. Let's add one more effect: `Filters → Blur → Gaussian Blur (RLE)`.

## Step 5

<figure>
<img src="image.5.jpg" alt="image.5.jpg"/>
</figure>

Now that there is a soft edge on the mask, click the dashed QuickMask button to convert the mask back into a selection.

## Step 6

<figure>
<img src="image.6.jpg" alt="image.6.jpg"/>
</figure>

See how the selection follows the mask? This is a powerful feature of QuickMask. You can use it to modify any existing selection, and you can even use it to create new selections. Our last step is to use `Select → Invert` and `Edit → Fill with BG Color`. The result, a soft white fade into the background, is shown in the final step.

## Final

<figure>
<img src="image.7.jpg" alt="image.7.jpg"/>
</figure>

And there you have it. Some more examples are listed below. Happy GIMPing!

## Examples

<figure>
<img src="spread-11.png" alt="spread-11.png"/>
</figure>

The above image used `Filters → Noise → Spread`, with horizontal and vertical settings at 11, to get the effect.

<figure>
<img src="newsprint.png" alt="newsprint.png"/>
</figure>

I used some blurring and the `Filters → Distorts → Newsprint` plugin to get this effect.

<figure>
<img src="pixelize-10.png" alt="pixelize-10.png"/>
</figure>

As in the tutorial, this one used Waves, but instead of blurring, I used `Filters → Blur → Pixelize` instead.

The original tutorial can be found [here](http://www.xach.com/gimp/tutorials/quickmask/).

