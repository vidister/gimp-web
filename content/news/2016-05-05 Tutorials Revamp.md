Title: Revamping Tutorials
Date: 2016-05-05
Category: News
Authors: Pat David
Status: draft

As part of building a new GIMP website we had to sort through all of the legacy pages in order to migrate content properly. A nice side effect of this sorting included addressing [tutorials][tuts] that were out of date (or in some cases, _really_ out of date).  This gave us an opportunity to re-build the tutorials index to focus on (_more_) current content as well as ensure that everything is being licensed in a permissive manner.

[tuts]: //www.gimp.org/tutorials/



## Cool URIs don't change

It was [true in 1998][cool] and is still just as true today. Possibly more so.  Great care was taken to make sure that we didn't break all of the inbound links to the old tutorials during the site update.

[cool]: https://www.w3.org/Provider/Style/URI.html

This means that if there were any links to the previous tutorials they will still work.  They are still at the same URL they had always been.  What we _did_ change was the listing of [tutorials on the index page][tuts]:  

[www.gimp.org/tutorials/][tuts]

That list now includes only more current content that has been permissively licensed for use. If you need the deprecated tutorials for some reason, see [the complete list](/tutorials/list-all.html).

An unfortunate side-effect of pruning old material is that we are now a little light on good tutorials...



## Help Write More Tutorials

Which is where you, the community, comes in! If you were looking for a way to contribute to the project, and you don't feel up to coding<sup>*</sup>, this is a great way to share and help others learn GIMP. We encourage you to come tell us about your tutorial on [the gimp-user mailing list][gu-mail] or, even better, drop by the [IRC channel][irc] and let us know what you're thinking (this is strongly encouraged to make sure there's not something already being worked on)!

[irc]: /irc.html
[gu-mail]: https://mail.gnome.org/mailman/listinfo/gimp-user-list

<small><sup>*</sup>Of course, if you _do_ feel up to coding we'd [love to hear from you too][]!</small>

[love to hear from you too]: http://testing.gimp.org/develop/

There's usually helpful team members around who can guide you with both ideas and content if needed.
We have a tutorial [template][tt] and the markdown file used to generate it can be [found on git][]. More information can be found on the [template tutorial page][tt].

[tt]: /tutorials/template/
[found on git]: https://git.gnome.org/browse/gimp-web/plain/content/tutorials/template/index.md

We can use tutorials of all types and skill levels so don't feel intimidated by what you might see on the current tutorials page.  Indeed many common questions we see might have solutions that are not obvious to others - the perfect opportunity to write a tutorial about it!  All proposed tutorials will absolutely be considered.



## New Tutorial - Tone Mapping with Levels

Speaking of tutorials, [Elle Stone][] has just [published a new tutorial][tut] on doing some simple tone mapping and shadow recovery of images using high bit depth GIMP and the GEGL _Exposure_ operation.

[Elle Stone]: http://ninedegreesbelow.com/
[tut]: /tutorials/Tone_Mapping_Using_GIMP_Levels/

<figure>
<img src='{filename}../tutorials/Tone_Mapping_Using_GIMP_Levels/gegl-exposure-add-one-stop-positive-exposure-compensation.jpg' alt='GEGL Exposure'>
<figcaption>
The GEGL <i>Exposure</i> dialog.
</figcaption>
</figure>

The tutorial covers a method for adding exposure compensation to an image's shadows and midtones while retaining highlight details.  She does this using _Exposure_ and combining the results with a mask based on a grayscale version of the working image (simliar to using a [luminosity mask][]).
This is also one of the first tutorials using the high bit depth version of GIMP.  Head over to the [tutorials][tuts] page and have a look:

[luminosity mask]: /tutorials/Luminosity_Masks/

[Tone Mapping and Shadow Recovery Using GIMP's 'Colors/Exposure'][tut]
