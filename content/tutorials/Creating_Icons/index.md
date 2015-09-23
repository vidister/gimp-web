Title: Creating Icons
Date: 2002
Modified: 2015-09-23T12:05:07-05:00
Author: Jakub Steiner

<small>Text and images Copyright (C) 2002 [Jakub Steiner](mailto:jimmacNOSPAM@ximian.com) and may not be used without permission of the author.</smalL>

## Intention

Almost every desktop enviroment I've seen has a special application for creating icons, usually a very limited drawing application. In this short tutorial, we'll show you how GIMP (GNU Image Manipulation Program) can help you create icons for your desktop.

## Before You Begin

As with any new task, it will help to have a little background information:

## Filenames and Structure

<figure>
<img src="files.png" alt="files.png"/>
</figure>
GIMP enables you to save compressed files and work with them transparently, using the .xcf format. However, since we're working with very small files, compression simply doesn't save enough space to justify the effort. Especially since filemanagers like [Nautilus](http://nautilus.eazel.com/) have problems with creating thumbnails for compressed images, it's best to accompany any .xcf files you produce with a .png version. (See Image above)

Nautilus (gnome-vfs) can't yet handle compressed GIMP native files

## Choosing a Color Palette

<figure>
<img src="palette.png" alt="palette.png"/>
</figure>
You may think palettes are only necessary in special cases like indexing colors of web images. However, if you're going to create more than one icon, having a pre-selected palette can give your icons a more consistent look and feel.

You may want to consider using a palette that already exists. Many operating systems like MS Windows or MacOS have a system-wide color palette that is used on low color depth screens. You could also use one of the palettes that Tuomas Kuosmanen has included in his [public palettes list](http://tigert.gimp.org/gimp/palettes/).

If you prefer to create your own palette, it's best to just define the most basic colors. That is, focus mostly on defining a set of hues you'll be using. Later on, you can tweak the value or saturation to create highlights or shadows of that particular color. Having a complex palette with many variations will make it complex and hard to navigate.

## Getting Started

When you're ready to start, run GIMP by selecting <span class="filter">Applications -> Graphics -> GIMP</span> Image Editor from your menu panel, or typing **gimp** at the command line. If you haven't used GIMP before, the default window layout may be a little confusing. It's a lot like Photoshop and other similar applications, in that it uses a large number of dialogs. Select items from the <span class="filter">File -> Dialogs</span> menu to choose which dialog windows you'd like to have open and which ones you'd like to have closed. For icon work, you may find it most convenient to use the main window, plus the palette and layers dialogs, and of course the actual image you're working on.

To create a new image file, press <kbd>Ctrl+N</kbd>. Select a 48x48 pixel image, the standard Gnome icon size. Because working on such a tiny pixmap requires a lot of detail, zoom in to work on a pixel-by-pixel level. Try _8:1_ magnification (<span class="filter"><Image> View -> Zoom -> 8:1</span>).

At that magnification, however, you will begin to lose perspective. It's best to keep an additional window open with an unmagnified view, so you can see what your icon will look like. To do that, choose <span class="filter"><Image> View -> New view</span> from the image context menu (the little arrow in the upper left side of the window). Use a _1:1_ zoom on this view, so that you can paint at an _8:1_ zoom and see the results immediately.

Make sure to turn off the selection decorations on the _1:1_ window. To do that, focus the window and press <kbd>Ctrl+T</kbd> or choose <span class="filter"><Image> View -> Toggle selection</span>.

## A Few Tricks

It seems at first that creating an icon is incredibly restrictive. After all, you have just a tiny grid where you will soon run out of pixels. However, there are a few tricks you can use to fool the human eye and make your icons look better. Basically, you'll be simulating or implying shape with color value and opacity.

## Antialiasing

<figure>
<img src="aa1.png" alt="aa1.png" />
<img src="aa2.png" alt="aa2.png" />
</figure>

One of the basic aspects of bitmap images is the negative effect of Aliasing.  
Although many tools like the brush tool work well in large images, they aren't effective at the icon size. In particular, drawing with a 1x1 pixel brush doesn't behave as well as could be hoped.

The solution is to anti-alias manually. Some people prefer to work at a higher resolution, with full anti-aliasing, and then scale down, but the icon loses smoothness and most of the benefit of the larger size. In the end, it's necessary to touch up the image manually. In most cases, you're better off starting with just your 48x48 square and not scaling.

As much as it sounds hard, manual anti-aliasing is easy, and even fun. All you need for this is the _opacity_ setting of the pencil tool. Say we have an outline that's aliased (Like the image to the left). Select a 1x1 brush and set the opacity to something like 40%. When you start drawing with this black brush by clicking on the white surface, it will become light gray. One more click and it gets darker. That way you can easily create fluent transitions between the two border colors. You can also change the active color using <kbd>Ctrl</kbd>-leftMB or just by swapping forground and background colors (**X**).

If you're using layers to have more freedom experimenting, you will find the erase tool as useful for anti-aliasing as the pencil (Right image). Make sure you turn on the hard edges option, for maximum precision.

## Shading with Gradients

You can use gradients to enhance the shape of an object. For round objects, choose a radial gradient, and for curves, use a linear gradient. For filling surfaces, you'll want to use linear gradients almost every time. Even when the surface is supposed to be flat, a slight gradient adds realism. Make sure to keep the gradient subtle, though: too much of a difference between the two extremes and you'll ruin the effect.

## Highlights and Shadows

For any given object, make sure you experiment a little with highlights and shadows, and not just the regular drop shadow used on most Gnome icons. Try giving your icon real material properties with some light reflections. Whether it's just a little gleam or shine from a corner or a suggestion of depth by lowering the saturation or value of a corner in the back, you can improve the look of an icon with just a little work.

For smooth shading, select the area you want to work with and then apply the airbrush tool. You'll only affect the selection, so you don't have to worry about overspray. To do hard highlights, use the one pixel pencil tool and, as before, a lowered opacity for the color.

## Work Example

In this small tutorial, Ximian artist Jakub Steiner will demonstrate most of the techniques described in the section called "A Few Tricks" as he draws a TV icon.

## Basic Shape

<figure>
<img src="rectangle.png" alt="rectangle.png"/>
</figure>
Normally, you'd use the bezier tool for shape editing, but a TV silhouette is simple enough that we'll just start with the rectangle selection tool.

Create a separate foreground layer for the shape, and choose a light, but not completely white, color for the background layer. After you're done with the icon, you can drag colors from the palette to the background layer to make sure that the icon looks right on any background.

Drag the black preview rectangle from the toolbox, or press <kbd>Ctrl-+</kbd> to fill the silhouette. You should have a black square on a light background. Then, use the eraser tool to smooth the edges of the square so that the shape is better. This will also add a slight white shine to the corners of the image.

## Making it Plastic

<figure>
<img src="gradient.png" alt="gradient.png"/>
</figure>
Next, we're going to use alpha blending of a selection to give a more three dimensional appearance to the silhouette.

Select the TV silhouette by right-clicking on the layer in the layer window and choosing Alpha to Selection. Shrink the selection by _1 pixel_ and fill it with a linear gradient similar to the image above. Now you have a dark grey shape with a black outline, and slightly shiny corners.

<figure>
<img src="highlight.png" alt="highlight.png"/>
</figure>
Now it's time to add a bit more depth, using the highlight trick from the section called "Highlights And Shadows". Use a white 1x1 pencil to create highlights, and a black one to create shadows. By setting opacity of the brush to something like 20% you can get results similar to the image above.

## Modelling the Screen

<figure>
<img src="screen.png" alt="screen.png"/>
</figure>
Of course, a television isn't just a single square with an outline. You can create the screen exactly the same way you did the TV silhouette. Create a new layer, and add a smaller rectangular selection, positioned inside the television one. Fill it with black, shrink the selection by 1 pixel and finally fill it with linear gradient to form a screen like the one shown in image above.

<figure>
<img src="reflection.png" alt="reflection.png"/>
</figure>
An important aspect of glass surfaces is the reflection. To make the television screen look shiny and reflective, shrink the selection by another pixel and create a new layer. Now, pick the airbrush tool and a mid-sized fuzzy brush. Paint a white reflection like the one in image above.

If you want to create horizontal monitor lines on the screen, you can use the interlace effect. To do so, create a new layer above the current one. Render white horizontal lines with <span class="filter"><Image> Filters -> Render -> Pattern -> Grid</span>. Make sure you set the layer mode to _Overlay_.

<figure>
<img src="button.png" alt="button.png"/>
</figure>
After that, you'll want to create buttons. This is relatively simple: just create a circular selection with the elipse tool and fill it with radial gradient (image above). Choosing a gradient instead of a solid fill provides a bit of shine to the button, so even if it's just a few pixels across, it looks distinct and three dimensional.

## Modelling the Remote Control

<figure>
<img src="remote1.png" alt="remote1.png"/>
</figure>
This time we'll use the bezier selection tool to create the outline of an object. With a small shape, it can sometimes be difficult to use the bezier tool, it's hard to create a small shape, because the nodes snap to the pixel grid, but it's worth the effort because it makes the shape look sharp, like the one above. You can look in the GIMP manual for more information about editing bezier paths and working with the bezier tool.

<figure>
<img src="remote3.png" alt="remote3.png"/>
</figure>
To create a shadow for the remote, copy the path window and moving just one node. The shadow in this image is done exactly this way.

<figure>
<img src="remote4.png" alt="remote4.png"/>
</figure>
You can make almost any image, especially a small one, easier to understand by adding black object outlines to enhance contrast. To do this, you'll use the opposite of technique you used to create the television silhouette with its outline. First, right-click on the remote control layer and select <span class="filter">Layers -> Alpha to selection</span>. Create a new empty layer below the remote control layer. Increase the size of the selection by 1 pixel, and fill the selection with black.

<figure>
<img src="remote5.png" alt="remote5.png"/>
</figure>
GIMP may not grow that selection perfectly, and you will probably have to alter the result manually. In this case, we'll use the erase tool with a 1x1 pixel brush, and opacity between 60 and 70 percent. Choose the "draw straight lines" option, and smooth the outline by drawing close to the border of the object.

<figure>
<img src="remote6.png" alt="remote6.png"/>
</figure>
Now, to make the object a little more realistic, we'll use our highlight trick. Use the pencil tool with a 1x1 pixel brush and opacity set quite low, near 20%. The result makes the object very real.

<figure>
<img src="remote8.png" alt="remote8.png"/>
</figure>
To create buttons on the remote control, use the same technique as you did to create the button on the TV: Make a selection with the bezeier tool, then fill it with a gradient, and apply highlights and shadows with the pencil tool as needed.

## Adding Glow

<figure>
<img src="remote9.png" alt="remote9.png"/>
</figure>
For extra realism you can add a TV glow. Create a layer above the screen, but below the remote. Create a rectangular selection of the screen, then increase its size by 6 pixels and fill it with blue. Now, shrink that selection by 3 pixels and fill with white. Deselect the are with <kbd>Ctrl-Shift-A</kbd> and apply <span class="filter"><Image> Filter -> Blur -> Gaussian Blur RLE</span> by about 5 pixels. Now set the layer mode to _overlay_, creating the transparency effect.

## The Final Product

<figure>
<img src="finished.png" alt="finished.png"/>
</figure>
Now, you've got a final product: a television, with remote.

