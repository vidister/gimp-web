Title: Gimp Quickies
Date: 2015-08-03T17:11:25-05:00
Modified: 2015-08-03T17:11:32-05:00
Authors: Pat David
Summary: A quick look at some easy features.
url: tutorials/GIMP_Quickies/
save_as: tutorials/GIMP_Quickies/index.html

<small><a href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US" rel="license"><img alt="Creative Commons License" src="http://i.creativecommons.org/l/by-sa/3.0/80x15.png" style="border-width:0; width: initial; display: inline; margin: 0;" /></a>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - GIMP Quickies (text & images)</span> by [Pat David](http://blog.patdavid.net)   
is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).
</small>

## Intention

So you installed GIMP on your computer, congratulations! GIMP is a very powerful image manipulation software, but don’t let that intimidate you. Even if you don’t have time to learn advanced computer graphics, GIMP can still be a very useful and handy tool for quick image modifications.

It is my hope that these few examples will help to solve those small, quick modifications that you may need to apply to an image. Hopefully this will lead to learning even more powerful image editing capabilities that GIMP is capable of as well.

For quick access, these are the four main points I’ll cover in this quick tutorial:

*   [Changing the Size (Dimensions) of an Image (Scale)](#scale)
*   [Changing the Size (Filesize) of a JPEG](#compress)
*   [Crop an Image](#crop)
*   [Rotate or Flip an Image](#transform)

In keeping with the spirit of the predecessor to this page, I will be using images from the Astronomy Picture of the Day ([APOD](http://apod.nasa.gov/apod/astropix.html)), provided by NASA.

All you need to know how to do to follow these quick examples is to be able to find your image and open it:

<div class="MenuCmd"><span><span style="text-decoration: underline;">F</span>ile → <span style="text-decoration: underline;">O</span>pen</span></div>

## Changing the Size (Dimensions) of an Image (Scale)

It’s a common problem that you may have an image that is too large for a particular purpose (embedding in a webpage, posting somewhere online, or including in an email for instance). In this case you will often want to _scale_ the image down to a smaller size more suitable for your use.

This is a very simple task to accomplish in GIMP easily.

The image we’ll be using to illustrate this with is [The Horsehead Nebula in Infrared](http://apod.nasa.gov/apod/ap130422.html).

When you first open your image in GIMP, chances are that the image will be zoomed so that the entire image fits in your canvas. The thing to notice for this example is that by default the window decoration at the top of GIMP will show you some information about the image.

<figure>
<img src="{attach}Scale-View-Pixel-Size-Original.png" alt="Test">
</figure>

<div class="centerImg">![GIMP Scale Image Tutorial Nebula]({attach}Scale-View-Pixel-Size-Original.png)  
<span class="caption">View of the GIMP canvas, with information at the top of the window.</span></div>

Notice that the information at the top of the window shows the <span style="color: #00FF00;">current pixel dimensions</span> of the image (in this case, the pixel size is 1225×1280).

To resize the image to new dimensions, we need only invoke the **Scale Image** dialog:

<div class="MenuCmd"><span><span style="text-decoration: underline;">I</span>mage → <span style="text-decoration: underline;">S</span>cale Image…</span></div>

This will then open the **Scale Image** dialog:

<div class="centerImg">![GIMP Scale Image Tutorial Dialog](Scale-Image-Dialog.png)  
<span class="caption">The **Scale Image** dialog.</span></div>

In the **Scale Image** dialog, you’ll find a <span style="color: #00FF00;">place to enter new values</span> for **Width** and **Height**. If you know one of the new dimensions you’d like for the image, fill in the appropriate one here.

You’ll also <span style="color: #0080FF;">notice a small chain</span> just to the right of the **Width** and **Height** entry boxes. This icon shows that the Width and Height values are locked with respect to each other, meaning that changing one value will cause the other to change in order to keep the same aspect ratio (no strange compression or stretching in the image).

For example, if you knew that you wanted your image to have a new width of 600px, you can enter that value in the **Width** input, and the **Height** will automatically change to maintain the aspect ratio of the image:

<div class="centerImg">![GIMP Scale Image Tutorial Dialog Scaled Values](Scale-Image-Dialog-Scaled.png)  
<span class="caption">Changing the **Width** to 600px.</span></div>

As you can see, entering **600px** for the width automatically changes the height to **627px**.

Also notice I have shown a different option under **Quality** → Interpolation. The default value for this is **Cubic**, but to retain the best quality it would better to use **Sinc (Lanczos3)**.

If you want to specify a new size using a different type of value (other than Pixel size), you can change the type by clicking on the “**px**” spinner:

<div class="centerImg">![GIMP Scale Image Value Types](Scale-Image-Dialog-Value-Types.png)  
<span class="caption">Changing input value types.</span></div>

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

<div class="centerImg">![GIMP JPEG compression example different quality](JPG-Compression-Sample.png)  
<span class="caption">Comparison of different JPEG compression levels.</span></div>

As you can see, even at a quality setting of 80, the image is significantly smaller in filesize (77% size reduction), while the image quality is still quite reasonable.

When you’ve finished any image modifications you are doing, and are ready to export, simply invoke the export dialog with:

<div class="MenuCmd"><span><span style="text-decoration: underline;">F</span>ile → Export…</span></div>

This will invoke the **Export Image** dialog:

<div class="centerImg">![GIMP JPEG compression export name filetype dialog](Export-Image-Dialog.png)  
<span class="caption"></span></div>

You can now enter a <span style="color: #00FF00;">new name for your file here</span>. If you include the filetype extension (in this case, .jpg), GIMP will automatically try to export in that file format for you. Here I am exporting the image as a JPEG file.

You can also navigate to a new location on your computer through the **Places** pane, if you need to export the file to a different location. When you are ready to export the image, just hit <span style="color: #0080FF;">the **Export** button.</span>

This will then bring up the **Export Image as JPEG** dialog, where you can change the quality of the export:

<div class="centerImg">![GIMP Export JPEG options dialog](Export-Image-as-JPEG.png)  
<span class="caption"></span></div>

From this dialog you can now <span style="color: #00FF00;">change the quality of the export</span>. If you also have the “Show preview in image window” option checked, the image on the canvas will update to reflect the quality value you input. This will also enable the “File size:” information to tell you what the resulting file size will be. (You may need to move some windows around to view the preview on the canvas in the background).

When you are happy with the results, hit the **<span style="text-decoration: underline;">E</span>xport** button to export.

To see more details about exporting different image formats, see [Getting Images out of GIMP](http://docs.gimp.org/2.8/en/gimp-images-out.html) in the manual.

## Crop an Image

There are numerous reasons you may want to crop an image. You may want to remove useless borders or information for aesthetic reasons, or you may want the focus of the final image to be of some particular detail for instance.

In a nutshell, cropping is just an operation to trim the image down to a smaller region than what you started with:

<div class="centerImg">![GIMP Crop Example](Crop-Example.png)  
<span class="caption">Original image (left), cropped image (right)</span></div>

The procedure to crop an image is straightforward. You can either get to <span style="color: #00FF00;">the **Crop Tool**</span> through the tools palette:

<div class="centerImg">![GIMP Crop Tool Palette](Crop-Tool.png)  
<span class="caption">Crop Tool on the Tools Palette.</span></div>

Or you can access the crop tool through the menus:

<div class="MenuCmd"><span><span style="text-decoration: underline;">T</span>ools → <span style="text-decoration: underline;">T</span>ransform Tools → <span style="text-decoration: underline;">C</span>rop</span></div>

![GIMP Crop Tool cursor](Crop-Cursor.png)Once the tool is activated, you’ll notice that your mouse cursor on the canvas will change to indicate the **Crop Tool** is being used.

Now you can Left-Click anywhere on your image canvas, and drag the mouse to a new location to highlight an initial selection to crop. You don’t have to worry about being exact at this point, as you will be able to modify the final selection before actually cropping.

<div class="centerImg">![GIMP Crop Tutorial Example first pass](Crop-First.png)  
<span class="caption">Initial pass with the Crop Tool.  
 Crop Tool options (left), cropping on the canvas (right).</span></div>

After making the initial selection of a region to crop, you’ll find the selection still active. At this point hovering your mouse cursor over any of the four corners or sides of the selection will change the mouse cursor, and highlight that region.

This allows you to now fine-tune the selection for cropping. You can click and drag any side or corner to move that portion of the selection.

Once you are happy with the region to crop, you can just press the “**Enter**” key on your keyboard to commit the crop. If at any time you’d like to start over or decide not to crop at all, you can press the “**Esc**” key on your keyboard to back out of the operation.

See [the documentation](http://docs.gimp.org/2.8/en/gimp-tool-crop.html) for more information on cropping in GIMP.

### Another Method

Another way to crop an image is to make a selection first, using the **Rectangle Select Tool**:

<div class="centerImg">![GIMP rectangle select tool crop image](Crop-Select-Tool.png)  
<span class="caption">Rectangle Select Tool.</span></div>

Or through the menus:

<div class="MenuCmd"><span><span style="text-decoration: underline;">T</span>ools → <span style="text-decoration: underline;">S</span>election Tools → <span style="text-decoration: underline;">R</span>ectangle Select</span></div>

You can then highlight a selection the same way as the **Crop Tool**, and adjust the selection as well. Once you have a selection you like, you can crop the image to fit that selection through:

<div class="MenuCmd"><span><span style="text-decoration: underline;">I</span>mage → <span style="text-decoration: underline;">C</span>rop to Selection</span></div>

## Rotate and/or Flip an Image

There may be a time that you would need to rotate an image. For instance, you may have taken the image with your camera in a vertical orientation, and for some reason it wasn’t detected by GIMP as needing to be rotated (GIMP will normally figure this out for you, but not always).

There may also be a time that you’d like to flip an image as well. These commands are grouped together under the same menu item:

<div class="MenuCmd"><span><span style="text-decoration: underline;">I</span>mage → <span style="text-decoration: underline;">T</span>ransform</span></div>

### Flip an Image

If you want to flip your image, the **Transform** menu offers two options, **Flip <span style="text-decoration: underline;">H</span>orizontally**, or **Flip <span style="text-decoration: underline;">V</span>ertically**. This operation will mirror your image along the specified axis. For example, here are all of the flip operations shown in a single image:

<div class="centerImg">![GIMP flip image samples](Flip-Sample-Arrow.jpg)  
<span class="caption">All flips applied to base image (top left).</span></div>

### Rotate an Image

Image rotation from the **Transform** menu is contrained to either 90° clockwise/counter-clockwise, or 180°.

Don’t mis-interpret this to mean that GIMP cannot do arbitrary rotations (any angle). Arbitrary rotations are handled on a per-layer basis, while the image rotation described here is applicable to the entire image at once.

<div class="centerImg">![GIMP rotate image samples](Rotate-Sample.jpg)  
<span class="caption">Original (top left), 90° clockwise (top right)  
 90° counter-clockwise (bottom left), 180° (bottom right)</span></div>

## In Conclusion

The simple examples shown here are just the tip of a really, really large iceberg. These are, however, common modifications that many people are often looking to make without having to learn too much about image processing. Hopefully they have been helpful.

I encourage you to peruse the [other tutorials](/tutorials/) for more advanced methods of image processing as well!

The original tutorial this was adapted from can be found [here](../Lite_Quickies).

[![Creative Commons License](http://i.creativecommons.org/l/by-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US)  
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - GIMP Quickies (text & images)</span> by [Pat David](http://blog.patdavid.net)  
 Licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).

<div><span id="footerleft"></span><span id="footerright"></span></div>
