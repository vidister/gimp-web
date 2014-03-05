#! /usr/bin/env python
#
#   File = autoWriteXml.py
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
from autoBase import *
#
############################################################################
#
def autoWriteXml():
    """Registered function autoWriteFlowXml. Uses the XmlGenerator class
    in the autoBase module to read the Psuedocode *.def files and write
    the information into xml files.  The methods GenCommanderXml,
    GenFlowXml, and GenPropertyXml read Pseudocode and write xml in the
    'commander', 'flow', and 'properties' subdirectories of the myXml
    directory.
    Additional information from within a Python shell:
      from autoBase import *
      print XmlGenerator.__doc__
      print dir(XmlGenerator)
      print XmlGenerator.GenCommanderXml.__doc__
      print XmlGenerator.GenFlowXml.__doc__
      print XmlGenerator.GenPropertyXml.__doc__
    The xml written with this command is referenced by the BaseXmlReader
    class which is also in the autoBase module and furnishes information
    to the AutoUpdate and Commander plug-in scripts.
    """
    xmlWriteObj = XmlGenerator()
    xmlWriteObj.GenCommanderXml()
    xmlWriteObj.GenFlowXml()
    xmlWriteObj.GenPropertyXml()
    pdb.gimp_message("Wrote / Updated xml for:\
        \n\tCommander\n\tProperties\n\tFlow")
#
############################################################################
#
register (
    "autoWriteXml",         # Name registered in Procedure Browser
    "Write Pseudocode (Flow, Property, & Commander) to xml", # Widget title
    "Write Pseudocode (Flow, Property, & commander) to xml", # 
    "Stephen Kiel",         # Author
    "Stephen Kiel",         # Copyright Holder
    "Aug 2013",             # Date
    "Pseudocode to XML", # Menu Entry
    "",     # Image Type
    [
    #( PF_FILENAME, "inputPseudo", "Psuedocode Text File", flowXmlDirPath ),
    ],
    [],
    autoWriteXml,   # Matches to name of function being defined
    menu = "<Image>/Automation/Utilities"  # Menu Location
    )   # End register
#
main()
