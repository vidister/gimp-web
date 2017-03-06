Title: Git Workflow 
Date: 2015-11-23T16:46:14-05:00
Author: Pat David
Summary: What the workflow should be with branches test and master.

<figure>
<img src="{filename}git.png" title="If that doesn't fix it, git.txt contains the phone number of a friend of mine who understands git. Just wait through a few minutes of 'It's really pretty simple, just think of branches as...' and eventually you'll learn the commands that will fix everything." alt="Git">
<figcaption>
Obligatory <a href="https://xkcd.com/1597/">XKCD</a>. 
(<a class='cc' href='http://creativecommons.org/licenses/by-nc/2.5/' title='Creative Commons Attribution-NonCommercial'>cbn</a>)
</figcaption>
</figure>

For hacking and trying things out on the website we use a branch called *testing*.
This branch builds the latest version every 5 minutes for checking to see if you broke something.
To access this testing branch publicly:

<https://testing.gimp.org> or <http://testing.gimp.org>

The general workflow is:

1. Do your testing/new material in a branch of your own.
2. If everything works fine locally, merge into *testing* and push.
        [testing.gimp.org][] will attempt a re-build every 5 minutes (00, 05, 10, 15, ...).  
3. If it builds ok on *testing*...
    1. merge the changes to *master* and push.
        [www.gimp.org][] will re-build every 20 minutes.
    2. create a patch and attach it to bugzilla

[testing.gimp.org]: //testing.gimp.org
[www.gimp.org]: //www.gimp.org



## Branches

There are two main branches we are working with.
Well, mainly *one* branch that is worked with mostly and another that is actually the main site.

The **testing** branch will build to [testing.gimp.org](http://testing.gimp.org).
This is the main branch for testing things out and checking that they will build correctly on the server.
Once a change works here ok, it can then be merged into **master** and pushed to the server.

The **master** branch will build to the full [www.gimp.org](http://www.gimp.org).



## Workflow

Clone the repository if you haven't already:

`git clone ssh://USERNAME@git.gnome.org/git/gimp-web LOCAL_DIR`

In my case, I use a local directory called `gimp-web`:

`git clone ssh://USERNAME@git.gnome.org/git/gimp-web gimp-web`

This will usually automatically setup a tracking branch to **master** for you.

Get all the objects from the repository: `git fetch`

You can now simply checkout the testing branch (or whichever branch you want):

`git checkout testing`



### Use Branches

I personally advocate the use of branches for just about anything you want to play with.
In particular using your own branches locally for trying things out or fixing stuff.

The reason is that if everything works great, you can easily merge the branch into *testing*.
If *testing* works ok, you can then easily merge the same branch into *master* without pulling extra things that may be in *testing* that is not yours (this may be due to you pulling on *testing* to make sure you're current before merging your work).

So for example, perhaps I'll create a branch locally to write an article in (trivial example).
Using the `-b` option with `git checkout` will create the branch and switch to it for you:

`git checkout -b newstuff`

Now I'll work on writing the article.
When it is finished and working fine, I can test it on [testing.gimp.org][] by merging my *newstuff* branch into *testing* and pushing:

    :::bash
    git checkout testing
    git merge newstuff
    git push

Wait for a rebuild to happen on the server, then check the site to make sure your changes propagated without breaking something.

**If** you don't have write access to gimp-web, you can instead [create a patch against *testing*](#creating-a-patch) from your branch and submit it to [bugzilla][report].

If it did and you're happy with the result, go ahead and get it into the *master* branch.
If you're allowed, simply switch to *master* and merge your *newstuff* branch into it also.

    :::
    git checkout master
    git merge newstuff
    git push

The reason why you would merge from *newstuff* rather than *testing* is in case some other work had already been pushed into testing (and you pulled it down from the remote).  If there was other work, and you pulled it down, you may inadvertently commit it into *master* when it wasn't ready yet.



### Creating a Patch

But what if you don't have rights to push to gimp-web?
No problem!
You can create patches instead that you can attach to [bug reports][report] in bugzilla.

Again, assuming you were working in your own branch (*which you should be*).
Say you've made a bunch of commits to your branch and are ready to have someone test it and possibly push it to *testing*.
You can use `format-patch` to generate one nice big patch for all of your work against a specific branch (*testing* in this example):

`git format-patch testing --stdout > my_awesome_work.patch`

Now attach that to a bug/enhancement report in [bugzilla][report] and wait to hear back!

[report]: https://bugzilla.gnome.org/enter_bug.cgi?product=gimp-web



## Applying Patches

This section is for those that have access on gimp-web, or those that want to test a patch from someone else locally.

Once we have a `.patch` file, we can see what it'll do:

`git apply --stat some_cool_stuff.patch`

If you want to see what the patch will actually do, open it in your favorite editor and look around.

To see if there will be any problems, we can test the patch before applying it:

`git apply --check some_cool_stuff.patch`

No errors == good.
Otherwise we'll need to deal with the errors (more on this later?).

When applying the patch it's helpful to use `git am` instead of `git apply`.
The reason is that `git am` is *signing off* on the patch, and will carry that information forward.
This is helpful if there's a different author but we need to track down who actually committed the patch.

`git am --signoff < some_cool_stuff.patch`

<small markdown=1>I referenced [this post][] by Ariejan de Vroom for some of this information.</small>
[this post]: https://ariejan.net/2009/10/26/how-to-create-and-apply-a-patch-with-git/



## Bugzilla Logging
If you fix something and need to reference what was fixed in a bugzilla thread, you can get consistent
output with the rest of GIMP log messages by using:

`git show --stat`

and pasting the results into the bugzilla message.
