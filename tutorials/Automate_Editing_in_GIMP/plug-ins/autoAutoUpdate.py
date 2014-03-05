#! /usr/bin/env python
#
#   File = autoAutoUpdate.py
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
#
if os.name == 'posix':
    Home = os.environ['HOME']
elif os.name == 'nt':
    Home = os.environ['HOMEPATH']
xcfDir = os.path.join(Home, "Pictures")
#
flowObj = BaseXmlReader()

def updateImage(fileName):
    """This image update function operates on one image at a time. 
    The variables are 'local' for each step for each image and go
    out of scope when a particular image update is finished.  The
    updateImage function is called by autoAutoUpdate.
    The WorkFlow Step commands are pulled from a 'tree' which is
    accessed through the BaseXmlReader class (from autoBase).
    """
    # Open the image indicated by passed fileName
    theImage = pdb.gimp_file_load(fileName, fileName)
    theActiveLayer = pdb.gimp_image_get_active_layer(theImage)
    # Get the image update flag and Flow Control properties
    UpdateFlag = str(theImage.parasite_find('UpdateFlag'))
    Flow = str(theImage.parasite_find('Flow'))
    CurrentStep = str(theImage.parasite_find('CurrentStep'))
    NextStep = str(theImage.parasite_find('NextStep'))
    pIndex = 5
    # If the update flag is "NO" do nothing and close the image. (done)
    #   autoAutoUpdate will move on to the next image
    if (UpdateFlag == 'NO'):
        pdb.gimp_image_delete(theImage)
    elif (UpdateFlag == "YES"):
        # get the list of commands and new next step based on the
        #   current state and flow of this image
        commandList, NewNextStep = flowObj.FlowExtract(Flow, NextStep)
        # Run the commands for this step
        for Cmd in commandList:
            exec(Cmd)
        # Update the properties
        theImage.attach_new_parasite('CurrentStep', pIndex, NextStep)
        theImage.attach_new_parasite('NextStep', pIndex, NewNextStep)
        theImage.attach_new_parasite('UpdateFlag', pIndex, 'NO')
        # Save the image and close it
        theActiveLayer = pdb.gimp_image_get_active_layer(theImage)
        pdb.gimp_xcf_save(0, theImage, theActiveLayer, fileName, fileName)
        pdb.gimp_image_delete(theImage)
    else:
        pdb.gimp_message("Parasite UpdateFlag has an unexpected value\n")
#    
def autoAutoUpdate(srcPath):
    """Registered function autoAutoUpdate. Creates a list of all of the
    *.xcf files in a selected directory and calls a function 'updateImage'
    with each filename in that list.
    """
    pdb.gimp_displays_flush()
    # Find all of the Xcf files.
    allFileList = os.listdir(srcPath)
    srcFileList = []
    for fileName in allFileList:
        if fileName.count('.xcf') > 0:
            fullName = os.path.join(srcPath, fileName)
            srcFileList.append(fullName)
    #   Pass them one at a time to function updateImage
    for fileName in srcFileList:
        updateImage(fileName)
#
############################################################################
#
register (
    "autoAutoUpdate",         # Name registered in Procedure Browser
    "Auto Update a Directory of Images", # Widget title
    "Auot Update a Directory of Images", # 
    "Stephen Kiel",         # Author
    "Stephen Kiel",         # Copyright Holder
    "Aug 2013",             # Date
    "2) Auto Update Images (Directory)", # Menu Entry
    "",     # Image Type - Operate with NO image loaded
    [
    ( PF_DIRNAME, "srcPath", "XCF (source) Directory:", xcfDir ),
    ],
    [],
    autoAutoUpdate,   # Matches to name of function being defined
    menu = "<Image>/Automation"  # Menu Location
    )   # End register
#
main() 
