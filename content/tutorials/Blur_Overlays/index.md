Title: Gaussian Blur Overlays
Date: 2002
Modified: 2015-08-28T15:01:29-05:00
Author: Eric R. Jeschke


<small>Text and images Copyright (C) 2002 [Eric R. Jeschke](mailto:ericNOSPAM@redskiesatnight.com) and may not be used without permission of the author.</small>

## Intention

<figure>
<img src="{filename}before.jpg" alt="before"/>
<img src="{filename}after.jpg" alt="after"/>
</figure>

In this tutorial I'll show you how to do gaussian blur overlays using GIMP. This is an interesting technique that intensifies and saturates the colors in the image, increases contrast, and adds a slightly hazy, "dreamy" feel to the image.

The basic technique is to create a duplicate layer in the image, lighten it and blur it, and combine it using a layer mode with the original.

Giving credit where credit is due: I did not come up with this method. I adapted it for GIMP from a Photoshop tutorial on the [luminous-landscape.com web site](http://www.luminous-landscape.com/) (great photography web site BTW; I recommend it).

## The Procedure

<figure>
<img src="{filename}image-original.jpg" alt="image-original.jpg"/>
</figure>

Here is the original example image, loaded into GIMP.

## Step 1

<figure>
<img src="{filename}layers1.jpg" alt="layers1.jpg"/>
<img src="{filename}layers2.jpg" alt="layers2.jpg"/>
</figure>

Open the Layers dialog (if it is not already open, it can be accessed through: <span class="filter"><Image> Windows → Dockable Dialogs → Layers</span>). Right-click on the Background layer and select Duplicate (there is also a button for this in the bottom button bar of the Layers dialog (![layerdup]({filename}layerdup.jpg)).

## Step 2

<figure>
<img src="{filename}editlayerattr.jpg" alt="editlayerattr.jpg"/>
<img src="{filename}layers3.jpg" alt="layers3.jpg"/>
</figure>

Now double-click on the duplicate layer and rename the new layer "Blur Overlay". This step is not strictly necessary, but it is helpful to prevent confusion about what is on each layer, especially if you add some additional layers for other editing purposes, or more importantly, if you save the file with layers and open it six months later.

## Step 3

<figure>
<img src="{filename}layers4.jpg" alt="layers4.jpg"/>
</figure>

<figure>
<img src="{filename}levels.jpg" alt="levels.jpg"/>
<img src="{filename}image-overlay.jpg" alt="image-overlay.jpg"/>
</figure>

In the Layers dialog, select the Blur Overlay layer. In the "Mode" drop-down box, select "Overlay".   
Now go back to the image window and apply a Levels (<span class="filter"><Image> Image -> Colors -> Levels</span>) or Curves (<span class="filter"><Image> Image -> Colors -> Curves</span>) and adjust it until the overall image has the proper brightness. You'll usually find it necessary to adjust the gamma slider (middle slider in Levels) down. You are only adjusting the upper layer, but you are viewing the cumulative effect of the layer blend.

**Tip:** If you don't get a good effect with Overlay mode, try Multiply mode (you can even change this while the Levels dialog is active).

**Tip #2:** while the Levels dialog is active you can toggle visibility of the upper layer to see the original image and compare to the blend. Just click on the "eye" next to the upper layer.

## Step 4

<figure>
<img src="{filename}gaussblur.jpg" alt="gaussblur.jpg"/>
<img src="{filename}image-overlay-blur.jpg" alt="image-overlay-blur.jpg"/>
</figure>

Go back to the image window and right click, selecting <span class="filter"><Image> Filters -> Blur -> Gaussian Blur</span>. You will need to experiment to find the best value, but typically a value between 10 and 30 will do nicely.

Voila! If you don't like the effect, you can undo the blur (<kbd>Ctrl+Z</kbd>) and redo it (<kbd>Shift+Alt+F</kbd>) with a different value.

Click on the "eye" next to the Blur Overlay layer in the Layers dialog to rapidly compare the image with and without the overlay. Similarly, turn off the Background layer if you want to view the overlay to do further work on it.

## Tip: Protecting Highlights with a Layer Mask

Although I like the effect, there is one problem with this technique and that is that it also increases contrast: the shadows get darker and the highlights get lighter.

You might be able to apply a contrast mask to counteract this effect, but in most cases it is the highlights that are the most troublesome in that they have lost detail. Fortunately we can apply a simple extension to the above technique to protect the highlights.

## Step 5

<figure>
<img src="{filename}layers-duplicate.jpg" alt="layers-duplicate.jpg"/>
</figure>

Duplicate the image (<kbd>Ctrl+D</kbd>).   
Flatten the duplicate (<span class="filter"><Image> Layers -> Flatten Image</span>).

## Step 6

<figure>
<img src="{filename}threshold.jpg" alt="threshold.jpg"/>
<img src="{filename}image-threshold.jpg" alt="image-threshold.jpg"/>
</figure>

In the duplicate, run a threshold filter (<span class="filter"><Image> Image -> Colors -> Threshold</span>).

In the threshold histogram, click and drag to the right to select all the pixels at the upper end of the scale. Retry or adjust the selection using the number controls in the dialog box until the display shows most of the pixels you want to preserve as white and all the rest black.

You only need to approximate this, since we're going to clean up the mask anyway.

## Step 7

<figure>
<img src="{filename}image-threshold-marqueeselect.jpg" alt="image-threshold-marqueeselect.jpg"/>
</figure>

<figure>
<img src="{filename}gaussblur2.jpg" alt="gaussblur2.jpg"/>
<img src="{filename}image-threshold-blur.jpg" alt="image-threshold-blur.jpg"/>
</figure>

To clean up the mask, I switched to the paintbrush (![paint]({filename}paint.jpg)), hit "x" in the mask image to switch the foreground and background colors (Black/White to White/Black), selected a nice opaque brush in the Brushes dialog and painted the few pixels of the sky white that hadn't been turned white (the darkest parts of the clouds).

Now the black parts. I switched the fg/bg colors back to (Black/White). I could have painted black all over the lake, but I had a faster idea in mind. I used the marquee selection tool (![selectrect]({filename}selectrect.jpg)) to select the whole area and then using the fill tool (![fill]({filename}fill.jpg)) I just clicked in the selection to fill it black in one fell swoop.

I then "feathered" the mask so that it will blend the layers without a harsh transition by applying a 6 pixel gaussian blur to the mask.

## Step 8

<figure>
<img src="{filename}image-threshold-blur-invert.jpg" alt="image-threshold-blur-invert.jpg"/>
</figure>

Invert the mask (<span class="filter"><Image> Image -> Colors -> Invert</span>), so that the white parts correspond to the parts of the combined layers that you want to keep and the black parts correspond to the parts that should only reflect the original image (the highlights).

## Step 9

<figure>
<img src="{filename}addmaskoptions.jpg" alt="addmaskoptions.jpg"/>
<img src="{filename}layers5.jpg" alt="layers5.jpg"/>
</figure>

<figure>
<img src="{filename}layers6.jpg" alt="layers6.jpg"/>
<img src="{filename}layers7.jpg" alt="layers7.jpg"/>
</figure>

Go to the Layers dialog. Select the overlay blur image in the "Image" drop down box (if it is not selected already).

Right-click on the Blur Overlay layer and select Add Layer Mask. In the Add Mask Options dialog, select White (Full Opacity) and click OK.

Now go back to the blurred threshold image, select all and copy (<kbd>Ctrl+A</kbd> then <kbd>Ctrl+C</kbd>). Go back to the overlay blur image and paste (<kbd>Ctrl+V</kbd>). Go to the Layers dialog and click the anchor button (![anchor]({filename}anchor.jpg)) to anchor the mask.

**Tip:** <kbd>Ctrl-click</kbd> on the layer mask icon in the Layers dialog to toggle the effect of the layer mask to compare the image with and without the highlight mask.

## Step 10

<figure>
<img src="{filename}image-original.jpg" alt="image-original.jpg"/>
<figcaption>
Original
</figcaption>
</figure>

<figure>
<img src="{filename}image-final.jpg" alt="image-final.jpg"/>
<figcaption>
Final
</figcaption>
</figure>


Here's the result. Compare to the original image. I would flatten and apply a smart sharpening (edges) to finish it out.

## Tips

*   Try other layer blending modes. "Multiply" often works well, but creates an even darker image than "Overlay"; you may have to really crank up the levels on the upper layer. One nice thing about Multiply is that you probably won't need the highlights mask.   
    "Screen" has a milder effect than either "Overlay" or "Multiply" and will generally just intensify the colors/saturation. You may not want to lighten the upper layer at all, or perhaps even darken it. Experiment to see what effects you can get.

## Other Examples

<figure>
<img src="{filename}example2-before.jpg" alt="example2-before.jpg"/>
<img src="{filename}example2-after.jpg" alt="example2-after.jpg"/>
</figure>

Using "Multiply" for the blending mode. (Final image on the right)

<figure>
<img src="{filename}example3-before.jpg" alt="example3-before.jpg"/>
<img src="{filename}example3-after.jpg" alt="example3-after.jpg"/>
</figure>

Using "Overlay" for the blending mode, plus a highlight mask for the sky and waterfall. (Final image on the right)

The original tutorial used to appear on [gimpguru](https://web.archive.org/web/20140704080338/http://gimpguru.org/tutorials/bluroverlays/).

