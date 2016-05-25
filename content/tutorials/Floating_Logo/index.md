Title: Simple Floating Logo
Date: 2015-09-24T11:20:59-05:00
Modified: 2015-09-24T11:21:06-05:00
Author: Pat David
Template: page_author



<small>
<a href='http://creativecommons.org/licenses/by-sa/3.0/deed.en_US'>
<img class='cc-badge' src='http://i.creativecommons.org/l/by-sa/3.0/80x15.png' alt='Creative Commons By Share Alike'/>
</a>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - GIMP Quickies (text & images)</span> by [Pat David](http://blog.patdavid.net)  
is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).</small>

## Intention

This tutorial is intended to introduce you to a few simple commands, and some concepts in order to create a logo that appears to be floating above a background, like this:

<figure>
<img src="{filename}Floating-Logo-Final.png" alt="GIMP floating logo example"/>
<figcaption>

</figcaption></figure>

The concepts are ones that you’ll likely come across multiple times while working in graphics processing. Layer masks are used to isolate a part of an image, thus allowing it to be placed over a random background for instance. The addition of a drop-shadow effect to make an object appear to be floating over the background is another example.

## Getting Started

Create a new image of appropriate size for your logo:

<div class="MenuCmd"><span><span style="text-decoration: underline;">F</span>ile → <span style="text-decoration: underline;">N</span>ew…</span></div>

This will open the “Create a New Image” dialog, with options for you to specify:

<figure>
<img src="{filename}New-Dialog.png" alt="GIMP create new image dialog"/>
<figcaption>

</figcaption></figure>

You can make this new image any dimensions you want, but for this tutorial I am going to specify a **Width** of 256 px, and a **Height** of 128 px. I haven’t specified any other options. When you’re ready, hit “OK” to create the new image.

You’ll be presented with the new image on your canvas. Chances are it will be a pure white image at this point (it may be a different color depending on how your GIMP is setup to handle new images - if it is, don’t worry).

## Fill the New Image with Black

The first thing we are going to do is fill our new image with black. The first step to doing so is to make sure that the **Foreground Color** is appropriately set. Click on the foreground color in the **Color area** to bring up the “Change Foreground Color” dialog (if your foreground color is already black you don’t have to do this step, but it can’t hurt to learn):

<figure>
<img src="{filename}Change-Foreground-Color.png" alt="GIMP change foreground color"/>
<figcaption>
Click the <span style="color:#00FF00;">foreground color</span> to change.
</figcaption></figure>

The “Change Foreground Color” dialog allows you to now set the foreground color. We want to set the color to black RGB(0, 0, 0):

<figure>
<img src="{filename}Change-Foreground-Dialog.png" alt="GIMP change foreground color dialog"/>
<figcaption>

</figcaption></figure>

With the foreground color set, we can now use the **Bucket Fill Tool** to fill in our image:

<div class="MenuCmd"><span><span style="text-decoration: underline;">T</span>ools → <span style="text-decoration: underline;">P</span>aint Tools → <span style="text-decoration: underline;">B</span>ucket Fill</span></div>

<figure>
<img src="{filename}Bucket-Fill-Tool.png" alt="GIMP bucket fill tool"/>
<figcaption>
Activating the <strong>Bucket Fill</strong> tool.
</figcaption></figure>

![Bucket Fill Cursor]({filename}Bucket-Fill-Cursor.png) Once the tool is activated, your cursor should appear as to the left. To fill the layer you need only click on the image area at this point. Your image should now fill with black.

## Adding Some Text

Now we want to add text to our image to create our logo with. To see what we’re doing, though, will require us to change the foreground color to something other than black (black text on black background doesn’t show up so well).

Now, you can follow the above procedures again to set the foreground color. If your background color is already white, though, you can quickly swap foreground/background colors using the <span style="color: #00FF00;">arrows</span>:

<figure>
<img src="{filename}Color-Swap.png" alt="GIMP swap color foreground background"/>
<figcaption>
<strong>Swap Foreground/Background</strong> quickly.
</figcaption></figure>

You can also use they keyboard shortcut “**X**” to swap the colors.

With the foreground color set to white, we can now use the **Text Tool** to add some text to our image:

<div class="MenuCmd"><span><span style="text-decoration: underline;">T</span>ools → Te<span style="text-decoration: underline;">x</span>t</span></div>

<figure>
<img src="{filename}Text-Tool.png" alt="GIMP text tool"/>
<figcaption>
Activating the <strong>Text Tool</strong>.
</figcaption></figure>

We can now draw a box on our canvas (image) to hold the text. You can click on the canvas where you’d like the top-left corner of your box to be, and drag the mouse down to the bottom right corner. You don’t have to worry about being exact at this point, because you can adjust the boundaries of the box after the fact.

This is what you should see on your canvas after clicking and dragging from the top-left to the bottom-right to define your text box:

<figure>
<img src="{filename}Text-Box.png" alt="GIMP text box canvas"/>
<figcaption>
Defining the text box boundaries.
</figcaption></figure>

If you’d like to re-size the box for some reason, you can now click and drag in any of the <span style="color: #00AA00;">green areas</span> shown below:

<figure>
<img src="{filename}Text-Box-Resize.png" alt="GIMP resize text box"/>
<figcaption>
<span style="color:#00AA00;">Resize handles</span> to modify text box boundary.
</figcaption></figure>

Your text will go into the black box inside the green areas shown above.

Once the text boundary box is sized appropriately, we can just type some text. In my case, I’ll use my name:

<figure>
<img src="{filename}Text-Entry.png" alt="GIMP enter text canvas"/>
<figcaption>
Text Tool Options (left), canvas view (right).
</figcaption></figure>

Chances are when you first start entering text, it will be very small on your canvas. So let’s have a look at some options on the **Text Tool Options** palette (left, above).

If you want to make your text appear bigger, you can change the <span style="color: red;">**Size**</span> in the field shown. For instance, here I’ve chosen to set my <span style="color: red;">**Size**</span> to 100px.

You may also not like the font that is chosen by default. In that case, we can change the <span style="color: #00FF00;">**Font**</span> to something better by clicking the icon. This will open a drop-down to scroll through all the fonts that GIMP knows about on your system. You can see in my example that I’ve changed the font to “Tw Cen MT Bold”.

<figure>
<img src="{filename}Text-New-From-Visible.png" alt="GIMP context new layer from visible"/>
<figcaption>
Creating a new layer from all visible layers.
</figcaption></figure>

Once we’ve gotten the text how we want it, we can now create a new layer from all the visible layers so far (the text layer, and the black background layer). On your **Layers** tab, right click on the text layer we just made, and choose “<span style="color: #00FF00;">New from Visible</span>”.

Alternatively, you can also create a new layer from visible using the menu:

<div class="MenuCmd"><span><span style="text-decoration: underline;">L</span>ayer → New from <span style="text-decoration: underline;">V</span>isible</span></div>

At this point, our layer palette will have three layers on it, the background, the text (“PAT”), and our new layer “Visible”:

<figure>
<img src="{filename}Layer-Palette-Visible.png" alt="GIMP layer palette visible"/>
<figcaption>

</figcaption></figure>

Notice that there is a white border around the “Visible” layer. This indicates that this layer is currently active, so that any operations we perform will apply to this layer.

Which is good, because we are about to blur this new layer a bit!

To apply a slight Gaussian blur to this layer, we simply invoke the command through the menu:

<div class="MenuCmd"><span>Filte<span style="text-decoration: underline;">r</span>s → <span style="text-decoration: underline;">B</span>lur → <span style="text-decoration: underline;">G</span>aussian Blur…</span></div>

This will invoke the **Gaussian Blur** dialog, where we can specify how much blur we want to apply:

<figure>
<img src="{filename}Gaussian-Blur.png" alt="GIMP gaussian blur dialog"/>
<figcaption>

</figcaption></figure>

The defaults were pretty good, but I wanted just a tad more blur, so I increased the **Blur Radius** to 7\. When you’re done, just hit “<span style="text-decoration: underline;">O</span>K”.

## Adding Some Color

Now that we have our text done, it’s time to add a splash of color!

We are going to add a new layer to our image first:

<div class="MenuCmd"><span><span style="text-decoration: underline;">L</span>ayer → <span style="text-decoration: underline;">N</span>ew Layer…</span></div>

Or by Right-Clicking on the “Visible” layer in the layer palette, and choosing “**New Layer…**” from the context menu:

<figure>
<img src="{filename}Layer-New.png" alt="GIMP new layer context menu"/>
<figcaption>
New Layer using the Right-Click context menu.
</figcaption></figure>

The “**Create a New Layer**” dialog will appear - it doesn’t matter what it gets filled with, so you can leave it at whatever **Layer Fill Type** it’s set at (White by default I believe). Hit **<span style="text-decoration: underline;">O</span>K** to create the new layer.

We are now going to fill this new layer with some color to add some interest. To do this we will use the **Plasma** plugin:

<div class="MenuCmd"><span>Filte<span style="text-decoration: underline;">r</span>s → <span style="text-decoration: underline;">R</span>ender → <span style="text-decoration: underline;">C</span>louds → <span style="text-decoration: underline;">P</span>lasma…</span></div>

I just left the default values and hit **<span style="text-decoration: underline;">O</span>K**, but feel free to fiddle with the values. Our layers now look like this:

<figure>
<img src="{filename}Layer-Plasma.png" alt="GIMP plasma layer"/>
<figcaption>

</figcaption></figure>

Here is what my canvas looks like right now (with the plasma layer on top and visible):

<figure>
<img src="{filename}Plasma.jpg" alt="GIMP plasma layer example"/>
<figcaption>

</figcaption></figure>

## Bump Mapping

Now we’re going to use the text we created earlier to generate a fake 3D shape on this plasma layer. The process is known as “bump mapping”. I won’t get into the technical details of how this works, as it is best seen rather than explained. Open the **Bump Map** dialog through the menu:

<div class="MenuCmd"><span>Filte<span style="text-decoration: underline;">r</span>s → <span style="text-decoration: underline;">M</span>ap → <span style="text-decoration: underline;">B</span>ump Map…</span></div>

The **Bump Map** dialog gives a good preview of what the plugin does:

<figure>
<img src="{filename}Bump-Map.jpg" alt="GIMP bump map dialog"/>
<figcaption>

</figcaption></figure>

To get it working correctly, this plugin requires that you properly point to the source for the bump mapping. In our case the source is the text layer we created earlier (the layer was named “Visible”). So we’ll click on the spinner for the <span style="color: #00FF00;">Bump map</span>, and choose our “Visible” layer from the list.

As before, feel free to play with the options. The only one that I changed was the **<span style="text-decoration: underline;">D</span>epth** to increase the illusion of depth (I finally set the value to 6 in my example). Once it looks good, we’ll hit the **<span style="text-decoration: underline;">O</span>K** button to apply it to the layer.

## Apply a Layer Mask

Now we are going to use a **Layer Mask** to isolate our bump mapped text. First we need to add a **Layer Mask** to the plasma layer:

<div class="MenuCmd"><span><span style="text-decoration: underline;">L</span>ayer → <span style="text-decoration: underline;">M</span>ask → Add Layer Mask…</span></div>

Or Right-Click on the plasma layer and choose “<span style="color:#00FF00;">Add Layer Mask…</span>” from the context menu:

<figure>
<img src="{filename}Bump-Mask.png" alt="GIMP add layer mask"/>
<figcaption>

</figcaption></figure>

When the “Add a Mask to the Layer” dialog comes up, set the **Initialize Layer Mask to:** <span style="text-decoration: underline;">W</span>hite (full opacity).

Once you’ve added a mask to the plasma layer, your layers should now look like this:

<figure>
<img src="{filename}Bump-Mask-Layers.png" alt="GIMP layer palette with mask"/>
<figcaption>

</figcaption></figure>

Remember, you can tell which layer (or mask) is active by noticing which one has the white border around it. The layers above show that the plasma layers mask is active (there is a white border around the white mask, so it’s hard to notice, but _no other_ layer/mask has a white border.

We are going to copy the “Visible” layer, and paste it into the layer mask for the plasma layer. So first, Left-Click on the “Visible” layer in the layers palette to activate it:

<figure>
<img src="{filename}Visible-Copy.png" alt="GIMP layer palette copy"/>
<figcaption>
Remember, the white border will indicate the layer is active.
</figcaption></figure>

With the layer active, we want to now copy it:

<div class="MenuCmd"><span><span style="text-decoration: underline;">E</span>dit → <span style="text-decoration: underline;">C</span>opy</span></div>

Then we want to make the plasma layer mask active by Left-Clicking on the **mask**:

<figure>
<img src="{filename}Bump-Mask-Layers.png" alt="GIMP bump map layer mask"/>
<figcaption>
Plasma layer mask now active again.
</figcaption></figure>

With the mask active again, we now want to paste the “Visible” layer back into the image:

<div class="MenuCmd"><span><span style="text-decoration: underline;">E</span>dit → <span style="text-decoration: underline;">P</span>aste</span></div>

This will now insert a _Floating Selection (Pasted Layer)_ into your image:

<figure>
<img src="{filename}Visible-Paste.png" alt="GIMP layer paste"/>
<figcaption>

</figcaption></figure>

To get this _Floating Selection_ into the mask, we need to **Anchor** it:

<div class="MenuCmd"><span><span style="text-decoration: underline;">L</span>ayer → <span style="text-decoration: underline;">A</span>nchor Layer</span></div>

This will **Anchor** the selection down onto the mask. Our image and layers should now look something like this:

<figure>
<img src="{filename}Masked.png" alt="GIMP layer mask example"/>
<figcaption>

</figcaption></figure>

We may now want to add a different colored background to help us fine-tune the results we have so far. Add a new layer to the image as we did when [creating the plasma layer](#addcolor), and place it below the plasma layer. (You can click and drag layers to change their order in the palette).

Pick an interesting background color and fill the new layer with this color. The layers should now look like this:

<figure>
<img src="{filename}Add-Background.png" alt="GIMP layer mask background"/>
<figcaption>

</figcaption></figure>

It doesn’t look bad, but we can perhaps tighten up the results by adjusting the mask a bit to clarify the edges of the text.

## Adjusting the Levels

I want to clean up the edges of the text with what we have so far. Right now, the mask being used on the plasma layer is a copy of the gaussian blurred text. To make it sharper, we are going to adjust the levels on the mask for that layer.

To do this, we first make sure the layer mask is active by clicking on it. Then we can open the **Adjust Color Levels** dialog through the menu:

<div class="MenuCmd"><span><span style="text-decoration: underline;">C</span>olors → <span style="text-decoration: underline;">L</span>evels…</span></div>

With the **Adjust Color Levels** dialog, we now want to sharpen up the edges of the mask a little bit:

<figure>
<img src="{filename}Levels.png" alt="GIMP adjust color levels dialog"/>
<figcaption>

</figcaption></figure>

What we want to do is adjust the **Gamma** and **White point** sliders. I started by dragging the **White point** slider down to increase the prominence of the plasma layer, then pushed the **Gamma** up to emphasize it more. (If you’re following along, you can also just copy my values from above).

The trick is to increase the definition of the edges of the text, without going too far and causing it to look very jagged (aliased). Play with the settings to see how they affect your results. Here is what my plasma layer looks like after applying the above levels to the mask:

<figure>
<img src="{filename}Levels-After.png" alt="GIMP color levels example"/>
<figcaption>

</figcaption></figure>

## Creating a Drop Shadow

Now we may want to get a little fancier and add an effect of a drop shadow behind the logo to make it seem as if it’s floating above the background. We’ve already created what we need to generate this effect, we just need to move a couple of things around to do so.

Make a copy of your “Visible” layer that had your original blurred text on it. Select the layer first to activate it, then you can do:

<div class="MenuCmd"><span><span style="text-decoration: underline;">L</span>ayer → D<span style="text-decoration: underline;">u</span>plicate Layer</span></div>

Or Right-Click on the “Visible” layer, and choose “<span style="color: #00FF00;">D<span style="text-decoration: underline;">u</span>plicate Layer</span>”:

<figure>
<img src="{filename}Duplicate-Layer.png" alt="GIMP context duplicate layer"/>
<figcaption>

</figcaption></figure>

This will create a new layer called “Visible copy”. Move this layer above your background color layer to just beneath your plasma layer as shown (you can Left-Click and drag the layer in the palette):

<figure>
<img src="{filename}Shadow-Layer.png" alt="GIMP example shadow layer"/>
<figcaption>
Click and drag the “Visible copy” layer to beneath the plasma layer
</figcaption></figure>

This layer will become our shadow, but we need to modify a couple of things first. We’ll first invert the colors of the layer to make the text black using:

<div class="MenuCmd"><span><span style="text-decoration: underline;">C</span>olors → In<span style="text-decoration: underline;">v</span>ert</span></div>

Then we need to change the layer so that all of the white areas will be transparent. This can be found in the menu:

<div class="MenuCmd"><span><span style="text-decoration: underline;">L</span>ayer → Tr<span style="text-decoration: underline;">a</span>nsparency → Color to <span style="text-decoration: underline;">A</span>lpha…</span></div>

The layer should now have black text over a transparent background. We’ll now just want to shift this layer a bit to simulate a height by offseting it down and to the right a bit. To do this we can use the **Move Tool**:

<div class="MenuCmd"><span><span style="text-decoration: underline;">T</span>ools → <span style="text-decoration: underline;">T</span>ransfom Tools → <span style="text-decoration: underline;">M</span>ove</span></div>

<figure>
<img src="{filename}Move-Tool.png" alt="GIMP move tool"/>
<figcaption>
Activate the <strong>Move Tool</strong>.
</figcaption></figure>

If we hold down **Shift** and click on the canvas, we restrict the **Move Tool** to modifying only the active layer (our shadow layer). Drag the layer to the right and down a bit to simulate the shadow. I ended up with this:

<figure>
<img src="{filename}Shadow.png" alt="GIMP example drop shadow"/>
<figcaption>
Shadow layer shifted to the right and down a bit.
</figcaption></figure>

At this point we can make it a bit more fancy by adding a **Gaussian Blur** to the shadow to spread it out a little more. We can also modify the layer **Opacity**, adjusting it to let the background show through a bit as well.

Here is the final state of my image, where I applied a **Gaussian Blur** with a 10px radius, and adjusted the shadow layer **Opacity** down to 80:

<figure>
<img src="{filename}Shadow-Final.png" alt="GIMP example drop shadow gaussian blur"/>
<figcaption>

</figcaption></figure>

## The End

Here is my final floating logo image when everything is done:

<figure>
<img src="{filename}Floating-Logo-Final.png" alt="GIMP example floating logo final"/>
<figcaption>

</figcaption></figure>

The neat thing about our process is that we can now use any background we want behind the image, and the effects and shadow will still be there:

<figure>
<img src="{filename}Floating-Logo-Sinus.png" alt="GIMP example floating logo sinus"/>
<figcaption>

</figcaption></figure>

Or we could save it as a PNG file with no background at all, thus allowing whatever background there is to show through:

<figure>
<img src="{filename}Floating-Logo-NoBG.png" alt="GIMP example floating logo no background transparent"/>
<figcaption>

</figcaption></figure>

So that’s it! Go on and have fun making floating logos.

## Errata

For those interested, I’ve made available the .xcf.bz2 file I used to create this tutorial available to [download here](Floating-Logo-Tut-patdavid.xcf.bz2) (96KB).

The original tutorial this was adapted from can be found [here](../The_Basics).

---

<a href='http://creativecommons.org/licenses/by-sa/3.0/deed.en_US'>
<img class='cc-badge' src='http://i.creativecommons.org/l/by-sa/3.0/80x15.png' alt='Creative Commons By Share Alike'/>
</a>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - GIMP Quickies (text & images)</span> by [Pat David](http://blog.patdavid.net)  
Licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).
