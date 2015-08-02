Title: Meta
Date: 2015-07-29T14:40:35-05:00
Modified: 2015-07-29T14:40:43-05:00
Authors: Pat David
Summary: A page about the new site.



I (Pat David) am creating this page to keep notes and information for building/maintaining the new site.


## A Static Site

Technically, the previous site could be considered "static".
There was some simple templating that was occuring using server side includes (SSI) in Apache.
The previous site infrastructure was fast and worked very well.

*Unless* you consider it in the context of ease-of-use and collaboration.

Working directly on the website required a possible committer to:

* Get a working Apache instance up and running (including SSI)
* Get familiar with GIT
* Be comfortable writing everything in plain HTML.
* Understand how SSI works in Apache.

An argument could be made that perhaps having these requirements in place helps to weed out the less commited from collaborating... :)



### Barriers to Collaboration

As noted on the [WGO Redesign] page on the wiki:

>We (the royal 'We') could benefit from having more content on WGO, in particular tutorials.  
Lowering the barrier-to-entry can help entice users to generate new content.  
A new facelift can't hurt from a PR standpoint.

This redesign is an attempt to make the barrier to collaboration lower.
In particular, the main ways to accomplish this include:

1. Writing new content in a simplified format, such as [Markdown] or [reStructuredText][] (*the official documentation was hosted on sourceforge as part of docutils... so this link is to the Sphinx project*).  
Contributors who may be able to write quality material may *not* be comfortable writing in pure HTML.


[WGO Redesign]: http://wiki.gimp.org/index.php?title=WGO_Redesign
[Markdown]: http://daringfireball.net/projects/markdown/ 
[reStructuredText]: http://sphinx-doc.org/rest.html
