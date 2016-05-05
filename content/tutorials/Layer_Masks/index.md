Title: Layer Masks
Date: 2002
Modified: 2015-09-24T15:00:00-05:00
Author: Pat David 


<small>
<a href='http://creativecommons.org/licenses/by-sa/3.0/deed.en_US'>
<img class='cc-badge' src='https://i.creativecommons.org/l/by-sa/3.0/80x15.png' alt='Creative Commons By Share Alike'/>
</a>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - Layer Masks (text & images)</span> by [Pat David](http://blog.patdavid.net) is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).
</small>

## Intention

Layer masks are a fundamental tool in image manipulations. They allow you to selectively modify the opacity (transparency) of the layer they belong to. This differs from the use of the layer **Opacity** slider as a mask has the ability to _selectively_ modify the opacity of different areas across a single layer.

This modification of a layer’s transparency through a mask is non-destructive to the layer itself.

This flexibility to define the opacity of different areas of a layer is the basis for more interesting image manipulation techniques such as selective coloring and luminosity masking.

## Adding a Mask to a Layer

Layer masks need to be added to a layer before they can be used. The process for adding them is simple.

<figure>
<img src="{filename}Layers-Base.png" alt="Layers-Base"/>
<figcaption>
Layers dialog for the image.
</figcaption>
</figure>

For this example I will use a simple image with only two layers, as shown above. There is a base image at the bottom of the stack, and a single layer of teal over it. The teal layer is the active layer (look for the white border), and the one which we will add a layer mask to.

**Right-Click** on the layer you want to add a mask to (the “Teal” layer in my example), and the Context menu will show an option to **Add Layer Mask…**:

<figure>
<img src="{filename}Layers-Add-Mask-Dialog.png" alt="Layers-Add-Mask-Dialog"/>
<figcaption>
Add Layer Mask in the context menu.
</figcaption>
</figure>

You can also add a layer mask through the menus:

<div class="MenuCmd"><span><u>L</u>ayer → <u>M</u>ask → Add Layer Mask…</span></div>

This will then bring up the “**Add a Mask to the Layer**” dialog with some options:

<figure>
<img src="{filename}Add-Mask-Dialog.png" alt="Add-Mask-Dialog"/>
<figcaption>
Add mask options dialog.
</figcaption>
</figure>

There are many options for initializing the Layer Mask. Notice that the first option is to set the entire mask to White, which will result in full opacity on the layer (no transparency from the mask). The option to initialize to Black shows that the mask will make the entire layer fully transparent.

For the purposes of this tutorial, we will let the mask initialize to **White** (full opacity). You should notice a change in your Layers dialog now that shows the layer mask thumbnail to the right of the layer it applies to (in this case the “Teal” layer):

<figure>
<img src="{filename}Layers-with-Mask.png" alt="Layers-with-Mask"/>
<figcaption>
Layers dialog with mask applied to Teal layer.
</figcaption>
</figure>

The layer mask has now been added to the “Teal” layer. It is also active (there is a white border around the thumbnail in the dialog, but is not visible due to the mask being white as well) and ready for modification.

## Modifying a Layers Transparency with the Mask

At this point any operations performed on the canvas will apply to the mask and not to any layers themselves. To illustrate how masks can affect its layers transparency, let’s paint!

I am going to use the **Rectangle Select** tool to select roughly the top third of the image, and I’ll fill this selection with black.

<div class="MenuCmd"><span><u>T</u>ools → <u>S</u>election Tools → <u>R</u>ectangle Select</span></div>

<figure>
<img src="{filename}Tool-Rectangle-Select.png" alt="Tool-Rectangle-Select"/>
<figcaption>
Activating the **Rectangle Select** tool.
</figcaption>
</figure>

Using the **Rectangle Select** tool, I'll select roughly the top third of the image:

<figure>
<img src="{filename}Selection-Top-Third.png" alt="Selection-Top-Third"/>
<figcaption>
Top third of the image selected.
</figcaption>
</figure>

I want to fill this selection with black, but before I do I need to make sure that my foreground color is black. Click on the foreground color in the **Color area** to bring up the “Change Foreground Color” dialog:

<figure>
<img src="{filename}Change-Foreground-Color.png" alt="Change-Foreground-Color"/>
<figcaption>
Click the <span style="color: #00FF00;">foreground color</span> to change.
</figcaption>
</figure>

The “Change Foreground Color” dialog allows you to set the foreground color. For this example set the color to black, RGB(0, 0, 0):

<figure>
<img src="{filename}Change-Foreground-Dialog.png" alt="Change-Foreground-Dialog"/>
<figcaption>
Change the color to black.
</figcaption>
</figure>

With the foreground color set, you can now use the **Bucket Fill Tool** to fill in the selection.

<div class="MenuCmd"><span><u>T</u>ools → <u>P</u>aint Tools → <u>B</u>ucket Fill</span></div>

<figure>
<img src="{filename}Bucket-Fill-Tool.png" alt="Bucket-Fill-Tool"/>
<figcaption>
Activating the **Bucket Fill** tool.
</figcaption>
</figure>

You can now click inside the selection to fill it with the foreground color (black). As soon as you do, you'll be presented with a new view of your image on the canvas:

<figure>
<img src="{filename}Masked-Top-Black.png" alt="Masked-Top-Black]"/>
</figure>

As you can see, filling the selected portion of the layer mask with black resulted in that area having 100% transparency, showing the layer below it.

If you **Rectangle Select** a different area of the mask, you can fill it in with a different shade of gray to produce a variable opacity. For example, I will select a few different regions of the mask, and fill it with different levels of gray:

<figure>
<img src="{filename}Masked-Various.png" alt="Masked-Various]"/>
</figure>

If you examine the layer mask, you'll see that there are different levels of gray being applied (black to white, from top to bottom), and their value is what determines the opacity of the layer.

## Selective Colorization Example

A good example of the application of layer masks is doing selective colorization of an image (selectively allowing color to show through a mostly black and white image). I'll walk through how to easily do this with an image from Mardi Gras 2013:

<figure>
<img src="{filename}SelCol-Base.jpg" alt="SelCol-Base"/>
<figcaption>
Mardi Gras 2013, Mobile, AL
</figcaption>
</figure>

Start the process by duplicating the base image (Shift+Ctrl+D, or Right-Click layer → Duplicate Layer). From the menu:

<div class="MenuCmd"><span><u>L</u>ayer → D<u>u</u>plicate Layer</span></div>

Then desaturate the upper layer using:

<div class="MenuCmd"><span>Colors &rarr; Desaturate</span></div>

Following the steps above, add a layer mask to the desaturated layer and initialize it to White (full opacity). At this point, the Layers dialog should look like this:

<figure>
<img src="{filename}SelCol-Layers.png" alt="SelCol-Layers]"/>
</figure>

As before, set your foreground color to black. This time, rather than filling selections, we are going to use the **Paintbrush Tool** to paint areas of the image we want the color to show through from the layer below.

I decided to paint the boy on the fence. Using the **Paintbrush Tool** I painted over his shirt and head. This allowed those colors to show through from the layer below. Here are the results after painting:

<figure>
<img src="{filename}SelCol-Boy.jpg" alt="SelCol-Boy"/>
<figcaption>
Simple Selective Colorization Example
</figcaption>
</figure>

To illustrate what was done, here is the layer mask I painted to achieve the above result:

<figure>
<img src="{filename}SelCol-Boy-Mask.jpg" alt="SelCol-Boy-Mask"/>
<figcaption>
Layer mask isolated to illustrate
</figcaption>
</figure>

Of course, I could have chosen a different color than black to create the mask. If I wanted a slightly more muted color I could have painted with a more middle gray vs. black:

<figure>
<img src="{filename}SelCol-Boy-50.jpg" alt="SelCol-Boy-50"/>
<figcaption>
Simple Selective Colorization Example (painted with gray vs. black).
</figcaption>
</figure>

## Further Reading

*   [Selective Colorization](../Selective_Color)
*   [Getting Around in GIMP - Layer Masks](http://blog.patdavid.net/2011/10/getting-around-in-gimp-layer-masks.html)
*   [Getting Around in GIMP - Luminosity Masks & Split Toning](http://blog.patdavid.net/2011/10/getting-around-in-gimp-luminosity-masks.html)

The original tutorial this was adapted from may be found [here](http://blog.patdavid.net/2011/10/getting-around-in-gimp-layer-masks.html) (possibly with updated information).

<a href='http://creativecommons.org/licenses/by-sa/3.0/deed.en_US'>
<img class='cc-badge' src='https://i.creativecommons.org/l/by-sa/3.0/80x15.png' alt='Creative Commons By Share Alike'/>
</a>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - Layer Masks (text & images)</span> by [Pat David](http://blog.patdavid.net).  
Licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).

