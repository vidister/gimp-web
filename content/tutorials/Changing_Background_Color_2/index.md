Title: Changing Background Color 2
Date: 2002
Modified: 2015-08-28T15:01:29-05:00
Author: Francisco Bustamante Hempe

<small>Text and images Copyright (C) 2002 [Francisco Bustamante Hempe](mailto:bit-at-mospan-bitbit-dot-org) and may not be used without permission of the author.</small>

## Intention

<figure>
<img src="img1_initial.jpg" alt="img1_initial.jpg"/>
</figure>

Many times you have an image with a colored background, like the one above and you want to take out the background to use the image's subject in a composition. With gimp there are many ways to achieve this, one of which is using a plug-in specifically designed for this: [Changing Background Color 1](/tutorials/Changing_Background_Color_1/).

## Step 1

<figure>
<img src="img3_step1.png" alt="img3_step1.png"/>
</figure>

In this tutorial I explore the select by color option to remove a particular color from the image. The first step, after you have loaded the image of course, is to click on the Select By Color tool.

## Step 2

<figure>
<img src="img4_step2.png" alt="img4_step2.png"/>
</figure>

Like other selection tools, this one provides several options that can be modified. The top row of buttons sets the Selection Mode. We will use the add option, which means any color we click on will be added to the selection. You can also use the Shift key to acheive the same result.

The other interesting setting is the Threshold. When you click on a color, the higher this setting is, the more similar colors to the one you clicked on will be selected. You can start by using the default setting and increasing it if you need to add more colors faster, or decrease it if you're selecting more then you want.

## Step 3

<figure>
<img src="img5_step3.png" alt="img5_step3.png"/>
</figure>

Now it's time to start selecting the color you want to remove. Just start clicking on the color you don't want and watch the selection update. If that didn't select all the color you want, continue clicking on the unselected parts until you get the desired result.

## Step 4

<figure>
<img src="img6_step4.png" alt="img6_step4.png"/>
</figure>

Finally, there is one last step before you can remove the background. You have to add an alpha channel (a common term for transparency in images) to your image. To do that you have to use the right button on the mouse to get the image menu and go to layers and add alpha channel.

## Step 5

<figure>
<img src="img7_step5.png" alt="img7_step5.png"/>
</figure>

With the selection complete and with an alpha channel just choose from the image menu <span class="filter"><Image> Edit -> Clear</span>, and the image background will be gone.

## Step 6

<figure>
<img src="img8_step6.png" alt="img8_step6.png"/>
</figure>

After the last step you should get something like this in Gimp.   
You can now use this image in a composition or in a web page with a different background like below:

## Final

<figure>
<img src="img2_final.png" alt="img2_final.png"/>
</figure>

Of course you still have to take care of the details if you want to merge an image perfectly into another.

The sunflower image was taken by the photographer Raymond Lofthouuse.

The original tutorial can be found [here](http://bitbit.org/cms.php/gimp/tutorials/remove_one_color.html) (dead link).

