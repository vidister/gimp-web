Title: Creating Translations
Date: 2015-08-27T10:18:03-05:00
Author: Pat David
lang: en
slug: creating-translations

I am assuming you are reading this because you'd like to submit a translation of an article?

If so - YAY!
**Thank you** for contributing!

Creating a new translation of an existing article is fairly straightforward:

1. Find the source file to translate.
2. Create a new file in the same place, with the lang in the filename:  
    original: `translating.md`  
    translation: `translating.fr.md`

3. Add the `lang` metadata to both the original and translation file:  
    add `lang: en` to original  
    add `lang: fr` to translation (example for French)

4. To have different titles (translated title as well):
    * Add the same `slug` metadata to both files:  
        add `slug: unique-slug-name` to both original and translation file
    * Then each file can have different titles.

## Locate the Article You'll Translate

Find the article source you want to translate.
I will use this article you're reading as an example.
It can be found in the source at this location:

    /content/about/meta/translating.md

Now create a new file in the same location, with a slightly different filename to indicate the new language.
A handy convention to follow is to use the ISO 639-1 two-letter code for the new language in the filename.
So to include a French version of this page, we will create a new file:

    /content/about/meta/translating.fr.md


## Modify/Add to Metadata

### lang attribute

The metadata for this article looks like this (Markdown):

    Title: Creating Translations
    Date: 2015-08-27T10:18:03-05:00
    Author: Pat David

There needs to be an addition of a `lang` attribute to **both** the original and new translation of the article.
So this (english) version of the file must now get a `lang` attribute that identifies it as such:

**translating.md:**

    :::markdown hl_lines="4 4"
    Title: Creating Translations
    Date: 2015-08-27T10:18:03-05:00
    Author: Pat David
    lang: en

Similarly, the new translation file must also get a `lang` attribute for the new language:

**translating.fr.md**

    :::markdown hl_lines="4 4"
    Title: Creating Translations
    Date: 2015-08-27T10:18:03-05:00
    Author: Pat David
    lang: fr


### slug attribute & different title

If you want to use a translated version of the article title, it will require one extra piece of metadata to work properly.
(Hopefully temporarily - still working on this).

The addition of the `slug` attribute will let a different title be used in the translated version of the article.
The actual value of the attribute is left to the author to choose, but it *needs to match* in all the translations of a page.

So the base english article will need this `slug` attribute added:

**translating.md:**

    :::markdown hl_lines="5"
    Title: Creating Translations
    Date: 2015-08-27T10:18:03-05:00
    Author: Pat David
    lang: en
    slug: creating-translations

Any other translation will need *the exact same* slug added as well:

**translating.fr.md**

    :::markdown hl_lines="5"
    Title: Creating Translations
    Date: 2015-08-27T10:18:03-05:00
    Author: Pat David
    lang: fr
    slug: creating-translations

Once that is done, the `Title` attribute can be different between the two files and they will still be marked as translations of each other:

**translating.fr.md**

    :::markdown hl_lines="1"
    Title: Créer Traductions
    Date: 2015-08-27T10:18:03-05:00
    Author: Pat David
    lang: fr
    slug: creating-translations


<style>
.codehilite .err {
    border: none;
}
</style>
