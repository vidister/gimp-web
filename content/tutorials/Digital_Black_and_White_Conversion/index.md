Title: Digital B&W Conversion
Date: 2002
Modified: 2015-09-23T12:05:07-05:00
Author: Pat David
Template: page_author


<small>
<a href='http://creativecommons.org/licenses/by-sa/3.0/deed.en_US'>
<img class='cc-badge' src='http://i.creativecommons.org/l/by-sa/3.0/80x15.png' alt='Creative Commons By Share Alike'/>
</a>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - Digital B&W Conversion (text)</span> by [Pat David](http://blog.patdavid.net) is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).</small>

## Intention

Black and White photography is a big topic that deserves entire books devoted to the subject. In this article we are going to explore some of the most common methods for converting a color digital image into monochrome in [GIMP](//www.gimp.org "GIMP Homepage").

There are a few things you should focus on in regards to preparing your images for a B&W conversion. You want to keep in mind that by removing color information you are effectively left with only tonal data (and composition) to convey your intentions.

<figure>
<img src="{filename}Into the Fog.jpg" alt="Into the Fog by Pat David" />
<figcaption markdown='1'>
<em>Into the Fog</em> by <a href="http://blog.patdavid.net">Pat David</a> (<a href="http://creativecommons.org/licenses/by-sa/4.0/">cc-by-sa</a>)
</figcaption>
</figure>

This can be both liberating and confining.

By liberating yourself of color data the focus is entirely on the subjects and composition (this is often one of the primary reasons street photography is associated with B&W). Conversely, the subjects and composition need to be much stronger to carry the result.

<figure>
<img src="{filename}nautilus.jpg" alt="Chambered Nautilus by Pat David" />

<figcaption>
Without color, the form and tones are all that’s left.<br/>
<em>Chambered Nautilus</em> by <a href="http://blog.patdavid.net">Pat David</a> (<a href="http://creativecommons.org/licenses/by-sa/4.0/">cc-by-sa</a>)
</figcaption>
</figure>

### Tonality

What I tend to refer to when using this term is the presence and relationship between different values of gray in the image. This can be subtle with smooth, even differences between values or much more pronounced.

When referred to as the singular _“tone”_, it is usually referring to a single value of gray in the image.

### Contrast

Contrast is the relative difference in tones between parts of an image. High contrast will have a sharper differentiation between tones, while low contrast will have less differences. Often, a straight conversion to grayscale can result in values that are all similar, yielding a tonally “flat” image.

Contrast is often considered in terms of the entire image _globally_, or in smaller sections _locally_.

### Dynamic Range

Dynamic range is the overall range of values in your image from the darkest to the brightest.

### The Approach

The approach we will take here is similar to what I had done in my film days. We’ll attempt to use different methods of grayscale conversion (and possibly blending them) to get to a working image that is as full of tonal detail as possible. Petteri Sulonen refers to this as his _“digital negative”_ — if you want a great look at a digital B&W workflow head over and read [his article](http://www.prime-junta.net/pont/How_to/n_Digital_BW/a_Digital_Black_and_White.html).

Then, with an image containing as much tonal detail as possible, we will modify it with adjustments of various types to produce a final result that is visually pleasing.

Before heading down that path, it may help to have a closer look at the tools being used. Let’s have a look at how an image gets displayed on your monitor first.

## Your Pixels and You

You are working in an RGB world when you stare at your monitors. Every single pixel is composed of 3 sub-pixels of Red, Green, and Blue.

<figure>
<img src="{filename}300px-TN_display_closeup_300X.jpg" alt="TN LCD Display 300X close up" />

<figcaption>
300X magnification of an LCD panel.<br/>
(Image from <a href="http://en.wikipedia.org/wiki/File:TN_display_closeup_300X.jpg">wikipedia</a>)
</figcaption>

</figure>

The variations in brightness of each of the sub-pixels will “mix” to produce the colors you finally see. The scales available in an 8-bit display are discrete levels from 0—255 for each color (2<sup>8</sup> = 256). So if all of the sub-pixel values are 0, the resulting color is black. If they are all 255, you’ll see white. Any other combination will produce some variation of a color.

<p class="color-ex color080205255" >
80, 205, 255 for instance
</p>
<p class="color-ex color255172080" >
or 255, 172, 80
</p>

<span>But what about 16-bit images?</span> Well - the data is still in the image file to correctly describe the colors at 16bit/channel, but most likely what you’ll be seeing on your monitor is an interpolation of the values to an 8-bit/channel colorspace. You should _always_ work in the highest bit depth color that you can, and leave any conversions to 8-bit for when you are saving your work to be viewed on a monitor.

The important point to take away from this is to realize that when all three color channels are the same value, you’ll got a grey color. So a middle gray value of 127, 127, 127 would look like this:

<p class="color-ex color127127127" >
127, 127, 127
</p>
<p class="color-ex color220220220" >
While this is a little brighter: 220, 220, 220
</p>

Very quickly you should realize that a true monochromatic grayscale image can display up to 256 discrete shades of gray going from 0 (pure black) to 255 (pure white), while for 16-bit images, 2<sup>16</sup> will yield 65,536 different shades. It is this limitation for purely gray 8-bit images that introduces artifacts over smooth gradations ([posterization](http://en.wikipedia.org/wiki/Posterization) or banding) — and is a good reason to keep your bit depths as high as possible.

## Getting to Grey

There are many different paths to get to a grayscale image and almost none of them are equal. They will all produce different images based on their method of conversion, and it will be up to you to decide which ones (or portions of) to keep and build upon to create your final result.

<figure class="big-vid">
<img src="{filename}Conversation in Hayleys.jpg" alt="Conversation in Hayleys by Pat David" />
<figcaption>
A combination of luminosity desaturation and GEGL C2G<br/>
<em>Conversation in Hayleys</em> by Pat David (<a href="http://creativecommons.org/licenses/by-sa/4.0/">cc-by-sa</a>)
</figcaption>

</figure>

For this tutorial we are going to try and cover as many different methods as possible. This means we’ll be having a look at:

*   Desaturate Command (Lightness, Luminosity, Average)
*   Channel Mixer
*   Decompose (RGB, LAB)
*   Pseudogrey
*   Layer Blending Modes
*   Film Emulation Presets
*   Combining these methods

One of these methods may work fine for you. Or, if you’re like me, it will most likely be a combination of one or more of these methods blended through a combination of layer masking and opacity adjustments.

## Desaturate (GIMP)

Perhaps the easiest and most straightforward path to a grayscale image is using the `Desaturate` command. It can be invoked from the [GIMP](//www.gimp.org "GIMP Homepage") menu:

<div class="MenuCmd"><span>Colors → Desaturate…</span></div>

There are three options available from this menu:

<figure>
<img src="{filename}GIMP desaturate dialog.png" alt="GIMP Desaturate Dialog" />
</figure>

Each of these options (Lightness, Luminosity, Average) will generate a grayscale image for you, but the difference lies in the _way_ they interpret the image colors into values of gray.

To illustrate the differences, consider the following two figures. One is a gradient of red, green and blue from black to full saturation. The other are overlapping circles of color in an additive mix.

<figure>
<img src="{filename}rgb-base.png" alt="RGB Base Gradient Image" />
<figcaption>Base RGB gradient of pure colors</figcaption>
</figure>

<figure>
<img src="{filename}rgb-mix-base.png" alt="RGB Base Mix Image" />
<figcaption>Base RGB (additive color) mix</figcaption>
</figure>

Let’s investigate each of the desaturation options on these test images.

### Lightness

The Lightness method will add the largest value of red, green _or_ blue and the smallest value, then divide the result by 2.

<p class="Cmd aside">½ × ( MAX(R,G,B) + MIN(R,G,B) )</p>

So, for instance, with an RGB value of 100, 20, 210, the equation would be:

<p class="Cmd aside">½ × ( <strong>210</strong> + <strong>20</strong> ) = 115</p>

Using the Lightness function on our test images yields the following results:

<figure>
<img src="{filename}rgb-lightness.png" alt="RGB Desaturate Lightness" />
<figcaption>Lightness conversion yields similar values regardless of color</figcaption>
</figure>

<figure>
<img src="{filename}rgb-mix-lightness.png" alt="RGB Lightness Mix" />
</figure>

This means that one channel is actually ignored in creating the final value.

### Average

Average will use the numerical average of the RGB values in each pixel.

<p class="Cmd aside">⅓ × ( R + G + B )</p>

<figure>
<img src="{filename}rgb-average.png" alt="RGB Desaturate Average" />
<figcaption>Averaging, the values will trend darker overall</figcaption>
</figure>

<figure>
<img src="{filename}rgb-mix-average.png" alt="RGB Average Mix" />
</figure>

### Luminosity

_Lightness_ and _Average_ both evaluate the final value of gray as a purely numerical function without regard to the actual color components. _Luminosity_ on the other hand, utilizes the fact that our eyes will perceive green as lighter than red, and both lighter than blue ([relative luminance](http://en.wikipedia.org/wiki/Luminance_(relative))). This is also why your camera sensor _usually_ has [twice as many green detectors as red and blue](http://en.wikipedia.org/wiki/Bayer_filter).

The weighted function describing relative luminance is:

<p class="Cmd aside">(0.2126 × R) + (0.7152 × G) + (0.0722 × B)</p>

<figure>
<img src="{filename}rgb-luminosity.png" alt="RGB Desaturate Luminosity" />
<figcaption>This is closer to how our eyes will actually perceive the brightness of each color</figcaption>
</figure>

<figure>
<img src="{filename}rgb-mix-luminosity.png" alt="RGB Luminosity Mix" />
<figcaption>
Notice the overwhelming contribution from green  
</figcaption>
</figure>

No one of these methods is necessarily any better than the other objectively for your own conversions. It really depends on the desired results. However, if you are in doubt about which one to use, _Luminosity_ may be the better option of the three to [more closely emulate](http://en.wikipedia.org/wiki/Luminosity_function) the brightness levels you will perceive.

### Examples

The image below, [Joseph N. Langan Park](http://www.flickr.com/photos/patdavid/3808678255), is an interesting example to see just how much green influences the conversion result using luminosity. Pay careful attention to what **Luminosity** does with the green bushes along the waters edge.

<figure>
<img src="{filename}langan.jpg" alt="Langan Park by Pat David" /> <br/>
<img src="{filename}langan-lightness.jpg" alt="Langan Park by Pat David" /> <br/>
<img src="{filename}langan-average.jpg" alt="Langan Park by Pat David" /> <br/>
<img src="{filename}langan-luminosity.jpg" alt="Langan Park by Pat David" /><br/>
<figcaption>Original, Lightness, Average, and Luminosity</figcaption>
</figure>

This shot of [Whitney](http://www.flickr.com/photos/patdavid/6231554301/) shows the effect on skin tones, as well as the change in her shirt color due to the heavy reds present. In just a **Lightness** conversion, the red shirt becomes relatively flat compared to her skin tones, but becomes darker and more pronounced using **Luminosity**. Her lips get a bit of a boost in tone in the **Luminosity** conversion as well.

<figure>
<img src="{filename}whitney.jpg" alt="Whitney by Pat David" /> <br/>
<img src="{filename}whitney-lightness.jpg" alt="Whitney by Pat David" /> <br/>
<img src="{filename}whitney-average.jpg" alt="Whitney by Pat David" /> <br/>
<img src="{filename}whitney-luminosity.jpg" alt="Whitney by Pat David" /><br/>
<figcaption>Original, Lightness, Average, and Luminosity</figcaption>
</figure>

## Channel Mixer

Using **Desaturate** lets you convert to grayscale based on pre-defined functions for calculating the final value, but what if you wanted even further control? What if you wanted to decide just how much the red channel should influence the final gray value, or to have more control over the ratios and weightings from each of the different channels independently? That’s precisely what the **Channel Mixer** will allow you to do.

For the examples below I’ll use a different color gradient test map going from blue to blue HSV gradient, with a gradient to black vertically. This represents the entire 8-bit colorspace.

<figure>
<img src="{filename}rgb-hsv.png" alt="RGB HSV Gradient" /> <br/>
<img src="{filename}rgb-hsv-lightness.png" alt="RGB HSV Gradient" /> <br/>
<img src="{filename}rgb-hsv-average.png" alt="RGB HSV Gradient" /> <br/>
<img src="{filename}rgb-hsv-luminosity.png" alt="RGB HSV Gradient" /><br/>
<figcaption>Gradient representing all the colors/shades in 8-bit sRGB colorspace.<br/>
Original, Lightness, Average, and Luminosity</figcaption>
</figure>

Take a quick moment to click through the various desaturation methods already mentioned.

The **Channel Mixer** can be invoked through:

<div class="MenuCmd"><span>Colors → Components → Channel Mixer…</span></div>

The dialog will look like this with the test gradient:

<figure>
<img src="{filename}channel-mixer.png" alt="GIMP Channel Mixer Dialog" />
</figure>

The **Channel Mixer** can be used to modify these channel on a full color image, but we are focusing on grayscale conversion right now. So check the box for _Monochrome_, which will disable the _Output channel_ option in the dialog (it’s no longer applicable). This will turn your preview into a grayscale image.

### Warning: Math Ahead

If you checked the _Monochrome_ option, and left the Red slider at 100, then you’d be seeing a representation of your image with no Green or Blue contribution (ie: you would basically be seeing the Red channel of your image):

<figure>
<img src="{filename}channel-mixer-red.png" alt="GIMP Channel Mixer monochrome full red" />
<figcaption>Basically just the red channel</figcaption>
</figure>

What this means is that with Green and Blue set to 0, the values of the Red are directly mapped to the output value for the grayscale image. If you were looking at a pixel with RGB components of 200, 150, 100, then the _Value_ for the pixel in this instance would become 200, 200, 200.

It’s also important to note that the sliders represent a _percent contribution to the final value_.

That is, if you set the Red and Green channels to 50(%), you would see something like this:

<figure>
<img src="{filename}channel-mixer-red50-green50.png" alt="GIMP Channel mixer monochrome 50% red and green" />
</figure>

In this case, Red and Green would contribute 50% of their values (with nothing from Blue) to the final pixel gray value. Considering the same pixel example from above, where the RGB components are 200, 150, 100, we would get:

<p class="Cmd aside" markdown='1'>
( 200 × 0.5 ) + ( 150 × 0.5 ) + ( 100 × 0 )  
( 100 ) + ( 75 ) + ( 0 ) = **175**
</p>

So the final grayscale pixel value would be: 175, 175, 175.

### Preserve Luminosity

<figure>
<img src="{filename}eleven.jpg" alt="Spinal Tap up to eleven" />
<figcaption>
<em>“These go up to 11”</em> — <a href="http://en.wikipedia.org/wiki/Up_to_eleven">Nigel Tufnel</a>
</figcaption>
</figure>

The astute will notice that the sliders actually have a range from -200 to 200. So you may be asking — what happens if two channels contribute more than what is possible to show?

Using the pixel example again, what if both the Red and Green channels were set to contribute 100%?

<p class="Cmd aside" markdown="1">
( 200 × 1.00 ) + ( 150 × 1.00 ) + ( 100 × 0 ) = **350**
</p>

While the **Channel Mixer** will allow us to set these values, we can’t very well set the grayscale pixel value to be 350 (in an 8-bit image). So anything above 255 will simply end up being clipped to 255 (effectively throwing away any tones above 255, bad!).

This means that you have to be careful to make sure that each of the three channel contributions don’t exceed 100 between all of them. 50% Red, 50% Green is ok — but 50% Red, 50% Green, _and_ 50% Blue (150%) will clip your data.

This is where the _Preserve Luminosity_ option comes into play. This option will scale your final values so the effective result will always add up to 100%. The scale factor from the above example would be calculated as:

<p class="Cmd aside" markdown="1">
<sup>1</sup>⁄<sub>( 1.00 + 1.00 + 0 )</sub> = **0.5**
</p>

So the value of **350** would be scaled by 0.5, giving the actual final value as 175. If _Preserve Luminosity_ is active, all the values would be scaled by this amount.

This is not to say that _Preserve Luminosity_ is always needed, just stay aware of the possible effects if you don’t use it.

#### Speaking of Luminosity

Previously we talked about the function used for desaturating according to _relative luminance_. If you’ll recall, the formula was:

<p class="Cmd aside" markdown="1">
( 0.2126 × R ) + ( 0.7152 × G ) + ( 0.0722 × B )
</p>

If you wanted to replicate the same results that `Desaturate → Luminosity` produces, you can just set the RGB sliders to the same values from that function (21.3, 71.5, 7.2):

<figure>
<img src="{filename}channel-mixer-lum.png" alt="GIMP Channel mixer luminosity values" />
<figcaption>Replicating the luminosity function</figcaption>
</figure>

If you’re just getting started with the **Channel Mixer**, this makes a pretty nice starting point to begin experimenting.

### Experimenting

A pretty landscape image by [Flickr](http://www.flickr.com) user [Cyndi Calhoun](http://www.flickr.com/people/cyndicalhounfineart/) serves as a nice test image for experimentation:

<figure class="big-vid">
<img src="{filename}cyndicalhounfineart-color.jpg" alt="Garden of the Gods by Cyndi Calhoun" />
<figcaption>
<a href="http://www.flickr.com/photos/cyndicalhounfineart/7990432224">Garden of the Gods - Looking North</a><br/>
by Cyndi Calhoun (<a href="https://creativecommons.org/licenses/by/2.0/">cc-by</a>)
</figcaption>
</figure>

You’ll want to keep in mind the primary RGB influences in different portions of your image as you approach you adjustments. For instance, this image (not coincidentally) happens to have strong Red features (the rocks), Blue features (the sky), and Green features (the trees).

Keep an eye on the individual channels from getting so bright that you lose detail (blowouts), or from crushing the shadows too much. Remember, you want to try to keep as much tonal detail as possible!

So, using the luminosity function as a starting point…

<figure class="big-vid">
<img src="{filename}cyndicalhounfineart-CM-luminosity.jpg" alt="Garden of the Gods by Cyndi Calhoun Luminosity" />
<figcaption>Straight conversion using the luminosity</figcaption>
</figure>

It’s not a bad start at all, but the prominence of the red rocks in the sunlight has been dulled quite a bit. It’s a central feature of the image and should really draw the eye towards it. So the reds could be more pronounced to make the stone pop a little more.

With the _Preserve Luminosity_ option checked, begin bumping the Red channel to taste.

<figure class="big-vid">
<img src="{filename}cyndicalhounfineart-CM-red-66.1.jpg" alt="Garden of the Gods by Cyndi Calhoun Red Channel" />
<figcaption>
Red channel bumped up to 66.1  
</figcaption>
</figure>

This gives a little more prominence to the red stone.

The Green channel seems ok, but for comparison try lowering it to about half of the Red channel value. Remember — _Preserve Luminosity_ is checked so the final values will scale to give Red values twice the weight as Green.

<figure class="big-vid">
<img src="{filename}cyndicalhounfineart-CM-green-33.jpg" alt="Garden of the Gods by Cyndi Calhoun Red Channel" />
<figcaption>
Green channel at ~half of Red.  
</figcaption>
</figure>

This brings up the shadow side of the central rocks a bit as well as adds some definition to the trees and vegetation. Also interesting is the apparent boost to the red rocks as well.

If you’re wondering why the red rocks got brighter as well, consider the math. Previously Red and Green were very near each other in value (around 70), so both colors had approximately equal weight. When Green got its influence cut in half, Red scaled to take a much larger influence, and because there was more red than green the final value will end up higher.

If we look at the RGB values of the red rocks, the values are roughly like this (ignoring Blue for the moment because for this example it’s staying constant): 226, 127.

If both Red and Green have equal influence, the final pixel value will be:

<p class="Cmd aside" markdown='1'>
( 226 × 0.5 ) + ( 127 × 0.5 ) = **176.5**
</p>

Now if Green is only half as strong as Red, the value will be:

<p class="Cmd aside" markdown='1'>
<sup>( 226 × 0.5 ) + ( 127 × 0.25 )</sup>⁄<sub>( 0.5 + 0.25 )</sub> = **193**
</p>

The result was divided by the influence amount to scale the way _Preserve Luminosity_ would. The final pixel value will become brighter in this case, which is why the red rocks got brighter with a decrease in the Green channel.

It should go without saying that the Blue channel will have a heavy influence on the sky (and many areas of the image in shadow). To add a little drama to the sky, try removing the Blue channel influence by setting it to 0:

<figure class="big-vid">
<img src="{filename}cyndicalhounfineart-CM-blue-0.jpg" alt="Garden of the Gods by Cyndi Calhoun Red Channel" />
<figcaption>Blue channel set to 0  
</figcaption>
</figure>

This will darken the sky up a bit (as well as some shadow areas).

Pay careful attention to what these changes do to the image in closer views. In this case there is a higher amount of banding and noise in the smooth sky if values get pushed too far. So try to approach it with a light hand.

The sliders also allow negative values. This will seriously crush the channel results when applied (and will quickly lead to funky results if you’re not careful). For example, to push the Blue channel even darker in the final result, try setting the Blue channel to -20:

<figure class="big-vid">
<img src="{filename}cyndicalhounfineart-CM-blue--20.jpg" alt="Garden of the Gods by Cyndi Calhoun Red Channel" />
<figcaption>Red: 66.1, Green: 33, Blue: -20  
</figcaption>
</figure>

The sky has become much darker, as have the shadow side of the rocks. There is an overall increase in contrast as well, but at the expense of nasty noise and banding artifacts in the sky.

<p class="aside" markdown='1'>
**General Rules of Thumb**  
The Red channel is well suited for contrast (particularly in the brighter tones).  
The Green channel will hold most of the details.  
The Blue channel contains grain and (often) a lot of noise.  
<br/>
In skin, the Red channel is very flattering to the final result and you’ll often get good results by emphasizing the Red channel in portraits.
</p>

### On Skin

The Red channel can be very flattering on skin and is a great tool to keep in mind when working on portraits. For instance, below is the color image of Whitney from earlier:

<figure>
<img src="{filename}whitney.jpg" alt="Whitney in color by Pat David" />
<figcaption>Whitney in color</figcaption>
</figure>

The straight _Luminosity_ conversion is below. Compare it to a version where the Red channel is set equal to the Green channel (giving a greater emphasis on the Reds):

<figure>
<img src="{filename}whitney-luminosity.jpg" alt="Whitney Luminosity by Pat David" /><br/>
<img src="{filename}whitney-bw-equal-RG.jpg" alt="Whitney Luminosity by Pat David" />
<figcaption>Whitney in Luminosity (top)<br/>
Whitney with Red channel = Green channel (bottom)</figcaption>
</figure>

### B&W Film Simulation

Due to the popularity of the **Channel Mixer** as a straightforward means of conversion with nice control over each of the RGB channel contributions, many people have used it as a basis for building profiles of what they felt was a close emulation to the tonal response of classic black and white films.

Borrowing the table from [Petteri Sulonen’s site](http://www.prime-junta.net/pont/How_to/100_Curves_and_Films/_Curves_and_films.html#N104E4), these are some common RGB Channel Mixer values to emulate some B&W films. These aren’t exact, of course, but some people may find them useful. Particularly as a starting-off point for further modifications.

<link rel='stylesheet' type='text/css' href='index.css' />

<table>
<thead>
<tr>
<th>Film</th>
<th>R, G, B</th>
</tr>
</thead>
<tbody>
<tr>
<td>Agfa 200X</td>
<td>18, 41, 41</td>
</tr>
<tr>
<td>Agfapan 25</td>
<td>25, 39, 36</td>
</tr>
<tr>
<td>Agfapan 100</td>
<td>21,40,39</td>
</tr>
<tr>
<td>Agfapan 400</td>
<td>20,41,39</td>
</tr>
<tr>
<td>Ilford Delta 100</td>
<td>21,42,37</td>
</tr>
<tr>
<td>Ilford Delta 400</td>
<td>22,42,36</td>
</tr>
<tr>
<td>Ilford Delta 400 Pro & 3200</td>
<td>31,36,33</td>
</tr>
<tr>
<td>Ilford FP4</td>
<td>28,41,31</td>
</tr>
<tr>
<td>Ilford HP5</td>
<td>23,37,40</td>
</tr>
<tr>
<td>Ilford Pan F</td>
<td>33,36,31</td>
</tr>
<tr>
<td>Ilford SFX</td>
<td>36,31,33</td>
</tr>
<tr>
<td>Ilford XP2 Super</td>
<td>21,42,37</td>
</tr>
<tr>
<td>Kodak Tmax 100</td>
<td>24,37,39</td>
</tr>
<tr>
<td>Kodak Tmax 400</td>
<td>27,36,37</td>
</tr>
<tr>
<td>Kodak Tri-X</td>
<td>25,35,40</td>
</tr>
</tbody>
</table>

There’s a good reason that **Channel Mixer** is such a popular means for converting an image to grayscale. It’s flexible and allows for a great level of control over the contributions from each channel.

Unfortunately the only way to preview what is happening is in the tiny dialog window. Even when zooming in it can sometimes be frustrating to make fine adjustments to the channel contributions.

## Decomposing Colors

Another method of converting the image to grayscale is to decompose the image into its constituent channels. When looking at the **Channel Mixer** previously, there was an option to set one of the RGB channels to 100 (and leaving the others at 0) that would isolate that specific channel.

If you wanted to isolate each of the RGB channel contributions into its own layer, it would be tedious to do manually. Luckily, GIMP has a built-in command to automatically **Decompose** the image into different channels:

<div class="MenuCmd"><span>Colors → Components → Decompose…</span></div>

Will bring up the **Decompose** dialog box:

<figure>
<img src="{filename}decompose-base.png" alt="GIMP Decompose color dialog" />
<figcaption>The <strong>Decompose</strong> dialog</figcaption>
</figure>

The options available are which _Color model_ to decompose to, and whether to create a new image with the decomposed channels as layers. If _Decompose to layers_ is not checked, there will be a new image for each channel separately (chances are that you’ll want to start out leaving this checked).

The most important option is which _Color model_ to decompose to. Up to now we have mostly been considering RGB, but there are other modes that might be handy as well. Let’s have a look at some of the most useful decomposition modes.

We will be using this image graciously provided by [Dimitrios Psychogios](https://plus.google.com/u/0/+DimitriosPsychogios/about):

<figure>
<img src="{filename}dmitrios-dice.jpg" alt="Dice by Dmitrios Psychogios" />
<figcaption><em>Dice</em> by <a href="https://plus.google.com/u/0/+DimitriosPsychogios/about">Dimitrios Psychogios</a> (<a href="http://creativecommons.org/licenses/by-sa/4.0/" title="CC-BY-SA">cc-by-sa</a>)</figcaption>
</figure>

### RGB(A)

This is the _Color mode_ that we’ve been focusing on up to now, and is usually the most helpful in terms of having multiple sources to draw from. This separates out the Red, Green, and Blue Channels into individual layers for you (and Alpha if your image has it).

<figure class="big-vid">
<img src="{filename}GIMP-Decompose-RGB.jpg" alt="Dimitrios Psychogios Dice decompose RGB" />
<figcaption>RGB decomposed.</figcaption>
</figure>

### HSV/HSL

Hue, Saturation, and Value/Lightness is another useful decomposition, though usually only the Value or Lightness is useful for B&W conversion.

<figure class="big-vid">
<img src="{filename}GIMP-Decompose-HSV.jpg" alt="Dimitrios Psychogios Dice decompose HSV" />
<figcaption>Hue, Saturation, Value (HSV) Channels</figcaption>
</figure>

The _Value_ in **HSV** is derived according to a simple formula:

<p class="Cmd aside" markdown='1'>
Value, V = MAX( R, G, B )
</p>

Which is basically just the largest value of Red, Green, or Blue.

<figure class="big-vid">
<img src="{filename}GIMP-Decompose-HSL.jpg" alt="Dimitrios Psychogios Dice decompose HSL" />
<figcaption>Hue, Saturation, Lightness (HSL) Channels</figcaption>
</figure>

The _Lightness_ in **HSL** is derived from this formula:

<p class="Cmd aside" markdown='1'>
Lightness, L = <sup>( MAX( R, G, B ) + MIN( R, G, B ) )</sup>⁄<sub>2</sub>  
</p>

Where _Lightness_ is simply determined as the average of the largest and smallest component of RGB.

While Hue and Saturation may seem interesting, it should be obvious that the most useful channels for a grayscale conversion here would likely be _Value_ or _Lightness_. Overall, _Lightness_ will tend to be a bit brighter than _Value_.

### LAB

There is far too much information concerning the [LAB colorspace](http://en.wikipedia.org/wiki/Lab_color_space) to really go into much detail here. Suffice it to say that the _L_ in _LAB_ is for **Lightness**, while _A_ and _B_ are for color opponents (**A** = Green⇔Red, **B** = Blue⇔Yellow).

The _LAB_ colorspace is based on a perceptual model (similar to the relative luminance previously discussed). In fact, the _Lightness_ in _LAB_ is calculated using the cube root of the luminance from that function.

<figure class="big-vid">
<img src="{filename}GIMP-Decompose-LAB.jpg" alt="Dimitrios Psychogios Dice decompose LAB" />
<figcaption>LAB Channels</figcaption>
</figure>

As you can see, the only channel of any use for a B&W conversion is really the **Lightness**, _L_ channel.

### CMY(K)

Cyan, Magenta, Yellow and (Black, K) are often discussed in terms of printing. When doing the decomposition in GIMP, you’ll have to invert the results to make them useful. Once you do, you may notice that they are, in fact, the same as RGB (for CMY decomposition):

<figure class="big-vid">
<img src="{filename}GIMP-Decompose-CMY.jpg" alt="Dimitrios Psychogios Dice decompose CMY" />
<figcaption>CMY conversion (inverted from direct conversion)</figcaption>
</figure>

CMYK produces a similar result, but adds another channel to control the level of black in the result. Inverting the _Black_, **K** channel yields something usable.

<figure>
<img src="{filename}GIMP-Decompose-CMYK.jpg" alt="Dimitrios Psychogios Dice decompose CMYK" />
<figcaption>CMYK conversion with the Black, <strong>K</strong> channel inverted</figcaption>
</figure>

### YCbCr

Anyone who has done video processing might recognize this colorspace representation, as it often shows up in digital video. _YCbCr_ is a means for encoding the RGB colorspace with three channels: _Luma_, **Y**, and two channels of Red (_Cr_) and Blue (_Cb_) chroma differences.

<figure class="big-vid">
<img src="{filename}GIMP-Decompose-YCbCr.jpg" alt="Dimitrios Psychogios Dice decompose YCbCr" />
<figcaption>YCbCr</figcaption>
</figure>

Try to use the _256_ variants of the ITU recommendations to allow the decomposition to span the full 256 values available (the non-256 versions will pad 16 to the range, only allowing values to go from 16-240).

### So What’s the Result?

Let’s summarize some of the most useful results from `Colors → Components → Decompose` for a B&W conversion:

*   RGB - All channels
*   HSV/HSL - V (Value) and L (Lightness)
*   LAB - L
*   CMYK - K
*   YCbCr - Y (Luma)

This gives a total of 9 different types of color mode conversions that may be useful for generating a B&W image. It helps to visually see all of the options at once to get a better feel for what is going on:

<figure class="big-vid">
<img src="{filename}GIMP-Decompose-All.jpg" alt="Dimitrios Psychogios Dice decompose All" />
<figcaption>
All 9 useful channels from <code>Colors → Components → Decompose</code>
</figcaption>
</figure>

Chances are that one of these conversions might prove useful as a direct B&W conversion.

It helps to notice that the first 4 conversions are all color channels, while the last 5 conversions are brightness values based on different functions for achieving the results (**K**, **V**alue, **L**ightness, **L**, **Y** (luma)).

#### The Script

I had previously written some Script-Fu to automate the task of generating these useful channel decompositions (it was tedious choosing each color model manually).

The script will take the active layer in an image, and decompose it to each of the useful color channels listed above, each on its own layer. Once downloaded and placed into your **Scripts** folder, the command can be found here:

<div class="MenuCmd"><span>Colors → Color Decompose…</span></div>

The Script-Fu for _Color Decompose_ can be downloaded here:  
[Color Decompose on GIMP Registry](http://registry.gimp.org/node/27745)  

#### Looking Forward

Likely that _some parts_ of _some conversions_ will be useful in some way. I am personally rarely satisfied with any of the straight conversion options on their own, but would like to pick and choose which parts of the image contain the best detail and tones from the different conversion options. The fun is then combining them in such a way so as to produce a final result that is pleasing.

## Pseudogrey

Pseudogrey (gr**_e_**y, not gray, per the original author, [Rich Franzen](http://r0k.us/rock/index.html)) is a means for increasing the available levels of _perceived_ gray in an image using a bit-stealing technique.

<figure class="big-vid">
<img src="{filename}Randi pseudogrey.jpg" alt="Randi pseudogrey by Pat David" />
<figcaption>
<em>Randi</em> in pseudogrey<br/>
by Pat David (<a href="https://creativecommons.org/licenses/by-sa/4.0/">cc-by-sa</a>)</figcaption>
</figure>

The basic approach in **Pseudogrey** is that you can achieve a much higher number of _perceived_ gray values in an image, if you allow some of the pixels to stray just a tiny bit away from pure gray. For instance, if a pixel value in a true gray image was: 180, 180, 180, **Pseudogrey** may actually make the pixel value something like 180, 18**1**, 180.

That is, the Green value may be just a bit higher. The [full post on Pseudogrey](http://blog.patdavid.net/2012/06/true-pseudogrey-in-gimp.html) goes into much more detail about the algorithm.

The results from using Pseudogrey will follow the same model as for Luminosity desaturation, but will provide a much larger range of tones (1786 possible shades vs 256 in a truly gray image).

There are a couple of ways to convert images to pseudogrey.

There is a Script-Fu available for download:

<p class="aside" markdown='1'>
The Script-Fu for _Pseudogrey_ can be downloaded here:  
[Pseudogrey on GIMP Registry](http://registry.gimp.org/node/26515)  
</p>

Once the file has been downloaded and placed into your _Scripts_ folder, the command can be found under:

<div class="MenuCmd"><span>Colors → Pseudogrey…</span></div>

Alternatively, if [G’MIC](http://gmic.sourceforge.net/ "G'MIC Homepage") is installed then the command can be found at the Black & white filter:

<div class="MenuCmd"><span>G’MIC → Black & white → Black & white</span></div>

At the end of all of the various options in the filter, there is a _Pseudo-gray dithering_ option to apply the algorithm at various levels (higher levels increase the distance from true gray for each pixel).

Pseudogrey can be helpful in areas with slight tonal value changes over a large area, as this is often where banding will become visible in an 8-bit image. While the differences may be slight in many cases, if allowing the tiniest amount of color shifting to creep into the image for an expanded tonal range is ok, then pseudogrey is a great option to have.

## GEGL C2G

The Generic Graphics Library (GEGL) is the underlying graphics engine for GIMP. There is one neat function in GEGL specificaly for B&W conversions called _Color 2 Grayscale_ (c2g). It can be found on the _Tools_ menu in GIMP:

<div class="MenuCmd"><span>Tools → GEGL Operation…</span></div>

Rolf Steinort covers c2g briefly in [episode 84 of Meet the GIMP](http://blog.meetthegimp.org/episode-084-the-3-letter-acronym-show/). [Paul Bou also looks](http://blog.wbou.de/index.php/2009/08/04/black-and-white-conversion-with-gegls-c2g-color2gray-in-gimp/) at using c2g for B&W conversions in a little more detail, and [Joel Cornuz also asks](http://jcornuz.wordpress.com/2009/05/30/could-this-be-the-ultimate-black-and-white-converter/) if c2g could be the “ultimate” B&W converter. It may not be worth all the hyperbole, but c2g does do some very interesting things.

The operation considers each pixel relative to its neighbors within a given radius. The value determined is evaluated as a function of perceived luminance weighted against neighboring pixels. The [description from GEGL.org](http://www.gegl.org/operations.html#op_gegl:c2g) is:

> Color to grayscale conversion, uses envelopes formed from spatial color differences to perform color-feature preserving grayscale spatial contrast enhancement

In practice, c2g will attempt to scale the values of pixels within its neighborhood (radius) to maximize contrast. What some people like about c2g is that the operation will also introduce a nice range of synthetic grain during the conversion. There are ways to minimize the resulting grain by adjusting settings, though.

Let’s consider this test image:

<figure class="big-vid">
<img src="{filename}Cars-Luminosity.jpg" alt="Deerfield Beach luminosity GIMP" />
<figcaption>
Straight <em>Luminosity</em> desaturation in GIMP
</figcaption>
</figure>

At first glance, GEGL c2g will likely produce ugly results. The default settings are not conducive to producing a pretty image:

<figure class="big-vid">
<img src="{filename}Cars-c2g-default.jpg" alt="Deerfield Beach c2g default GIMP by Pat David" />
<figcaption>
c2g conversion, default settings (radius 300, samples 4, iterations 10)  
</figcaption>
</figure>

The default settings will (usually) produce a nasty halo effect on edges where the radius is not large enough to fully consider transitions. The edges of the buildings/trees against the sky show this particularly. There is also an excessive amount of synthetic graininess to the result.

Tweaking parameters can lead to better results at the cost of processing time. GEGL c2g is not a fast algorithm.

Haloing can be decreased by increasing the radius and graininess can be decreased by increasing the samples or iterations. Iterations seem to have a larger effect on overall noisiness in the result but (again) at the cost of increased processing time.

<figure class="big-vid">
<img src="{filename}Cars-c2g-r750-s8-i15.jpg" alt="Deerfield Beach c2g r750 s8 i15 GIMP by Pat David" />
<figcaption>
Betters results after increasing some parameters (radius 750, samples 8, iterations 15)  
</figcaption>
</figure>

Increasing the radius helped to alleviate some of the halos and will allow the algorithm to spread the contrast over a larger area. The increase in samples and iterations helps to keep the noise down to a more manageable level as well. Refining even further yields slightly better results:

<figure class="big-vid">
<img src="{filename}Cars-c2g-r1500-s8-i20.jpg" alt="Deerfield Beach c2g r1500 s8 i20 GIMP by Pat David" />
<figcaption>
Betters results after increasing some parameters (radius 1500, samples 8, iterations 20)  
</figcaption>
</figure>

At this point the noise is nicely suppressed while the halos have mostly been eliminated. The overall image still has more contrast than the straight luminosity desaturation and the contrast has been _weighted for the surrounding pixels as well_.

If a luminosity desaturation will choose a pixel value based on the perceived color brightness, c2g will do the same in addition to weighting the result relative to neighboring pixels.

For example, below is an optical illusion showing the effect on perceived luminosity relative to nearby brightness:

<figure>
<img src="{filename}Same_color_illusion.png" alt="checkerboard luminosity optical illusion" />
<figcaption>Square A and B are the same value of gray!</figcaption>
</figure>

Squares A & B are the same exact shade of gray. The reason we perceive B as lighter than A is due to the way our eyes are perceiving nearby colors (and our expectations are strengthened by the checkerboard pattern as well).

The results of running the image through c2g aligns the pixel values closer to what our eyes see:

<figure>
<img src="{filename}illusion.png" alt="checkerboard luminosity optical illusion" />
<figcaption>After letting c2g do its thing</figcaption>
</figure>

This operation can be very handy for bringing out micro-contrasts in an image (or increasing global contrast at large radius settings).

## Conversion Examples

_Finally_, a look at a simple workflow for applying these various methods of grayscale conversion to arrive at a final result.

The overall workflow here will be to decompose the image to various grayscale layers. Then to investigate each of the different versions to identify features of interest aesthetically. Finally, combine the different decompositions and mask accordingly to highlight those features or tones.

### Pretty Woman

Do a [Creative Commons search](https://www.flickr.com/creativecommons) on Flickr, and it’s _very_ likely that photographer [Frank Kovalchek](https://www.flickr.com/photos/72213316@N00/) will show up in some fashion. He liberally licenses many photographs under [Creative Commons](http://creativecommons.org/) licenses, and we will be using one of his portraits for this first example.

<figure>
<img src="{filename}aldude-color.jpg" alt="GIMP B&W base image by Frank Kovalchek" />
<figcaption><a href="http://www.flickr.com/photos/72213316@N00/4589410278"><em>What a sweet looking portrait</em></a> by <a href="http://www.flickr.com/people/72213316@N00/">Frank Kovalchek</a> on Flickr (<a href="https://creativecommons.org/licenses/by/2.0/ "Creative Commons - By Attribution"">cc-by</a>)</figcaption>
</figure>

Utilizing [the script from earlier](#the-script) to quickly break the image down into multiple layers using different decomposition modes produces a nice array overview to consider:

<figure class="big-vid">
<img src="{filename}aldude-array.jpg" alt="GIMP B&W Decompose Array" />
</figure>

These various decompositions supply a large amount of possible variations in getting to a finished product. Keep in mind that the goal in this example is to maintain good tonal density as well as imparting a sense of texture and detail.

#### The Scarf

As good a starting point as any, consider the texture and detail of the scarf. Looking at the various decompositions in the array, the question you should be asking yourself is:

> Which of these results produces the best quality/texture in the fabric of the scarf?

Looking at the previews leads to three possible choices: _Luma Y709F_, _Luma Y470F_, and _HSL - Lightness_. Of those let’s go with _Luma Y709F_. This is very subjective, of course. The important point to take away is the choice being made due to qualities it possesses _for a particular purpose_.

<figure>
<img src="{filename}aldude-bw-y709f.jpg" alt="GIMP B&W y709f" />
<figcaption>The Y709F - Luma channel as a “base” layer - chosen for the fabric texture</figcaption>
</figure>

The main focus of the image will be the models face but you will still want to retain detail and texture in the scarf as well.

#### The Skin

Looking at the model and her skin there is already fine detail , but could use a bit more emphasis overall. Perhaps get the skin a little bit brighter and in a higher key to offset the dark background and the scarf. It would be nice to smoothen/soften the skin tones as well.

Keeping that in mind, look back at the various decompositions again, this time with an eye towards skin tones and her face. Not surprisingly, the **RGB - Red** channel looks very pretty (as well as the HSV - Value). It’s fairly common that the red channel will be complimentary on (Caucasian) skin. There is even an old trick to use the red channel as an overlay on a color image to help “enhance” skin tones.

So let’s try that here. Place the _RGB - Red_ channel over the _Luma - y709f_ channel and change the layer blending mode to **Overlay**.

<figure>
<img src="{filename}aldude-bw-y709f-Red-Overlay.jpg" alt="GIMP B&W y709f with Red channel Overlay" />
<figcaption>
Luma Y709F base, with Red channel over (layer blend mode: Overlay)  
</figcaption>
</figure>

Visually this appears to have more impact, but the skin may be blown out a little too much. One option to attenuate this would be to lower the opacity on the _RGB - Red_ layer.

Also, note that very often the visual impact may also be due to the higher contrast in the image at this point. Sometimes it’s best to stand up and look away from the image for a while before committing to a change…

The problem with adjusting the opacity for the entire layer is that the ratio of levels between the skin and scarf may not be desirable for the final output. Adjusting the opacity might reduce the effect on the skin, but at the same time will reduce the effect on the scarf by an equal amount. What is needed is a way to apply the effect stronger on the scarf or skin separately.

This is exactly what _Layer Masks_ are for!

#### Masks

At this point a layer mask could be added to the _RGB - Red_ layer, and then painted by hand to modify the intensity by isolating the face and giving a little less opacity to the scarf. It’s a lot of tedious, detailed work.

However, if you look back on the array of decompositions you may notice that channels like _RGB - Blue_ and _RGB - Green_ look pretty good for isolating the face from the scarf already.

So we are going to use the _RGB - Green_ layer and apply it as a layer mask to the _RGB - Red_ layer.

The **Layers** palette should look something like this in GIMP now:

<figure><img src="{filename}aldude-bw-y709f-RoverlayMask-Layers.png" alt="GIMP Layer Palette with layer mask" /></figure>

Keep in mind, a layer mask will be more transparent the darker the color is in it. The lighter areas will show more of the layer it is applied to. In this case, the lighter areas will allow more of the _RGB - Red_ layer to show, while darker areas will show more of the layer below, _Luma - Y709F_.

The results at this point with the mask:

<figure><img src="{filename}aldude-bw-y709f-Red-Overlay-Masked.jpg" alt="GIMP B&W y709f with Red channel Overlay" />
<figcaption><em>RGB - Red</em> as overlay with <em>RGB - Green</em> as a layer mask  
</figcaption>
</figure>

What this has done is to isolate the models face from the surrounding scarf. You can now modify the opacity of the layer, or adjust the values of the mask using _Levels_ or _Curves_ to adjust the intensity of the result.

Any changes to the _RGB - Red_ layer will now be masked to apply mainly to the models face.

Looking at the results, the scarf has become much more flat in tones, while the models face has brightened up. Considering it, the ratios look backwards a bit. The scarf has flattened out, and the face has brightened a bit too much.

To flip the ratios, simply invert the colors of the layer mask. Select the _mask_ (not the layer itself!), and run:

<div class="MenuCmd"><span>Colors → Invert</span></div>

The layers palette will now look like this:

<figure><img src="{filename}aldude-bw-y709f-RoverlayMaskInvert-Layers.png" alt="GIMP Layer Palette with inverted mask" /></figure>

The result on the image so far:

<figure><img src="{filename}aldude-bw-y709f-Red-Overlay-Masked-Inverted.jpg" alt="GIMP B&W y709f with Red channel Overlay" />
<figcaption>Inverted mask results  
</figcaption>
</figure>

At this point the results look pretty nice and would make a fine stopping point. The overlay and mask added some nice depth to the scarf fabric while maintaining a nice effect on the skin of the model as well. More work could be done if wanted with adjusting layer mask levels and increasing/decreasing the results on the models skin but this looks good as it is.

A final comparison of the results against a straight color desaturation:

<figure>
<img src="{filename}aldude-desaturation.jpg" alt="GIMP B&W Desaturation" /><br/>
<img src="{filename}aldude-bw-y709f-Red-Overlay-Masked-Inverted.jpg" alt="GIMP B&W y709f with Red channel Overlay" />
<figcaption>
Straight desaturation (top)<br/>
Final result (bottom)
</figcaption>
</figure>

This path was a little fussier than doing a straight color desaturation but the results are much nicer and is visually more interesting.

### Methuselah

Well, this isn’t the _actual_ [Methuselah](http://en.wikipedia.org/wiki/Methuselah_(tree)), but it is a similar species of Bristlecone Pine. Once again, image courtesy of [Flickr](http://www.flickr.com) user [Frank Kovalchek](http://www.flickr.com/people/72213316@N00/).

<figure><img src="{filename}aldude2-color.jpg" alt="GIMP B&W Base Image 2 by Frank Kovalchek" />
<figcaption>
<a href="http://www.flickr.com/photos/72213316@N00/6956555116"><em>Bristlecone pine hanging on for dear life at 10,000 feet</em></a> <br/> 
by <a href="http://www.flickr.com/people/72213316@N00/">Frank Kovalchek</a> on Flickr (<a href="https://creativecommons.org/licenses/by/2.0/">cc-by</a>)</figcaption>
</figure>

As before, a first look at multiple decomposition modes originally pointed to _Luma - Y709F_ as being a good candidate for the conversion. In this case, the focus would be on the texture of the tree itself. The _RGB - Green_ decomposition also looks quite good to use as a base moving forward.

The primary focus is the gnarled old tree itself and the secondary focus the lighting of the sun across the ground.

<figure><img src="{filename}aldude2-bw-green.jpg" alt="GIMP B&W Base Image 2 Green Channel" />
<figcaption><em>RGB - Green</em> channel decomposition</figcaption>
</figure>

While the _RGB - Green_ channel is nice for the tree texture, the sky still appears too bright and the ground could be a bit darker compared to the tree. The sunlight on the upper branches of the tree and topping the brush on the ground gets slightly lost when the sky is so bright comparatively.

Having found a good layer for the tree texture, the other decompositions are examined for something that represents the sky and ground a little better. The _RGB - Red_ channel is a good compromise (the _RGB - Blue_ channel is a little too noisy).

<figure><img src="{filename}aldude2-bw-red.jpg" alt="GIMP B&W Base Image 2 Green Channel" />
<figcaption><em>RGB - Red</em> channel decomposition  
</figcaption>
</figure>

_RGB - Red_ looks like a great candidate for the sky and ground, while _RGB - Green_ will do nicely for the tree textures. As before, layer masks can be used to modify the mix of the two layers to arrive at a final result.

Set the _RGB - Green_ channel above the _RGB - Red_ channel on the layer palette, and add a layer mask to the _RGB - Green_ channel layer initialized to **Black (full transparency)**. This lets all of the underlying _RGB - Red_ channel layer show through.

<figure><img src="{filename}aldude2-bw-green-Layers.png" alt="GIMP B&W Green channel with mask" />
<figcaption>Red channel layer, with Green channel over + mask</figcaption>
</figure>

Now with the layer mask active (see the white outline around the layer mask, not the layer itself above), paint with a white color to allow that portion of the _RGB - Green_ channel layer to show through. When painting with white, it will turn the current layer the mask is associated with opaque in those areas — so focus on painting white where the tree is.

Below is a quick mask to illustrate.

<figure><img src="{filename}aldude2-bw-green-mask.jpg" alt="GIMP B&W Tree Layer Mask" />
<figcaption>It’s only a quick mask, don’t judge it too harshly…</figcaption>
</figure>

The layers at this point will look like this:

<figure><img src="{filename}aldude2-bw-green-Layers-mask.png" alt="GIMP Layer Mask B&W Dialog" /></figure>

The results from applying the mask above to the image:

<figure><img src="{filename}aldude2-bw-greenred-masked.jpg" alt="GIMP B&W Tree Final" />
<figcaption>Final blend of <em>RGB - Red</em> and <em>RGB - Green</em> channels with mask  
</figcaption>
</figure>

This could be a good final version, though there is still a bit of noise in the upper-left corner of the sky from the Red channel. This could be fixed by adding another layer mask just for the sky which would allow adjustments to the levels of the sky relative to everything else.

## Grain

Following some ideas from the great tutorial by Petteri Sulonen on [Digital Black and White](http://www.prime-junta.net/pont/How_to/n_Digital_BW/a_Digital_Black_and_White.html), he speaks a bit about grain in B&W images. There are a few different methods of adding synthetic grain to an image but visually the results are less than impressive.

Petteri was kind enough to make available a grain field that he processed himself from scanned film. An easy way to add grain to an image using this grain field is to add it as a layer over the image, set the layer blending mode to _Overlay_, and adjust opacity to suit.

<figure><img src="{filename}aldude2-100-grain.png" alt="GIMP B&W Tree Grain Comparison" />
<figcaption>100% crop with Petteri’s grain field applied as <em>Overlay</em> layer</figcaption>
</figure>

You can download the grain-field to use here: [Petteri Sulonen’s grain field](http://farm8.staticflickr.com/7228/7314861896_292120872b_o.png).

## Conclusion

There are many ways to get to a monochrome image. The important process to take way from this article is to consider _elements_ of the final image as built up from multiple conversion methods, and controlling/applying them as needed to serve the final result best.

Mix and match the methods presented here to get to the best base for further modifications.

## Further Reading

*   [Layer Masks](../Layer_Masks)
*   [Luminosity Masks](../Luminosity_Masks)
*   [Getting Around in GIMP - Luminosity Masks & Split Toning](http://blog.patdavid.net/2011/10/getting-around-in-gimp-luminosity-masks.html)
*   [Getting Around in GIMP - Luminosity Masks Revisited](http://blog.patdavid.net/2013/11/getting-around-in-gimp-luminosity-masks.html)
*   [Pixls.us - Digital B&W Conversion (GIMP)](http://pixls.us/articles/digital-b-w-conversion-gimp/)

The original tutorial this was adapted from may be found [here](http://blog.patdavid.net/2012/11/getting-around-in-gimp-black-and-white.html) and [here](http://pixls.us/articles/digital-b-w-conversion-gimp/) (possibly with updated information).

The old _"Converting Color Images to B&W"_ tutorial can be found [here](../Color2BW/).

<small>
<a href='http://creativecommons.org/licenses/by-sa/3.0/deed.en_US'>
<img class='cc-badge' src='http://i.creativecommons.org/l/by-sa/3.0/80x15.png' alt='Creative Commons By Share Alike'/>
</a>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - Digital B&W Conversion (text)</span> by [Pat David](http://blog.patdavid.net).  
Licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).</small>
