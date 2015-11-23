Title: Translations (i18n)
Date: 2015-08-21T11:45:47-05:00
Author: Pat David
lang: en
slug: translations

Pelican already had a nice simple support for translating pages and articles.

To do a translation, simply create another file alongside the base file.
As long as the *slug* would be the same, one file would be considered a translation of the other.
Setting the `lang` attribute in the file metadata would signal what type of file it is.

<small>
The *slug* is currently generated from the filename.
</small>

As an example, this file is:

    content/about/meta/translating.md

And the metadata at the top of this file looks like this:

    Title: Translations (i18n)
    Date: 2015-08-21T11:45:47-05:00
    Author: Pat David
    lang: en

To create a translated version of this page, we would create a new file:

    content/about/meta/translating.fr.md

The metadata would look slightly different, in that the `lang` attribute would be different now:


    Title: Translations (i18n)
    Date: 2015-08-21T11:45:47-05:00
    Author: Pat David
    lang: fr

Otherwise everything else could stay the same.

When doing this, Pelican will now automatically list the translation(s) being available
(by default it is listed just under the title).
It would typically look like this (for a French translation being available):

    Translations: fr


## i18n_subsites

With the implementation of i18n_subsites, the behavior is mostly the same.

The difference now is that an entirely new sub-site is built.
The site with the old translations would serve a translated page, but it would be a simple static page.

This means that any links off the page to other content would bring you to the default language (en) again.
*If* that page had a translation, and you wanted to see it, you would have to click on the appropriate translation option again.

The single-page translation option doesn't have any mechanism for translating the templates as well (just the page content).

Implementation of the i18n_subsites plugin now allows an entire sub-site to be built based on the language option.
So clicking on a language translation for a page will now bring the user to the corresponding sub-site.

These are the sub-sites that get created for example:

    gimp.org/fr/about/...
    gimp.org/de/about/...

And so on for each translation.


### Fallback

A nice feature of the i18n_subsites plugin is that pages that are linked, but lack a translation, will still show the **en** version as a fallback.


### I Can't Believe That Worked...

So I had to hack at the `mimic_hierarchy` plugin again to fix one piece of small weirdness with i18n_subsites.

The problem was that if you had a file, and it's translation:

    /about/meta/index.md
    /about/meta/index.fr.md

Then the path/files that get created with i18n look like this, respectively:

    gimp.org/about/meta/index.html
    gimp.org/fr/about/meta/index.fr.html

Which is _less_ than ideal.  The reason is that if I wanted to get to the first instance with a pretty url, I could go to:

    gimp.org/about/meta/

Likewise, linking to that page internally could be done easily through either `{filename}` to the pre-rendered file:

    [A link to meta]({filename}../../about/meta/index.md)

Which would render this: [A link to meta]({filename}../../about/meta/index.md)

The problem with using this link is that if it is called from a translated page, it will cause it to lead back to the **en** version of the page.
A better solution would be to allow internal links to simply point to locations directly without having to worry about the sub-site.
Some different link types to test:

* [A link to meta](/about/meta/) `[A link to meta](/about/meta/)`  
    Leads back to english version of the site from everywhere.
* [<del>A link to meta</del>](./about/meta/) `[A link to meta](./about/meta/)`  
    Doesn't work right (as expected).
* [A link to meta](../../about/meta/) `[A link to meta](../../about/meta/)`  
    Leads to the translated version of the page correctly!
* [A link to meta](../meta/) `[A link to meta](../meta/)`  
    Also leads back to translated version of the page correctly.
* [A link to meta](./) `[A link to meta](./)`  
    Also leads back to translated version of the page correctly.

At the moment, we basically need to use relative links to the output files, which will then work no matter what the translation is it's used from.

The other option is to continue using direct linking to files pre-rendering, as in the Pelican manual (and above).
The writer just needs to be careful to link to the correct place when doing this.
