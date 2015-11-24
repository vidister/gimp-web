Title: Git Workflow 
Date: 2015-11-23T16:46:14-05:00
Author: Pat David
Summary: What the workflow should be with branches test and master.

<figure>
<img src="//imgs.xkcd.com/comics/git.png" title="If that doesn't fix it, git.txt contains the phone number of a friend of mine who understands git. Just wait through a few minutes of 'It's really pretty simple, just think of branches as...' and eventually you'll learn the commands that will fix everything." alt="Git">
<figcaption>
Obligatory <a href="https://xkcd.com/1597/">XKCD</a>. 
(<a class='cc' href='http://creativecommons.org/licenses/by-nc/2.5/' title='Creative Commons Attribution-NonCommercial'>cbn</a>)
</figcaption>
</figure>

For hacking and trying things out on the website we use a branch called *testing*.
This branch builds the latest version every 5 minutes for checking to see if you broke something.
To access this testing branch publicly:

<https://testing.gimp.org> or <http://testing.gimp.org>



## Branches

There are two main branches we are working with.
Well, mainly *one* branch that is worked with mostly and another that is actually the main site.

The **master** branch will build to the full [www.gimp.org](//www.gimp.org).

The **testing** branch will build to [testing.gimp.org](//testing.gimp.org).
This is the main branch for testing things out and checking that they will build correctly on the server.
Once a change works here ok, it can then be merged into **master** and pushed to the server.
