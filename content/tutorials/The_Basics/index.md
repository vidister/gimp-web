Title: The Basics Tutorial
Date: 2002
Modified: 2015-10-05T10:19:55-05:00
Author: Jens Lautenbacher


Text and images Copyright (C) 2002 [Jens Lautenbacher](mailto:jtlNOSPAM@gimp.org) and may not be used without permission of the author.

## Intention

On this page, the first section of our ever growing (?) collection of tutorials, I will demonstrate the basic operation you will need to perform over and over again in your life as a computer artist: Generate isolated parts of a picture and combine them with a random background. What we want to achieve in this example is to generate a 3-dimensional text logo flying (and movable) over the background (a simple uni-color layer in our case, but you will easily see that you could use any other (stack of) layers/images instead. Start with a plain white picture, black as the foreground color and open the layer dialog!

## Adding text

<figure>
<img src="tut-basic-1.gif" alt="tut-basic-1.gif"/>
</figure>

Use the text tool to add some text. You will get a new text layer which you can also see if you look at the layers dialog. You can use the move tool to move the text where you like to have it. Then merge it with the white layer below by choosing _Merge Down_ from the Layer menu. You should now have one layer with black text on white background. Using <span class="filter"><Image> Colors → Invert</span> you will achieve something like the picture above.

## Adding colors

<figure>
<img src="tut-basic-2.gif" alt="tut-basic-2.gif"/>
<img src="tut-basic-3.gif" alt="tut-basic-3.gif"/>
</figure>

First of all: Blur the image a bit using <span class="filter"><Image> Filters → Blur → Gaussian Blur</span> (a value of 5 may be a good start). Now add a new layer to the image with the help of the New Layer button in the layers dialog. Choose it to be white. It will be created above the just made text layer effectively hiding it. It will be active which can be seen from the fact that it has a blue background in the layers dialog. Click some times on the eye symbol to see how you can make a layer invisible and make the other layer active by clicking on its small preview in the layer dialog. At the end, leave the new white layer visible and active. Use the plasma plugin to make this layer a little colorful: <span class="filter"><Image> Filters → Render → Clouds → Plasma</span> (Yes, you are invited to experiment with the parameters...). The layer dialog should look something like this now:

<figure>
<img src="tut-basic-dia-1.gif" alt="tut-basic-dia-1.gif"/>
</figure>

## Bumpmapping

<figure>
<img src="tut-basic-4.gif" alt="tut-basic-4.gif"/>
</figure>

It's getting funny now: Use the bumpmap plugin with the blurred text layer as a bumpmap on the plasma layer. You can play with the other parameters, but they have sensible defaults. You'll get an image like the one above. Now (still on the plasma layer) choose Add layer mask from the layer dialog menu. Choose the mask to be white. Nothing will change on the image for now, but the layer dialog will look like this:

<figure>
<img src="tut-basic-dia-2.gif" alt="tut-basic-dia-2.gif"/>
</figure>

You can toggle whether a layers mask or the actual picture is active by clicking on their previews in the layers dialog.

## Using the layer mask

<figure>
<img src="tut-basic-5.gif" alt="tut-basic-5.gif"/>
</figure>

Now activate the text layer again. (you don't have to make the layers on top invisible to work on this layer. It's enough that you activate it in the layers dialog.) Now do <span class="filter"><Image> Edit → Copy</span>. Make sure you have the mask of the top layer selected and the layer is activated. Choose <span class="filter"><Image> Edit → Paste</span>. You will again get a floating selection, shown in the layer dialog like this:

<figure>
<img src="tut-basic-dia-3.gif" alt="tut-basic-dia-3.gif"/>
</figure>

Use the layer dialog menu to Anchor Layer, which will anchor the floating selection into the previous activated layer (which is the mask of the plasma layer in our case). This will leave you with the following scenario:

<figure>
<img src="tut-basic-dia-4.gif" alt="tut-basic-dia-4.gif"/>
</figure>

## Adjusting the levels

<figure>
<img src="tut-basic-6.gif" alt="tut-basic-6.gif"/>
</figure>

Now add a new layer and fill it with some color (e.g. with the help of the bucket fill tool) and use Raise Layer or Lower Layer from the layer dialog menu to achieve something like this:

<figure>
<img src="tut-basic-dia-5.gif" alt="tut-basic-dia-5.gif"/>
</figure>

Now you'll see that the image of the logo isn't very sharp. We'll change this now. Make sure you have selected the plasma layer's mask and open <span class="filter"><Image> Layers → Colors → Levels</span>. This tool is one of the most important tools you have! Play with the little triangles you'll see in the two grey gradients and watch their effect on the image. For now, try to achieve something like the following:

<figure>
<img src="tut-basic-dia-6.gif" alt="tut-basic-dia-6.gif"/>
</figure>

What we do here is making the border of the mask sharper, and by that means, sharpening the whole picture (the area which is neither 100% opaque nor transparent will become smaller). But we can easily avoid the picture getting pixel-steps by leaving still a smooth transition between opaque and transparent parts of the layer. (If you didn't realize it by now - I bet you did - the layer mask works in such a way that all black parts of the mask will become transparent parts of the layer and all white parts will stay opaque (with smooth transitions realized by values of grey).

## Creating a drop-shadow

<figure>
<img src="tut-basic-7.gif" alt="tut-basic-7.gif"/>
</figure>

Using the layer menu you will have noticed the entry Duplicate Layer. Use this now. Then use Apply Layer Mask and Lower Layer which should leave you with something like this:

<figure>
<img src="tut-basic-dia-7.gif" alt="tut-basic-dia-7.gif"/>
</figure>

Make sure you check the Keep Transparency option (the little box next to the layer mode) and then fill that duplicated layer with black. You can paint over the text with a paint tool or simply drag a black color from the color selector and drop it over the image. You do not have to be careful: the Keep Transparency button will let you paint only on opaque parts of the image. This will give you:

<figure>
<img src="tut-basic-dia-8.gif" alt="tut-basic-dia-8.gif"/>
</figure>

Now make sure you uncheck the button again and move the layer some pixels to the right and downwards. You can move it with the Move tool while pressing Shift so that it moves the current layer instead of picking a new one. (Alternatively, can use <span class="filter"><Image> Layer → Transform → Offset</span> and enter a small offset for both X and Y: this will offset the contents of the layer without moving the layer itself.) Then blur your layer and adjust the transparency with the slider so the background will shine through: You've just generated a so-called drop shadow, which greatly enhances the 3D effect and is used in very many places.

<figure>
<img src="tut-basic-dia-9.gif" alt="tut-basic-dia-9.gif"/>
</figure>

That's it! Now have a lot of fun making flying logos!

An updated version of this tutorial can be found here: [Simple Floating Logo](../Floating_Logo)

The original tutorial can be found [here](http://classic.gimp.org/tut-basic.html).

