Title: Meta 
Date: 2015-07-29T14:40:35-05:00
Modified: 2015-08-10T14:53:46-05:00
Author: Pat David
Summary: A page about the new site.
lang: en


I (Pat David) am creating this page to keep notes and information for building/maintaining the new site.

(Meta) pages of interest:

* [To Do](./to-do/)
* [Using Pelican](./using-pelican/)
* [Markdown Cheatsheet](./markdown.html)
* [Edit the Front Page]({filename}./frontpage.md)
* [Translations]({filename}./translating.md)

The work I am doing here is based on a couple of suggestions over the past year (or more, I'm sure) to refresh the design of WGO.
In particular, I had created a brief mockup to show and have been using that as a sort of visual guide for approaching the main page.
You can view that [mockup .PNG here](/images/mockup3.png) (~1.8MB), or a smaller preview:

<figure>
<a href="/images/mockup3.png"><img src="/images/mockup3_600.png" alt="GIMP Mockup Pat David"/></a>
</figure>



## Why

There are two main reasons for **Why** we might want to revamp the site: Modernization and Collaboration.


### Modernization

A new facelift for the website can't hurt from a PR standpoint.
We can also leverage more modern design ideas around responsiveness for various screen sizes.

There was no good method previously of writing news/blog-type postings that would easily maintain a post history that could be referred to.
A modernization effort can take that into account and allow for a means to post news items that will be archived and maintained for posterity.
For example, you can read about a [GIMP Perl release candidate from June, 2014](/news/2014/06/12/gimp-perl-release-candidate-ready-for-testing/), as well as have a permalink to that particular news item in the future.



### Collaboration

I have *no* data to back this up, but can't help feel that some of the lack of new tutorials or content for the site could be attributed to the convoluted ways to submit information 
(plus it is generally more lucrative for folks to host their own tutorials and content in an effort to monetize them vs. sharing them openly here -- that's a different issue).

If someone *does* want to submit new content, it can only be helpful to make the barrier to collaboration as low as possible.

Currently, if someone wants to contribute content, and test it before attempting to push it, they need to:

* Get a working instance of Apache httpd running (with SSI)
* Get familiar with git to pull down the current site
* Write everything in plain html

Some of these things are non-trivial.
Especially for someone who may be good at writing quality content but not technically inclined enough to stand up the build environment.

The [How](#how) section below covers the means to making things easier to test and contribute.



## What

I thought a bit about the main reasons a person would be visiting the site.
*What* is someone looking to do when coming to WGO?

These are what I thought would be the main reasons for visiting the site (in order):

1. Download/Get GIMP
2. Learn *about* GIMP
3. Learn *how to use* GIMP (tutorials + documentation)
4. News
5. Help the project (financially or manpower)

It seems like #2 could probably cease being a reason after someone has learned about the project.



## How

After talking with schumaml, it was decided to leverage the existing Python on the server to build the site.
Some research revealed that the most ubiquitous (read: maintained) static site generator for Python is [Pelican].

The basic workflow for just about any SSG (static site generator) is to take a directory full of content (writing, images, and other assets), then process them in some fashion before finally writing a new directory containing the site ready for upload.

The build systems will often help to abstract away portions of the underlying html.
For instance, many will take files written as [Markdown] or [reStructuredText], which are simpler format for writing content that can easily be parsed into html (or other formats).



### Python & Pelican

For anyone who wants to build and view the site, they will need only Python, and a couple of extra components (Pelican, Markdown, typogrify).
This is the same procedure anyone can use to test new content they would like to propose or push.

#### Getting a build environment

1. Install [Python].  
2.7.x is best, earlier versions are not supported.  
Only provisional support for 3.3+.
2. Install [Pelican].  
Simplest method is simply: `pip install pelican`
3. Install some extra components:
    * For [Markdown] support:  
    `pip install Markdown`
    * For fancy typography elements with [typogrify]:  
    `pip install typogrify`


For detailed information refer to the [Pelican documentation](http://docs.getpelican.com/en/stable/).



#### Building the site

Building the site is relatively straightforward:

From the project directory, simply invoke pelican:

`pelican`

If you are writing content or developing other parts of the site, there is an option to watch the directory of files for changes and to automatically re-compile the site as needed:

`pelican -r`

In some cases, it can be beneficial to avoid using the cache that Pelican creates internally (to help speed up the build).
To avoid using the cache, *and* to watch for changes and rebuild as necessary:

`pelican -r --ignore-cache`


#### Viewing the site

Python has a simple web server available to preview the site.

For Python 2:  
`cd output`  
`python -m SimpleHTTPServer`

For Python 3:  
`cd output`  
`python m http.server`

The site can then be accessed locally at:  
`localhost:8000`

Further notes on using Pelican can be found on the page [Using Pelican](./using-pelican).

## Who

<figure>
<img src="{attach}fluffle-puff.jpg" alt='Fluffle Puff'>
<figcaption>
This is not superfluous, it's a test of local image linking from this directory.
</figcaption>
</figure>


[WGO Redesign]: http://wiki.gimp.org/index.php?title=WGO_Redesign
[Markdown]: http://daringfireball.net/projects/markdown/ 
[reStructuredText]: http://sphinx-doc.org/rest.html
[WGO]: http://www.gimp.org "The GIMP Website"
[Pelican]: http://blog.getpelican.com/ 
[Python]:https://www.python.org/ 
[smartypants]:http://pythonhosted.org/smartypants/ 
[typogrify]: https://github.com/mintchaos/typogrify
