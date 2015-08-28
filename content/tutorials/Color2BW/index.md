Title: Converting Color Images to B&W
Date: 2002
Modified: 2015-08-28T15:01:29-05:00
Author: Eric R. Jeschke

<small>Text and images Copyright (C) 2002 [Eric R. Jeschke](mailto:ericNOSPAM@redskiesatnight.com) and may not be used without permission of the author.</small>

## Intention

<figure>
<img src="before-384x288.jpg" alt="before-384x288.jpg"/>
<img src="after-384x288.jpg" alt="after-384x288.jpg"/>
</figure>

In this tutorial I'll show you some different ways to convert color RGB images to B&W:

*   [the "standard" grayscale conversion operation](#grayscale).
*   [the desaturate operation](#desaturate).
*   [decomposing to RGB and using any one of the channels](#decomposeRGB).
*   [decomposing to HSV and using the Value (V) channel](#decomposeHSV).
*   [decomposing to LAB and using the Lightness (L) channel](#decomposeLAB).
*   [using the Channel Mixer filter](#channelmixer).

We'll examine each of these in turn.

## The Procedure

<figure>
<img src="image-original-481x397.jpg" alt="image-original-481x397.jpg"/>
</figure>

Here is an example image, loaded into GIMP. I thought it might look nice as a black and white image.

## <a name="grayscale">Via Grayscale</a>

<figure>
<img src="image-grayscale-481x397.jpg" alt="image-grayscale-481x397.jpg"/>
</figure><figure>
<img src="image-grayscale-zoom100-481x397.jpg" alt="image-grayscale-zoom100-481x397.jpg"/>
</figure>

Here is what I get if I use the standard mode change to grayscale from RGB.

Duplicate the original image (<kbd>Ctrl+D</kbd>) and right-click on the copy. Select <span class="filter"><Image> Image -> Mode -> Grayscale</span>. I don't know how this conversion works in GIMP, but I have read that Photoshop uses a standard mix of the RGB channels for their grayscale conversion: RED=30%, GREEN=59% and BLUE=11%. Supposedly this mix accounts for the eye's sensitivity to different colors. This formula does a pretty nice job in the general case, but some images do not work as well with it, particularly if the green channel component is not strong.

I suspect GIMP uses a similar formula. My experiments with the Channel Mixer (more on this below) support this.

## <a name="desaturate">Via Desaturate</a>

<figure>
<img src="image-desaturate-481x397.jpg" alt="image-desaturate-481x397.jpg"/>
</figure><figure>
<img src="image-desaturate-zoom100-481x397.jpg" alt="image-desaturate-zoom100-481x397.jpg"/>
</figure>

Here is what I get if I use desaturate instead. Duplicate the original image (<kbd>Ctrl+D</kbd>) and right-click on the copy. Select <span class="filter"><Image> Image -> Colors -> Desaturate</span>. Unlike the grayscale mode change above, the channels are not remixed in different percentages, so we should expect different results.

The result is visually different; note the increased contrast in the scales. Also, compare the 100% zoom views at right and in the previous grayscale example. You can see a lot more noise in the desaturated zoomed view (examine the blurred area below the spikes). The reason is that we are getting more blue and red channel noise, whereas in the grayscale mode change operation the algorithm is giving us a remix of 60% of the clean, detailed green channel.

## <a name="decomposeRGB">Via Decompose RGB</a>

<figure>
<img src="decompose-rgb-186x265.jpg" alt="decompose-rgb-186x265.jpg"/>
</figure>

<figure>
<img src="image-red-481x397.jpg" alt="image-red-481x397.jpg"/>
</figure><figure>
<img src="image-red-zoom100-481x397.jpg" alt="image-red-zoom100-481x397.jpg"/>
</figure>

<figure>
<img src="image-green-481x397.jpg" alt="image-green-481x397.jpg"/>
</figure><figure>
<img src="image-green-zoom100-481x397.jpg" alt="image-green-zoom100-481x397.jpg"/>
</figure>

<figure>
<img src="image-blue-481x397.jpg" alt="image-blue-481x397.jpg"/>
</figure><figure>
<img src="image-blue-zoom100-481x397.jpg" alt="image-blue-zoom100-481x397.jpg"/>
</figure>

A third method is to consider the red/green/blue channels of the image. Each one can be represented as an independent grayscale image. Right-click on the original image and select <span class="filter"><Image> Image -> Mode -> Decompose</span>. Select the RGB option and click OK.

Here you can see the three channels: red (top), green (middle) and blue (bottom). You can see that the red channel contains most of the luminance information as well as a lot of noise, the green channel has the least noise, and the blue channel has shadows and noise. Often the blue channel has the most noise, but not in this case.

Very often the green channel contains an excellent B&W version of the image. If nothing else, taking a look at the RGB decomposition is important to give you an idea of where the important information is in your image, and where the noise is.

## <a name="decomposeHSV">Via Decompose HSV</a>

<figure>
<img src="decompose-hsv-186x265.jpg" alt="decompose-hsv-186x265.jpg"/>
<img src="image-value-481x397.jpg" alt="image-value-481x397.jpg"/>
</figure>

Another possibility is to decompose to Hue/Saturation/Value components and consider the Value image (the other two are not usually useful for this purpose). Right-click on the original image and select <span class="filter"><Image> Image -> Mode -> Decompose</span>. Select the HSV option and click OK.

## <a name="decomposeLAB">Via Decompose LAB</a>

<figure>
<img src="decompose-lab-186x265.jpg" alt="decompose-lab-186x265.jpg"/>
<img src="image-lightness-481x397.jpg" alt="image-lightness-481x397.jpg"/>
</figure>

Yet another decompose option: LAB mode. Right-click on the original image and select Image/Mode/Decompose. Select the LAB option and click OK.

The Lightness component is a very interesting one because it contains all of the luninance information (whereas in RGB and HSV some of that information is spread into other components). You can very often see an expanded tonal range and discover hidden detail in the shadows by examining this component.

Not often useful by itself, but it can be combined with other layers for interesting results (see Tips at end of article).

**Note:** the LAB decompose option was not distributed with the version of GIMP I got (ver 1.2.3). I don't know whether it comes bundled with newer versions. I downloaded it from the [GIMP Plug-in Registry](http://registry.gimp.org/) and compiled it myself.

## <a name="decomposeCMYK">Via Decompose CMYK</a>

<figure>
<img src="decompose-cmyk-186x265.jpg" alt="decompose-cmyk-186x265.jpg"/>
<img src="image-black-481x397.jpg" alt="image-black-481x397.jpg"/>
</figure>

Just for fun I tried decomposing into CMYK. The Black channel is interesting: it resembles a negative.

## <a name="channelmixer">Via Channel Mixer</a>

<figure>
<img src="channelmixer-481x307.jpg" alt="channelmixer-481x307.jpg"/>
</figure>

<figure>
<img src="image-channelmixer-481x397.jpg" alt="image-channelmixer-481x397.jpg"/>
</figure><figure>
<img src="image-channelmixer-zoom100-481x397.jpg" alt="image-channelmixer-zoom100-481x397.jpg"/>
</figure>

The final technique is the Channel Mixer filter. Right-click on the original image and select <span class="filter"><Image> Filters -> Color -> Channel Mixer</span>.

You'll get a dialog box like the one at right. Click the checkbox that says Monochrome. Make sure the preview checkbox is also checked.

Now play around with the levels of the three channels, seeing the results in the preview window. If you don't want to change the overall brightness of the image then the three values should add up to 100%, but feel free to experiment (checking the "Preserve Luminosity" box will also preserve the overall brightness of the image--see the Tips section below for more explanation of this option). Dialing in Red=30%, Green=59%, Blue=11% ought to give you something that looks nearly identical to what you would get with a mode change to grayscale.

When you have something that looks decent in the preview, click OK. If you don't like the look of the result, Undo (<kbd>Ctrl+Z</kbd>) and reapply the filter with different settings (<kbd>Shift+Alt+F</kbd>).

The advantage of the channel mixer is (obviously) flexibility. I like to decompose and examine the individual RGB channels, as we did earlier. That way I can see what is good and bad about each, and then use the channel mixer to combine them accordingly. In this example, I could see that the green channel did not really have much to offer, and had the least contrast in the iguana's scales; still, I mixed in 30% to help with the noise. I liked the blue channel for the great contrast it adds to the scales. Red's got a lot of noise, but I mixed in just enough to use some of the contrast and luminance information. You can see from the close up that it isn't quite as good the grayscale version in terms of noise, but the noise isn't too bad, and the trade-off is a lot more contrast and interest in the overall tonalities of the image.

**Note:** the channel mixer plug-in was not distributed with the version of GIMP I got (ver 1.2.3). I don't know whether it comes bundled with newer versions. I downloaded it from [the GIMP Plug-in Registry](http://registry.gimp.org/plugin?id=1918) and compiled it myself.

## Tips

*   Once you have a good B&W version of your image you may be interested in adding some simulated film grain.
*   If you are wondering what the "Preserve Luminosity" option does in the Channel Mixer, I have the answer. I was curious myself, and asked the author of the Channel Mixer, Martin Guldahl, about it. This was his reply:   

    Hi Eric:   

    The 'Preserve Luminosity' option just maintains the luminosity at the same level regardless of the slider values.   

    For example, suppose the sliders were are Red:75%, Green:75%, Blue:0%. With 'Monochrome' on and the 'Preserve Luminosity' option off, the resulting picture would be at 75%+75%+0% =150%, very bright indeed. A pixel with a value of, say, R,G,B=127,100,80 would map to 127*0.75+100*0.75+80*8=170 for each channel. With the 'Preserve Luminosity' option on, the sliders will be scaled so they always add up to 100%. In this example, that scale value is 1/(75%+75%+0%) or 0.667\. So the pixel values would be about 113\. The 'Preserve Luminosity' option just assures that the scale values from the sliders always adds up to 100%. Of course, strange things happen when any of the sliders have large negative values.

## Other Examples

<figure>
<img src="middlesister-384x259.jpg" alt="middlesister-384x259.jpg"/>
</figure><figure>
<img src="middlesister-bw-384x259.jpg" alt="middlesister-bw-384x259.jpg"/>
</figure>

**Left image**: The original image.   
**Right image**: Converted using channel mixer (80% green, 20% red).

<figure>
<img src="example2-before-384x288.jpg" alt="example2-before-384x288.jpg"/>
</figure><figure>
<img src="example2-after-384x288.jpg" alt="example2-after-384x288.jpg"/>
</figure>

**Left image**: The original image.   
**Right image**: Converted using channel mixer.

## Further Reading

*   [A discussion of what's in the red, green and blue channels of a digital image](http://www.microweb.com/idig/content/seybold/imgchanl.htm).
*   A [Photoshop channel mixer tutorial](http://luminous-landscape.com/tutorials/b-w_better.shtml) on the [luminous landscape](http://www.luminous-landscape.com) web site.
*   [Carl Volk's Photoshop tips for converting color images to B&W](http://www.carlvolk.com/photoshop21.htm).
*   zuga.net: [Digital RGB to Greyscale Conversions](http://www.zuga.net/printer_55.shtml)
*   Ian Lyons Computer Darkroom: [Monochrome from Colour](http://computer-darkroom.com/tutorials/tutorial_2_1.htm)

The original tutorial used to appear on [gimpguru](https://web.archive.org/web/20140810135206/http://gimpguru.org/tutorials/color2bw/).

