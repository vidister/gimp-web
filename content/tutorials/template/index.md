Title: TITLE GOES HERE
Date: 2015-10-04
Modified: 2015-10-05T10:19:55-05:00
Author: YOUR NAME


Please use only permissive licensing, such as [CC-BY](http://creativecommons.org/licenses/by/4.0/) or [CC-BY-SA](http://creativecommons.org/licenses/by-sa/4.0/).
Something like the following works well:

<small>
<a href='http://creativecommons.org/licenses/by-sa/3.0/deed.en_US'>
<img class='cc-badge' src='/images/creativecommons/by-sa 80x15.png' alt='Creative Commons By Share Alike'/>
</a>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - TITLE (text & images)</span> by [Pat David](http://blog.patdavid.net) is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).
</small>


You can use standard [Markdown][] formatting for posts.
We have a short [Markdown reference][] here on gimp.org if you want to see it with our styling.

[Markdown]: https://daringfireball.net/projects/markdown/syntax
[Markdown reference]: /about/meta/markdown.html

This page is generated from a [Markdown][] source.  The source .md file for this page can be found on GIMP-web git:

<https://git.gnome.org/browse/gimp-web/plain/content/tutorials/template/index.md>

Pelican makes it easy to generate a Table of Contents for your tutorial based on headings.
Just include `[TOC]` on a line by itself where you'd like an automatic TOC list generated.

**Table of Contents:**

[TOC]

---


## Style Guide
Consider your content as an outline first if possible.  This will help you visualize the heading breakdown and will make it easier for readers to follow your content.


## Headings
Headings in Markdown are denoted using two different syntaxes (setext and atx).
Usually the `<H1>` element of a page is already being used for a title, so the tutorial should use at most H2 and below.
Thus, the easiest way to denote headings is using the atx-style:

```markdown
# This is an H1
## This is an H2
### This is an H3
...
###### This is an H6
```

Try to use logical heading structure for your tutorials.
It helps if you consider your tutorial as an outline first.


## Links
Markdown links are written in one of two ways, inline or reference.
The link text is delimited using [square brackets] in both ways.

**Inline** links are created by:

```markdown
Here's a link to [GIMP.org](https://www.gimp.org)
```

**Reference** links follow the link text with square brackets again with a label or reference for the link.  Then anywhere else in the document the link label is defined with the url:


```
Here's a link to [GIMP.org][wgo]

...more content...

[wgo]: https://www.gimp.org
```

**Note**: another type of reference link that works with our flavor of Markdown is to forgo the ref name, and instead refer to the link text:

```
Here's a link to [GIMP.org][]

...more content...

[GIMP.org]: https://www.gimp.org
```


## Images
The tutorial file structure tries to be self-contained.  This means that you should try to keep any assets needed for the tutorial together in the same directory (this helps with portability in case the tutorial gets used somewhere else).

You can insert images using Markdown like this (but should really use the `<figure>` option
described below):

```markdown
![Alt Text](wilber-big.png)
```

You can also use plain html (the Markdown parser will pass it through to the output page):

```html
<img src="wilber-big.png" alt="Alt Text">
```

In either case, the results will be the same:

![Alt Text]({filename}wilber-big.png)

There is a better way, though...


### Better Figures
It may make more semantic sense to encapsulate images inside of `<figure>` tags.
This will also allow the use of a `<figcaption>` element to provide a caption:

```html
<figure>
<img src="wilber-big.png" alt="Alt Text">
<figcaption>
A caption for the image/figure.
</figcaption>
</figure>
```

Which will result in:

<figure>
<img src="{filename}wilber-big.png" alt="Alt Text">
<figcaption>
A caption for the image/figure.
</figcaption>
</figure>

Use this form wherever an image is to be included (which _should_ be almost always).
(Possible exception use-cases might be right/left aligned small images that don't require a full figure+caption).


## GIMP Menu Commands
For consistency, there is a pre-defined class for referencing menu commands in GIMP, such as:

<div class='GIMPCmd'>Filters → Blur → Gaussian Blur</div>

Which can be accomplished using `class='GIMPCmd'` on a div (or a `<span>` or `<kbd>`):

```html
<div class='GIMPCmd'>Filters → Blur → Gaussian Blur</div>
```

This is used when referring to operations that require menu interactions with GIMP.
