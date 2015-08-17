#! /usr/bin/env python
#
#   File = autoCommander.py
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
import xml.etree.ElementTree as ET
import os
import re
import sys
from autoBase import *
#
############################################################################
#
cmdrReadObj = BaseXmlReader()
cmdList = cmdrReadObj.CommanderMacros()
#
############################################################################
#
def autoCommander(theImage, cmdListIndex):
    """Registered function autoCommander.  Prompt the user to select a 
    macro sequence by name.  Use the name to locate the set of commands
    associated with that macro in the commander tree.  Form a list from the
    command set, ignoring comments, and run that list of commands on the
    open image with the python 'exec' command.
    """
    # Get the selected command name from the list
    commanderName = cmdList[cmdListIndex]
    commandList = cmdrReadObj.CommanderExtract(commanderName)
    # Run the commands in newly created commandList through 'exec'
    # Set up and 'undo' group
    pdb.gimp_image_undo_group_start(theImage)
    for Cmd in commandList:
        exec(Cmd)
    pdb.gimp_image_undo_group_end(theImage)     
#
############################################################################
#
register (
    "autoCommander",         # Name registered in Procedure Browser
    "Commander", # Widget title
    "Commander", # 
    "Stephen Kiel",         # Author
    "Stephen Kiel",         # Copyright Holder
    "August 2013",          # Date
    "Commander - Command Sequencer", # Menu Entry
    "*",     # Image Type, an open image
    [
    ( PF_IMAGE, "theImage", "Input Image", None ),
    ( PF_OPTION, "cmdSet", "Select a command", 0, cmdList ),
    ],
    [],
    autoCommander,   # Matches to name of function being defined
    menu = "<Image>/Automation"  # Menu Location
    )   # End register

main()
