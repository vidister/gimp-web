Title: 3-D Floating Logo
Date: 2015-08-17T16:40:00-05:00
Modified: 2015-08-17T16:40:05-05:00
Author: Mel Boyce
Summary: A quick look at some easy features.

<small>
Text and images Copyright (C) 2002 [Mel Boyce](mailto:syngin-at-gimp-dot-org) and may not be used without permission of the author.
</small>

## Intention

This tutorial is aimed squarely at the novice GIMP user. The more experienced user may find some techniques here useful. This is the same procedure I used to create the logo on my homepage, albeit with slightly different settings. I'll point out the differences as I go along. I've taken a lot of screen shots to support this tutorial, so enjoy :)

## Step 1

<figure>
<img src="{filename}logo-00.png" alt="Floating Logo" />
</figure>


Fire up GIMP and create a new image. I used a white background at 500px by 200px. I feel this size it adequate as my website at the time of writing uses 500px tables.

## Step 2

<figure>
<img src="{filename}logo-01.png" alt="Floating Logo" />
</figure>

Start by laying down some text that is wider than 400px and not too thin. I've used a font called Pricedown. The text should be created as a new layer. If you use GIMP FreeType then it is done for you, otherwise click the New Layer button in the Layers, Channels, & Paths dialog (looks like a blank piece of paper). It will help to change the layer size to that of the image. Do so by accessing the Layers menu (right click or Control+Click on the layer you wish to operate on) and select Layer to Imagesize.

## Step 3

<figure>
<img src="{filename}logo-02.png" alt="Floating Logo" />
</figure>

Duplicate the text layer (text) twice. One for the highlight effect (highlight) and one for the shaded part of the effect (lowlight). The highlight layer needs to be white, so select that layer, check the Keep Trans. box on the Layers, Channels, & Paths dialog, and fill it with white. You can do this easily by dragging the white color swatch from the toolbox over to the image (assuming that the highlight layer is currently selected). Keep Trans. means "Keep Transparency"; this will ensure that any transformations or fills made to that layer will only affect the non-transparent part of the image.

## Step 4

<figure>
<img src="{filename}logo-03.png" alt="Floating Logo" />
</figure>

Duplicate the text layer again and move it to the top of the Layers stack (use the little up facing arrow head on the Layers, Channels, & Paths dialog). Make sure that Keep Trans. is un-checked and then blur it. I used Gaussian Blur (RLE) at 10 pixels. When I did the original logo, it was set lower than this to make the effect less rounded.

You will need to make sure that the layer boundary is larger than the layer so that the blur can spread nicely. Step 2 mentions this.

## Step 5

<figure>
<img src="{filename}logo-04.png" alt="Floating Logo" />
</figure>

Duplicate the blurred layer once (tmp1 and tmp2). These layers are used to create the edge lighting for the text.

## Step 6

<figure>
<img src="{filename}logo-05.png" alt="Floating Logo" />
</figure>

Nudge one of the blurred layers (tmp1) down and to the right about 5 pixels. The precise number of pixels depends on how blurred and thus how round the text will appear to be, so use your best judgement. You can nudge layers my using the Move tool and the cursor keys on your keyboard. It doesn't matter which of the blurred layers you use in this step, as long as you know which one you didn't move \x{2013} you'll be needing to do a very similar thing to that one soon.

## Step 7

<figure>
<img src="{filename}logo-06.png" alt="Floating Logo" />
</figure>

Now create a selection using the blurred layer (the one you moved in step 6) using Alpha to Selection. This selection is a precise selection based on the layer and includes alpha (transparency) information. Handy stuff. You'll notice that I've turned off the layer below (the other blurred layer). This was done to make sure I could see how far I moved this layer during step 6.

## Step 8

<figure>
<img src="{filename}logo-07.png" alt="Floating Logo" />
</figure>

Now that the layer is selected...

## Step 9

<figure>
<img src="{filename}logo-08.png" alt="Floating Logo" />
</figure>

Select the highlight layer and...

## Step 10

<figure>
<img src="{filename}logo-09.png" alt="Floating Logo" />
</figure>

Cut (edit/cut or <kbd>CTRL+X</kbd> on PC or <kbd>Command+X</kbd> on Mac). This will remove the blurred layers selection from the highlight layer. You could do this with channel masks, but I'm a man of simple needs and wants. There's another step after this that I haven't documented, but that's because it's the same thing again (steps 6-10) but with the other layer (tmp2: see steps 5 and 6). Move (nudge) that layer in the opposite direction (up and to the left about 5 pixels), then make the cut from the lowlight layer. Once you're done, delete the two blurred layers (tmp1 and tmp2).

## Step 11

<figure>
<img src="{filename}logo-10.png" alt="Floating Logo" />
</figure>

I like to take quasi-breaks while doing some images, and this is one of those times. A good time to roll a cigarette or grab a cup coffee. I also tend to clean up temporary layers occasionally.

## Step 12

<figure>
<img src="{filename}logo-11.png" alt="Floating Logo" />
</figure>

Now we'll add the first elements of 3D-ness to the logo. The original text layer is the base layer for any color you want to add. I'll use grey70, but you could just as easily use any old color you like. It's a good idea to play with this as you can get some funky plastic logos too. Make sure Keep Trans. is checked when you fill the layer.

## Step 13

<figure>
<img src="{filename}logo-12.png" alt="Floating Logo" />
</figure>

As you can see, it's starting to look like something now.

## Step 14

<figure>
<img src="{filename}logo-13.png" alt="Floating Logo" />
</figure>

Click the blank piece of paper on the Layers, Channels, & Paths dialog and make a new transparent layer called outline. Move this new layer down the layers stack until it's underneath the original text layer.

## Step 15

<figure>
<img src="{filename}logo-14.png" alt="Floating Logo" />
</figure>

Select the original text layer (the one you added some color to) and do the Alpha to Selection trick again. Right click on the image and use <span class="filter"><Image> Select -> Grow</span>. This will make the new selection larger by a number of pixels - I used a value of 2 pixels. Once you have a selection, be sure to reselect the new layer (outline) so that you can fill it (step 17). And below is what it looks like.

## Step 16

<figure>
<img src="{filename}logo-15.png" alt="Floating Logo" />
</figure>

And this is what it looks like.

## Step 17

<figure>
<img src="{filename}logo-16.png" alt="Floating Logo" />
</figure>

Fill the layer with black and deselect (<kbd>CTRL+SHIFT+A</kbd> on PC or <kbd>Command+SHIFT+A</kbd> on Mac). As you can see, the image now has more background contrast. Now, duplicate that layer and lower the copy below the original outline layer. Make sure that Keep Trans. is not checked, and blur it. I like soft shadows, so I used a Gaussian Blur (RLE) of about 30 pixels. Drop the Opacity of the layer down to about 50 and nudge it to the right and down until it looks okay.

A nice way to fill selection areas or layers that have Keep Trans. selected, is to simply drag the color from the toolbox color swatch to the layer.

## Step 18

<figure>
<img src="{filename}logo-17.png" alt="Floating Logo" />
</figure>

This is what the Layers, Channels, & Paths dialog should look like.

## Step 19

<figure>
<img src="{filename}logo-18.png" alt="Floating Logo" />
</figure>

I've duplicated the highlight and lowlight layers and made them all blend with the lower layers using the Overlay mode. This helps to make the edges more 3D.

## Step 20

<figure>
<img src="{filename}logo-19.png" alt="Floating Logo" />
</figure>

Create a new transparent layer called rust and select the bezier tool (shown here as the depressed button).

## Step 21

<figure>
<img src="{filename}logo-20.png" alt="Floating Logo" />
</figure>

Rust isn't uniform and I've decided to only worry about the lower half of the letters. Use the bezier tool on the new rust layer to start a selection that looks like...

## Step 22

<figure>
<img src="{filename}logo-21.png" alt="Floating Logo" />
</figure>

This. Click inside the bezier path once you close it (close it by clicking one the first node). This will create a selection. Use <span class="filter"><Image> Select -> Feather</span> to feather (blur) the selection. I used a value of about 10 pixels.

## Step 23

<figure>
<img src="{filename}logo-22.png" alt="Floating Logo" />
</figure>

Pick a nice bright orange or brown color for the rust. My site logo used a reddy-borwn color, but here I've chosen a bright orange. Fill the selection with it. Using the famed Alpha to Selection move, get the selection for the original text layer. Once you have that selection area, click the rust layer to make it active. Invert the selection (<kbd>CTRL+I</kbd> or <kbd>Command+I</kbd>) and Cut. This will leave only the part of the rust layer that actually covers the letters and not the extra.

## Step 24

<figure>
<img src="{filename}logo-23.png" alt="Floating Logo" />
</figure>

Change the Layer Mode of the rust layer to Muliply (Burn).

## Step 25

<figure>
<img src="{filename}logo-24.png" alt="Floating Logo" />
</figure>

The image should now look a little like this. Don't worry, it'll look better soon.

## Step 26

<figure>
<img src="{filename}logo-25.png" alt="Floating Logo" />
</figure>

With the rust layer selected, add a Layer Mask.

## Step 27

<figure>
<img src="{filename}logo-26.png" alt="Floating Logo" />
</figure>

Making sure that you reset the color swatches on the toolbox, use the gradient tool to make a gradient in the Layer Mask so it looks like this.

## Step 28

<figure>
<img src="{filename}logo-27.png" alt="Floating Logo" />
</figure>

The image should now look like this.

## Final

<figure>
<img src="{filename}logo-28.png" alt="Floating Logo" />
</figure>

With a little playing around you can get to this. I duplicated the rust layer and moved them (the original rust and the copy) down the stack until the highlight and lowlight layers were above them. I also duplicated the original text layer, switched on Keep Trans., and used <span class="filter"><Image> Render -> Clouds -> Solid Noise</span> to add a bit of interest to the layer. Try using the Curves tool to help with this. You may also notice that the outline layer is blurred. Sometimes this can help. The idea is, try stuff and find out.

Well, thats it. Hope that taught you the power of selections and layer modes to some degree. There are many people who tout the use of channel masks, but don't under estimate the power of selections to do your dirty work.

<small>
Text and images Copyright (C) 2002 [Mel Boyce](mailto:syngin-at-gimp-dot-org) and may not be used without permission of the author.
</small>
