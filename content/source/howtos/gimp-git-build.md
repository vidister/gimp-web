Title: Best Way to Keep Up with GIMP from git
Date: 2015-08-17T15:38:06-05:00
Modified: 2015-08-17T15:38:12-05:00
Author: Martin Nordholts
Template: page_author
Status: hidden


The more people that use the latest GIMP code from git the better. It keeps the required effort to contribute code upstreams small, which in turn increases the likelihood of upstream contributions, and it makes bugs more vulnerable to early discovery which minimizes their impact.

However, keeping up with GIMP from git means extra work compared to using prebuilt packages. Unless you know of an easy way you might not withstand it. What follows is a description of how I do it, which is almost effortless once setup. I assume you know how to install necessary dependencies (note you can use the method I describe for the key dependencies, including babl, GLib, GEGL and GTK+), what "the install prefix" means, and that you run Linux. The approach I use differs in two principal way compared to the many guides found on the net:

1.  I use autoconf's config.site feature instead of setting up environment variables manually
2.  I install in my home directory

Making use of config.site nullifies the need to manually manage environment variables, and installing in the home directory makes it easy to tinker with an installation since you don't need to be root. So, put this in $PREFIX/share/config.site where $PREFIX is in your home directory such as PREFIX=/home/martin/gimp-git, either manually or using this script:

    export PATH="$PREFIX/bin:$PATH"
    export PKG_CONFIG_PATH="$PREFIX/lib/pkgconfig:$PKG_CONFIG_PATH"
    export LD_LIBRARY_PATH="$PREFIX/lib:$LD_LIBRARY_PATH"
    export ACLOCAL_FLAGS="-I $PREFIX/share/aclocal $ACLOCAL_FLAGS"


Then, assuming you have all the dependencies, you build GIMP the first time with:

    git clone git://git.gnome.org/gimp
    cd gimp
    ./autogen.sh --prefix=$PREFIX
    make
    make install


and then to get updated with the latest changes from the constantly moving code base you regularly do

    git pull --rebase
    make
    make install

Note that the latter works without requiring any environment variables to be set since configure will source config.site. And because autogen.sh passes --enable-maintainer-mode to configure, it will also work when Makefile.am's or configure.ac are changed. In those rare occasions where things break, just run git clean -xdf which removes all non-version-controlled files so that you can start over from autogen.sh.

The above approach works for as good as all GNOME projects, including GLib, babl, GEGL and GTK+. This makes it easy to adapt to GIMP's build requirements of these and other libraries even if your distro doesn't meet them. Let me know if you have problems!

<small>
Originally published at:  
[http://www.chromecode.com/2009/12/best-way-to-keep-up-with-gimp-from-git_26.html](http://www.chromecode.com/2009/12/best-way-to-keep-up-with-gimp-from-git_26.html)
</small>
