Title: Blending Exposures
Date: 2015-08-18T16:27:00-05:00
Modified: 2015-08-18T16:27:04-05:00
Author: Eric R. Jeschke


Text and images Copyright (C) 2002 [Eric R. Jeschke](mailto:ericNOSPAM@redskiesatnight.com) and may not be used without permission of the author.

## Intention

<figure>
<img src="{filename}before-light.jpg" alt="before-light.jpg" />
</figure>
<figure>
<img src="{filename}before-dark.jpg" alt="before-dark.jpg" />
</figure>
<figure>
<img src="{filename}after.jpg" alt="after.jpg" />
</figure>

In this tutorial I'll show you how to do blend two different exposures of the same scene that you would like to combine to get the best parts of both images. This procedure works best if you have:

1.  (obviously) have shot two different exposures that would be pleasing to combine,
2.  had the camera mounted on a tripod (not strictly necessary, but helps greatly in aligning the images),
3.  the scenes are not too different at the boundaries of the blend. If the scene has changed too much (trees blowing, waves, people or cars moving, etc. between the images), especially at or near the "seams" of the blend, it will make the blend more difficult.

If you have only one image that needs exposure adjustment, you might look at using the "digital" neutral density filter or the contrast masking technique.

Giving credit where credit is due: I did not come up with this method. I adapted it for GIMP from a Photoshop tutorial on the luminous-landscape.com photography web site (great web site BTW, I recommend it).

## The Procedure

The basic technique is to create a layer above the image that contains the other exposure of the same scene. Finally, we apply a layer mask to the this layer which makes parts of the image transparent that we want to show through from below.

## Step 1

<figure>
<img src="{filename}image-original-light.jpg" alt="image-original-light.jpg" />
</figure>
<figure>
<img src="{filename}image-original-dark.jpg" alt="image-original-dark.jpg" />
</figure>


Here are the two exposures, loaded into GIMP. I am going to sandwich these on different layers and then combine them with a layer mask.

## Step 2

<figure>
<img src="{filename}layers1.jpg" alt="layers1.jpg" />
</figure>
<figure>
<img src="{filename}newlayeroptions.jpg" alt="newlayeroptions.jpg" />
</figure>
<figure>
<img src="{filename}layers2.jpg" alt="layers2.jpg" />
</figure>


The first decision is which one goes on top. In this case I have decided to put the lighter image on top and the darker one on the bottom. The reason is because I hand-held the shots, and they are far from aligned. I'm going to have to move the bottom image until the arch is aligned as best I can get it. Also, the top image is the composition I want anyway, and I'll have less painting to do that way.

Go the image that is going to be on the bottom. Open the Layers dialog (<kbd>Ctrl+L</kbd>) and click on the new layer button (![New Layer]({filename}newlayer.jpg)) to create a new layer.

## Step 3

<figure>
<img src="{filename}layers3.jpg" alt="layers3.jpg" />
</figure>
<figure>
<img src="{filename}layers4.jpg" alt="layers4.jpg" />
</figure>


Go to the image that is going to be on top. Select all and copy (<kbd>Ctrl+A</kbd> then <kbd>Ctrl+C</kbd>). In the Layers dialog, make sure the new layer is selected, then go to the bottom image window and paste (<kbd>Ctrl+V</kbd>). In the Layers dialog, click on the anchor button (![anchor]({filename}anchor.jpg)) to anchor the floating image.

## Step 4

<figure>
<img src="{filename}layers5.jpg" alt="layers5.jpg" />
</figure>
<figure>
<img src="{filename}image-composite-paste.jpg" alt="image-composite-paste.jpg" />
</figure>


Crank down the opacity of the upper layer so that you can see both images.

If they are perfectly aligned you can skip the next step. Unless you used a digital capture on a tripod, the images probably need to be aligned. (Even if you had a film camera on a tripod, it is difficult to get two successive scans to feed through in perfect alignment.)

## Step 5

<figure>
<img src="{filename}layers6.jpg" alt="layers6.jpg" />
</figure>


<figure>
<img src="{filename}image-composite-move.jpg" alt="image-composite-move.jpg" />
</figure>
<figure>
<img src="{filename}image-composite-align.jpg" alt="image-composite-align.jpg" />
</figure>


In the Layers dialog, select the layer you need to move or rotate. In this case it is the lower layer.

Using the arrow keys, nudge the image into alignment. You may need to rotate the image slightly too.

When you get close to alignment, zoom in to get a good close-up view and get the best possible fit.

## Step 6

![Add mask options]({filename}addmaskoptions.jpg)![Layers]({filename}layers7.jpg)

In the Layers dialog, right-click on the upper layer and select Add Layer Mask. In the Add Mask Options dialog, select White (Full Opacity) and click OK.

## Step 7

<figure>
<img src="{filename}image-select1.jpg" alt="image-select1.jpg" />
</figure>
<figure>
<img src="{filename}image-fill.jpg" alt="image-fill.jpg" />
</figure>


Now I want to paint black (transparency) onto the layer mask wherever I want the lower image to show through.

To minimize painting time, use the hand-select ("lasso"![Lasso]({filename}lasso.jpg) ) tool to select a large, hand-drawn region just inside all the borders of the area you want to paint, as shown at right. Then using the fill tool (![Fill]({filename}fill.jpg)) fill the selection with black.

## Step 8

<figure>
<img src="{filename}brushes1.jpg" alt="brushes1.jpg" />
</figure>
<figure>
<img src="{filename}image-paint1.jpg" alt="image-paint1.jpg" />
</figure>


Next, I select a large opaque brush from the Brushes dialog (Dialogs/Brushes), select the Paint tool (![Paint]({filename}paint.jpg)) and begin painting into the mask close to the boundaries of the blend.

Notice that I still have the opacity cranked down on the upper layer so that I can see both layers.

## Step 9

<figure>
<img src="{filename}brushes2.jpg" alt="brushes2.jpg" />
</figure>


<figure>
<img src="{filename}image-paint2.jpg" alt="image-paint2.jpg" />
</figure>
<figure>
<img src="{filename}image-donepainting.jpg" alt="image-donepainting.jpg" />
</figure>


For the very edges, I switch to a small, feathered brush and very carefully paint the edges.

While I'm painting, I'll zoom in and out frequently ("=" key to zoom in, "-" key to zoom out) to inspect the work. Don't worry too much about the borders, since we'll probably have to touch those up anyway.

## Step 10

<figure>
<img src="{filename}image-preclone.jpg" alt="image-preclone.jpg" />
</figure>
<figure>
<img src="{filename}image-postclone.jpg" alt="image-postclone.jpg" />
</figure>


Now the most painstaking part: blending the seams. This is a little tricky due to the different tonalities of the two exposures.

For blending work, the Clone (![Clone]({filename}clone.jpg)), Smudge (![Smudge]({filename}smudge.jpg)), Airbrush (![Airbrush]({filename}airbrush.jpg)) and Blur (![Blur]({filename}convolve.jpg)) are my tools of choice.

Since I'm not sure if these tools have the ability to work across layers (as they do in Photoshop), I duplicate the image (<kbd>Ctrl+D</kbd>) and flatten the duplicate (<span class="filter"><Image> Layers -> Flatten Image</span>) and work on it. This has the additional benefit that if I ever mess up the blending job too badly I can always easily start over at this step.

**Note:** see [this tutorial on correcting blown out highlights](/tutorials/Photo_Edit/Blown_Out_Highlights/) for another example of using these tools for blending and some useful tips on their use.

Here I've used primarily clone and a touch of smudge to blend the seams of the two exposures. I didn't do a very thorough job with this image, since it is more of an example and not something I'm planning to display at any significant size.

**Note:** notice the chromatic aberration of the lens in the form of purple fringing at the edge of the arch. These tools are great for dealing with that even if I were not blending two exposures.

## Final Step

<figure>
<img src="{filename}image-finished.jpg" alt="image-finished.jpg" />
</figure>


Finished. The image still has some problems with blown out highlights in the sunlight of the rock face. It is also a little too dark in the foreground shadow.

## Further Reading on Blending Exposures

*   [Dynamic Ranger.](http://www.digitalsecrets.net/secrets/DynamicRanger.html)
*   [Vincent Bockaert's method of blending in Photoshop](http://www.vincentbockaert.com/Tutorials/ImagesFramePST_08_PS.htm)
*   [Digital Photography For What it's Worth.](http://www.cliffshade.com/dpfwiw/)

The original tutorial used to appear on [gimpguru](https://web.archive.org/web/20140704035059/http://gimpguru.org/tutorials/blendingexposures/).

