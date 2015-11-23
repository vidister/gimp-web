Title: The Print Plugin
Date: 2015-08-14T15:07:00-05:00
Author: Pat David
Status: hidden




<figure>
<img src='print-main.png' alt="Main Window" />
<figcaption>
Figure 1\. The Main Window
</figcaption>
</figure>

The main window is divided into five panes:

<dl>
<dt><span class="GUILABEL">Preview</span></dt>
<dd>
The <span class="GUILABEL">Preview</span> pane contains a <span class="GUIBUTTON">positioning widget</span> that allows interactively positioning the output on the page. It contains an outer border, representing the sheet of paper; an inner border, representing the printable area of the printer; an arrow, pointing to the top of the page (the end that's fed into the printer); and a black rectangle, representing the position of the image on the page. The image can be moved around on the paper. When the first (<span class="MOUSEBUTTON">left</span>) button is used, the image is moved in screen pixels; when any other button is used, the image is moved in points[[1]](#FTN.AEN19). The arrow resizes depending upon the media size chosen; the shaft of the arrow is always equal to one inch on the output.
</dd>

<dt><span class="GUILABEL">Printer Settings</span></dt>
<dd>
The <span class="GUILABEL">Printer Settings</span> pane contains a dropdown menu for selecting a printer to print to. There is a special <span class="QUOTE">"printer"</span> named File that allows you to choose a file to print to, rather than a printer queue. The <span class="GUILABEL">Setup</span> box to the right allows specification of a printer type, a PPD file[[2]](#FTN.AEN29), and the command to be used to print. Each distinct printer in the <span class="GUIBUTTON">Printer</span> list can have different settings applied to it. Below that is a <span class="GUIBUTTON">combo box</span> allowing choice of media size. The choices are constrained to those that the printer supports. Below that are <span class="GUIBUTTON">dropdown</span> menus for choosing media type (what kind of paper), media source (what input tray), ink type, and resolution. All of these settings are printer-specific.


<figure>
<img src="print-setup.png" alt="Print Setup" />
<figcaption>
Figure 2. The setup
</figcaption>
</figure>

</dd>

<dt><span class="GUILABEL">Position</span></dt>
<dd>
The <span class="GUILABEL">Position</span> pane contains various widgets to place the image on the paper. These widgets work in conjunction with the <span class="GUILABEL">Preview</span> pane. At the top left of the pane is a button to center the image on the paper (not on the printable area). To its right is a <span class="GUIBUTTON">button group</span> that allows choosing English (inch) units or metric (centimeter) units. Below these are <span class="GUIBUTTON">four boxes</span> that allow entry of the left, top, right, and bottom of the image. These positions are relative to the top left of the paper[[3]](#FTN.AEN48). There are two additional boxes that allow specification of the right margin and bottom margin if you prefer; these are relative to the bottom right corner of the paper. Any of these may have values entered into them; the preview image will be moved appropriately.

<blockquote>**Note:** These entries do not resize the image.</blockquote>

Finally, there is a pick box for <span class="GUIBUTTON">orientation</span> (landscape or portrait). There is an <span class="GUIBUTTON">Auto</span> mode that picks the orientation that yields the orientation that best matches that of the image to be printed.
</dd>

<dt><span class="GUILABEL">Scaling</span></dt>
<dd>
The <span class="GUILABEL">Scaling</span> pane contains a slider that allows scaling of the image. The image can be scaled in either percent of the printable area (NOT the page in this case) or pixels per inch (<span class="ACRONYM">PPI</span>) via a <span class="GUIBUTTON">radio button</span> below the slider. <span class="ACRONYM">PPI</span> allows matching image resolution to printer resolution. The image may be scaled using either method to between 5 and 100% of the imageable area. It is not possible to crop with the Print plugin. In <span class="GUIBUTTON">Percent</span> mode, the image is scaled so that neither axis will be longer than the percent of the printable area specified. For example, if you print an image at 20%, it will be possible to tile the image 5 times on one axis and at least 5 times on the other. To the right of the radio button is a button called <span class="GUIBUTTON">Set Image Scale</span>. This sets the scaling to <span class="ACRONYM">PPI</span>, and sets the resolution as closely as possible to the resolution stored in the image. To the right of the <span class="GUIBUTTON">Set Image Scale</span> button are two boxes that allow entry of <span class="GUIBUTTON">width</span> and <span class="GUIBUTTON">height</span> of the image. These set the scaling mode to <span class="ACRONYM">PPI</span>. Specifying one automatically sets the other, and the image is repositioned as needed to prevent it from falling off the edge of the page.
</dd>

<dt><span class="GUILABEL">Image Settings</span></dt>

<dd>

The <span class="GUILABEL">Image Settings</span> pane allows choice of <span class="GUIBUTTON">Line Art</span>, <span class="GUIBUTTON">Solid Colors</span>, <span class="GUIBUTTON">Photograph</span>, or <span class="GUIBUTTON">Monochrome</span> image type. Line art or Solid Colors should be used for graphics containing mostly solid areas of color. They're very similar to each other. Photograph mode dithers more slowly, but produces more accurate colors. Finally, Monochrome mode can be used to print absolute black and white very quickly. To the right of these four radio buttons is a button called <span class="GUIBUTTON">Adjust Color</span>. This pops up a new window that controls various output quality settings. That will be described separately. Finally, there is a choice of Black and White and Color output.

</dd>

<dt><span class="GUILABEL">Action Buttons</span></dt>
<dd>
The last pane contains four action buttons:

*   <span class="GUIBUTTON">Print and Save Settings</span> — immediately print the image (or, if the File printer is chosen, display a file selection window to pick the output file), and save all current settings for all printers.

*   <span class="GUIBUTTON">Save Settings</span> — immediately save the settings, and continue working in the Print plugin.

*   <span class="GUIBUTTON">Print</span> — immediately print the image (or, if the File printer is chosen, display a file selection window to pick the output file), but do not save settings.

*   <span class="GUIBUTTON">Cancel</span> — immediately quit without saving or printing.

</dd>

</dl>


<div class="SECT2">

## <a name="ADJUST-COLOR"><span class="GUIBUTTON">Adjust Color</span></a>

The Adjust Color button button pops up a non-modal dialog that allows adjustment of various parameters related to the print quality. These are independent of the controls within the <span class="APPLICATION">GIMP</span> itself and only affect the print.

<div class="FIGURE"><a name="PRINT-COLOR-PNG"></a>

**Figure 3\. The Color Settings**

<div class="MEDIAOBJECT">

![](print-color.png)

</div>

</div>

At the top of the window is a thumbnail of the image that changes to reflect the color settings of the image. This enables you to get an idea of how the image will print out as you adjust settings.

Below that there are eight sliders:

<div class="VARIABLELIST">

<dl>

<dt><span class="GUILABEL">Brightness (0-2.0, default 1.0)</span></dt>

<dd>

adjust the brightness of the image.

</dd>

<dt><span class="GUILABEL">Contrast (0-4.0, default 1.0)</span></dt>

<dd>

adjust the output contrast.

</dd>

<dt><span class="GUILABEL">Cyan, Magenta, Yellow (0-4.0, default 1.0)</span></dt>

<dd>

adjust the cyan, magenta, and yellow in the output. These should not normally need to be adjusted very much; even very small adjustments can go quite a long way to restoring color balance..

</dd>

<dt><span class="GUILABEL">Saturation (0-9.0, default 1.0)</span></dt>

<dd>

adjust the color brilliance (saturation) of the output. Saturation of 0 means pure gray scale, with no color. Saturation of 9.0 will make just about anything but pure grays brilliantly colored.

</dd>

<dt><span class="GUILABEL">Density (0.1-2.0, default 1.0)</span></dt>

<dd>

adjust the density (amount of ink) in the print. The density is automatically corrected for the particular printer, resolution, and in some cases paper choices. If solid black in the input is not solid in the print, the density needs to be increased; if there is excessive ink bleed-through and muddy dark colors, the density should be decreased.

<div class="NOTE">

> **Note:** that the density will not increase beyond a certain amount no matter what the slider is set to.

</div>

</dd>

<dt><span class="GUILABEL">Gamma (0.1-4.0, default 1.0)</span></dt>

<dd>

adjust the output gamma. The gamma value is automatically corrected for the choice of printer; this is used if you believe the automatic setting is incorrect.

</dd>

<dt><span class="GUILABEL">Dither Algorithm</span></dt>

<dd>

There is also a selection box for the <span class="GUILABEL">dither algorithm</span> to be used. There are currently seven choices:

*   Adaptive Hybrid usually yields the best output quality; it chooses a modified Floyd-Steinberg error diffusion algorithm or ordered dithering depending upon the image characteristics.

*   Ordered uses a pure ordered dither. It generally yields excellent quality for simple black and white or four color printers without variable drop size or drop modulation; it is not recommended if high quality is desired on six color printers. It is considerably faster than Adaptive Hybrid.

*   Fast also uses a pure ordered dither, but uses a very simple black model and makes no attempt to handle multi-level (6-color, variable drop size, or drop modulation) at all cleanly. It is substantially faster than Ordered dither. The quality tends to be quite poor except on simple four color printers. On three color printers, quality is probably competitive with anything else.

*   Very Fast is similar to Fast, except that it uses a very simple dither matrix that can be looked up much more quickly than the matrix used in the Fast dither. For simple pure black and white images dominated by horizontal and vertical lines, this may actually yield the best results; for other types of image, the quality will be poor.

*   Adaptive Random is similar to Adaptive Hybrid, except that the modifications to the Floyd-Steinberg algorithm are slightly different. This is slower than Adaptive Hybrid on most systems. For some images the quality may be better than Adaptive Hybrid, but generally Adaptive Hybrid should yield slightly superior images.

*   Hybrid Floyd-Steinberg uses the modified Floyd-Steinberg algorithm of Adaptive Hybrid on the entire image. Generally, the results are poor in pale regions.

*   Random Floyd-Steinberg uses the modified Floyd-Steinberg algorithm of Adaptive Random on the entire image. Generally, the results are poor in pale regions.

</dd>

</dl>

</div>

</div>

</div>

### Notes

<table border="0" class="FOOTNOTES" width="100%">

<tbody>

<tr>

<td align="LEFT" valign="TOP" width="5%">[[1]](print.html#AEN19)</td>

<td align="LEFT" valign="TOP" width="95%">

the output resolution of the plugin

</td>

</tr>

<tr>

<td align="LEFT" valign="TOP" width="5%">[[2]](print.html#AEN29)</td>

<td align="LEFT" valign="TOP" width="95%">

for Postscript printers

</td>

</tr>

<tr>

<td align="LEFT" valign="TOP" width="5%">[[3]](print.html#AEN48)</td>

<td align="LEFT" valign="TOP" width="95%">

again, that's relative to the paper corner, not the printable area, which is usually smaller

</td>

</tr>

</tbody>

</table>
