Title: Building WGO
Date: 2015-08-11T11:56:58-05:00
Modified: 2015-08-11T11:57:04-05:00
Author: Pat David
Summary: A page about the new site.
lang: fr


Donc, vous voulez contribuer? 
Génial! 
Voici les étapes à suivre pour obtenir votre propre copie du site Web!

[TOC]

## Building the Site

### Get git

You will need to get git: <https://git-scm.com/>

The examples here will use git from the command line, but you may be more comfortable using a GUI.
In that case, find one you're comfortable with.
If you are going to be contributing and want commit access to the repository, [learn git][] also.

[learn git]: https://git-scm.com/documentation

You can still contribute without commit access to the repository.
You'll be creating patches instead of pushing changes directly to the repository.
We'll cover those steps a little later.



### Get the Source

The source for the GIMP websites can be found here: <https://git.gnome.org/browse/gimp-web/>

At the bottom of that page you should see a section title **Clone**.
It will provide some common means to clone the repository:

[git://git.gnome.org/gimp-web](git://git.gnome.org/gimp-web)  
<https://git.gnome.org/browse/gimp-web>
<ssh://USERNAME@git.gnome.org/git/gimp-web>

From your shell, navigate to your desired location to hold the files.

If you are only interested in the new site while it's being developed, you don't have to fetch the entire repository.
You can tell git to clone a particular branch (only) into the sub-directory `gimp-web-static`:

`git clone -b gimp-web-static --single-branch https://git.gnome.org/browse/gimp-web gimp-web-static`

That is,  
`git clone -b gimp-web-static`  
clone the branch gimp-web-static

`--single-branch`  
just the branch, not the entire repository

`https://git.gnome.org/browse/gimp-web/`  
the repository we are cloning from

`gimp-web-static`  
into this sub-directory from where we are.

Be patient.
At the moment the total download size will be around 111MB.
This is because the gimp-web-static branch is still referencing all of WGO.
This may be fixed later *or not*.
So just sit tight while it fetches everything... :)

Once it finishes, you'll have a sub-directory called `gimp-web-static`.
If you enter that directory and run `git status` you should see some information:

    $cd gimp-web-static/
    $git status
        On branch gimp-web-static
        Your branch is up-to-date with 'origin/gimp-web-static'.
        nothing to commit, working directory clean

Congratulations!
You now have your very own copy of the site source code.
Now we just need to get the rest of the tools in place for you to make use of it.



### Get Python

You will need to download and install Python 2.7.x.

<https://www.python.org/downloads/>

2.6.x is not supported by Pelican, and there is only rudimentary support for 3.x at the moment.



### Get Pelican

Install [Pelican](http://blog.getpelican.com/):

<http://blog.getpelican.com/>

The easiest way to get it after installing Python is to use pip:

`pip install Pelican`



#### Some Extras

Some extra components that we use on the site are [Markdown][] and [typogrify][]:

`pip install Markdown`  
`pip install typogrify`

[Markdown]: http://daringfireball.net/projects/markdown/
[typogrify]: https://github.com/mintchaos/typogrify



### Build the Site

Once the requirements are installed building the site is straightforward.
Enter the project directory and issue the `Pelican` command to build:

    cd gimp-web-static/
    pelican

After a few moments, the command will finish, and the site files will be in the `output` directory.


#### Auto Rebuild

If you are developing the site or content and want pelican to automatically regenerate the site when files change then you can run the command with the `-r` switch to reload automatically (and will possibly want to ignore any caches as well):

    pelican -r --ignore-cache



### View the Site

To accurately see the site it is best to access it through a web server.
Python has one built in that can be used.
Enter the output directory, and start the HTTP server:

    cd output/
    python -m SimpleHTTPServer

The site will then be accessible to a web browser at:

    http://localhost:8000

Do note that the SimpleHTTPServer won't serve SVG elements as images correctly.
See [this section][] for a solution

[this section]: ../using-pelican/#python-simplehttpserver-svg



## Writing for the Site

This section will cover writing something for the site.
In particular it will focus on writing page content (a tutorial, or page like this).
News items are similar, but will be covered in a different place (not all users will be allowed
to publish news items).

The actual structure of the site and directory hierarchies are covered in the [Using Pelican][] page.
For this page, we will stick to writing a tutorial for the site.
[Using Pelican]: ../using-pelican/

The directories of page sections will be nested just as they are in the source directories now.
This means that new tutorials will be located in their own directories under the `content/tutorials/` directory.
They will then be accessible on a url like `www.gimp.org/tutorials/NEW_TUTORIAL_NAME/`

For this example, we will create a new tutorial called `GIMP-Test`.
Create this new directory under the tutorials directory:

    cd content/tutorials/
    mkdir GIMP-Test

Inside that directory, create a new `index.md` file.
This will be the page content.


### Markdown File

The `index.md` [Markdown][] file requires that any metadata be located first in the file.
To finish describing metadata, follow it with a blank line and then start the actual file contents.
The minimum metadata for files should at least be *Title*, *Date*, and *Author*.
A sample leading section of an `index.md` file might look like this:

    :::Markdown
    Title: GIMP Test Tutorial
    Date: 2015-08-11T14:11:02-05:00
    Author: Pat David

    Welcome to a quick test of writing new content!

The rest of the file will contain the actual tutorial content.
There is a Markdown cheatsheet available [here]({filename}../markdown.md) for reference.
There will also be a more detailed article for writing a tutorial coming soon...

When finished, save the file.
If the webserver is running, and pelican was run with the `-r` option, refreshing the browser page should reflect the changes.
Otherwise run pelican in the base directory again to rebuild the site and show the latest changes.

Due to the way the directories are nested, the above example can be found at:

    localhost:8000/tutorials/GIMP-Test/
