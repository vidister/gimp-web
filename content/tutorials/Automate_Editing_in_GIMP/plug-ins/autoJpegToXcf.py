#! /usr/bin/env python
#
#   File = autoJpegToXcf.py
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
xmlObj = BaseXmlReader()
flowList = xmlObj.FlowNames()

if os.name == 'posix':
    Home = os.environ['HOME']
elif os.name == 'nt':
    Home = os.environ['HOMEPATH']
xcfDir = os.path.join(Home, "Pictures")
jpegDir = os.path.join(Home, "Pictures")

def PropWrite(theImage, pList):
    pIndex = 5
    for (pName, pVal) in pList:
        theImage.attach_new_parasite(pName, pIndex, pVal)

def autoJpgToXcf(srcPath, tgtPath, flowIndex):
    """Registered function autoJpgToXcf, Converts all of the
    jpegs in the source directory into xcf files in a target 
    directory.  Requires two arguments, the paths to the source and
    target directories.  DOES NOT require an image to be open.
    """
    ###
    pdb.gimp_displays_flush()
    open_images, image_ids = pdb.gimp_image_list()
    if open_images > 0:
        pdb.gimp_message ("Close open Images & Rerun")
    else:
        flowName = flowList[flowIndex]
        flowStepDict = xmlObj.FlowFirstNameDict()
        nextStep = flowStepDict[flowName]
        propList = xmlObj.PropertyDefaults()
        propList.append(('Flow', flowName))
        propList.append(('NextStep', nextStep))
        propList.append(('CurrentStep', 'First'))
        allFileList = os.listdir(srcPath)
        existingList = os.listdir(tgtPath)
        srcFileList = []
        tgtFileList = []
        xform = re.compile('\.jpg', re.IGNORECASE)
        # Find all of the jpeg files in the list & make xcf file names
        for fname in allFileList:
            fnameLow = fname.lower()
            if fnameLow.count('.jpg') > 0:
                srcFileList.append(fname)
                tgtFileList.append(xform.sub('.xcf',fname))
        # Dictionary - source & target file names
        tgtFileDict = dict(zip(srcFileList, tgtFileList))
        # Loop on jpegs, open each & save as xcf
        for srcFile in srcFileList:
            # Don't overwrite existing, might be work in Progress
            if tgtFileDict[srcFile] not in existingList:
                tgtFile = os.path.join(tgtPath, tgtFileDict[srcFile])
                srcFile = os.path.join(srcPath, srcFile)
                theImage = pdb.file_jpeg_load(srcFile, srcFile)
                theDrawable = theImage.active_drawable
                # Set Flag Properties / Parasites
                PropWrite(theImage, propList)
                pdb.gimp_xcf_save(0, theImage, theDrawable, tgtFile, \
                    tgtFile)
                pdb.gimp_image_delete(theImage)
            else:
                # Check to see if flag for overwrite
                tgtFile = os.path.join(tgtPath, tgtFileDict[srcFile])
                theImage = pdb.gimp_file_load(tgtFile, tgtFile)
                OverwriteFlag = str(theImage.parasite_find('OverwriteXcf'))
                if (OverwriteFlag == 'YES'):
                    # Close xcf, open Jpeg and overwrite with new 
                    pdb.gimp_image_delete(theImage)
                    srcFile = os.path.join(srcPath, srcFile)
                    theImage = pdb.file_jpeg_load(srcFile, srcFile)
                    theDrawable = theImage.active_drawable
                    # Set Flag Properties / Parasites
                    PropWrite(theImage, propList)
                    pdb.gimp_xcf_save(0, theImage, theDrawable, tgtFile, \
                        tgtFile)
                    pdb.gimp_image_delete(theImage)
                else:
                    # Close the xcf leave it alone & move on
                    pdb.gimp_image_delete(theImage)
                    
    # AutoUpdate the images just imported with first step of assigned flow
    pdb.python_fu_autoAutoUpdate(tgtPath)
#
############################################################################
#
register (
    "autoJpgToXcf",         # Name registered in Procedure Browser
    "Convert jpg files to xcf", # Widget title
    "Convert jpg files to xcf", # 
    "Stephen Kiel",         # Author
    "Stephen Kiel",         # Copyright Holder
    "July 2013",            # Date
    "1) Import JPG to XCF (Directory)", # Menu Entry
    "",     # Image Type - No Image Loaded
    [
    ( PF_DIRNAME, "srcPath", "JPG Originals (source) Directory:", jpegDir ),
    ( PF_DIRNAME, "tgtPath", "XCF Working (target) Directory:", xcfDir ),
    ( PF_OPTION, "flowIndex", "Select Workflow", 0, flowList ),
    ],
    [],
    autoJpgToXcf,   # Matches to name of function being defined
    menu = "<Image>/Automation"  # Menu Location
    )   # End register
#
main() 
