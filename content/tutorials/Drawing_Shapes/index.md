Title: Drawing Shapes with the Path Tool
Date: 2002
Modified: 2015-09-23T12:05:07-05:00
Author: Tuomas Kuosmanen


Text and images Copyright (C) 2002 [Tuomas Kuosmanen](mailto:tigertNOSPAM@gimp.org) and may not be used without permission of the author.

## Intention

The Path Tool (replacing the old Bezier Selection tool) can be used in many creative ways. Maybe the best thing in it is the smooth, beautiful curves it produces. But you can also use paths to create different polygonal shapes if you don't 'pull out the handles'. Polygonal shapes are especially useful when painting some geometric objects, as you can draw one side at a time (into different layers if you want).

## Shapes with Paths!?

<figure>
<img src="box.png" alt="box.png"/>
</figure>

This tutorial is about making simple geometrical shapes with GIMP. I will concentrate on the Path tool since I find it so useful for this purpose. I hope you get some help and new stuff to put in your GIMP Tricks Sack :) I personally use this technique for nearly all my work.

**Notice!** This is not a 'back to basics' -tutorial. You should be familiar with GIMP's dialogs and menus. I was thinking about this, and I did not want to make this an 'entry level' thing, basically to avoid bloating this too big and duplicating other people's work. [Paths are covered in my other tutorial](/tutorials/Bezier_Selections/), and I recommend you to read it before going further if you find the material here confusing. If you are new to GIMP I suggest you to go to the GIMP homepage in [www.gimp.org](http://www.gimp.org/) and first read through the Documentation section there.

## Let's get started!

First we must **create a new image** for our creation. Make the **size 256x256** pixels and choose **RGB** for the type. The image background should be white. During this tutorial, you will have to use the Layers tab and optionally the Paths tab from the dock "Layers, Channels, Paths, Undo". This dock is present in the default GIMP installation. You can also get these tabs using <span class="filter"><Image> Dialogs -> Layers</span> and <span class="filter"><Image> Dialogs -> Paths</span>.

## 1. Left side

<figure>
<img src="box_numb.png" alt="box_numb.png"/>
</figure>

Now create a new transparent layer, and name it *Left_side* so you know what layer I'll talk about later on. Make sure you have the new layer active by checking the layers-dialog. If it is not selected, click the layer's name in the dialog.

Imagine the blue cube on the right side into your canvas, we'll be doing side #1 now.

<figure>
<img src="left_side.png" alt="left_side.png"/>
</figure>


<img src="bezier_button.png" alt="bezier_button.png"/> Choose the Path tool and make something like the side #1 on the blue cube, think about the perspective. (If this causes you trouble, don't worry. You will learn by experience).

You can adjust the points' places if you can't get them right at the first try, see the [Path tutorial](/tutorials/Bezier_Selections/) for more information on that. Your path should look something like the one on the right.

Once you are satisfied with your "box", convert it to a selection using the button "Create Selection from Path" (in the Path Options dialog) or using "Selection to Path" (in the Paths tab).

<figure>
<img src="gradient1.png" alt="gradient1.png"/>
</figure>

Next we must choose some nice colors for our gradient, choose white for the foreground color and some dark-blue for the background (we are making a blue box, remember?) Something like that on the image nearby.

<figure>
<img src="colors.png" alt="colors.png"/>
</figure>

<img src="gradient_button.png" alt="gradient_button.png"/> Select the gradient-fill tool and, starting from the top-left of the selection, 'drag' the gradient quite far down-right (see the arrow in the image. This way you get a quite light-colored face for the cube, and it is just what we want here. We also want the lighter end of the gradient to be near our imaginative light source. (The light was coming from the left)

## 2. Right side

<figure>
<img src="gradient2.png" alt="gradient2.png"/>
</figure>

Now on to the right side, side #2. Create a new transparent layer and name it *Right_side*. Use the Path Tool and try to make the right side of the cube and turn it into a selection.

Take the Gradient Tool again and, still with the same colors, make a gradient from farther up-left to near the selection's lower-right corner (see image on right). This way we get a darker gradient suitable for the shadow-side.

**Hint!** Be careful with the edges. You don't want to leave any holes so the background can be seen through... It's better to overlap the lower layer a bit than leave a space between them.

## 3. Top side

<figure>
<img src="gradient3.png" alt="gradient3.png"/>
</figure>

Our final ultimate task is to create the top, side #3. Again, create a new transparent layer and name it (who quessed? :) *Top_side*.

Now you probably know we want to make yet another path and this time the gradient has to be even lighter than in the first side. So I suggest you lighten the dark blue color a fair amount, it's easier to get a light gradient that way. This time you pull the gradient from left to right, according the arrow in the picture. Once you find the shading look good, you can flatten the image and our little tutorial-cube is finished. Now apply for your 'Cube GIMP Licence' from the nearest GIMP Station ;)

## 4. Finished Work

<figure>
<img src="finished_image.png" alt="finished_image.png"/>
</figure>

Now you have a cool image of a Light-Source-Shaded Cube. You can choose <span class="filter"><Image> Image -> Flatten Image</span> to merge the layers togerher so you can save as jpeg or any other format than xcf. Or, better still, from the layers dialog, make the background invisible and choose <span class="filter"><Image> Image -> Merge Visible Layers</span> so you will have the background on a separate layer and you can work further on it if you like.

The next thing is to start using the geometrical shapes as building blocks to make things. And you can twist the beziers to make a bit more fancy stuff...

I have provided [the xcf-file](example.xcf.gz) for the image we just created, if you want to experiment with it, although you should be perfectly able to do just as good yourself.  
Thanks for your interest.

tigert

<del>The original tutorial can be found [here](http://www.tigert.com/gimp/tutorials/bezier_shapes/).</del>  
It was updated for GIMP 2.0 by Raphaël Quinet.
