Title: Gimp Quickies
Date: 2015-08-03T17:11:25-05:00
Modified: 2015-08-03T17:11:32-05:00
Authors: Pat David
Template: page_author
Summary: A quick look at some easy features.

<small>
<a href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US" rel="license"><img class='cc-badge' alt="Creative Commons License" src="http://i.creativecommons.org/l/by-sa/3.0/80x15.png" /></a>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - GIMP Quickies (text & images)</span> by [Pat David](http://blog.patdavid.net)   
is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).
</small>


## Intention

So you installed GIMP on your computer, congratulations! GIMP is a very powerful image manipulation software, but don’t let that intimidate you. Even if you don’t have time to learn advanced computer graphics, GIMP can still be a very useful and handy tool for quick image modifications.

It is my hope that these few examples will help to solve those small, quick modifications that you may need to apply to an image. Hopefully this will lead to learning even more powerful image editing capabilities that GIMP is capable of as well.

For quick access, these are the four main points I’ll cover in this quick tutorial:

* [Changing the Size (Dimensions) of an Image (Scale)](#changing-the-size-dimensions-of-an-image-scale)
* [Changing the Size (Filesize) of a JPEG](#changing-the-size-filesize-of-a-jpeg)
* [Crop an Image](#crop-an-image)
* [Rotate or Flip an Image](#rotate-andor-flip-an-image)

In keeping with the spirit of the predecessor to this page, I will be using images from the Astronomy Picture of the Day ([APOD](http://apod.nasa.gov/apod/astropix.html)), provided by NASA.

All you need to know to follow these quick examples is to be able to find your image and open it:

<div class="MenuCmd"><span>File → Open</span></div>

## Changing the Size (Dimensions) of an Image (Scale)

It’s a common problem that you may have an image that is too large for a particular purpose (embedding in a webpage, posting somewhere online, or including in an email for instance). In this case you will often want to _scale_ the image down to a smaller size more suitable for your use.

This is a very simple task to accomplish in GIMP easily.

The image we’ll be using to illustrate this with is [The Horsehead Nebula in Infrared](http://apod.nasa.gov/apod/ap130422.html).

When you first open your image in GIMP, chances are that the image will be zoomed so that the entire image fits in your canvas. The thing to notice for this example is that by default the window decoration at the top of GIMP will show you some information about the image.

<figure>
<img src="{filename}Scale-View-Pixel-Size-Original.png" alt="Test">
<figcaption>
View of the GIMP canvas, with information at the top of the window.
</figcaption>
</figure>

Notice that the information at the top of the window shows the <span class="tGreen">current pixel dimensions</span> of the image (in this case, the pixel size is 1225×1280).

To resize the image to new dimensions, we need only invoke the **Scale Image** dialog:

<div class="MenuCmd"><span>Image → Scale Image…</span></div>

This will then open the **Scale Image** dialog:

<figure>
<img src='{filename}Scale-Image-Dialog.png' alt='Scale Image'>
<figcaption>
The <strong>Scale Image</strong> dialog.
</figcaption>
</figure>  

In the **Scale Image** dialog, you’ll find a <span class="tGreen">place to enter new values</span> for **Width** and **Height**. If you know one of the new dimensions you’d like for the image, fill in the appropriate one here.

You’ll also <span class='tLightBlue'>notice a small chain</span> just to the right of the **Width** and **Height** entry boxes. This icon shows that the Width and Height values are locked with respect to each other, meaning that changing one value will cause the other to change in order to keep the same aspect ratio (no strange compression or stretching in the image).

For example, if you knew that you wanted your image to have a new width of 600px, you can enter that value in the **Width** input, and the **Height** will automatically change to maintain the aspect ratio of the image:

<figure>
<img src='{filename}Scale-Image-Dialog-Scaled.png' alt='Scaled Image'>
<figcaption>
Changing the <strong>Width</strong> to 600px.
</figcaption>
</figure>  

As you can see, entering **600px** for the width automatically changes the height to **627px**.

Also notice I have shown a different option under **Quality** → Interpolation. The default value for this is *Cubic*, but to retain the best quality it would better to use **Sinc (Lanczos3)**.

If you want to specify a new size using a different type of value (other than Pixel size), you can change the type by clicking on the “**px**” spinner:

<figure>
<img src='{filename}Scale-Image-Dialog-Value-Types.png' alt='Value Types'>
<figcaption>
Changing input value types.
</figcaption>
</figure>  

A common use for this could be if you wanted to specify a new size as a percentage of the old one. In this case you could change to “percent”, and then enter 50 in either field to scale the image in half.

Once you are done scaling the image, don’t forget to export the changes you’ve made:

<div class="MenuCmd"><span>File → Export…</span></div>

to export as a new filename, or:

<div class="MenuCmd"><span>File → Overwrite {FILENAME}</span></div>

to overwrite the original file (use caution).

For more detail about using **Scale Image**, you can see [the documentation](http://docs.gimp.org/2.8/en/gimp-image-scale.html).

## Changing the Size (Filesize) of a JPEG

You can also modify the filesize of an image when exporting it to a format like JPEG. JPEG is a _**lossy**_ compression algorithm, meaning that when saving images to the JPEG format, you will sacrifice some image quality to gain a smaller filesize.

Using the same Horsehead Nebula image from above, I have resized it to 200px wide (see above), and exported it using different levels of JPEG compression:

<figure>
<img src='{filename}JPG-Compression-Sample.png' alt='JPG Compression comparison'>
<figcaption>
Comparison of different JPEG compression levels.
</figcaption>
</figure>  

As you can see, even at a quality setting of 80, the image is significantly smaller in filesize (77% size reduction), while the image quality is still quite reasonable.

When you’ve finished any image modifications you are doing, and are ready to export, simply invoke the export dialog with:

<div class="MenuCmd"><span>File → Export…</span></div>

This will invoke the **Export Image** dialog:

<figure>
<img src='{filename}Export-Image-Dialog.png' alt='Export Image Dialog'>
<figcaption>

</figcaption>
</figure>  

You can now enter a <span class="tGreen">new name for your file here</span>. If you include the filetype extension (in this case, .jpg), GIMP will automatically try to export in that file format for you. Here I am exporting the image as a JPEG file.

You can also navigate to a new location on your computer through the **Places** pane, if you need to export the file to a different location. When you are ready to export the image, just hit <span class='tLightBlue'>the **Export** button.</span>

This will then bring up the **Export Image as JPEG** dialog, where you can change the quality of the export:

<figure>
<img src='{filename}Export-Image-as-JPEG.png' alt='Export as JPG'>
<figcaption>

</figcaption>
</figure>  

From this dialog you can now <span class="tGreen">change the quality of the export</span>. If you also have the “Show preview in image window” option checked, the image on the canvas will update to reflect the quality value you input. This will also enable the “File size:” information to tell you what the resulting file size will be. (You may need to move some windows around to view the preview on the canvas in the background).

When you are happy with the results, hit the **Export** button to export.

To see more details about exporting different image formats, see [Getting Images out of GIMP](http://docs.gimp.org/2.8/en/gimp-images-out.html) in the manual.

## Crop an Image

There are numerous reasons you may want to crop an image. You may want to remove useless borders or information for aesthetic reasons, or you may want the focus of the final image to be of some particular detail for instance.

In a nutshell, cropping is just an operation to trim the image down to a smaller region than what you started with:

<figure>
<img src='{filename}Crop-Example.png' alt='Cropping'>
<figcaption>
Original image (left), cropped image (right).
</figcaption>
</figure>  

The procedure to crop an image is straightforward. You can either get to <span class="tGreen">the **Crop Tool**</span> through the tools palette:

<figure>
<img src='{filename}Crop-Tool.png' alt='Crop Tool'>
<figcaption>
Crop Tool on the Tools Palette.
</figcaption>
</figure>  

Or you can access the crop tool through the menus:

<div class="MenuCmd"><span>Tools → Transform Tools → Crop</span></div>

![GIMP Crop Tool cursor]({filename}Crop-Cursor.png)Once the tool is activated, you’ll notice that your mouse cursor on the canvas will change to indicate the **Crop Tool** is being used.

Now you can Left-Click anywhere on your image canvas, and drag the mouse to a new location to highlight an initial selection to crop. You don’t have to worry about being exact at this point, as you will be able to modify the final selection before actually cropping.

<figure>
<img src='{filename}Crop-First.png' alt='Crop First'>
<figcaption>
Initial pass with the Crop Tool.  
Crop Tool options (left), cropping on the canvas (right).
</figcaption>
</figure>  
<span class="caption"></span></div>

After making the initial selection of a region to crop, you’ll find the selection still active. At this point hovering your mouse cursor over any of the four corners or sides of the selection will change the mouse cursor, and highlight that region.

This allows you to now fine-tune the selection for cropping. You can click and drag any side or corner to move that portion of the selection.

Once you are happy with the region to crop, you can just press the **“Enter"** key on your keyboard to commit the crop. If at any time you’d like to start over or decide not to crop at all, you can press the **“Esc”** key on your keyboard to back out of the operation.

See [the documentation](http://docs.gimp.org/2.8/en/gimp-tool-crop.html) for more information on cropping in GIMP.

### Another Method

Another way to crop an image is to make a selection first, using the **Rectangle Select Tool**:

<figure>
<img src='{filename}Crop-Select-Tool.png' alt='Crop Select'>
<figcaption>
Rectangle Select Tool.
</figcaption>
</figure>  

Or through the menus:

<div class="MenuCmd"><span>Tools → Selection Tools → Rectangle Select</span></div>

You can then highlight a selection the same way as the **Crop Tool**, and adjust the selection as well. Once you have a selection you like, you can crop the image to fit that selection through:

<div class="MenuCmd"><span>Image → Crop to Selection</span></div>

## Rotate and/or Flip an Image

There may be a time that you would need to rotate an image. For instance, you may have taken the image with your camera in a vertical orientation, and for some reason it wasn’t detected by GIMP as needing to be rotated (GIMP will normally figure this out for you, but not always).

There may also be a time that you’d like to flip an image as well. These commands are grouped together under the same menu item:

<div class="MenuCmd"><span>Image → Transform</span></div>

### Flip an Image

If you want to flip your image, the **Transform** menu offers two options, **Flip Horizontally**, or **Flip Vertically**. This operation will mirror your image along the specified axis. For example, here are all of the flip operations shown in a single image:

<figure>
<img src='{filename}Flip-Sample-Arrow.jpg' alt='Flipping'>
<figcaption>
All flips applied to base image (top left).
</figcaption>
</figure>  

### Rotate an Image

Image rotation from the **Transform** menu is contrained to either 90° clockwise/counter-clockwise, or 180°.

Don’t mis-interpret this to mean that GIMP cannot do arbitrary rotations (any angle). Arbitrary rotations are handled on a per-layer basis, while the image rotation described here is applicable to the entire image at once.

<figure>
<img src='{filename}Rotate-Sample.jpg' alt='Rotating Sample'>
<figcaption>
Original (top left), 90° clockwise (top right)  
90° counter-clockwise (bottom left), 180° (bottom right)
</figcaption>
</figure>  
<span class="caption"></span></div>

## In Conclusion

The simple examples shown here are just the tip of a really, really large iceberg. These are, however, common modifications that many people are often looking to make without having to learn too much about image processing. Hopefully they have been helpful.

I encourage you to peruse the [other tutorials](/tutorials/) for more advanced methods of image processing as well!

The original tutorial this was adapted from can be found [here](../Lite_Quickies).


---


<small>
<a href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US" rel="license"><img class='cc-badge' alt="Creative Commons License" src="http://i.creativecommons.org/l/by-sa/3.0/80x15.png" /></a>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - GIMP Quickies (text & images)</span> by [Pat David](http://blog.patdavid.net)   
is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).
</small>

