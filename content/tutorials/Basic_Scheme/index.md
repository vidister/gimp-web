Title: Basic Scheme
Date: 2015-08-18T16:27:00-05:00
Modified: 2015-08-18T16:27:04-05:00
Author: Dov Grobgeld


Text and images Copyright (C) 2002 [Dov Grobgeld](mailto:dovNOSPAM@imagic.weizmann.ac.il) and may not be used without permission of the author.

_Editor's note: since this tutorial was published, the old GIMP Script-Fu interpreter (SIOD) has been replaced by a newer and better one (TinyScheme). A [Script-Fu migration guide](/docs/script-fu-update.html) is available._

## Intention

One of the wonderful features of GIMP is that it all its functionality may be accessed through scripting. The major scripting language for GIMP that has been attached to it today is Scheme. This document will try to be a brief introduction to Scheme, just teaching the essentials in order to write Script-Fu scripts, without getting into the programming language theory that is so typical of other Scheme references.

## 1\. Expressions

Scheme is a Lisp variant and all expressions are surrounded by parentheses. E.g. a list which will calculate the sum of 3 and 4 is written

    :::scheme
	(+ 3 4)


The + sign is the addition function and 3 and 4 are the first and second parameters to this function. Expressions may be nested, so the expression (3+4)*(5/6) would in Scheme be written

    :::scheme
	(* (+ 3 4) (/ 5 6))


White space has no importance so the above expression may as well be written:

    :::scheme
    (*
     (+ 3 4)
     (/ 5 6))


## 2\. Functions

Aside from the four arithmetic functions that are represented through the symbols + - * / there are lots of other functions built into the language. All of them have the form

    :::scheme
    (foo param1 param2 ...)


Additional functions may be defined by the user through the define keyword. E.g. a function that calculates the square value of its single argument may be declared like this

    :::scheme
    (define (square x) (* x x))


and this function may be called through

    :::scheme
    (square 5)


## 3\. Variables and lists

Variables may be declared and set through the set! command. (These variables will be global but this should not bother the casual GIMP programmer). Here are a couple of assignments:

    :::scheme
    (set! grey_value 85)
    (set! angle (* (/ 30 180) 3.141)


Lisp and its variants make heavy use of lists. Script-Fu is no exception and it uses e.g. a list of three elements to write a RGB color. E.g. the color orange would be written

    :::scheme
    '(255 127 0)


The ' sign is necessary in order to tell Scheme that this is a literal list. If the ' was omitted Scheme would try to look up a function with the name 255 and send it the two parameters 127 and 0, which is obviously not what we want.

To create a variable called orange with the above value and then set the background color to it we may do

    :::scheme
    (set! orange '(255 127 0))
    (gimp-set-background-color orange)


## 3.1 car, cdr and friends (*)

A list in Scheme is always composed of a head and a tail. The head is the first entry in the list, and the tail is the rest of the elements in the list. This means that the list (255 127 63) really means (255 (127 (63 ()))) but Scheme allows the previous form as a shortcut. The car function is used to return the head of the list and the cdr (usually pronounced cudder) is used to get the tail of the list.

[The following is a test of the above functions which may be interactively conducted in the Script-Fu console.]

    :::scheme
    => (set! color '(255 127 63))
    (255 127 63)
    => (car color)
    255
    => (cdr color)
    (127 63)


To get the blue component of a color it is necessary to apply the cdr function twice and then the car function.

    :::scheme
    => (car (cdr (cdr color)))
    63


This is very inconvenient to write. Therefore there have been defined abreviations of the form cadr, cddr, caddr, etc that concatenate the operations described above. The previous expression may therefore be much more conveniently written:

    :::scheme
    => (caddr color)
    63


For the Script-Fu writer one of the most important uses of the car function is to access the returned values from the built-in GIMP functions. All gimp-functions return a list, and even if the list contains only one element it must be accessed by car. This is e.g. the case for the important functions gimp-new-image and gimp-new-layer used below.

## 3.2 Local variables (*)

More experienced Scheme programmers mostly use local variables instead of the global variables described above. This is considered better programming practice and this construct should be recognized in order to be able to read others Script-Fu scripts.

Local variables are declared through the the let keyword as in the following example:

    :::scheme
    (let* ((a 3)
           (b 4))
          ((* a b)))


Here a and b have a local scope and retain their values only up to the closing paren matching the one before let\* .

## 4\. The GIMP PDB

All functionality of GIMP is available through the procedural database (PDB). Each procedural database function has a corresponding Scheme function mapping. E.g.

    :::scheme
    (gimp-image-new 100 150 RGB)


produces a new GIMP image of type RGB and size 100x150.

All the functions of the PDB may be accessed through the Procedure Browser that is available from the main menu through <span class="filter">Xtns ->Procedure Browser</span>.... E.g. the Procedure Browser entry for uni-img, which we will define in the example below looks like this:

<figure>
<img src="{filename}pdb-uni-entry.png" alt="pdb-uni-entry.png" />
</figure>

For the Script-Fu programmer this information shows that uni-img may be called with three parameters of the types INT32, STRING and COLOR. The different types will be explained below.

## 5\. Registering the script with Script-Fu

After a function has been written it has to be registered with Script-Fu before it can be used. This is done through the Scheme function script-fu-register. The registering has following purposes:

1.  Tell Script-Fu the type of parameters the script takes and give these parameters default values.
2.  Give the script a name to be used as the menu label.
3.  Register the script as a command in the PDB.

The last point above actually means that a script is from Gimp's viewpoint in no way different from a built-in command or a plugin command. As long as a command is registered in the PDB it can be called by any script or plugin.

The parameters of script-fu-register may be divided into two groups. The first group of seven parameters must always be given. These are:

1.  The name of the function.
2.  The name of the script to be used as a menu entry.
3.  A help string describing the function of the script.
4.  The script author.
5.  The script copyright.
6.  Script date.
7.  List of valid image types for the script. This only has a meaning on scripts operating on images that already exist.

After these seven parameters have been given, a list of the parameters required by the script follows. Each parameter is given as a group of three items:

1.  The type of the parameter. Some of the valid types are:

    <dl>

    <dt>**SF-COLOR**</dt>

    <dd>An RGB color.</dd>

    <dt>**SF-TOGGLE**</dt>

    <dd>A true or false value.</dd>

    <dt>**SF-STRING**</dt>

    <dd>A string of characters enclosed in double quotes.</dd>

    <dt>**SF-VALUE**</dt>

    <dd>Any scalar value, integer, or floating point.</dd>

    <dt>**SF-IMAGE**</dt>

    <dt>**SF-DRAWABLE**</dt>

    </dl>

2.  A label for Script-Fu to display when querying for the parameter.
3.  A default value.

## 6\. A commented script

The following script **uni.scm** receives two parameters from the user, the size of the image and a color, and goes on to produce a uniform image of the requested size and the requested color. Not very useful, but it shows the essential steps in producing a Script-Fu script.

    :::scheme
    ; Define the function of the script and list its parameters
    ; The parameters will be matched with the parameters listed
    ; below in script-fu-register.

    (define (uni-img size color)
      ; Create an img and a layer
      (set! img (car (gimp-image-new size size RGB)))
      (set! layer (car (gimp-layer-new img size size
                                       RGB "layer 1" 100 NORMAL)))

     ; The following is done for all scripts
     (gimp-image-undo-disable img)
     (gimp-image-add-layer img layer 0)

     ; Here is where the painting starts. We now have an image
     ; and layer and may paint in the layer through the PDB functions.
     (gimp-palette-set-background color)
     (gimp-edit-fill layer BG-IMAGE-FILL)

     ; The following is also done for all script
     (gimp-display-new img)
     (gimp-image-undo-enable img))

    ; Finally register our script with script-fu.
    (script-fu-register "uni-img"
                        "Uniform image"
                        "Creates a uniform image"
                        "Dov Grobgeld <dov@imagic.weizmann.ac.il>"
                        "Dov Grobgeld"
                        "2002-02-12"
                        ""
                        SF-VALUE "size" "100"
                        SF-COLOR "color" '(255 127 0))
    (script-fu-menu-register "uni-img" "<Toolbox>/Xtns/Script-Fu/Tutorials")


To test the script save it in $HOME/.gimp-2.2/scripts/uni.scm and then select <span class="filter">Xtns -> Script-Fu -> Refresh</span>:

<figure>
<img src="{filename}refresh.png" alt="refresh.png" />
</figure>

The script **Uniform image** should now appear in the pulldown menu <span class="filter">Xtns -> Script-Fu -> Tutorials -> Uniform image</span>. Selecting this script results in the following popup:

<figure>
<img src="{filename}uni-img.png" alt="uni-img.png" />
</figure>

Accepting these default parameters through the **OK** button gives us the following new image:

<figure>
<img src="{filename}uni-result.png" alt="uni-result.png" />
</figure>

It is also possible to access this script through the Script-Fu console by typing the command

    :::scheme
    (uni-img 100 '(0 255 127))


## 6.1 Hanging a script in the image menu

In the **uni-img** script it was placed under **Xtns/...** in the main Gimp window. This is done to create a new image that is independant of earlier images. It is also possible to create a script which works on an already existing image. If in **script-fu-menu-register** the second argument is written:

&lt;Image&gt;/Script-Fu/...

then the script will be available through the GIMP menu that is launched by the right mouse button over an image. Such script must also have as their first and second argument a SF-IMAGE and a SF-DRAWABLE.

Here is an example script which copies the current layer to a new layer, blurs it and inverts it.

    :::scheme
    ; An example script that blurs an image according to a blur radius.
    ; It illustrates how to hang a script in the image menu, and
    ; how a plug-in may be called.

    (define (script-fu-copy-blur img
                                 drawable
                                 blur-radius)
      ; Create a new layer
      (set! new-layer (car (gimp-layer-copy drawable 0)))

      ; Give it a name
      (gimp-layer-set-name new-layer "Gauss-blurred")

      ; Add the new layer to the image
      (gimp-image-add-layer img new-layer 0)

      ; Call a plugin to blur the image
      (plug-in-gauss-rle 1 img new-layer blur-radius 1 1)

      ; Invert the new layer
      (gimp-invert new-layer)

      ; Flush the display
      (gimp-displays-flush)
    )

    (script-fu-register "script-fu-copy-blur"
                        "Copy and Blur"
                        "Copy and blur a layer"
                        "Dov Grobgeld"
                        "Dov Grobgeld"
                        "2002"
                        "RGB*, GRAY*"
                        SF-IMAGE    "Image"         0
                        SF-DRAWABLE "Layer to blur" 0
                        SF-VALUE    "Blur strength" "5")
    (script-fu-menu-register "script-fu-copy-blur"
                             "<Image>/Script-Fu/Tutorials")



## 7\. Painting areas with selections

In uni-img we called the procedure gimp-edit-fill to fill the whole image. Looking at the info for gimp-edit-fill in the Procedure Browser we find the following:

<table class='tut'>
<tbody>
<tr>
<th align="right" valign="top">Name:</th>
<td class="emphesize" colspan="3">gimp-edit-fill</td>
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
<td valign="top">The type of fill: FG-IMAGE-FILL (0), BG-IMAGE-FILL (1), WHITE-IMAGE-FILL (2), TRANS-IMAGE-FILL (3), NO-IMAGE-FILL (4)</td>
</tr>
<tr>
<th valign="top">Help:</th>
<td colspan="3">This procedure fills the specified drawable with the fill mode. If the fill mode is foreground, the current foreground color is used. If the fill mode is background, the current background color is used. Other fill modes should not be used. This procedure only affects regions within a selection if there is a selection active.</td>
</tr>
</tbody>
</table>

Thus, if we have a selection active when gimp-edit-fill is called, then only the selection is painted. There are lots of ways of choosing a selection as can be seen when searching for a "select" in the PDB. We will use gimp-rect-select, whose entry in the PDB looks as follows:

<table class='tut'>
<tbody>
<tr>
<th align="right" valign="top">Name:</th>
<td class="emphesize" colspan="3">gimp-rect-select</td>
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
<td valign="top">the width of the rectangle: width > 0</td>
</tr>
<tr>
<th></th>
<td valign="top">FLOAT</td>
<td valign="top">height</td>
<td valign="top">the height of the rectangle: width > 0</td>
</tr>
<tr>
<th></th>
<td valign="top">INT32</td>
<td valign="top">operation</td>
<td valign="top">the selection operation: {ADD (0), SUB(1), REPLACE (2), INTERSECT (3) }</td>
</tr>
<tr>
<th></th>
<td valign="top">INT32</td>
<td valign="top">feather</td>
<td valign="top">feather option for selections</td>
</tr>
<tr>
<th></th>
<td valign="top">FLOAT</td>
<td valign="top">feather_radius</td>
<td valign="top">radius for feather operation</td>
</tr>
<tr>
<th valign="top">Help:</th>
<td colspan="3">This tool creates a rectangular selection over the specified image. The rectangular region can be either added to, subtracted from, or replace the contents of the previous selection mask. If the feather option is enabled, the resulting selection is blurred before combining. The blur is a gaussian blur with the specified feather radius.</td>
</tr>
</tbody>
</table>

A simple use of this function which selects the rectangle (x,y,width,height) = (0,25,100,50), paints this region blue, and releases the selection looks as follows:

    :::scheme
    (gimp-rect-select img 0 25 100 50 REPLACE 0 0)
    (gimp-palette-set-background '(0 0 255))
    (gimp-edit-fill layer BG-IMAGE-FILL)
    (gimp-selection-none img)


## 8\. Loops

The only looping construct that exists in Script-Fu is **while**

[Note: this constraint is due to the current Scheme interpreter SIOD used for Script-Fu.] The while loop looks as follows:

    :::scheme
    (while (condition)
    (statement1)
    (statement2)
    :
    )


Here's an example which draws horizontal lines, 16 pixels high, on an image:

    :::scheme
    (set! y 0)
    (while (< y size)
    (gimp-rect-select img 0 y size 16 REPLACE 0 0)
    (gimp-edit-fill layer-one BG-IMAGE-FILL)
    (set! y (+ y 32)))


## 9\. Floating selections

When pasting an image from the clipboard, or when creating text in a a drawable, the result is not put directly in the drawable. Instead it is put into a special temporary layer known as a floating selection. The floating selection may be manipulated in several ways, and finally it is merged into its associated layer, a process known as anchoring.

## 9.1 Hello World - writing text in an image

When creating text through the gimp-text command, the text is always put into a temporary layer. This temporary layer then has to be anchored. Here is an example of creating some text which is pasted into the current drawable:

    :::scheme
    ; An example script that writes a fixed string in the current
    ; image.
    (define (script-fu-hello-world img drawable)

      ; Start an undo group. Everything between the start and the end will
      ; be carried out if an undo command is issued.
      (gimp-undo-push-group-start img)

      ; Create the text. See the Procedure Browser for parameters of gimp-text.
      (set! text-float (car (gimp-text-fontname img drawable
                                                10 10 "Hello world" 0 1 50 0
                                                "Sans")))

      ; Anchor the selection
      (gimp-floating-sel-anchor text-float)

      ; Complete the undo group
      (gimp-undo-push-group-end img)

      ; Flush output
      (gimp-displays-flush))

    (script-fu-register "script-fu-hello-world"
                        "Hello World"
                        "Write Hello World in the current image"
                        "Dov Grobgeld <dov@imagic.weizmann.ac.il>"
                        "Dov Grobgeld"
                        "2002-02-12"
                        "RGB*, GRAY*"
                        SF-IMAGE "Input Image" 0
                        SF-DRAWABLE "Input Drawable" 0)
    (script-fu-menu-register "script-fu-hello-world"
                              "<Image>/Script-Fu/Tutorials")


This script shows another feature we haven't mentioned before. The possibility of creating an undo group. All the commands between the commands gimp-undo-push-group-begin and gimp-undo-push-group-end are undone together if the undo command is issued.

## 9.2 Copying a selection

To copy a selection, the command gimp-edit-copy is used. It places a copy of the selection contents in the cut-buffer. The contents of the cut-buffer may then be pasted into a layer, the same layer or another one, and it is then pasted as a floating layer.

In the following example the selection is copied, pasted into the same layer, offset a fixed distance, finally anchored. Try it by drawing a small blob in the middle of the image, select the blob, and then call this script.

    :::scheme
    ; An example of how to create a floating layer and how to ancor it.
    (define (script-fu-sel-copy img
                              drawable)

      (gimp-undo-push-group-start img)
      (gimp-edit-copy drawable)
      (set! sel-float (car (gimp-edit-paste drawable FALSE)))
      (gimp-layer-set-offsets sel-float 100 50)

      ; Anchor the selection
      (gimp-floating-sel-anchor sel-float)

      ; Complete the undo group
      (gimp-undo-push-group-end img)

      ; Flush output
      (gimp-displays-flush))

    (script-fu-register "script-fu-sel-copy"
                        "Selection Copy"
                        "Copy the selection into the same layer"
                        "Dov Grobgeld"
                        "Dov Grobgeld"
                        "2002-02-12"
                        "RGB*, GRAY*"
                        SF-IMAGE "Image" 0
                        SF-DRAWABLE "Layer" 0)
    (script-fu-menu-register "script-fu-sel-copy"
                             "<Image>/Script-Fu/Tutorials")


The original tutorial can be found [here](http://imagic.weizmann.ac.il/~dov/gimp/scheme-tut.html).

