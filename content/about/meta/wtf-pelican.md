Title: WTF Pelican?
Date: 2015-08-05T17:07:40-05:00
Modified: 2015-08-05T17:07:46-05:00
Author: Pat David



## All I Wanted to do...

So I wanted to work on being able to organize the content in a meaningful way.

I had two things in mind,

1. Keep discrete content inside their own folders.
 In particular this is handy for tutorials, where the tutorial files and all of its assets (images, scripts) are all contained in the same folder.
2. Each folder would represent a base url path on its own.  
 This means that for an **About** page, the folder would be `/content/about/`, and the page for it would be `/content/about/index.html`.

For a given input folder, and file, such as:

`/content/about/`  
`/content/about/index.md`

There would be a generated url/file as:

`gimp.org/about/`  
`gimp.org/about/index.html`

This way, nested folder structures in the `content` folder would be mirrored on the final site URL paths.

The addition of a second file under the same directory:

`/content/about/ancient_history.md`

Would properly render as:

`gimp.org/about/ancient_history.html`



### Nested Folders

This works well for extra nested folders, such as the [Tutorials](/tutorials/) section of the site.
The old structure had a `/tutorials/` page that then listed all of the tutorial directories under it:

```
/tutorials/
/tutorials/GIMP_Quickies/
/tutorials/Layer_Masks/
```


## What Did you do Ray?
<figure>
<img src="https://upload.wikimedia.org/wikipedia/en/d/d8/Stay-puft-marshmallow-man.jpg" alt="Stay Puft" title='Ray, when someone asks you if you&rsquo;re a god, you say "YES"!' />
<figcaption>
*It's the Stay Puft Marshmallow Man...*
</figcaption>
</figure>

The problem is, Pelican doesn't want to do this naturally.
There were a couple of plugins that produced similar type of output but wasn't *quite* the same thing.

The closest thing I could find was a plugin on the plugin repository called [*Page Hierarchy*](https://github.com/akhayyat/pelican-page-hierarchy).

This plugin was close, but was missing a few things that I had to add.

1. OS-agnostic file system separators.   
This was a simple fix that was already pushed to the plug-in author.

2. The metadata override was a little more problematic.  
Basically, the plug-in was overriding the *slug* object with a custom one for the nesting based on the filesystem.
All I did was continue that line of thought and brute-forced the index.md under each directory to the right slug.

        :::python
        # PLD: this is my doing, sorry...
        # ok, if path is empty, use page.slug
        # if path is not empty, use path
        # still need to test if lang works properly after this
        if path:
            print( "got path" )
            print( path )
            metadata['slug'] = path
        else:
            print( "path empty!" )
            print( page.slug )
            metadata['slug'] = page.slug

        if metadata['filename'] != 'index.html':
            setattr(page, 'override_url', metadata['slug'] +'/'+ metadata['filename'] )

So far, so good?  Nothing seems to explode, so I'm taking that as a positive sign.
The only thing I haven't checked yet (and that I think will be awesome) is the ability to provide translated versions of all pages.
I may have to wrangle someone to translate a page for me to test with (or just use gibberish to test, I guess).



### Slugs and Filenames

In migrating some of the old pages from the previous site, I found that a few of them existed off of the base URL for the site.
This was slightly problematic, as the nested folders all assumed content would exist at least under a single directory from the URL root (except for the index.html page of course).

The page I tested this on is www.gimp.org/irc.html.

To fix it we override the *url* and *save_as* metadata in the file to force a particular file:

    :::markdown
    Title: IRC Page Example
    Author: Pat David
    Date: 2015-08-12T14:03:57-05:00
    url: irc.html
    save_as: irc.html

Which will then force the file to be saved as (and referred to by url):

    www.gimp.org/irc.html

This is not a thing that should normally have to happen that often.
I am only doing it this way to support a few legacy pages that will exist directly on the root URL.

Those pages currently are:

* [archive.html](http://www.gimp.org/archive.html)  
    An archive of news items that were on the front page.
    Likely deprecated for the "News" section now?
* [index.html](http://www.gimp.org/index.html)  
    The main page (still).
* [irc.html](http://www.gimp.org/irc.html)
* [mail_lists.html](http://www.gimp.org/mail_lists.html)
* [team.html](http://www.gimp.org/team.html)
* [template.html](http://www.gimp.org/template.html)  
    This seems to be a simple test page.
* [webmasters.html](http://www.gimp.org/webmasters.html)
