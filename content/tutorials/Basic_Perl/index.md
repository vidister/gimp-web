Title: A Tutorial for GIMP-Perl Users
Date: 2014-05-02
Modified: 2014-05-02
Author: Ed J
Template: page_author


<small>
<a href='http://creativecommons.org/licenses/by-sa/3.0/deed.en_US'>
<img class='cc-badge' src='/images/creativecommons/by-sa 80x15.png' alt='Creative Commons By Share Alike'/>
</a>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - A Tutorial for GIMP-Perl Users (text & images)</span> 
by [Ed J] is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).
</small>

[Ed J]: https://metacpan.org/author/ETJ

<small>Updated for Gimp 2.8 / Gimp-Perl 2.3</small>

**Table of contents**

[TOC]


## 1. Version notes

This work is a slightly modified version of Dov Grobgeld's excellent tutorial. It has been updated to Gimp-Perl 2.3 and GIMP 2.8.

## 2. Background

One of the wonderful features of GIMP is that it all its functionality may be accessed through scripting. Available scripting environments include Scheme through Script-Fu and Python.

Perl has CPAN, giving access to vast numbers of modules to get things done. Now, GIMP may also be scripted in Perl. This tutorial will describe how to write such plug-ins and scripts for Gimp.

As there are several excellent tutorial texts describing the perl language, this tutorial will assume a working knowledge of Perl, and will instead concentrate on the use of GIMP together with the perl modules Gimp and Gimp::Fu.

## 3. What you need

The tutorial scripts have been tested on Linux (a Windows version is in the works) with the following versions:

1.  Gimp version 2.8.10.
2.  Perl version 5.14 or later.
3.  The perl module Gtk2, version 1.249, available from [http://gtk2-perl.sourceforge.net](http://gtk2-perl.sourceforge.net/)
4.  The Gimp-Perl module, version 2.3 or later, available from [http://search.cpan.org/dist/Gimp/](http://search.cpan.org/dist/Gimp/)

Perl and all its associated modules are available in source form from the Comprehensive Perl Archive network, CPAN.

## 4. The Gimp module

Most scripts make use of the simplified interface Gimp::Fu provided with the Gimp module. Gimp::Fu provides a framework for entering parameters to the script in a dialog-box interface, just like Script-Fu, but also allows running of the script in batch mode from the command line. This tutorial will go into detailed descriptions of the construction of a Gimp::Fu script, but before we do this, here is the general framework of such a script.

    #!/usr/bin/perl -w 

    use Gimp; 
    use Gimp::Fu; 

    podregister {
     # code...
    }; 

    exit main; 
    __END__ 

    =head1 NAME 

    test_exception - exercise gimp-perl filter testing exceptions 

    =head1 SYNOPSIS 

    <Image>/Filters/Languages/_Perl/_Test/Exception 

    =head1 DESCRIPTION 

    Exercise Gimp-Perl exceptions. 

    =head1 AUTHOR 

    The Author. 

    =head1 DATE 

    20140310 

    =head1 LICENSE 

    The licensing terms. 

The key points to note in the script are:

*   the use of the two modules `Gimp` and `Gimp::Fu`,
*   the podregister function, which will be described in detail below,
*   the way the control is handed over to `Gimp` module on line 8, and
*   the POD documentation below the `__END__` line.

## 5. The GIMP PDB

Before going into the details of the Gimp::Fu script, we will describe how to access the functionality of GIMP. All functions known to GIMP are available through the procedural database (PDB). All the PDB functions may be called from perl, as will be seen below. These PDB functions are either internal to GIMP, or have been made available through a plug-in or a script extension, but as far as the caller is concerned there is no difference. As we will see below, when a perl function is registered through the `podregister` function, it will appear in the PDB as well.

Gimp comes with a PDB browser available in **Help/Procedure Browser**. This browser provides a way of seeing all the functions in the PDB, as well as their input and output parameters. E.g. the DB Browser entry for `plug-in-gauss-iir`, which will be used in the example below looks like this:

<table class='tut'>
<tbody><tr><th align="right" valign="top">Name:</th><td colspan="3">plug-in-gauss-iir</td></tr>
<tr><th align="right" valign="top">Blurb:</th><td colspan="3" valign="top">Apply a gaussian blur</td></tr>
<tr>
<th align="right" valign="top">In:</th><td valign="top">INT32</td><td valign="top">run-mode</td><td valign="top">The run mode { RUN-INTERACTIVE (0), RUN-NONINTERACTIVE (1) }</td>
</tr>
<tr>
<th valign="top"></th><td valign="top">IMAGE</td><td valign="top">image</td><td valign="top">Input image (unused)</td>
</tr>
<tr>
<th valign="top"></th><td valign="top">DRAWABLE</td><td valign="top">drawable</td><td valign="top">Input drawable</td>
</tr>
<tr>
<th valign="top"></th><td valign="top">FLOAT</td><td valign="top">radius</td><td valign="top">Radius of gaussian blur (in pixels, &gt; 0.0)</td>
</tr>
<tr>
<th valign="top"></th><td valign="top">INT32</td><td valign="top">horizontal</td><td valign="top">Blur in horizontal direction</td>
</tr>
<tr>
<th valign="top"></th><td valign="top">INT32</td><td valign="top">vertical</td><td valign="top">Blur in vertical direction</td>
</tr>
<tr><th valign="top">Help:</th><td colspan="3">Applies a gaussian blur to the drawable, with specified radius of affect.  The standard deviation of the normal distribution used to modify pixel values is calculated based on the supplied radius.  Horizontal and vertical blurring can be independently invoked by specifying only one to run.  The IIR gaussian blurring works best for large radius values and for images which are not computer-generated.</td>
</tr>
</tbody>
</table>

All the the constants mentioned in the PDB Explorer have been defined within Gimp::Fu and may be used within perl. E.g. a call to blur an image looks as follows:

    Gimp::Plugin->gauss_iir($image, $drawable, 50, 6, 6);

Note that Perl is using underline characters where the DB browser uses hyphens! The PDB entry above shows that `plug-in-gauss-iir` is called with various parameters, of various types. These will be explained below.

You will also see that the first parameter, `run-mode`, was omitted. This is a feature of Gimp-Perl, which will automatically supply that parameter if you leave it off. This will make your code a lot tidier-looking.

Script-Fu scripts are called just like any other script according to the PDB signature in the PDB browser. E.g. to run the script-fu-basic1-logo just do:

    script_fu_basic1_logo("Hello", 72,
                          "Utopia 72", 
                          [0,0,0],[255,255,255]);

### 5.1. Gimp::Fu and the podregister function

Gimp::Fu is Perl's answer to Script-Fu. It provides a simplified method for accepting parameters for a script through a Gtk2 interface, just like script-fu, but as we shall see below, it has some additional bells and whistles.

The main function for a Gimp-Fu script is the <tt>podregister</tt> function. This function declares the interface of the script to GIMP. The <tt>podregister</tt> function provides GIMP with the following information, from various sections of its [POD (plain old documentation)](http://perldoc.perl.org/perlpod.html):

*  The name of the function. It comes from the first part of the <tt>NAME</tt> section, before the dash. Tells GIMP the name by which the function will be known in the PDB.

*  A small description, from the <tt>NAME</tt> section, after the dash.

*  A help text, from the <tt>DESCRIPTION</tt> section.

*  The author's name, from the <tt>AUTHOR</tt> section.

*  The copyright of the script, from the <tt>LICENSE</tt> section.

*  Creation date - any text, from the <tt>DATE</tt> section.

*  Menu path - a string, from the <tt>SYNOPSIS</tt> section. The path can take these forms, though there are other options:
    * "&lt;Image&gt;/Filters/Menu/Script Name"
    * "&lt;Toolbox&gt;/Xtns/Perl/Script Name"If you specify "&lt;Image&gt;", then the script is expecting to operate on, or create, an image. In this case Gimp::Fu will add as the first two parameters to the script the image and the drawable active when the script was invoked. If, however, the "image types" is left as blank or not specified, the plugin is expected to create and therefore return an image (and it will normally be placed under the <tt>File/Create</tt> menu).

    If you specify "&lt;Toolbox&gt;", then the script is a standalone script that appears in the menu hierarchy under Filters (this is a historical thing) and takes all its inputs through the Gimp::Fu interface dialog.

*  The acceptable image types, from the <tt>IMAGE TYPES</tt> section - a string. 
This list contains a list of image types acceptable.
This field is only used for scripts that are in the "&lt;Image&gt;" hieararchy. Some possible values are listed in the table below:

    <table class='tut'>
    <tbody>
    <tr>
    <th bgcolor="#dfdfdf">value</th>
    <th bgcolor="#dfdfdf">meaning</th>
    </tr>
    <tr>
    <td  valign="top">*</td>
    <td  valign="top">Any images are accepted</td>
    </tr>
    <tr>
    <td  valign="top">RGB</td>
    <td  valign="top">RGB images</td>
    </tr>
    <tr>
    <td  valign="top">RGBA</td>
    <td  valign="top">RGB images with alpha channels</td>
    </tr>
    <tr>
    <td  valign="top">GREY</td>
    <td  valign="top">Grey level images</td>
    </tr>
    <tr>
    <td></td>
    <td  valign="top">(left empty or no such section) Does not take image as input, **does** return an image. <tt>Gimp::Fu</tt> will automatically add that return value.</td>
    </tr>
    </tbody>
    </table>

*  Parameters, from the <tt>PARAMETERS</tt> section. This will be Perl code, which Gimp::Fu evaluates as a list of parameters. Each parameter in turn is a reference to an array containing the following four or five values (A reference to an array in Perl is simply an array written within square brackets):
    * The type of the parameter. The types recognized by Gimp::Fu and their Perl counterparts are given in the following table:

        <table class='tut'>
        <tbody>
        <tr>
        <th >Type</th>
        <th  width="30%">Possible forms</th>
        <th  width="50%">Comment</th>
        </tr>
        <tr>
        <td  valign="top">PF_INT32  
         PF_INT16  
         PF_INT8  
        </td>
        <td  valign="top">42</td>
        <td  valign="top">An integer.</td>
        </tr>
        <tr>
        <td  valign="top">PF_FLOAT  
        </td>
        <td  valign="top">3.141</td>
        <td  valign="top">A floating point number.</td>
        </tr>
        <tr>
        <td  valign="top">PF_TOGGLE</td>
        <td  valign="top">0  
        1</td>
        <td  valign="top">A boolean value.</td>
        </tr>
        <tr>
        <td  valign="top">PF_SLIDER  
         PF_SPINNER</td>
        <td  valign="top">An integer value through a slider and a spinner interface. The range parameter should be specified and is interpreted as minimum, maximum, and step, e.g. [0,100,1].</td>
        <td  valign="top">![tpix]({filename}tpix.gif)</td>
        </tr>
        <tr>
        <td  valign="top">PF_FONT</td>
        <td  valign="top">"Arial"</td>
        <td  valign="top">A font name.</td>
        </tr>
        <tr>
        <td  valign="top">PF_STRING</td>
        <td  valign="top">"A string"</td>
        <td  valign="top">A string</td>
        </tr>
        <tr>
        <td  valign="top">PF_COLOR  
         PF_COLOUR</td>
        <td  valign="top">[255,127,0]  
         <tt>#ff7f00</tt></td>
        <td  valign="top">A color may either be expressed as a reference to an array of three components, or as a hexadecimal triple, proceeded by the hash sign.</td>
        </tr>
        <tr>
        <td  valign="top">PF_TOGGLE</td>
        <td  valign="top">0  
        1</td>
        <td  valign="top">A boolean toggle</td>
        </tr>
        <tr>
        <td  valign="top">PF_IMAGE</td>
        <td  valign="top">-</td>
        <td  valign="top">An image</td>
        </tr>
        <tr>
        <td  valign="top">PF_DRAWABLE</td>
        <td  valign="top">-</td>
        <td  valign="top">A drawable.</td>
        </tr>
        <tr>
        <td  valign="top">PF_BRUSH</td>
        <td  valign="top">![tpix]({filename}tpix.gif)</td>
        <td  valign="top">A brush</td>
        </tr>
        <tr>
        <td  valign="top">PF_GRADIENT</td>
        <td  valign="top">![tpix]({filename}tpix.gif)</td>
        <td  valign="top">A gradient</td>
        </tr>
        <tr>
        <td  valign="top">PF_PATTERN</td>
        <td  valign="top">![tpix]({filename}tpix.gif)</td>
        <td  valign="top">A pattern</td>
        </tr>
        </tbody>
        </table>

    *  The name of the parameter - a string.
    *  A help text for the parameter.
    *  Default value for the parameter. This should be given in the form listed in the table above.
    *  An array defining allowed range for the value. This is only used for PF_SLIDER and PF_SPINNER.

*  Optionally, the return types of the function can be provided, from a <tt>RETURN VALUES</tt> section. This is specified in the same way as the Parameters above. There is no default or extra argument required.
*  The perl code implementing the function - most commonly with a sub-reference, surrounded by "{" and "};", as below - thanks to Perl's prototyping, you don't need to specify "sub". 
This will be called when the associated menu entry declared through the _Menu path_ described above. 
When the sub is called it is passed a list of parameters as declared in field 9. 
In the case of a "&lt;Image&gt;..." script, the active image and drawable (layer or channel) will be passed as first and second parameters. Thanks to the magic of Perl source filtering, you do not need to declare your variables but may simply use them:

        :::perl
        podregister {
          $drawable->gauss_iir($radius, $horizontal, $vertical);
        };
        # ...
        =head1 PARAMETERS

          [ PF_FLOAT, 'radius', "Radius", 50.0 ],
          [ PF_INT32, 'horizontal', 'Horizontal blur', 6 ],
          [ PF_INT32, 'vertical', 'Vertical blur', 6 ],

    You will also note that "plug_in_" has been omitted from the method call above, and that not all its parameters appear to be getting passed! This is thanks to the object-oriented implementation in Gimp-Perl, which when given a method name, searches various prefixes for the underlying function including the plug-in related ones (including <tt>script_fu_</tt>).

    The code will normally display a new image if it creates one, and also return the new image, in accordance with the return types declared in parameter 10 of the <tt>podregister</tt> call described above. This enables Gimp::Fu scripts to be used noninteractively by other scripts. More about that behaviour below.

### 5.2. podregister parameters

You will have noticed above that the parameters to the function given to <tt>podregister</tt> used parameters either named in the POD, or supplied by <tt>Gimp::Fu</tt>, such as <tt>$drawable</tt>. This is because <tt>podregister</tt> automatically makes available to your function all the variables declared either in the POD documentation (the "PARAMETERS" section) or added depending on your "image types".

### 5.3. A commented script

The following Gimp::Fu script example shows the steps described in the previous section. It registers a script that takes two values, the size of the image and a color, and then produces an image of the requested size with the requested color. Quite useless, but it shows the important steps of how to register a script, how to create a new image, and how to access some PDB functions.

    #!/usr/bin/perl -w 

    use strict; 
    use Gimp; 
    use Gimp::Fu; 

    podregister { 
     # no need to have my ($size, $color) = @_; 
     my $img = Gimp::Image->new($size, $size, RGB); # Create a new image 
      # Create a new layer 
      my $layer = $img->layer_new($size, $size, RGB, "Layer 1", 100, NORMAL_MODE); 
      $img->insert_layer($layer, -1, 0); # add the layer to the image 
      Gimp::Context->set_background($color); # Set background to required color 
      $layer->edit_fill(BACKGROUND_FILL); # Paint the layer  
      Gimp::Display->new($img); 
      return $img; # Return image - return implied by no IMAGE TYPES 
    }; 

    exit main; 
    __END__ 

    =head1 NAME 

    img_uni - Create a uniform image 

    =head1 SYNOPSIS 

    <Image>/File/Create/Tutorial/Img Uni 

    =head1 DESCRIPTION 

    A tutorial script. 

    =head1 PARAMETERS 

    [PF_INT32,   "size", "Img size", 100], 
    [PF_COLOR, "color", "Img color", [255,127,0]] 

    =head1 AUTHOR 

    Dov Grobgeld 

    =head1 DATE 

    2004-03-27 

    =head1 LICENSE 

    Dov Grobgeld (c) 

Most of these commands are directly copied out the PDB.

This script shows the essential steps of producing a stand-alone script:

<table class='tut'>
<tbody>
<tr>
<th>line(s)</th>
<th>Description</th>
</tr>
<tr>
<td>7</td>
<td>Registration of the extension</td>
</tr>
<tr>
<td>9</td>
<td>Creating a new image.</td>
</tr>
<tr>
<td>11</td>
<td>Creating one or more layers.</td>
</tr>
<tr>
<td>12</td>
<td>Attaching the layer to the image.</td>
</tr>
<tr>
<td>13-14</td>
<td>Do some painting operations in the layers.</td>
</tr>
<tr>
<td>15</td>
<td>Display the new image</td>
</tr>
<tr>
<td>16</td>
<td>Return the image to the caller</td>
</tr>
</tbody>
</table>

To test the script, save it in the directory <tt>$HOME/.gimp-2.8/plug-ins</tt>. (A more official way to add scripts is to use the <tt>gimptool-2.0 --install-bin</tt> command). It must then be made executable through the command:

    chmod +x $HOME/.gimp-2.8/plug-ins/uni

Then start GIMP. It is generally a good idea to test the syntax of the script with <tt>perl -c</tt> before starting GIMP.

**Note:** Due to the way GIMP works, it is not possible to add scripts once GIMP is running. On the other hand, it is possible to change a script which has already been registered, as long as the parameters don't change.

The script is now accessible through the menu system through the **File/Create/Tutorial** top menu:

<figure>
<img src="{filename}uni-menu.png" alt="uni-menu.png" />
</figure>

When choosing this menu entry the following screen is popped up:

<figure>
<img src="{filename}uni-entry.png" alt="uni-entry.png" />
</figure>

Choosing the default values results in the image:

<figure>
<img src="{filename}uni-result.png" alt="uni-result.png" />
</figure>

## 6. Object oriented syntax

Gimp-Perl provides an alternative object-oriented syntax for the image and the drawable commands. Here is a table showing the procedural vs the object oriented syntax for a few commands:

<table class='tut'>
<tbody>
<tr>
<th bgcolor="#E0E0E0">procedural syntax</th>
<th bgcolor="#E0E0E0">object oriented syntax</th>
</tr>
<tr>
<td >gimp_image_insert_layer($drw,0,0);</td>
<td >$img->insert_layer($drw,0,0);</td>
</tr>
<tr>
<td >gimp_drawable_width($drw);</td>
<td >$drw->width;</td>
</tr>
</tbody>
</table>

The substitution rule for converting a PDB into a method is as simple as erasing `gimp_image_` (or sometimes `gimp_`) from the beginning of the function call and calling this method through the image object. Similarly for the <tt>gimp_drawable_...</tt> functions. See the [Gimp-Perl docs](http://search.cpan.org/dist/Gimp/Gimp.pm#OBJECT-ORIENTED_SYNTAX) for more detail.

Note that the object-oriented syntax appears to be only syntactic sugar that makes the calling syntax cleaner. The error messages are still given in the procedural format. What is going on is that GIMP, and the library on which it is implemented (Glib), use C in an object-oriented fashion.

## 7. Painting areas with selections

In the <tt>uni</tt> script the function <tt>gimp_edit_fill</tt> was called to fill the whole image. Looking at the info for <tt>gimp_edit_fill</tt> in the DB browser we find the following:

<table class='tut'>
<tbody>
<tr>
<th align="right" valign="top">Name:</th>
<td  colspan="3">gimp_edit_fill</td>
</tr>
<tr>
<th align="right" valign="top">Blurb:</th>
<td colspan="3" valign="top">Fill selected area of drawable</td>
</tr>
<tr>
<th align="right" valign="top">In:</th>
<td valign="top">DRAWABLE</td>
<td valign="top">drawable</td>
<td valign="top">The drawable to fill from</td>
</tr>
<tr>
<th></th>
<td valign="top">INT32</td>
<td valign="top">fill_type</td>
<td valign="top">The type of fill { FOREGROUND-FILL (0), BACKGROUND-FILL (1), WHITE-FILL (2), TRANSPARENT-FILL (3), PATTERN-FILL (4), NO-FILL (5) }</td>
</tr>
<tr>
<th valign="top">Help:</th>
<td colspan="3">This procedure fills the specified drawable with the fill mode. If the fill mode is foreground, the current foreground color is used. If the fill mode is background, the current background color is used. Other fill modes should not be used. This procedure only affects regions within a selection if there is a selection active. If you want to fill the whole drawable, regardless of the selection, use 'gimp-drawable-fill'.</td>
</tr>
</tbody>
</table>

Thus, if a selection is active when <tt>gimp_edit_fill</tt> is called, only the selected region of the drawable is painted. Note also that you must substitute "\_" for "-" in the names.

There are lots of ways of choosing a selection as can be seen when searching for a "select" in the PDB. The example below uses <tt>gimp_image_select_rectangle</tt>, whose entry in the PDB looks as follows:

<table class='tut'>
<tbody>
<tr>
<td >
<table class='tut'>
<tbody>
<tr>
<th align="right" valign="top">Name:</th>
<td  colspan="3">gimp-image-select-rectangle</td>
</tr>
<tr>
<th align="right" valign="top">Blurb:</th>
<td colspan="3" valign="top">Create a rectangular selection over the specified image</td>
</tr>
<tr>
<th align="right" valign="top">In:</th>
<td valign="top">IMAGE</td>
<td valign="top">image</td>
<td valign="top">The image</td>
</tr>
<tr>
<th></th>
<td valign="top">INT32</td>
<td valign="top">operation</td>
<td valign="top">The selection operation { CHANNEL-OP-ADD (0), CHANNEL-OP-SUBTRACT (1), CHANNEL-OP-REPLACE (2), CHANNEL-OP-INTERSECT (3) }</td>
</tr>
<tr>
<th></th>
<td valign="top">FLOAT</td>
<td valign="top">x</td>
<td valign="top">x coordinate of upper-left corner of rectangle</td>
</tr>
<tr>
<th></th>
<td valign="top">FLOAT</td>
<td valign="top">y</td>
<td valign="top">y coordinate of upper-left corner of rectangle</td>
</tr>
<tr>
<th></th>
<td valign="top">FLOAT</td>
<td valign="top">width</td>
<td valign="top">the width of the rectangle: width >= 0</td>
</tr>
<tr>
<th></th>
<td valign="top">FLOAT</td>
<td valign="top">height</td>
<td valign="top">the height of the rectangle: width >= 0</td>
</tr>
<tr>
<th valign="top">Help:</th>
<td colspan="3">This tool creates a rectangular selection over the specified image. The rectangular region can be either added to, subtracted from, or replace the contents of the previous selection mask. This procedure is affected by the following context setters: 'gimp-context-set-feather', 'gimp-context-set-feather-radius'.</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

A simple use of this function which selects a rectangle in the middle of an image and paints that rectangle with a user defined color. This example also introduces a couple of new features we haven't seen before:

*   The script is associated with an image since its menu path starts with "&lt;Image&gt;/...". Note that as a result of this the callback sub in line 6 receives two additional parameters, the active image and the selected drawable.
*   The use of the PDB functions <tt>gimp_image_undo_group_start</tt> and <tt>gimp_image_undo_group_end</tt>. These functions declare an undo group. When an undo is done on the image, instead of having the individual operators undo, all the actions between the undo start and the undo end calls will be undone at once.

<table markdown='1' class='tut'> 
<tbody>
<tr>
<th bgcolor="#E0E0FF">[paint-select](paint-select)</th>
</tr>
<tr>
<td bgcolor="#FFE0E0"><font color="black">

    #!/usr/bin/perl -w 

    use Gimp; 
    use Gimp::Fu; 

    podregister { 
     my ($width, $height) = ($image->width, $image->height); 
     # Select a rectangle inside the image and paint it with color 
     $image->undo_group_start; 
      $image->select_rectangle( 
        CHANNEL_OP_REPLACE, $width/4, $height/4, $width/2, $height/2, 
      ); 
      Gimp::Context->set_background($color); 
      $drawable->edit_fill(BACKGROUND_FILL); 
      $image->selection_none; 
      $image->undo_group_end; 
      (); 
    }; 

    exit main; 
    __END__ 

    =head1 NAME 

    img_paint_select - Paints the selection 

    =head1 SYNOPSIS 

    <Image>/Filters/Tutorial/Paint Select 

    =head1 DESCRIPTION 

    Paints the selection 

    =head1 PARAMETERS 

    [PF_COLOR, "color", "Rectangle color", [0,0,255]], 

    =head1 RETURN VALUES 

    =head1 IMAGE TYPES 

    * 

    =head1 AUTHOR 

    Dov Grobgeld 

    =head1 DATE 

    1999-05-14 

    =head1 LICENSE 

    Dov Grobgeld 

</font></td>
</tr>
</tbody>
</table>

The result when run on our previous image:

<figure>
<img src="{filename}paint-select.png" alt="paint-select.png" />
</figure>

### 7.1. Complex selections

Besides rectangular selections elliptical selections may also be created through the PDB functions <tt>gimp_image_select_ellipse</tt> and <tt>gimp_image_select_polygon</tt> which allows the selection of ellipses and polygons.

More complex selections may be created through the channel mechanism. The PDB <tt>gimp_channel_new()</tt> (<tt>Gimp::Channel->new</tt>) creates a new channel. The channel is a drawable that may be painted into, just like any other drawable, but with the difference that it is always a grey level image. Once the channel is finished, the channel may be loaded into the selection through the PDB function <tt>gimp_image_select_item</tt>.

Search for "select" in the DB Browser to see a list of all the selection related functions.

### 7.2. Loops

In perl it is trivial to write loops that together with the various selection tools gives powerful creative possibilities. Here is an example that mixes colors in circles. There is nothing really new here, but it shows the power of what we have described above.

<table markdown="1" class='tut'>
<tbody>
<tr>
<th bgcolor="#E0E0FF">[circles](circles)</th>
</tr>
<tr>
<td bgcolor="#FFE0E0"><font color="black">

    #!/usr/bin/perl 

    use Gimp; 
    use Gimp::Fu; 

    podregister { 
     # Create the background 
     my $img = Gimp::Image->new($size, $size, RGB); 
     $layer = $img->layer_new($size, $size, RGB, "Layer 1", 100, NORMAL_MODE); 
      $img->insert_layer($layer, -1, 0); 
      Gimp::Context->set_background($bgcolor); 
      $layer->edit_fill(BACKGROUND_FILL); 
      my $ncircles = int($size/$radius/2); 
      for ($i=0; $i<$ncircles; $i++) { 
        for ($j=0; $j<$ncircles; $j++) { 
          # Select a circle 
          $img->select_ellipse( 
        CHANNEL_OP_REPLACE, $i*$radius*2, $j*$radius*2, $radius*2, $radius*2 
          ); 
          my $color = [$i*30, ($ncircles-$j)*25, ($i+$j)*15]; # mix colors 
          Gimp::Context->set_background($color); 
          $layer->edit_fill(BACKGROUND_FILL); 
        } 
      } 
      Gimp::Display->new($img); 
      return $img; 
    }; 

    exit main; 
    __END__ 

    =head1 NAME 

    circles - a loop 

    =head1 SYNOPSIS 

    <Image>/File/Create/Tutorial/Circles 

    =head1 DESCRIPTION 

    a loop 

    =head1 PARAMETERS 

    [PF_INT32, "size", "Image size", 100], 
    [PF_COLOR, "bgcolor", "Background color", [40,180,60]], 
    [PF_INT32, "radius", "Circle radius", 10] 

    =head1 AUTHOR 

    Dov 

    =head1 DATE 

    1999-05-14 

    =head1 LICENSE 

    Dov 

</font></td>

</tr>

</tbody>

</table>

The result:

<figure>
<img src="{filename}circles.png" alt="circles.png" />
</figure>

## 8. Creating text

### 8.1. Hello World - writing text in an image

To create text the PDB function <tt>gimp_text_fontname()</tt> may be used.

Here is an example of a script that creates an image containing "Hello world".

<table markdown="1" class='tut'>
<tbody>
<tr>
<th bgcolor="#E0E0FF">[hello-world1](hello-world1)</th>
</tr>
<tr>
<td bgcolor="#FFE0E0">

    #!/usr/bin/perl 

    use Gimp; 
    use Gimp::Fu; 

    podregister { 
     my $img = Gimp::Image->new(350, 100, RGB); 
     my $drw = $img->layer_new($img->width, $img->height, 
                RGB, "BG", 100, NORMAL_MODE); 
      $img->insert_layer($drw, -1, 0); 
      Gimp::Context->set_background("black"); 
      $drw->edit_fill(BACKGROUND_FILL); 
      Gimp::Context->set_foreground([255,255,0]); # Choose color of text 
      # Create the text 
      my $textlayer = $drw->text_fontname(0, 0, $text, 10, 1, $size, POINTS, $font); 
      $textlayer->floating_sel_anchor; 
      Gimp::Display->new($img); 
      return $img; 
    }; 

    exit main; 
    __END__ 

    =head1 NAME 

    hello_world1 - basic text 

    =head1 SYNOPSIS 

    <Image>/File/Create/Tutorial/Basic text 1 

    =head1 DESCRIPTION 

    basic text 

    =head1 PARAMETERS 

    [PF_FONT, "font", "Font", "Sans"], 
    [PF_INT32, "size", "Font size", 70], 
    [PF_STRING, "text", "Text", "Hello world!"] 

    =head1 AUTHOR 

    Dov 

    =head1 DATE 

    2004-03-27 

    =head1 LICENSE 

    Dov 

</td>
</tr>
</tbody>
</table>

The result:

<figure>
<img src="{filename}hello-world1.png" alt="hello-world1.png" />
</figure>

One thing to note in this script is that the text that is created on line 15 is a _floating layer_, that needs to be anchored to its parent layer. This is done in line 16 through the call to <tt>gimp_floating_sel_anchor()</tt>.

This script suffers from the problem that the image size is unrelated to the text size. This is taken care of in the following more complex example which shows the basic steps for a logo generating script:

*   Creation of an image of arbitrary size
*   Creation of a background drawable of an arbitrary size
*   Creation of text layer which exactly fits the text with the command <tt>gimp_text_fontname</tt>.
*   Resizing the image and the background to the size of the text layer.

The result is an image composed of two layers; a transparent text layer on top of a uniform background.

<table markdown="1" class='tut'>
<tbody>
<tr>
<th bgcolor="#E0E0FF">[basic-logo](basic-logo)</th>
</tr>
<tr>
<td bgcolor="#FFE0E0"><font color="black">

    #!/usr/bin/perl 

    use Gimp; 
    use Gimp::Fu; 

    podregister { 
     my $img = Gimp::Image->new(100, 100, RGB); # any old size 
     my $background = $img->layer_new( 
       100, 100, RGB, "Background", 100, NORMAL_MODE 
     ); 
     $img->insert_layer($background, 0, 0); 
     Gimp::Context->set_foreground($fgcolor); # Choose color of text 
     # Create the text layer. Using -1 as the drawable creates a new layer. 
     my $text_layer = $img->text_fontname( 
       -1, 0, 0, $text, $border, 1, $size, POINTS, $font 
     ); 
     # Get size of the text drawable and resize the image and the 
     # background layer to this size. 
     my ($width, $height) = ($text_layer->width, $text_layer->height); 
     $img->resize($width, $height, 0, 0); 
     $background->resize($width, $height, 0, 0); 
     # Fill the background layer now when it has the right size. 
     Gimp::Context->set_background($bgcolor); 
     $background->edit_fill(BACKGROUND_FILL); 
     Gimp::Display->new($img); 
     return $img; 
    }; 

    exit main; 
    __END__ 

    =head1 NAME 

    basic_logo - Basic logo 

    =head1 SYNOPSIS 

    <Image>/File/Create/Tutorial/Basic Logo 

    =head1 DESCRIPTION 

    Make a basic logo. 

    =head1 PARAMETERS 

    [PF_FONT, "font", "Font",   "Utopia Bold"], 
    [PF_INT32, "size", "Font size", 10], 
    [PF_INT32, "border", "Border", 10], 
    [PF_STRING, "text", "Text", "Hello world!"], 
    [PF_COLOR, "bgcolor", "Background color", [40,180,160]], 
    [PF_COLOR, "fgcolor", "Foreground color", [255,255,0]], 

    =head1 AUTHOR 

    Dov Grobgeld 

    =head1 DATE 

    2004-03-27 

    =head1 LICENSE 

    Dov Grobgeld 

</font></td>

</tr>

</tbody>

</table>

Note the special syntax of <tt>gimp_image_text_fontname</tt> in line 14 in <tt>basic-logo</tt> with the drawable = -1. The special case drawable=-1 means that instead of creating a floating layer, a new image layer will be created.

The dialog and the resulting image:

<figure>
<img src="{filename}basic-logo-dialog.png" alt="basic-logo-dialog.png" />
</figure>

## 9. Floating selections

When a region has been selected through one of the selection routines, the area outlined by the selection may be copied to the cut-buffer through the <tt>gimp_edit_copy</tt> command. The cut-buffer may subsequently be pasted into a different layer through the <tt>gimp_edit_paste</tt> command. When a layer is pasted it becomes a floating selection. This floating selection may be moved to its required position by the command <tt>gimp_layer_set_offsets</tt>, and finally it is pasted by the <tt>gimp_floating_sel_anchor</tt> command. Another way of determining the position of a pasted layer is to create a selection in the target image before the cut-buffer is pasted.

This is illustrated in the following program, which works on one image and takes as a parameter another image, which it concatenates to the right of the first image. The lines 28-38 shows how the second image is copied and glued into the first image.

<table markdown="1" class='tut'>
<tbody>
<tr>
<th bgcolor="#E0E0FF">[horiz-cat](horiz-cat)</th>
</tr>
<tr>
<td bgcolor="#FFE0E0"><font color="black">

    :::perl
    #!/usr/bin/perl 

    use Gimp; 
    use Gimp::Fu; 

    podregister { 
     die "Must select layer.\n" unless $drawable->is_layer; 
     $drawable->become('Gimp::Layer'); 
     my $image2 = $drawable2->get_image; 
     my ($w1, $h1) = ($drawable->width, $drawable->height); 
     my ($w2, $h2) = ($drawable2->width, $drawable2->height); 
     my $hmax = $h1 > $h2 ? $h1 : $h2; # new height is maximum height of the images 
     $image->undo_group_start; # Create an undo group 
     # Resize the drawable layer to make room for the image 
     $image->resize($w1+$w2, $hmax, 0, ($hmax-$h1)/2); 
     $drawable->resize($w1+$w2, $hmax, 0, ($hmax-$h1)/2); 
     # Copy $drawable2 and paste it into the new space of $drawable1 
     $image2->selection_all; # select all of image2 
     $drawable2->edit_copy; 
     $image2->selection_none; 
     # make a selection in image 1 where $drawable2 is to be pasted 
     $image->select_rectangle(CHANNEL_OP_ADD, $w1, ($hmax-$h2)/2, $w2, $h2); 
     $drawable->edit_paste(0)->floating_sel_anchor; # paste and then anchor it 
     $image->undo_group_end; # Close the undo group 
     return; 
    }; 

    exit main; 
    __END__ 

    =head1 NAME 

    horiz_cat - Horizontal concat 

    =head1 SYNOPSIS 

    <Image>/Filters/Tutorial/Horizontal Concat 

    =head1 DESCRIPTION 

    Horizontal concatenation of images. 

    =head1 PARAMETERS 

    [PF_DRAWABLE,   "drawable2", "Drawable to concatenate", undef], 

    =head1 IMAGE TYPES 

    * 

    =head1 AUTHOR 

    Dov Grobgeld 

    =head1 DATE 

    2004-03-27 

    =head1 LICENSE 

    Dov Grobgeld 

</font></td>
</tr>
</tbody>
</table>

You might notice something very important on lines 7 and 8: we "know" that we'll always pass a layer as the first drawable, but we're checking that anyway. Then we're telling Gimp-Perl the drawable definitely _is_ a layer. The reason for that is that (obviously) <tt>Gimp::Layer</tt> and <tt>Gimp::Drawable</tt> have different methods available to them, and what matters here is that <tt>Gimp::Drawable</tt> does not have a resize method. (i.e. The PDB does not have a <tt>gimp_drawable_resize</tt> function)

## 10. The Perl Server and stand-alone scripts

So far the scripts have all been started from the menu structure within GIMP. But using <tt>Gimp::Fu</tt> there is another possibility, and that is to run the scripts from the command line, as a normal Perl program. When run this way the script tries to connect to the Perl-Server, and if it fails it will launch a GIMP of its own. If you plan to run several scripts this way, it is obviously much faster to run the Perl-Server since launching GIMP takes quite a bit of time. The Perl-Server may be started from the <tt>Filters/Perl</tt> menu.

When a <tt>Gimp::Fu</tt> script is run from the command line, the result is the same as when it is run through the menus, except that it may be run with the <tt>--output</tt> parameter. This will save the result to a file instead of displaying it within GIMP. This is great for batch creation of logos, etc.

The filename for the <tt>--output</tt> has some special magic that allows to set some special image saving parameters, like interlace, quality factor, etc. See the [<tt>Gimp::Fu</tt> docs](http://search.cpan.org/dist/Gimp/Gimp/Fu.pm#MISCELLANEOUS_FUNCTIONS) for more detail

Here are two invocations of the scripts declared above, but with output written to a jpg file and a png file.

<table border="None" class='tut'>
<tbody>
<tr>
<th bgcolor="#E0E0FF"><a href="perl-gimp-from-shell">perl-gimp-from-shell</a></th>
</tr>
<tr>
<td bgcolor="#FFE0E0"><font color="black">
<pre> <font color="red" size="-1">1:</font> uni -o /tmp/uni.png --size 100 --color purple 
 <font color="red" size="-1">2:</font> basic-logo --font 'utopia 100' -o /tmp/bl.ppm --size 20 --text "Perl rules" </pre>
</font></td>
</tr>
</tbody>
</table>

Another important use of this interface is that it enables running the Perl debugger on the perl scripts.

### 10.1. A shell for Gimp-Perl

When using the Perl-Server it is not necessary to use <tt>Gimp::Fu</tt> and the <tt>podregister</tt> function. Instead you may call <tt>Gimp::on_net</tt>, which takes as a parameter a reference to a sub routine that is called when your script has connected to a GIMP (or started one up).

For a simple but powerful example of the use of the Gimp without Fu, here is a an interactive Gimp-Perl shell that may be run from the command line:

<table markdown="1" class='tut'> 
<tbody>
<tr>
<th bgcolor="#E0E0FF">[pg-shell](pg-shell)</th>
</tr>
<tr>
<td bgcolor="#FFE0E0"><font color="black">

    #!/usr/bin/perl 

    #  An interactive command line shell to GIMP. 
    use Gimp; 
    use Term::ReadLine; 

    Gimp::on_net { 
       $term = new Term::ReadLine("Gimp"); 
       while( defined ($_ = $term->readline("Gimp> "))) { 
            $res = eval($_) . "\n"; 
            print("Error: $@"), next if $@; 
            print "\n"; 
            Gimp->displays_flush(); 
        } 
     }; 
     
     exit Gimp::main; 

</font></td>
</tr>
</tbody>
</table>

Here is an example of an interactive session with this shell:

<table border="None" class='tut'>

<tbody>

<tr>

<th bgcolor="#E0E0FF"><a href="interact">interact</a></th>

</tr>

<tr>

<td bgcolor="#FFE0E0"><font color="black">

<pre> <font color="red" size="-1">1:</font> Gimp> $img = Gimp::Image->new(100,100,RGB) 
 <font color="red" size="-1">2:</font> Gimp> $drw = $img->layer_new(100,100,RGB_IMAGE, "bg", 100, NORMAL_MODE) 
 <font color="red" size="-1">3:</font> Gimp> $img->insert_layer($drw,-1, 0) 
 <font color="red" size="-1">4:</font> Gimp> Gimp::Display->new($img) 
 <font color="red" size="-1">5:</font> Gimp> $drw->edit_clear 
 <font color="red" size="-1">6:</font> Gimp> print Gimp::Image->list 
 <font color="red" size="-1">7:</font> Gimp::Image->existing(1) </pre>

</font></td>

</tr>

</tbody>

</table>

## 11. End notes

This tutorial has covered only a small part of the possibilities available to a script writer. In particular the following issues available to Gimp::Perl scripts have not been covered:

*   The possibility of writing customized Gtk interfaces (see <tt>[examples/example-no-fu](http://search.cpan.org/dist/Gimp/examples/example-no-fu)</tt> in the Gimp-Perl distribution).
*   Writing fully-fledged plug-ins that manipulate the tile data through the Perl Data Language (PDL) module (see <tt>[examples/map_to_gradient](http://search.cpan.org/dist/Gimp/examples/map_to_gradient)</tt> in the Gimp-Perl distribution).
*   Using Gimp-Perl in a CGI environment.
*   How to fill with gradients in a plugin (see <tt>[examples/randomblends](http://search.cpan.org/dist/Gimp/examples/randomblends)</tt> in the Gimp-Perl distribution).
*   How to do polygon selections (see <tt>[examples/triangle](http://search.cpan.org/dist/Gimp/examples/triangle)</tt> in the Gimp-Perl distribution).

The Gimp-Perl distribution also has over 50 more example scripts supplied. Take a look through those for further inspiration!

## 12. Links and references

*   [<tt>Gimp::Fu</tt> documentation](http://search.cpan.org/dist/Gimp/Gimp/Fu.pm)
*   [The rest of the Gimp-Perl module docs](http://search.cpan.org/dist/Gimp/)
*   [GIMP Registry with Perl plug-ins](http://registry.gimp.org/)

---


<small>Please send your comments to [dov.grobgeld@gmail.com](mailto:dov.grobgeld@gmail.com).</small>

<small>
<a href='http://creativecommons.org/licenses/by-sa/3.0/deed.en_US'>
<img class='cc-badge' src='/images/creativecommons/by-sa 80x15.png' alt='Creative Commons By Share Alike'/>
</a>
<span xmlns:dct="http://purl.org/dc/terms/">GIMP Tutorial - A Tutorial for GIMP-Perl Users (text & images)</span> 
by [Ed J] is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US).
</small>

