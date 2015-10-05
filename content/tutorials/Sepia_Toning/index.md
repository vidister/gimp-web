Title: Sepia Toning
Date: 2002
Modified: 2015-10-05T10:19:55-05:00
Author: Eric R. Jeschke


Text and images Copyright (C) 2002 [Eric R. Jeschke](mailto:ericNOSPAM@redskiesatnight.com) and may not be used without permission of the author.

## Intention

<figure>
<img src="before.jpg" alt="before.jpg"/>
<img src="after.jpg" alt="after.jpg"/>
</figure>

In this tutorial I'll show you how to sepia tone a color or black and white image. This technique is modeled on the traditional darkroom method of sepia toning in that the sepia color is applied "unevenly" to areas of different tonality. It works much better than most of the simple methods I've seen for image editors and provides great control!  
The basic technique is to create a "Sepia Mask" that will apply a sepia color layer according to a layer mask that is based on the tonality of the image.  
Giving credit where credit is due: I did not come up with this method. I adapted it for GIMP from [a Photoshop tutorial on the RetouchPRO web site](http://www.retouchpro.com/tutorials/lum-mask-sepia.html).

## The Procedure

<figure>
<img src="original.jpg" alt="original.jpg"/>
</figure>

Here is the original image, loaded into GIMP. It has a bit of an old-time look, so I thought it might work well as a sepia-toned image.

## Step 1

<figure>
<img src="decor.jpg" alt="decor.jpg"/>
<img src="image-wdecorfu.jpg" alt="image-wdecorfu.jpg"/>
</figure>

You can compare the result we will get below to GIMP's built-in Script-Fu for sepia toning (<span class="filter"><Image> Script-Fu -> Decor -> Old Photo</span>) as shown at right.  
Come back and compare to this when you get to the end of the tutorial.

## Step 2

<figure>
<img src="image2.jpg" alt="image2.jpg"/>
</figure>

Duplicate the original image (<span class="filter"><Image> Image -> Duplicate</span> or <kbd>Ctrl+D</kbd>). You may want to minimize the original now (or close it) so you don't choose it by mistake.

Using whatever technique you like best, convert the duplicate to B&W. I recommend the channel mixer for best results, but you can also convert to grayscale (<span class="filter"><Image> Image -> Mode -> Grayscale</span>) or desaturate (<span class="filter"><Image> Image -> Colors -> Desaturate</span>).

Whatever technique you use, convert the B&W image back into RGB mode when you're done (<span class="filter"><Image> Image -> Mode -> RGB</span>).  
In this case I simply did a mode change to grayscale, then back to RGB mode.

## Step 3

<figure>
<img src="colorselection.jpg" alt="colorselection.jpg"/>
<img src="toolbox2.jpg" alt="toolbox2.jpg"/>
</figure>

Double-click on the foreground color swatch to bring up the Color Selection dialog. Dial in the color RED=162, GREEN=138 and BLUE=101 (you can experiment with this color too; this is a good starting point though.)

## Step 4

<figure>
<img src="layers1.jpg" alt="layers1.jpg"/>
<img src="newlayeroptions.jpg" alt="newlayeroptions.jpg"/>
<img src="layers2.jpg" alt="newlayeroptions.jpg"/>
</figure>

Bring up the Layers dialog (<kbd>Ctrl+L</kbd>) and click on the button for a new layer. Give it the name "Sepia Mask" and choose the option to fill it with the foreground color. Click OK.  
You should see nothing but the color now in the image window, since it obscures the image in the layer below. We are going to selectively apply this color to the image.

## Step 5

<figure>
<img src="addmaskoptions.jpg" alt="addmaskoptions.jpg"/>
<img src="layers3.jpg" alt="layers3.jpg"/>
</figure>

Right-click on the Sepia Mask layer and select Add Layer Mask. In the Add Mask Options dialog, choose White (Full Opacity).

## Step 6

<figure>
<img src="layers4.jpg" alt="layers4.jpg"/>
<img src="image3.jpg" alt="image3.jpg"/>
</figure>

In the Layers dialog, click on (select) the Background layer. Go up to the image window, select all and copy (<kbd>Ctrl+A</kbd> then <kbd>Ctrl+C</kbd>). In the Layers dialog, click on the layer mask icon in the Sepia Mask layer (the little white square). Then go back up to the image window and paste (<kbd>Ctrl+V</kbd>)

## Step 7

<figure>
<img src="layers5.jpg" alt="layers5.jpg"/>
<img src="image4.jpg" alt="image4.jpg"/>
</figure>

In the Layers dialog, click the Anchor button to anchor the pasted image into the layer mask.  
In the image window, invert the color (<span class="filter"><Image> Image -> Colors -> Invert</span>). This layer mask insures that the shadow parts of the image receive most of the color, the mid-tones a little less, and the highlights little to none, much the way a print sepia-toned the traditional way would be.

## Step 8

<figure>
<img src="layers6.jpg" alt="layers6.jpg"/>
<img src="image5.jpg" alt="image5.jpg"/>
</figure>

In the Layers dialog, change the Mode (blending mode) of the layer to "Color". This applies the color from the Sepia Mask layer according to the layer mask to the image.  
You now have your base result. It might be a good idea to save this under a new name at this point.

## Step 9

<figure>
<img src="curves.jpg" alt="curves.jpg"/>
<img src="image-curves.jpg" alt="image-curves.jpg"/>
</figure>

Once you've got the base image, you can duplicate it (Ctrl+D), flatten the duplicate (<span class="filter"><Image> Layers -> Flatten Image</span>) and then experiment with:

*   Hue and Saturation (<span class="filter"><Image> Image -> Colors -> Hue..Saturation</span>)
*   Color Balance (<span class="filter"><Image> Image -> Colors -> Color Balance</span>)
*   Levels or Curves (<span class="filter"><Image> Image -> Colors -> Levels|Curves</span>)
*   etc. etc!

You can always compare the result to the base image. If you want to start over, just duplicate the base image again and off you go.

**Hint:** if GIMP had adjustment layers, like Photoshop, we'd just create one of those to experiment with further adjustments. Since GIMP does not have those, we have to flatten the image to apply some of the standard controls and filters. Ergo, work on a duplicate or save the base image..

Here I decided that the image was a little flat and so I punched up the contrast using curves.

## Step 10

<figure>
<img src="decor2.jpg" alt="decor2.jpg"/>
<img src="final.jpg" alt="final.jpg"/>
</figure>

As a final touch, I ran the "Old Photo" Script-Fu without the "sepia" and "mottle" options. Here is the final image.

## Tips and Tweaks

*   You can reduce the effect of the sepia toning by adjusting the opacity of the Sepia Mask layer.
*   Try adding some grain or noise to the image (probably before you desaturate).
*   We used a single, flat color for the sepia color. Experiment with different colors, multiple colors or a color gradient for the Sepia Mask layer.
*   You can apply levels, curves or other adjustments to the contrast mask to increase or decrease "absorbency" of the sepia color into different areas of the image.
*   The method by which you get a black and white image makes a big difference in how the sepia toning comes out.

<figure>
<img src="grayscale-final-446x512.jpg" alt="grayscale-final-446x512.jpg"/>
<img src="desaturate-final-446x512.jpg" alt="desaturate-final-446x512.jpg"/>
</figure>

The one on the left was from a grayscale conversion (<span class="filter"><Image> Image -> Mode -> Grayscale</span>); the one on the right started as a desaturate (<span class="filter"><Image> Image -> Colors -> Desaturate</span>). Notice that there is a lot more blue-channel noise in the right-hand one. This can add a nice "grain" effect (see tip above also) if that is what you are looking for. For this particular image, I prefer the smoother tonality and darker contrast of the left-hand image.

## Further Reading on Sepia Toning

*   Doing this same process with Photoshop ([Part I](http://www.retouchpro.com/tutorials/lum-mask-sepia.html), [Part II](http://www.retouchpro.com/tutorials/lum-mask-sepia2.html))
*   [Stepwise Sepia Toning Using Adobe Photoshop](http://www.photo.net/photo/sepia/index). This method, using Duotones and Tritones, seems to be quite popular.

The original tutorial used to appear on [gimpguru](https://web.archive.org/web/20140704035654/http://gimpguru.org/tutorials/sepiatoning2/).
