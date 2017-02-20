Title: Image Formats Overview
Date: 2016-09
Modified: 2016-09-04T21:58:31-05:00
Author: Ofnuts
Template: page_author
Summary: Selecting the best image format for your purposes.

## Pros and cons of various images formats from a GIMP perspective

<br>

### XCF

#### Pros

* The Native GIMP image format. Everything is saved: layers, selections, channels, paths and more.

#### Cons

* Not a "display" format, even if you can find codecs to display thumbnails of XCF image in file explorers.
* Bulky.
* Color channels are coded in 8 bits (in GIMP 2.8).
 
#### Recommended uses

* Saving all GIMP work.

---

### JPG

#### Pros

* Compresses the files quite efficiently.
* Universally supported for display.

#### Cons

* Compression is "_lossy_" and it slightly alters the image data. In case of global changes (color, contrast...) repeated file editing will slowly degrade the image quality.
* At good quality levels, compression is invisible in photography, but can be seen (so called "artifacts") in computer-generated graphics and text.
* Doesn't support transparency.
* Color channels are coded on 8 bits.

#### Recommended uses

* Display of photography
* Storage of photography

[A more complete FAQ on the subject](http://www.faqs.org/faqs/jpeg-faq/part1/)


---

### PNG

#### Pros

* Lossless format, all pixels are kept.
* Supports partial transparency.
* Produces small files with most computer graphics.
* Supported by all browsers.

#### Cons

* Complex images (photos) are bulky.
* Color channels are coded in 8 bits.

#### Recommended uses

* Web page widgets: banners, buttons, frames, etc...
* Computer graphics.
* Screenshots (unless this screenshot contain mostly a photo).


---


### GIF

#### Pros

* Universally supported for animation.

#### Cons

* Only 256 colors per image, leads to blocky look.  
(a modern variant supports 256 colors per frame, but GIMP doesn't use it).
* Supports transparency but only as fully transparent/fully opaque.

#### Recommended uses

* Small animated images.  
(in all other still-image uses PNG is a better alternative, and for bigger animation modern HTML supports video)


---

### TIFF

#### Pros

* Lossless format, all pixels are kept.
* Color channels can be coded in 16 bits.
* Can store several images (layers).
* Supported by all image processing software.

#### Cons

* Can be bulky on complex images.

#### Recommended uses

* Storage and exchange of high quality images.

---


### Raw images formats (NEF (Nikon), CR2 (Canon)...)

#### Pros

* No loss of information from the camera sensor (in theory).
* High-depth color channels (12 or 14-bit).

#### Cons

* Proprietary (except DNG).
* Content format can change without notice (new camera models), this can impact support by your favorite software.
* Bulky.
* Not suitable for display.

#### Recommended uses

* Storage of camera output, but a secondary copy in some universal format could be a good idea.


There are of course many other image formats, but the formats above cover most uses. 
Use them unless you know better, they can usually be converted easily to any other format should the need arise.


<small>
<a href='http://creativecommons.org/licenses/by-sa/3.0/deed.en_US'>
<img class='cc-badge' src='/images/creativecommons/by-sa 80x15.png' alt='Creative Commons By Share Alike'/>
</a>
<br/>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - Image Formats Overview</span> by Ofnuts is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).</small>
