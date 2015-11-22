Title: 20 Years of GIMP, release of GIMP 2.8.16
Date: 2015-11-22T09:32:24-05:00
Category: News
Authors: Wilber
Status: draft

This week the GIMP project celebrates its 20th anniversay.

Back in 1995, University of California students, Peter Mattis and Kimball Spencer, were members of the eXperimental Computing Facility, a Berkeley campus organization of undergraduate students enthusiastic about computers and programming. In June of that year, the two hinted at their intentions to write a free graphical image manipulation program as a means of giving back to the free software community.

On November 21st, 20 years ago today, Peter Mattis [announced the availability](/about/prehistory.html#november-1995-an-announcement) of the "General Image Manipulation Program" on Usenet (later on, the acronym would be redefined to stand for the "GNU Image Manipulation Program"). 

<figure>
<img src='{filename}./images/201512birthday_975.png' alt='Wilber Birthday Strip'/>
</figure>

Since its public release the project has been evolving in many ways as a testbed for new ideas, which was considerably assisted by adding plug-in architecture. Over the years, GIMP amassed a huge amount of new features designed for all kinds of users and practical applications: general image editing, retouching and color grading, digital painting, graphic design, science imaging etc.

Between 2006 and 2012, the team collaborated with Peter Sikking of _man+machine works_ to define [product vision](http://gui.gimp.org/index.php/GIMP_UI_Redesign#product_vision) and improve user experience. Thanks to this collaboration GIMP's user interface has become more conventional for professional users, and various tools have become more powerful and easy to use. But more importantly, we got a much better idea how to design good interfaces.

In the past several years we've been working hard on porting GIMP to a newer image processing engine called GEGL. The switch to GEGL made us rewrite or at least tweak pretty much every part of GIMP's source code. Fortunately, this work is nearing completion, and you'll soon be able to benefit from all the changes that it's bringing.

## New Releases and The Future

To celebrate the 20th anniversary, we released an update of the current stable version of GIMP. Newly released [GIMP 2.8.16](/downloads/) features support for layer groups in OpenRaster files, fixes for layer groups support in PSD, various user inrterface improvements, OSX build system fixes, translation updates, and more changes.

Our immediate future plans are to release first public version in the unstable 2.9.x series that will feature fully functional GEGL port, 16/32bit per channel processing, basic OpenEXR support, vastly improved color management implementation, new tools, on-canvas preview for many filters, and more. This release will encompass over three years of work and become the first milestone towards 2.10.

Following v2.10 release, we shall complete the GTK+3 port that is required to bring back state of the art Wacom support for Windows users. When it's done and GIMP 3.0 is out, we shall finally be able to get started on some very exciting and much anticipated features like non-destructive editing. Please refer to [Roadmap](http://wiki.gimp.org/wiki/Roadmap) for more details.

## New website

In conjunction with the 20th anniversary we have updated and revamped the website. 
The vast majority of the work on the new website was done by [Pat David](http://blog.patdavid.net/).

The update (*finally*) includes some much needed improvements such as [news items] with permalinks and [full RSS/Atom feeds][].
The site is also now responsive to adapt to various screen sizes.
Try it on a mobile device or tablet!

[News items]: //www.gimp.org/news/
[full RSS/Atom feeds]: //www.gimp.org/feeds/atom.xml

<figure>
<img src='{filename}images/birthday2_500.png' alt='Wilber Birthday Snapshot' />
</figure>

<small>
Wilber & Co. comics courtesy of [Aryeom & Jehan](http://libreart.info/).
</small>
