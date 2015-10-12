Title: Selective Colorization
Date: 2002
Modified: 2015-09-25T13:33:27-05:00
Author: Eric R. Jeschke


<small>
Text and images Copyright (C) 2002 [Eric R. Jeschke](mailto:ericNOSPAM@redskiesatnight.com) and may not be used without permission of the author.
</small>

## Intention

<figure>
<img src="{filename}before.jpg" alt="before.jpg"/> <img src="{filename}after.jpg" alt="after.jpg"/>
</figure>

In this tutorial I will explain how to convert a color photograph to a B&W one with color restored to selective areas. With the right subject this can give really striking results, as you can see for yourself. This technique is elsewhere referred to sometimes as "hand coloring" :-)

The basic technique is to duplicate the color photograph, convert the duplicate to B&W, and paste it as a new layer on top of the color image. Add an opaque layer mask and then selectively paint transparency into the upper mask, exposing the color photograph underneath.

Giving credit where credit is due: I did not come up with this method. I adapted it for GIMP from a reader comment I saw in [a "hand-coloring" tutorial on photo.net](http://www.photo.net/digital/editing/hand-coloring) (great web site by the way, I recommend it).

## The Procedure

<figure>
<img src="{filename}original.jpg" alt="original.jpg"/>
</figure>

Here is the original example image, loaded into GIMP.

## Step 1

<figure>
<img src="{filename}image2.jpg" alt="image2.jpg"/>
</figure>

Duplicate the image (<kbd>Ctrl+D</kbd>). 
By whatever method suits you best, convert the duplicate image to B&W. Once you have gotten the B&W version that you like, change it back to RGB mode (`Image → Mode → RGB`).

In this example, I tried the [channel mixer](/tutorials/Color2BW/#channelmixer), but ended up in this case preferring a simple conversion to grayscale (`Image → Mode → Grayscale`), then back to RGB.

## Step 2

<figure>
<img src="{filename}layers1.jpg" alt="layers1.jpg"/> <img src="{filename}newlayeroptions.jpg" alt="newlayeroptions.jpg"/> <img src="{filename}layers2.jpg" alt="layers2.jpg"/>
</figure>

Open the Layers dialog (<kbd>Ctrl+L</kbd>). Make sure that the original color image is selected in the Image drop down box. Click on the new layer button at the bottom of the dialog.  
Here I've named the new layer "B&W"  
Make sure the new layer is selected in the layers dialog.

## Step 3

<figure>
<img src="{filename}layers3.jpg" alt="layers3.jpg"/> <img src="{filename}layers4.jpg" alt="layers4.jpg"/>
</figure>

Go to the B&W image and select all, then copy (<kbd>Ctrl+A</kbd> then <kbd>Ctrl+C</kbd>). Then go to the color image window and paste (<kbd>Ctrl+V</kbd>). The B&W image should be pasted into that layer, obscuring the color image.  
Click the anchor button in the Layers dialog to anchor the pasted image.  
You can close the B&W image window you just copied from now, if you want.

## Step 4

<figure>
<img src="{filename}addmaskoptions.jpg" alt="addmaskoptions.jpg"/> <img src="{filename}layers5.jpg" alt="layers5.jpg"/>
</figure>

In the Layers dialog, right-click on the B&W layer and select "Add Layer Mask". In the Add Mask Options dialog, select White (Full Opacity).

## Step 5

<figure>
<img src="{filename}toolbox.jpg" alt="toolbox.jpg"/> <img src="{filename}brushes1.jpg" alt="brushes1.jpg"/> <img src="{filename}image3.jpg" alt="image3.jpg"/>
</figure>

Make sure that Black is selected as the foreground color in the toolbox. We're going to paint transparency into the layer mask to reveal the color image below.  
Bring up the Brushes dialog (`Dialogs → Brushes`) and select a big brush. In the toolbox, select the paint tool (<img src="{filename}paint.jpg" alt="paint.jpg"/>). Begin painting the interior of the parts you want to be in color.

## Step 6

<figure>
<img src="{filename}image4.jpg" alt="image4.jpg"/>
</figure>

When you get to the edges of the colored part, zoom in to make life easier.

## Step 7

<figure>
<img src="{filename}brushes2.jpg" alt="brushes2.jpg"/> <img src="{filename}image5.jpg" alt="image5.jpg"/>
</figure>

At the very boundaries of the colored image I typically zoom in to 300% or so. Switch to a small, feathered brush and very carefully paint the edges.

If you only paint a little at a time it makes it much easier to use GIMP's excellent undo feature if you accidentally stray outside the boundary. If for some reason you can't undo, don't worry: just switch to white paint and paint opacity back over your mistake to repair the mask.

## Final Step

<figure>
<img src="{filename}final.jpg" alt="final.jpg"/>
</figure>

When your all done, go over the colored part carefully to see if there are any gray (opaque) specks that you missed. Then zoom out and have a look. Voila!

## Tips

<figure>
<img src="{filename}tablet.jpg" alt="tablet.jpg"/>
</figure>

*   For this kind of fine paint work, a pen tablet like this Wacom one is very useful. For photo retouching you don't need any bigger than a 4x5 model.
*   In this example I restored the original color from the color image, but there is no reason that you couldn't paint other colors onto the second layer. Just make sure that the image is selected and not the layer mask in the upper layer of the Layers dialog (click on either the image icon or the mask icon to select the one you want to work on).
*   Try blurring the lower color layer, or running one of the interesting "artistic" filters on it (pastels, oil painting, etc). You probably want to do this before you create the B&W copy.

## Other Examples

<figure>
<img src="{filename}example3.jpg" alt="example3.jpg"/><br/><img src="{filename}example2.jpg" alt="example2.jpg"/>
</figure>

## Further Reading

*   [a "hand-coloring" tutorial on photo.net](http://www.photo.net/digital/editing/hand-coloring)

The original tutorial used to appear on [gimpguru](https://web.archive.org/web/20141114051244/http://gimpguru.org/Tutorials/SelectiveColorization/).

