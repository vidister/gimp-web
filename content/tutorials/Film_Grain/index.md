Title: Film Grain Tutorial
Date: 2002
Modified: 2015-09-23T12:05:07-05:00
Author: Eric Kidd

<small>Text and images Copyright (C) 2002 [Eric Kidd](mailto:eric.kiddNOSPAM@pobox.com) and may not be used without permission of the author.</small>

## Intention

Real-world images have lots of noise: film grain, scanner lines, CCD noise, paper texture, and just about anything else you can imagine. Computer-generated images, on the other hand, tend to be too real. If you need to make computer-generated images look like real-world ones, then this tutorial is for you.

## Why Would Anyone Want to Ruin Perfectly Good Images?

Perhaps you've rendered a gorgeous 3D scene, but want to make it look more like a photograph. Perhaps you're compositing two different photos, and need make the grain match. Or maybe you're just perverse.

## Extracting the Film Grain

This is a subject for another, longer tutorial. But here are the basic steps:

1.  Take a noisy image.
2.  Duplicate it into a new layer.
3.  Blur it to remove the noise.
4.  Set the blurred layer to **Grain Extract** mode to extract the noise.
5.  Flatten the image.
6.  Choose an interesting area of the noise, and make it into a tileable pattern.

![film-grain-vertical](film-grain-vertical.jpg)([GIMP pattern file](film-grain-vertical.pat))

Some good ways of making tileable patterns include **Make Seamless**, the [Resynthesizer and Homogenizer](http://www.logarithmic.net/pfh/resynthesizer/), mirroring, and hand-editing. You'll have to experiment a bit. In the following example, we'll use a weird, vertically-striped noise pattern. It looks like some kind of scanner noise, or perhaps an artifact of old newsprint.

## Ruining a Perfectly Good Image

<figure>
<img src="sailboat-01-original.jpg" alt="sailboat-01-original.jpg" />
<img src="sailboat-08-grain-masked-rebalanced.jpg" alt="sailboat-08-grain-masked-rebalanced.jpg" />
</figure> 

First, desaturate the image. You can do this using 

<div class="MenuCmd"><span>Image &rarr; Colors &rarr; Desaturate</span></div>

or the **Desaturate** filter provided with the MathMap plugin.(The latter actually returns the luminosity of an image, not a desaturated version. Technically, it's better, but it's unnecessary for most images.)

## Step 2

<figure>
<img src="sailboat-02-luminosity.jpg" alt="sailboat-02-luminosity.jpg" />
<img src="sailboat-03-grain.jpg" alt="sailboat-03-grain.jpg" />
</figure>

Next add a new layer to the image, and use the bucket to fill it with your tileable noise.

## Step 3

<figure>
<img src="sailboat-04-grain-added.jpg" alt="sailboat-04-grain-added.jpg" />
</figure>

Position the noise layer above the image layer, and set the mode to **Grain Merge**.

## Step 4

<figure>
<img src="sailboat-05-luminosity-blurred.jpg" alt="sailboat-05-luminosity-blurred.jpg" />
</figure>

So far, so good. But the noise is too strong in the shadows and highlights of the image. To demphasize it, we can use a layer mask.  
First, add a layer mask to the noise layer. Then, make a copy of the image, gaussian blur it with a radius of 15 pixels, and paste the blurred image into the layer mask. Use 

<div class="MenuCmd"><span class="filter">Image &rarr; Colors &rarr; Invert</span></div>

to swap bright for dark. This will cause the grain to show through strongly in the shadows and midtones, but not in the highlights.

## Step 5

<figure>
<img src="sailboat-08-grain-masked-rebalanced.jpg" alt="sailboat-08-grain-masked-rebalanced.jpg" />
</figure>

Next, use 

<div class="MenuCmd"><span class="filter">Image &rarr; Colors &rarr; Curves</span></div>

to adjust the value of the layer mask. We want to make the midtones bright, and the shadows and hightlights dark. You can adjust the curves to taste. Curves Dialog This increases the grain in the midtones, and reduces it elsewhere.  
Here's the **Layers, Channels & Paths** dialog for the finished image.

## Related Techniques

You can use various brushes in the mask layer to selectively edit the grain. You can also use the bucket tool in **Pattern Fill**, **Grain Merge** mode to fill a selection with grain directly.  
Many kinds of noise can be created using 

<div class="MenuCmd"><span class="filter">Filters &rarr; Noise &rarr; Scatter HSV</span></div>

You can apply this directly to an image, or to a film grain pattern.  
To denoise an image, try 

<div class="MenuCmd"><span class="filter">Filters &rarr; Blur &rarr; Selective Guassian Blur</span></div>

It's slow, but very nifty.
