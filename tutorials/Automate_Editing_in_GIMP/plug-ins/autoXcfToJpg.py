#! /usr/bin/env python
#
############################################################################
#
from gimpfu import *
import os
import re
#
if os.name == 'posix':
    Home = os.environ['HOME']
elif os.name == 'nt':
    Home = os.environ['HOMEPATH']
xcfDir = os.path.join(Home, "Pictures")
jpegDir = os.path.join(Home, "Pictures")
#
def autoXcfToJpg(srcPath, tgtPath):
    """Registered function autoXcfToJpg, Converts all of the
    Xcfs in the source directory into jpeg files in a target 
    directory.  Requires two arguments, the paths to the source and
    target directories.  DOES NOT require an image to be open.
    """
    # Run autoUpdate on all of the images in the source directory
    pdb.python_fu_autoAutoUpdate(srcPath)
    
    # Find all of the files in the source and target directories
    allFileList = os.listdir(srcPath)
    existingList = os.listdir(tgtPath)
    srcFileList = []
    tgtFileList = []
    # Index for parasites
    pIndex = 5
    xform = re.compile('\.xcf', re.IGNORECASE)
    # Find all of the xcf files in the list & make jpg file names
    for fname in allFileList:
        fnameLow = fname.lower()
        if fnameLow.count('.xcf') > 0:
            srcFileList.append(fname)
            tgtFileList.append(xform.sub('.jpg',fname))
    tgtFileDict = dict(zip(srcFileList, tgtFileList))
    quality = 0.95
    for srcFile in srcFileList:
        doIt = False
        srcFilePath = os.path.join(srcPath, srcFile)
        theImage = pdb.gimp_file_load(srcFilePath, srcFilePath)
        theDrawable = theImage.active_drawable
        if 'FINISHED' == str(theImage.parasite_find('CurrentStep')):
            if 'YES' == str(theImage.parasite_find('OverwriteJpg')):
                doIt = True
                # Reset the overwrite flag to NO, so it does it once.
                theImage.attach_new_parasite('OverwriteJpg',pIndex, 'NO')
                pdb.gimp_xcf_save(0, theImage, theDrawable, 
                    srcFilePath, srcFilePath)
            if tgtFileDict[srcFile] not in existingList:
                doIt = True
            if doIt:
                tgtFilePath = os.path.join(tgtPath, tgtFileDict[srcFile])
                # All sorts of parameters on jpeg save, no idea what
                #   most of them are.
                theDrawable = pdb.gimp_image_flatten(theImage)
                pdb.file_jpeg_save(theImage, theDrawable, tgtFilePath,
                tgtFilePath, quality, 0, 1, 0, "", 0, 1, 0, 0)
                pdb.gimp_image_delete(theImage)
#
############################################################################
#
register (
    "autoXcfToJpg",         # Name registered in Procedure Browser
    "TITLE", # Widget title
    "TITLE", # 
    "Stephen Kiel",         # Author
    "Stephen Kiel",         # Copyright Holder
    "July 2013",            # Date
    "3) Export XCF to JPG (Directory)", # Menu Entry
    "",     # Image Type
    [
    ( PF_DIRNAME, "srcPath", "XCF Edited Images (source) Directory:", xcfDir ),
    ( PF_DIRNAME, "tgtPath", "JPG Finished (target) Directory:", jpegDir ),
    ],
    [],
    autoXcfToJpg,   # Matches to name of function being defined
    menu = "<Image>/Automation"  # Menu Location
    )   # End register

main() 
