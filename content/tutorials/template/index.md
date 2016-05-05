Title: TITLE GOES HERE
Date: 2015
Modified: 2015-10-05T10:19:55-05:00
Author: Pat David


Please use only permissive licensing, such as [CC-BY](http://creativecommons.org/licenses/by/4.0/) or [CC-BY-SA](http://creativecommons.org/licenses/by-sa/4.0/).
Something like the following works well:

<small>
<a href='http://creativecommons.org/licenses/by-sa/3.0/deed.en_US'>
<img class='cc-badge' src='https://i.creativecommons.org/l/by-sa/3.0/80x15.png' alt='Creative Commons By Share Alike'/>
</a>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - TITLE (text & images)</span> by [Pat David](http://blog.patdavid.net) is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).
</small>


You can use standard [Markdown][] formatting for posts.

[Markdown]: https://daringfireball.net/projects/markdown/syntax


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


## Images

You can insert images using Markdown like this:

```markdown
![Alt Text](/images/frontpage/wilber-big.png)
```

You can also use plain html (the Markdown parser will pass it through to the output page):

```html
<img src="/images/frontpage/wilber-big.png" alt="Alt Text">
```

In either case, the results will be the same:

![Alt Text](/images/frontpage/wilber-big.png)


### Better Figures

It may make more semantic sense to encapsulate images inside of `<figure>` tags.
This will also allow the use of a `<figcaption>` element to provide a caption:

```html
<figure>
<img src="/images/frontpage/wilber-big.png" alt="Alt Text">
<figcaption>
A caption for the image/figure.
</figcaption>
</figure>
```

Which will result in:

<figure>
<img src="/images/frontpage/wilber-big.png" alt="Alt Text">
<figcaption>
A caption for the image/figure.
</figcaption>
</figure>
