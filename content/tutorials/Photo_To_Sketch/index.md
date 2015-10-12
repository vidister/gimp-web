Title: Photo to Sketch
Date: 2002
Modified: 2015-09-25T13:33:27-05:00
Author: Dave Neary


<small>
Text and images Copyright (C) 2002 [Dave Neary](mailto:bolshNOSPAM@gimp.org) and may not be used without permission of the author.
</small>

## Intention

Tutorial on how to make a nice baby & daddy photo into a nice baby & daddy painting.

## 1. Original image

<figure>
<img src="{filename}original.jpeg" alt="original.jpeg"/>
</figure>

Nice picture of a baby & dad. Ah.

## 2. After a Sobel edge detect

<figure>
<img src="{filename}sobel.jpeg" alt="sobel.jpeg"/>
</figure>

Straightforward Sobel edge detect (<span class="filter"><Image> Filters -> Edge-Detect -> Sobel</span>) of original (don't forget to save a copy of the original) The Sobel edge detect should be done on the background image (without an alpha channel) rather than a copy of the background (which has an alpha channel).

## 3. Equalised & desaturated Sobel

<figure>
<img src="{filename}equalised_sobel.jpeg" alt="equalised_sobel.jpeg"/>
</figure>

Bring out detail with an auto-equalise (<span class="filter"><Image> Layer -> Colors -> Auto -> Auto-Equalize</span>) of the sobel edge detect, and convert it to greys using desaturate (<span class="filter"><Image> Layer -> Colors -> Desaturate</span>).

## 4. Curves window for how to do a highpass filter

<figure>
<img src="{filename}highpass.png" alt="highpass.png"/>
</figure>

We only want the strong edges, otherwise it'll look crap. To get them, we eliminate the edges with small magnitude. The easiest way to do this is with the curves tool (<span class="filter"><Image> Image -> Colors -> Curves</span>) like this.

We set the curve type to free (which allows discontinuities), and then for the bottom 3/4 of the curve (or thereabouts) to 0. Just drag the mouse/pen along the bottom of the curves tool.

## 5. Image after the highpass

<figure>
<img src="{filename}after_highpass.jpeg" alt="after_highpass.jpeg"/>
</figure>

The result is much cleaner. The only problem is it's white-on-black, when we want black-on-transparent ideally.

## 6. L&C dialog for creating an edges mask

<figure>
<img src="{filename}edges.jpeg" alt="edges.jpeg"/>
</figure>

Small trick to get to black-on-transparent. Invert the Sobel edge detect (you did keep a copy, right?) with <span class="filter"><Image> Layer -> Colors -> Invert</span> and apply our highpass-filtered copy as a mask. To do this, open the Layers & Channels dialog (if it's not open already), and add a layer mask to the layer with the inverted edge detect layer (<span class="filter"><Image> Edit -> Copy</span> with the highpass layer selected, <span class="filter"><Layer> Add Layer Mask</span> with the inverted edge layer selected, then select the mask and <span class="filter"><Image> Edit -> Paste</span>) Since we kept the strong edges in the highpass filtered layer, this means that we end up with a rather nice black-on-transparent layer.

## 7. Save of the image above to show effect

<figure>
<img src="{filename}photo_edges.jpeg" alt="photo_edges.jpeg"/>
</figure>

This is the result of the trick above. It's shown here with a white layer behind it. We could stop here, and this is a decent sketch effect. For the colouring, we need some more work (mostly slogging, though).

## 8. L&C dialog with set-up for the colouring trick

<figure>
<img src="{filename}colour_trick.png" alt="colour_trick.png"/>
<figcaption>
images,original image & colouring layer in overlay mode
</figcaption>
</figure>


We put our original image back in the background, and set the white layer to overlay (as we see here) - this means we can see the coloured areas behind the white layer - this is extremely helpful when we're painting the white layer, as sometimes the edges are rather fine, or are in the middle of an area that's more or less the same colour.

## 9. Colouring looks after doing one area of the image

<figure>
<img src="{filename}starting_colouring.jpeg" alt="starting_colouring.jpeg"/>
</figure>

Using the colour-picker tool (looks like an eye-dropper), we select the colour we want to paint from the original image (just activate the "original image" layer and try to pick a colour representative of an area), and then we re-activate our colouring layer, which is still in overlay mode. Using a big brush (with the brush tool for more natural edges) we fill in the area of that colour roughly (doesn't have to be perfect). You should see the colour darkening as we draw with a colour similar to the background colour.

## 10. Colouring layer in normal mode

<figure>
<img src="{filename}viewing_colouring.jpeg" alt="viewing_colouring.jpeg"/>
</figure>

This is what we see if we set the colour drawing layer to normal mode. And we're on our way.

## 11. Finished with a completed colour layer

<figure>
<img src="{filename}pencil_and_paint_sketch.jpeg" alt="pencil_and_paint_sketch.jpeg"/>
</figure>

After some effort, all the regions get filled in. Final touches to make faces and the like look better for shadows and highlights were accomplished by selecting a representative shadow/highlight colour, and adding the extra bits with the airbrush tool (looks like an airbrush). After all our work, we end up with this very nice looking painting effect.

