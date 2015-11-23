Title: Simple Paths (Bezier Selections)
Date: 2015-08-18T16:27:00-05:00
Modified: 2015-08-18T16:27:04-05:00
Author: Tuomas Kuosmanen


Text and images Copyright (C) 2002 [Tuomas Kuosmanen](mailto:tigertNOSPAM@gimp.org) and may not be used without permission of the author.

## Intention

The Path tool (previously known as Bezier Selection) is a powerful tool in GIMP. The rectangle- and ellipse-selections are not very flexible if you happen to need something more special. And since many of us GIMPers don't have a graphics tablet, it's not so easy to make the mouse pointer move the way you want. The paths can solve the problem by using smooth mathematical curves instead your own shaky mouse trail. Paths are also very useful when used with gradient fills, see [Drawing Shapes with Bezier](/tutorials/Drawing_Shapes/) for more information on this great tool.

## What is it?

<figure>
<img src="{filename}bezier_box.png" alt="bezier_box.png" />
</figure>

![Bezier Button]({filename}bezier_button.png)The Path tool can make complex selections by specifying certain points that are connected together with a curve. So to make a box you would specify four points, one for each corner of the box. Example in image above. The great thing is the corners don't have to be 90 degrees.   
In older GIMP versions (1.2.x), you had to close all paths by joining the last point of the path to the first one. This is not necessary anymore in 2.0 and later versions, but this is still useful to create closed shapes such as a box. So after creating the fourth point, press and hold the Ctrl key and click on the first point to close the path. Of course you can have as many points as you need.   
Finally, click the "Stroke Path" button (in the Path Options dialog) or use the menu Edit->Stroke Path... to draw the new shape. You can also use the button "Create Selection from Path" if you want to have a selection that you can fill or stroke.

## Modifying the curves

<figure>
<img src="{filename}bezier_curve.png" alt="bezier_curve.png" />
</figure>

Straight lines alone are a useful thing, but it's not all. Actually they are not lines but curves. Cool anti-aliased smooth curves.   
The curves can be modified quite flexibly by adjusting the 'handles' of the nearest points. 'What handles?' you say... See the image above? The small circles are those familiar points we used with the box in the previous section. The little boxes are those handles. The handles are not visible by default, you must drag them 'out' from a point. To make the handles visible 1\. click to a point to make it active, 2\. while pressing the Ctrl key, click again on the same point and 3\. drag the handles out with the mousebutton still pressed down. You notice the curves between the points are not straight anymore. You can control the shapes by dragging the handles around.

## A Few Tips

*   Always before modifying any points or handles, click the handle or a point to make it active.
*   To have a smooth curve, both handles should be aligned at each point. Press Shift while dragging a handle to ensure that the other one remains aligned.
*   A path can have multiple components. If you have closed a path, you can create a new component by clicking where you want to place the first point of the new component.
*   If you want to create several components without closing them, press Shift and click where you want to start a new one.
*   When you are satisfied with the shape, you can use Stroke Path or Create Selection from Path.
*   The default GIMP installation creates a dock containing the tabs "Layers, Channels, Paths, Undo". Click on the Paths tab to manage your paths.

The original tutorial can be found [here](http://www.tigert.com/gimp/tutorials/bezier/).   
It was updated for GIMP 2.0 by Raphaël Quinet.

