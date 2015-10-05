Title: Tilable Textures
Date: 2002
Modified: 2015-10-05T10:19:55-05:00
Author: Adrian Likins


Text and images Copyright (C) 2002 [Adrian Likins](mailto:adrianNOSPAM@gimp.org) and may not be used without permission of the author.

## Intention

The GIMP 1.2 series have a nice new feature I refer to as gradient brushes. Essentially, this is just the regular paint tool, but instead of painting with a constant color, it gets its color from a gradient and rotates through the gradient as you paint.

## Using Gradient Brushes

<figure>
<img src="grad_brush_dialog.png" alt="grad_brush_dialog.png"/>
</figure>

Gradient brushes can be accessed from the standard paintbrush dialog. Just check the option "Use Color from Gradient" and start painting. You can also press the Gradient button to change the current gradient. Try "German flag smooth", for instance.

<figure>
<img src="grad1.jpg" alt="grad1.jpg"/>

<img src="grad_text1.jpg" alt="grad_text1.jpg"/>

<img src="grad_text2.jpg" alt="grad_text2.jpg"/>
</figure>

Just filling in an image with a gradient brush is a good start for interesting textures, and you can make some nice ones that way.

But that gets a little boring after a while. To really spice thigns up a bit, you need some more interesting brushes. So called "grunge brushes" work quite well for this use. A very nice set can be found in the June 1999 edition of thegimp.com, in the brushes section. Get these for real fun with gradient brushes.

Basically, just select one of those brushes, and se the spacing to something reasonable (most default to 10 or so). I would suggest setting the spacing to about 80-120 or so. Of course, please experiment.

For example, lets choose the "Grunge 15" brush. Set its spacing to about 70 or so. Now choose a gradient from the the gradient selector (<span class="filter"><Image> Dialogs -> Gradients</span>). Just about any of them will do fine. Pick one at random, you can get nice results from any of them. For this particular example, I used "Caribbean_Blues".

Now for the easy part. Draw random stuff on the image. Or not random. It doesnt really matter. If you want to stick to a very set pattern, your texture might look a bit more orderly. Fill the image completely if you dont want alpha poking though. Nice eh?

<figure>
<img src="grad_example_1.jpg" alt="grad_example_1.jpg"/>
</figure>

The hard part is making the image tilable. The easiest way to do this is to offset your image by half its height, and half its width. Select <span class="filter"><Image> Layer -> Transform -> Offset</span>. Then choose the convient "x/2, y/2" option, and hit OK. Your image will now show what used to be at its edges at the center of the image. The secret to making tileable images is to make this transition smooth.

<figure>
<img src="grad_example_2.jpg" alt="grad_example_2.jpg"/>

<img src="grad_example_3.jpg" alt="grad_example_3.jpg"/>
</figure>

For gradient painting with grunge brushes, this typicaly just means painting along those lines. You probabaly want to give it a bit of character so it looks more natural. You will probabaly want to avoid painting at the edges of the image when you do this. But if you do, just repeat the above steps again and you should be fine.

<figure>
<img src="grad_example_4.jpg" alt="grad_example_4.jpg"/>
</figure>

Offset that image one more time (or not,actually...), and your ready to go.

## Things to tweak

Of course changing the gradient type, and the brush will have a big effect on the look of the texture, but so will more subtle things like the opacity of the brush, and the paint mode can make for some interesting effects. These type of textures also seem to work well for layering two or three textures together with different layer modes.

All in all, this is nice and simple, and fast way to create some colorful textures.

## Examples

<figure>
<img src="texture1.jpg" alt="texture1.jpg"/>

<img src="texture2.jpg" alt="texture2.jpg"/>

<img src="texture3.jpg" alt="texture3.jpg"/>

<img src="texture4.jpg" alt="texture4.jpg"/>
</figure>

Just some examples whipped up in a few minutes.

The original tutorial can be found [here](http://adrian.gimp.org/texture_tut/).

