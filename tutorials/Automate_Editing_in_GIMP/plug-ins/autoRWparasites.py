#! /usr/bin/env python
#
#   File = autoRWparasites.py
#   Part of a set of scripts to Automate the Editing of images with Gimp
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################
#
from gimpfu import *
import os
import re
import xml.etree.ElementTree as ET
from autoBase import *
xmlObj = BaseXmlReader()

#
def autoDisplayAssignedParasites(theImage):
    """Registered function autoDisplayAssignedParasites.  Displays the 
    parasites assigned to the current image in a gimp message window.
    """
    flowPropNameList = ['Flow', 'CurrentStep', 'NextStep']
    flagPropNameList = xmlObj.PropertyNames()

    messageStr = "**Flow Control Parasites\n"
    for parasiteName in flowPropNameList:
        messageStr = messageStr + str(parasiteName) + ":   " + \
            str(theImage.parasite_find(parasiteName)) + "\n"
    messageStr = messageStr + "\n**Status Flag Parasites\n"
    for parasiteName in flagPropNameList:
        messageStr = messageStr + str(parasiteName) + ":   " + \
            str(theImage.parasite_find(parasiteName)) + "\n"
    
    pdb.gimp_message(messageStr)
#
############################################################################
#
register (
    "autoDisplayAssignedParasites",  # Name registered in Procedure Browser
    "Display Parasites",    # Widget title
    "Display Image Parasites in Gimp Message",    # 
    "Stephen Kiel",         # Author
    "Stephen Kiel",         # Copyright Holder
    "July 2013",            # Date
    "A1) Display Assigned Parasites (File)", # Menu Entry
    "*",     # Image Type -  Valid image loaded
    [
    ( PF_IMAGE, "theImage", "Input Image", None ),
    ],
    [],
    autoDisplayAssignedParasites,   # Matches function being defined
    menu = "<Image>/Automation"  # Menu Location
    )   # End register
#
############################################################################
#
def autoMarkAutoUpdate(theImage):
    """Registered function autoMarkAutoUpdate. Writes parasite value to
    YES for for UpdateFlag.  Used for process flow control.  The
    function takes on argument, the image object.
    """
    theImage.attach_new_parasite('UpdateFlag', 5, 'YES')
#
############################################################################
#
register (
    "autoMarkAutoUpdate",         # Name registered in Procedure Browser
    "Mark AutoUpdate", # Widget title
    "Mark AutoUpdate", # 
    "Stephen Kiel",         # Author
    "Stephen Kiel",         # Copyright Holder
    "July 2013",            # Date
    "A2) Mark for AutoUpdate (File)", # Menu Entry
    "*",     # Image Type - Valid image open
    [
    ( PF_IMAGE, "theImage", "Input Image", None ),
    ],
    [],
    autoMarkAutoUpdate,   # Matches to name of function being defined
    menu = "<Image>/Automation"  # Menu Location
    )   # End register
#
############################################################################
#
def autoMarkXcfOverWriteYes(theImage):
    """Registered function autoMarkXcfOverWriteYes. Writes parasite value to
    YES for for UpdateFlag.  Used for process flow control.  The
    function takes on argument, the image object.
    """
    theImage.attach_new_parasite('OverwriteXcf', 5, 'YES')
#
############################################################################
#
register (
    "autoMarkXcfOverWriteYes",         # Name registered in Procedure Browser
    "Mark XCF Overwrite", # Widget title
    "Mark XCF Overwrite", # 
    "Stephen Kiel",         # Author
    "Stephen Kiel",         # Copyright Holder
    "July 2013",            # Date
    "A3) Mark Xcf Overwrite (File)", # Menu Entry
    "*",     # Image Type - Valid image open
    [
    ( PF_IMAGE, "theImage", "Input Image", None ),
    ],
    [],
    autoMarkXcfOverWriteYes,   # Matches to name of function being defined
    menu = "<Image>/Automation"  # Menu Location
    )   # End register
#
############################################################################
#
def autoMarkJpgOverWriteYes(theImage):
    """Registered function autoMarkJpgOverWriteYes. Writes parasite value to
    YES for for OverwriteJpg.  Used for process flow control.  The
    function takes on argument, the image object.
    """
    theImage.attach_new_parasite('OverwriteJpg', 5, 'YES')
#
############################################################################
#
register (
    "autoMarkJpgOverWriteYes",         # Name registered in Procedure Browser
    "Mark XCF Overwrite", # Widget title
    "Mark XCF Overwrite", # 
    "Stephen Kiel",         # Author
    "Stephen Kiel",         # Copyright Holder
    "July 2013",            # Date
    "A4) Mark Jpg Overwrite (File)", # Menu Entry
    "*",     # Image Type - Valid image open
    [
    ( PF_IMAGE, "theImage", "Input Image", None ),
    ],
    [],
    autoMarkJpgOverWriteYes,   # Matches to name of function being defined
    menu = "<Image>/Automation"  # Menu Location
    )   # End register
#
#
############################################################################
#
levelList = xmlObj.PropertyOption('EnhanceColorLevel')
#
def autoSetEnhanceColorLevel(theImage, colorlevelIndex):
    """Registered function autoSetEnhanceColorLevel. Writes parasite value to
    assigned value for for EnhanceColorLevel.  Used for process flow control.
    The function takes two arguments, the image object and parasite value. A
    separate function reads the xml tree to make a list of the available 
    options.  That option list is presented in the PF_OPTION widget.
    """
    pValue = levelList[colorlevelIndex]
    theImage.attach_new_parasite('EnhanceColorLevel', 5, pValue)
#
############################################################################
#
register (
    "autoSetEnhanceColorLevel",         # Name registered in Procedure Browser
    "Set Enhance Color Level Parasite / Property", # Widget title
    "Set Enhance Color Level Parasite / Property", # 
    "Stephen Kiel",         # Author
    "Stephen Kiel",         # Copyright Holder
    "July 2013",            # Date
    "A5) Set Color Enhance Level (File)", # Menu Entry
    "*",     # Image Type - Valid image open
    [
    ( PF_IMAGE, "theImage", "Input Image", None ),
    ( PF_OPTION, "colorlevel", "Select Color Level", 0, levelList ),
    ],
    [],
    autoSetEnhanceColorLevel,   # Matches to name of function being defined
    menu = "<Image>/Automation"  # Menu Location
    )   # End register
#
############################################################################
#
levelList = xmlObj.PropertyOption('EnhanceContrastLevel')
#
def autoSetEnhanceContrastLevel(theImage, colorlevelIndex):
    """Registered function autoSetEnhanceContrastLevel. Writes parasite value to
    assigned value for for EnhanceContrastLevel.  Used for process flow control.
    The function takes two arguments, the image object and parasite value. A
    separate function reads the xml tree to make a list of the available 
    options.  That option list is presented in the PF_OPTION widget.
    """
    pValue = levelList[colorlevelIndex]
    theImage.attach_new_parasite('EnhanceContrastLevel', 5, pValue)
#
############################################################################
#
register (
    "autoSetEnhanceContrastLevel",         # Name registered in Procedure Browser
    "Set Enhance Contrast Level Parasite / Property", # Widget title
    "Set Enhance Contrast Level Parasite / Property", # 
    "Stephen Kiel",         # Author
    "Stephen Kiel",         # Copyright Holder
    "July 2013",            # Date
    "A6) Set Contrast Enhance Level (File)", # Menu Entry
    "*",     # Image Type - Valid image open
    [
    ( PF_IMAGE, "theImage", "Input Image", None ),
    ( PF_OPTION, "colorlevel", "Select Contrast Level", 0, levelList ),
    ],
    [],
    autoSetEnhanceContrastLevel,   # Matches to name of function being defined
    menu = "<Image>/Automation"  # Menu Location
    )   # End register
#
#
############################################################################
#
main() 
