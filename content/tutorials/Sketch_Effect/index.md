Title: Vidar's GIMPy high pass filter sketch effect
Date: 2004
Modified: 2015-10-05T10:19:55-05:00
Author: Vidar Madsen


Text and images Copyright (C) 2004 [Vidar Madsen](mailto:vidarNOSPAM@gimp.org) and may not be used without permission of the author.

## Intention

Meet Marius, my son. :)


<figure>
<img src="{filename}01-original.jpg" alt="01-original.jpg"/>
<img src="{filename}09-retouched.jpg" alt="09-retouched.jpg"/>
</figure>


## 1. High pass filtering

High pass filtering means that we filter away the low frequencies of something, and let the high frequency bands pass. In image terms, this means that the detail of an image is kept, while the larger scale gradients are removed. Luckily, it's not as complicated as it sounds.

First, duplicate the layer.

<figure>
<img src="{filename}02-dupdialog.png" alt="02-dupdialog.png"/>
</figure>

Then Gaussian Blur the top layer with an appropriate radius.

You need to experiment to find good values, but roughly speaking one can say that the larger the radius, the wider the high pass filter's frequency response, and the "fatter" the lines in the final sketch. In this example I used 7 pixels, giving this result;

<figure>
<img src="{filename}02-blurdialog.png" alt="02-blurdialog.png"/>
<img src="{filename}02-blurred.jpg" alt="02-blurred.jpg"/>
</figure>

Now we have a low pass filtered version of our image; all gradients and no detail. Exactly the opposite of what we wanted. So, how do we obtain a high pass filtered version? Why, we subtract it from our original, of course. A good way to do that is to simply Invert the image, and blend it 50-50 with the original. First, `Image → Colors → Invert`;

<figure>
<img src="{filename}03-inverted.jpg" alt="03-inverted.jpg"/>
</figure>

Then, to blend the two, we adjust the Layer's Opacity slider to 50%, and our high pass filtered image appears;

<figure>
<img src="{filename}04-dialog.png" alt="04-dialog.png"/>
<img src="{filename}05-highpass.jpg" alt="05-highpass.jpg"/>
</figure>

Now it's time to Merge the two layers, so that we can continue to process them as one. Right-click on the top layer and pick Merge Down.

Now, back to the image. Was the effect a bit too subtle, perhaps? While not necessary, we can apply the Levels tool (<span class="filter">Layer->Colors->Levels</span>) to increase the contrast a bit, so that it's easier to inspect visually. In this example, I set Input Levels to 100-155;

<figure>
<img src="{filename}05-dialog.png" alt="05-dialog.png"/>
<img src="{filename}06-highpass-contrast.jpg" alt="06-highpass-contrast.jpg"/>
</figure>

## 2. The sketch part

Now it's time to make the image background white. First, <span class="filter">Layer->Colors->Desaturate</span> the image, and fire up that Levels tool again. Here you need to experiment a bit to find the best values for your image. But you will most likely want to set max Input Level (the right value) to 128 or thereabout. This makes the 50%-grey part of the image go white, which is a good start. (If you look at the Levels histogram, you should notice a strong peak in the middle. This is where we want the Max Input Level.)

The primary target of experimentation would be the gamma value field in the middle (the grey triangle just below the histogram). With a bit of tweaking, you could end up with something like this;

<figure>
<img src="{filename}06-dialog.png" alt="06-dialog.png"/>
<img src="{filename}07-white.jpg" alt="07-white.jpg"/>
</figure>

That's pretty much it. I tend to want to hand-polish my images to get rid of various imperfections, though. Below is the result of softening the contrast on the lower right region, which is where the bright skin fell against the black background; The higher the contrast, the stronger the lines. I also fine-tuned the overall contrast (with Levels) to get rid of some of the noise in the face;

<figure>
<img src="{filename}08-brightened.jpg" alt="08-brightened.jpg"/>
</figure>

Finally I wanted to remove the annoying shadow below his chin and some of the specks scattered around his face, so I manually hand-brushed away parts of it, giving the final result;

<figure>
<img src="{filename}09-retouched.jpg" alt="09-retouched.jpg"/>
</figure>

Voila. That's it. Hope you liked it. :)

