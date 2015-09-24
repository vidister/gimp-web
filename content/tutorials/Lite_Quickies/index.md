Title: GIMPLite Quickies
Date: 2002
Modified: 2015-09-24T15:00:00-05:00
Author: Carol Spears

<small>
Text and images Copyright (C) 2004 [Carol Spears](mailto:carolNOSPAM@gimp.org) and may not be used without permission of the author.
</small>

## Intention

So, you have GIMP installed on your computer, you need to make a quick change to an image for some project, but don't want to learn about computer graphics right now in order to get the image changed. Totally understandable. GIMP is a powerful image manipulator with many options and tools. However, it is quick and somewhat intuitive (after a time) for the small jobs as well. Hopefully, these quickies will help you with your quick problem and help you to stay friends with GIMP and ready for its more complex tools and methods later, when you have the time and inspiration.

A couple of words about the images used here. The came from [APOD](http://antwrp.gsfc.nasa.gov/apod/astropix.html), Astronomy Picture Ofthe Day. The screenshots were taken on my desktop which is sporting this [APOD](http://antwrp.gsfc.nasa.gov/apod/ap040309.html) image.

All you should need to know to start here is how to find your image and open it. <span class="filter">File -> Open</span>.

## <a id="scale">Change the Size of an Image (Scale)</a>

<figure>
<a href="scale-menu.png"><img src="scale-menu-t.png" alt="scale-menu"/></a>
<a href="scale-dialog.png"><img src="scale-dialog-t.png" alt="scale-dialog"/></a>
</figure>


Problem: you have a huge image and you want to put it nicely for viewing on a web page. GIMP is a quick solution. Our example image is this beauty [m51_hallas_big.jpg](m51_hallas_big.jpg) from [APOD](http://antwrp.gsfc.nasa.gov/apod/ap020710.html).

The first thing that you might notice is that GIMP opens the image at a logical size for viewing. So, if your image is really big (like the sample image) it will display it zoomed out until it fits nicely. You can tell if GIMP has done this by the percentage number in the title bar. (you can click on the little screenshot to see the full view of the screenshot) Just because it looks right in this "View" doesn't mean anything.

The other thing to look at in the titlebar is the mode. If it says RGB in the title bar, you are fine. If it says Indexed or grayscale there, you should read the [Change the Mode Quickie](#mode).

Image entry in the menu and the sub menu from the screenshot should reveal itself. Click on "Scale Image...". When ever you click an option from the menu that has ... behind it, expect another dialog. This time, you should get the "Scale Image Dialog".

If you have a desired width, put it in the dialog at the top where it says "New Width". If you don't have such a number in mind, you can steal the width of GIMP's default image size, which is 256 pixels. This is demonstrated in this [screenshot](scale-dialog1.png). You can see the image that this scale dialog produced [here](m51_hallas_256.jpg).

Perhaps you want your image to look more like a 4x6 inch photo on most image rendering web browsers. Simply switch the units to "inches" and put 4 inches in the height box (opting for smaller than 4x6 rather than bigger). You can see this dialog [here](scale-dialog2.png). The image this dialog produced [here](m51_hallas_6x4.jpg).

Let GIMP choose the other dimension length for you. Meaning, it will take more image knowledge to change both width and height and have it look correct. So only change one and let GIMP change the rest. To change the other length see the crop quickie.

## <a id="reduce">Make jpegs Smaller</a>

<figure>
<a href="jpegsave-menu.png"><img src="jpegsave-menu-t.png" alt="jpegsave-menu"/></a>
<a href="jpegsave-dialog-de.png"><img src="jpegsave-dialog-de-t.png" alt="jpegsave-dialog"/></a>
</figure>


You can make your jpegs smaller without changing the pixel width of the image. Actually you can change the weight of the image a lot. I used an(other) image from [APOD](http://antwrp.gsfc.nasa.gov/apod/ap020215.html). The [original image](lordofrings_hst_big.jpg) is huge (3000 pixels wide) so I also made a [smaller (pixel width)](lordofrings_hst_med.jpg) image available. To prepare this image for the web, you should first reduce the image to a better width and height for web viewing as described in the scale quickie. Right click on the properly scaled image and follow the menus <span class="filter"><Image> File -> Save As....</span> The [Save Dialog](save-dialog.png) will pop up.

I generally type the filename I want into the text box, but the Extension drop menu can tell you the available file formats (depending on the libraries you have installed and the conditions of the image you are trying to save). If GIMP complains right now, or if "JPEG" is grayed out in the Extensions menu you should just cancel out of everything and step through the [Change the Mode Quickie](#mode).

In the JPEG Save Dialog, you can opt for GIMP defaults which reduce the size quite a bit, without hurting the visual quality in a way that I can detect. This would be the safest and quickest thing to do.

If you would like to make it smaller still, make sure that the "Preview" toggle is on and then watch the image area and change the compression level by moving the "Quality" slider down. You can see the quality of the image changing, especially towards the leftmost end of the slider. [Here](jpegsave-sample.png) is a screenshot of me doing this very thing. As you can see, very small is also very bad. I have a screenshot of me setting the Quality slider to a more acceptable level [here](jpegsave-sample1.png).

I have not been showing the actual jpegs I created so that we could end this quickie with a race. Clicking [this page](jpegrace.html) should "race" these jpegs to a web page (the first time you see an image in most browsers, you are also waiting for it to write to the cache, so the first time is the worst). With my cable modem, I was unable to see a difference in the load time, but the difference in what you actually see is fairly interesting.

## <a id="crop">Crop An Image</a>

<figure>
<a href="crop-menu.png"><img src="crop-menu-t.png" alt="crop-menu"/></a>
<a href="crop-dialog.png"><img src="crop-dialog-t.png" alt="crop-dialog"/></a>
</figure>


Many reasons to need to crop an image. Making rectangles square, or making squares into rectangles. Cutting alot of useless background to bring out the subject better. etc. To get to the crop tool, you can either push the button on the toolbox ![crop-button](crop-button.png) or right click on the image and follow the menu <span class="filter"><Image> Tools -> Transform Tools -> Crop & Resize</span>. This will change the cursor and allow you to click and drag a rectangular shape. The button in the toolbox is the nicest way to get to any of the tools. I have chosen one of the huge and beautiful [APOD](http://antwrp.gsfc.nasa.gov/apod/ap021108.html) images, [ngc6369 heritage](ngc6369_heritage_big.jpg).

I always click on the approximate upper left corner and drag to the lower [right corner](crop-drag.png). You don't need to worry about being accurate on this first swipe with the crop tool, since a little dialog will pop up and you can make a better choice for your new borders there..

After completeing the click and drag motion, a little "[Crop & Resize Information](crop-dialog.png) Dialog" (shown above also) pops up, telling you information about the borders that were defined in the click and drag. We will have to change all of the numbers. If you would like to make this rectangular image square, you should find the width and height from the [Get Image Information Quickie](#info). Use the smallest of the two lengths to determine the size of the square. In my 300 x 225 pixel image, the largest square I can get is 225 x 225 pixels, and I will need to make sure the Y origin is 0\. At that point, I use the image and the squares to get the best part of the image for the area. The upper right and lower left crop squares will move the marked area. The other two (upper left and lower right) will change the dimensions of the marked area, so be careful. I have a [screenshot](crop-dialog1.png) of this, right after I fixed the width and height and the Y origin, but before the final positoning. The arrows show the move points.

I decided that the image looked the best with the [X Origin at 42](crop-dialog2.png). The final image appears [here](ngc6369_heritage_sq.jpg).

## <a id="info">Find Info About Your Image</a>

<figure>
<a href="info-menu.png"><img src="info-menu-t.png" alt="info-menu"/></a>
<a href="info-dialog.png"><img src="info-dialog-t.png" alt="info-dialog"/></a>
</figure>


This window will tell you the pixel lengths. Right click on the image and follow <span class="filter"><Image> View -> Info Window...</span> Here is a screenshot of a [calculator](info-calculator.png) which also gives lots of good information. I got another [image](quintet_hst_big.jpg) from [APOD](http://antwrp.gsfc.nasa.gov/apod/ap001113.html) It is pretty big. (Not as big as Saturn though) You can see in the dialog above, it is 2241 x 1548 pixels.

If you are just making a square out of a rectangle, like in the [Crop An Image Quickie](#crop), you need only to open the dialog and find the lesser length and use that as described. Since this is very little information, and definately not enough to fill the space between the menu thumbnail and the dialog screenshot in my layout, I thought I would run through some calculator exercises that might help you to meet your image needs.

It is nice to have images appear on a browser window as a photo would. Photos online appear to be 4x6 inches when scaled to 288x432 pixels (72 dpi for many monitors). There is a [problem](info-scale.png), however, if you try to scale this image. The ratio of width to length of the original does not match the ratio of the photo. So, to make the scaled image the correct size crop 10 pixels from the height. For the sample image, it was best to [crop](info-crop-4x6.png) 10 pixels off from the top. The final [image](quintet_hst_6x4.jpg) should "appear" as a 6x4 inch photo on most monitors.

There will be problems whenever mixing scanned photos with digital photos and also with scanned negatives. Modern film developing machines automatically crop one half of an inch off from each image -- the rumor is that the photo printing machines match a certain style of camera view. If you are preparing an image to be printed on a machine like this; or if you are planning on a gallery where the images are from different sources, some intelligent cropping to fit the best size for the medium you have chosen will be a plus. If this is confusing; please blame the photo printing industry and not GIMP.

You can change the Resolution of your image as well, using the same methods as we used in the Scale, although, in my somewhat limited use, the issue is more about how many pixels. Let's say you want to get this image printed at the photo lab. 300 pixels for every inch is preferred. This original image will print easily as a 7 x 5 photo. 2241px/300ppi = 7.47in. Get out your calculator for the short side. 1548/300 = _.

There is another brutal fact you should come to terms with if you are new to graphics and computers. Just because it looks good on the screen (the [image](quintet_hst_6x4.jpg) from before) doesn't mean that it will print that nicely. I tried to emulate how this image would appear printed at 300dpi [here](quintet_hst_emul.jpg). Sorry. There are some options, for instance my friend printed images and then scanned them back in. Terrible business!

## <a name="mode">Change the Mode</a>

<figure>
<a href="mode-menu.png"><img src="mode-menu-t.png" alt="mode-menu"/></a>
<img alt="mode-dialog" src="mode-dialog.png"/>
</figure>

As with anything else, images come in different kinds and serve different purposes. Sometimes, a small size is important (for web sites) and at other times, retaining a high colour depth in all its glory (a family portrait) is what you want. GIMP can handle all of this, and more, primarily by converting between three fundamental modes, as seen in this menu. In order to switch your image to one of these modes, you open it and follow that menu and click the mode you want.

**RGB -** This is the default mode, used for high quality rich colour images. This is also the mode to do most of your image work with including [scaling](#scale), [cropping](#crop) and even [flipping](#flip) as it gives the computer more information to work with. This extra information also makes RGB Mode the largest to store as a result.

A little bit of detail if you are interested. Each pixel or point when in this mode consists of three different components. R->Red, G->Green, B->Blue. Each of these in turn can have an intensity value of 0-255\. So, at every pixel, what you see is an additive combination of these three components. All these combinations result in a way to represent millions of colours.

As an example to practice with images have been provided in various sizes and formats. Indexed images of different sizes: from a very old <a href="">APOD</a> a small <a href="">gif</a> and a larger gif <a href="">of the same image</a> from a later <a href="">APOD</a>. Also the same image in RGB as provided by [Earth Observatory](http://earthobservatory.nasa.gov/Newsroom/NewImages/images.php3?img_id=4573) a [smaller version](AS17-148-22727.jpg) and a [huge version](AS17-148-22727_lrg.jpg).

**Indexed -** This is the mode usually used when file size is of concern, or when you are working with images with few colours. It involves using a fixed number of colours, 256 or less, at each point to represent the colour at that point. GIMP defaults to attempting to figure out an "optimum palette" to best represent your image. Try it, you can undo it if you don't like the results, or use a custom palette or more colours.

<figure>
<a href="mode-index.png"><img src="mode-index-t.png" alt="mode-index"/></a>
</figure>


As you might expect, since the information needed to represent the colour at each pixel is less, the file size is a lot smaller. However, sometimes, there will be options in the various menus that seem to have been "greyed" out for no apparent reason. This usually means the filter or option cannot be applied when your image is in its current mode. Changing the mode to RGB as outlined above should solve this issue. If that doesn't work either, perhaps the option you're trying requires your layer to have the ability to be transparent. This can be done just as easily via (Image)->Layer->Transparency->Add Alpha Channel.

<figure>
<a href="mode-alpha.png"><img src="mode-alpha-t.png" alt="mode-alpha"/></a>
</figure>

**Grayscale -** In case you want to convert your brilliant colour image to something that's black and white (with a lot of shades of grey), this is one of the easiest ways in which to do it. Some photos do look a lot fancier when displayed in grayscale. Again, if you're interested in some detail, this is achieved by taking the RGB values at the pixels in your image, and suitably weighted averaging them to get an _intensity_ at that point.

There is no need to convert an image to a specific mode before saving it in your favourite format, as GIMP is smart enough to [export](mode-export.png).

## <a id="flip">Flip An Image</a>

<figure>
<a href="flip-menu.png"><img src="flip-menu-t.png" alt="flip-menu"/></a>
<img alt="flip-dialog" src="flip-dialog.png"/>
</figure>

When you need the person in the photo looking in the other direction, or you need to top of the image to be the bottom. Mirroring the image (sort of). Right click on the image and follow the menus <span class="filter"><Image> Tools -> Transform Tools -> Flip</span>, or use the button on the toolbox. ![flip-button](flip-button.png)

Using another [APOD](http://antwrp.gsfc.nasa.gov/apod/ap021114.html) image I demonstrated all of the flips on [this](sunspot_swedish_label2.jpg) image. You might get bored before it is over ....

The tool used as is (the default) will do [this](flip-sample-h.png) to an image.

If you double click on the button, up will pop the means to flip images vertically as well. I did just that on [this](flip-sample-v.png) image.

For a really big finish, I flipped [this](flip-sample-b.png) image both ways. At least it is such a cool image for all of this silliness.

The flips are all displayed on one page for you, [here](flips.html). One might ask themselves, useful? or filler for a pre-established format?

## <a id="rotate">Rotate An Image</a>

<figure>
<a href="rotate-menu.png"><img src="rotate-menu-t.png" alt="rotate-menu"/></a>
</figure>


Let's say you turned your brand new digital camera to get a vertical shot, now some of your images are on their sides. Right click on the image, and follow the menus <span class="filter"><Image> Image -> Transforms -> Rotate -> 90 degrees</span> (or 270 depending on the orientation). Using an [APOD](http://antwrp.gsfc.nasa.gov/apod/ap000228.html) image. I rotated it once to demonstrate. [90 degrees CCW](sombrero_vlt-270.jpg).

