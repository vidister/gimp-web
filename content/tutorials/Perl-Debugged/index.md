Title: Perl Debugged
Date: 2002
Modified: 2015-09-25T13:33:27-05:00
Author: Seth Burgess

<small>
Text and images Copyright (C) 2002 [Seth Burgess](mailto:sjburgesNOSPAM@gimp.org) and may not be used without permission of the author.
</small>

## Intention

The Perl module for GIMP is a nice evolution of the scripting interface of GIMP. It removes the dependence on the relatively rarely encountered scheme language of script-fu and replaces it with one that is familiar to a much larger audience. In doing so, the perl interface to GIMP also can take advantage of many of the features that have been added to perl over the years.

My aim in creating this tutorial is to make debugging scripts easier. We'll touch on the facilities provided by the Gimp module, and then focus on using the perl debugger to interactively develop scripts.

To illustrate the points in this tutorial, this is a simple script that will change as we progress:

    :::perl
    #!/usr/bin/perl

    use Gimp qw(:auto);
    use Gimp::Fu;
    use Gimp::Util;

    register "example", "Example", "Dumb example for debugging",
       "Seth Burgess", "Seth Burgess ", "1.0",
        "/Xtns/Dumb Example", "*", [], sub {

       $fname = "/home/seth/dumb.jpg";
       $img = gimp_file_load($fname, $fname);
       $img->display_new();

       return();
       };

    exit main;


## Gimp::set_trace

The Gimp module provides tracing ability, which is a form of debugging. To activate this, start GIMP from an XTerm, and place the following at the top of the script:

    :::perl
    #!/usr/bin/perl

    use Gimp qw(:auto);
    use Gimp::Fu;
    use Gimp::Util;

    **Gimp::set_trace(TRACE_ALL);**

    register "example", "Example", "Dumb example for debugging",
       "Seth Burgess", "Seth Burgess ", "1.0",
       "/Xtns/Dumb Example", "*", [], sub {

       $fname = "/home/seth/dumb.jpg";
       $img = gimp_file_load($fname, $fname);
       $img->display_new();

       return();
       };

    exit main;

This will give the maximum amount of tracing information, displayed on the console window you start GIMP from. You can cut back on what all gets displayed by using an "or'ed" combination of the following other options in place of TRACE_ALL:

<link rel='stylesheet' type='text/css' href='index.css' />

<table class='ptable'>

<tbody>

<tr>

<td class='t20'>TRACE_NONE</td>

<td class='t40'>turn off tracing</td>

</tr>

<tr>

<td>TRACE_CALL</td>

<td>trace only GIMP Procedural Database (PDB) calls (including arguments and return values)</td>

</tr>

<tr>

<td>TRACE_TYPE</td>

<td>also print the parameter types</td>

</tr>

<tr>

<td>TRACE_NAME</td>

<td>print the parameter names</td>

</tr>

<tr>

<td>TRACE_DESC</td>

<td>print the parameter descriptions</td>

</tr>

</tbody>

</table>

Using TRACE_ALL can let you see easily what parameters are wrong so you can fix misbehaviour in scripts. It provides a powerful history of what could be going wrong in your script.

## Perl Debugger

Perl comes with a debugger built in, which we can effectively utilize for interactive execution of our scripts. To invoke this, put a -d on the invocation line for the script as follows:

    :::perl
    #!/usr/bin/perl **-d**

    use Gimp qw(:auto);
    use Gimp::Fu;
    use Gimp::Util;
    # Gimp::set_trace(TRACE_ALL); # uncomment to do tracing

    register "example", "Example", "Dumb example for debugging",
       "Seth Burgess", "Seth Burgess <sjburges\@gimp.org>, "1.0",
       "/Xtns/Dumb Example", "*", [], sub {

       $fname = "/home/seth/dumb.jpg";
       $img = gimp_file_load($fname, $fname);
       $img->display_new();

       return();
    };

    exit main;

If you change a Gimp-Perl script to utilize this, you'll notice GIMP halting on startup. This is because GIMP is querying the plug-in, and it is halting due to having debugging enabled. Just type 'c' in the window, and then 'q' to let GIMP continue loading:

    :::perl
    Enter h or `h h' for help, or `man perldebug' for more help.

    main::(/home/seth/.gimp-1.3/plug-ins/demo:21):
    21:     };
      DB<1> c
    Debugged program terminated.  Use q to quit or R to restart,
      use O inhibit_exit to avoid stopping after program termination,
      h q, h R or h O to get additional info.  
      DB<1> q

This is not a part of the script we're really intrested in - its the registration of the plug-in with GIMP. It turns out to be a really annoying behaviour, since every time we modify the script we'll need to do this on startup. Luckily we have another way of attacking this provided by the Gimp module - that is the Perl Server.  

First, move your script out of your plug-ins directory to somewhere else. Then startup GIMP. Start the Perl Server by going to <span class="filter">Xtns -> Perl Server</span>. You'll see something like the following in the XTerm window of GIMP:

    :::
    989020828: server version 1.201 started
    989020828: accepting connections on /tmp/gimp-perl-serv-uid-1000/gimp-perl-serv

Now from another XTerm, execute the script (just type its name). This will immediately start debugging the new script. You can set a breakpoint on a line of your choice and execute 'c' to let it execute until that line.

    :::
      DB<1> b 13
      DB<2> c
        13:        $fname = "/home/seth/dumb.jpg";

You can now examine variables with perl functions (print $fname) and modify them during runtime. You can change the point of execution, and do most everything you'd expect from a debugger.

## $DB::single

Instead of having to remember what line the intresting part of your script starts on and set a breakpoint there, perl provides a way to programmatically jump into single-step mode. Add the following to the top of your sub:

    :::perl
    #!/usr/bin/perl -d

    use Gimp qw(:auto);
    use Gimp::Fu;
    use Gimp::Util;
    # Gimp::set_trace(TRACE_ALL); # uncomment to do tracing

    register "example", "Example", "Dumb example for debugging",
      "Seth Burgess", "Seth Burgess <sjburges\@gimp.org>", "1.0",
      "/Xtns/Dumb Example", "*", [], sub {

      **$DB::single = 1; # Enter single step if using -d**

      $fname = "/home/seth/dumb.jpg";
      $img = gimp_file_load($fname, $fname);
      $img->display_new();

      return();
    };

    exit main;

Now when you run your script, hit 'c' and it will break on the entry of the sub {} call. Using $DB::single will only have any effect when using -d - its ignored otherwise, so you can leave it in scripts without any side effects.

## Example Session

After invoking the perl server, I run 'Example' from a commandline shell:

    :::
    Default die handler restored.

    Loading DB routines from perl5db.pl version 1.07
    Editor support available.

    Enter h or `h h' for help, or `man perldebug' for more help.

    main::(./Example:20):   };
      DB<1> c
    main::CODE(0x83f240c)(./Example:15):
    15:        $fname = "/home/seth/dumb.jpg";
      DB<1> n
    main::CODE(0x83f240c)(./Example:16):
    16:        $img = gimp_file_load($fname, $fname);
      DB<1> print $fname
    /home/seth/dumb.jpg
      DB<2> $fname = "/home/seth/foo.png";

      DB<3> print $fname
    /home/seth/foo.png
      DB<4> n
    main::CODE(0x83f240c)(./Example:17):
    17:        $img->display_new();
      DB<4> n
    main::CODE(0x83f240c)(./Example:19):
    19:        return();
      DB<4> c
    Debugged program terminated.  Use q to quit or R to restart,
      use O inhibit_exit to avoid stopping after program termination,
      h q, h R or h O to get additional info.
      DB<4> q

This example session shows changing a value of a variable at run-time so to load a different file than the one hard-coded into the script. Note that I continue ('c') and it stops immediately after $DB::single is set.

Far more complex debugging is possible, but this should give you a good taste of what its all about.

## Conclusion

Thats all there is to it! I hope this has been useful to you.

You can [download a compressed copy](perldebug.tar.gz) of this tutorial. You can also get a [copy of the script](Example). Feel free to use either/both however you want.

This tutorial has gone over the basics of using the Gimp module for tracing, the Perl Server for starting your scripts, and using the perl debugger to interactively execute your scripts. If you have comments, questions, or suggestions about this tutorial, please drop me a line.

Happy GIMPing, Seth

The original tutorial can be found [here](http://classic.gimp.org/~sjburges/perl_debug/intro.html).

