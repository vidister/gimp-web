#   File = autoBase.py
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
import xml.etree.ElementTree as ET
import os
import re
import sys
#from gimpfu import *

class BaseXmlReader(object):
    """\tReads data for xml files.  Used for automating the editing process
    with Gimp.  Has methods to obtain and format the data for 'Commander'
    and 'AutoUpdate'.  The public functions are: CommanderMacros, 
    CommanderExtract, FlowNames, FlowExtract, FlowTree, PropertyNames, and
    PropertyTree.  Creating an instance does not require any arguments or
    attributes to be set.
    """
    def __init__(self):
        self._srcPath = ''
        self.cmdrPath = 'commander/combinedCommander.xml'
        self.propPath = 'property/flagProperties.xml'
        self.flowPath = 'flow/combinedFlow.xml'

    def __BasePath(self):
        self.basePath = os.path.realpath(__file__)
        (self.basePath, tail) = os.path.split(self.basePath)
        (self.basePath, tail) = os.path.split(self.basePath)
        self.basePath = os.path.join(self.basePath, 'myXml')
        return self.basePath

    def __XmlPath(self):
        self.basePath = self.__BasePath()
        self.xmlPath = os.path.join(self.basePath, self.srcPath)
        return self.xmlPath

    def __Reader(self):
        #
        self.getpath = self.__XmlPath()
        self.tree = ET.parse(self.getpath)
        return self.tree

    def __Lev1List(self):
        self.lev1List = []
        self.L1tree = self.__Reader()
        self.L1root = self.L1tree.getroot()
        for self.l1 in self.L1root:
            self.lev1List.append(self.l1.text)
        return self.lev1List
        
    def __Lev2List(self):
        self.lev2List = []
        self.L2tree = self.__Reader()
        self.L2root = self.L2tree.getroot()
        for self.l1a in self.L2root:
            for self.l2 in self.l1a:
                self.lev2List.append(self.l2.text)
        return self.lev2List

    def CommanderExtract(self, MacName):
        """\tA Commander specific method which takes a Commander Macro
        name as an argument and returns the list of commands associated
        with that Macro.  This list is used by Commander and passed to
        the Python 'exec' function and executed.
        """
        self.srcPath = self.cmdrPath
        self.commanderList = []
        cmdrTree = self.__Reader()
        cmdrRoot = cmdrTree.getroot()
        for cName in cmdrRoot:
            if cName.text == MacName:
                for command in cName:
                    if command.tag == 'command':
                        self.commanderList.append(command.text)
        return self.commanderList

    def CommanderMacros(self):
        """\tA Commander specific method which takes no arguments and returns
        a list of the Commander Macro names represented in the xml.
        """
        self.srcPath = self.cmdrPath
        self.macros = self.__Lev1List()
        self.macros.sort()
        return self.macros

    def PropertyNames(self):
        """\tA Property specific method which takes no arguments and returns
        a list of the Property Names represented in the xml.
        """
        self.srcPath = self.propPath
        self.pNames = self.__Lev2List()
        return self.pNames

    def PropertyTree(self):        
        """\tA Property specific method which takes no arguments and returns a
        tree that can be processed using the python 'ElementTree'.  All of the
        property information in the xml will be represented in this tree.
        """
        self.srcPath = self.propPath
        self.pTree = self.__Reader()
        return self.pTree

    def PropertyOption(self,PropMatch):
        """\tA Property specific method which takes a property name as an 
        argument and returns the list of options for that property.  Can be
        used to populate a list for a menu in the user interface.
        """
        self.optionList = []
        self.srcPath = self.propPath
        pTree = self.__Reader()
        proproot = pTree.getroot()
        for top in proproot:
            for propName in top:
                if propName.text == PropMatch:
                    for option in propName:
                        if option.tag == 'option':
                            self.optionList.append(option.text)
        return self.optionList

    def PropertyDefaults(self):
        self.defaultList = []
        self.srcPath = self.propPath
        pTree = self.__Reader()
        proproot = pTree.getroot()
        for top in proproot:
            for propName in top:
                pName =  propName.text
                for default in propName:
                    if default.tag == 'default':
                        nameVal = (pName, default.text)
                        self.defaultList.append(nameVal)
        return self.defaultList                      

    def FlowNames (self):
        """\tA Flow specific method which takes no arguments and returns a list
        of the Work Flows defined in the xml.
        """
        self.srcPath = self.flowPath
        self.fNames = self.__Lev1List()
        return self.fNames

    def FlowTree (self):
        """\tA Flow specific method which takes no arguments and returns a tree
        that can be processed using the python 'ElementTree'.  All of the flow
        information in the xml will be represented in this tree.
        """
        self.srcPath = self.flowPath
        self.fTree = self.__Reader()
        return self.fTree

    def FlowExtract (self, flowMatch, stepMatch):
        """\tA Flow specific method which takes two arguments, a {flow name}, and
        a {step name}.  The method returns a list and the name of the 'next step'.
        The list is the commands associated with the given flow and step arguments.
        This method is used by the AutoUpdate function.
        """
        self.srcPath = self.flowPath
        self.NewNextStep = "FINISHED"
        getNextStep = False
        self.commandList = []
        flowtree = self.__Reader()
        flowroot = flowtree.getroot()
        for flowname in flowroot:
            if flowname.text == flowMatch:
                for stepName in flowname:
                    if stepName.text == stepMatch:
                        for command in stepName:
                            if command.tag == 'command':
                                self.commandList.append(command.text)
                    if getNextStep:
                        self.NewNextStep = stepName.text
                        getNextStep = False
                    if stepName.text == stepMatch:
                        getNextStep = True
        return self.commandList, self.NewNextStep

    def FlowFirstNameDict(self):
        self.firstNameDict = {}
        self.srcPath = self.flowPath
        flowtree = self.__Reader()
        flowroot = flowtree.getroot()
        for flowname in flowroot:
            self.firstNameDict[flowname.text] = flowname[0].text
        return self.firstNameDict



#
############################################################################
#
class XmlGenerator(object):
    """\tXmlGenerator has three methods which write xml to a file.  The three 
    methods are: 
    ** GenCommanderXml
    ** GenFlowXml
    ** GenPropertyXml.
    The methods set the following internal variables that are used to specify 
    the xml tree being written to disk and then calls internal method gentree.
    * srcType - one of 'cmdr', 'flow', or, 'prop' used to derive path name
    * fglob - the common extension for pseudo code files '.def'
    * rootList - list of tags for root level, should be one element
    * lev1List - list of tags for the 1st level of hierarchy under root
    * lev2List - list of tags for the 2nd level of hierarchy under root.
    After the variables have been set the 'gentree' internal function writes a
      tree that is written as an xml file (by calling function).  gentree 
      uses internal sub - functions 'parsetag' and 'psuedo2Xml'.
    """
    
    ################# Set up Attributes
    
    def __init__(self):
        #self._srcDirectory = ''
        self._fglob = ''
        self._rootList = []
        self._lev1List = []
        self._lev2List = []
        self._srcType = ''

    def setPath(self):
        derivedPath = os.path.realpath(__file__)
        (derivedPath, tail) = os.path.split(derivedPath)
        (derivedPath, tail) = os.path.split(derivedPath)
        derivedPath = os.path.join(derivedPath, 'myXml')
        if self.srcType == 'flow':
            xmlPath = os.path.join(derivedPath, 'flow', 
                'combinedFlow.xml')
        elif self.srcType == 'prop':
            xmlPath = os.path.join(derivedPath, 'property', 
                'flagProperties.xml')
        elif self.srcType == 'cmdr':
            xmlPath = os.path.join(derivedPath, 'commander', 
                'combinedCommander.xml')
        return xmlPath

    def parsetag(self, line):
        """\tSplit the input string into 'tags' and 'tails'.  The tags 
        will be the xml identifiers or enclosures, and the tails will be 
        the associated text.  If a line is blank or starts with a '#' 
        it will be ignored and skipped.
        """
        tag = ''
        tail = ''
        level = ''
        # Ignore blank Lines and commented out
        if len(line) > 0 and line[0] != '#':
            # Find tag & tail, for tag to lower case
            tag = line[0:line.find(">")]
            tag = tag.lower()
            tail = line[line.find(">")+1:]
            # Tag hierarchy level in tree
            if tag in self.rootList:
                level = 'root'
            elif tag in self.lev1List:
                level = 'level1'
            elif tag in self.lev2List:
                level = 'level2'
            else:
                level = 'none'
        return tag, tail, level
    #
    def psuedo2Xml(self, inputPseudo):
        """\tRead the passed pseudo code file and parse it into an xml
        tree.  Pass the newly created tree back to the calling function.
        The generated tree will have a root with two levels of sub 
        hierarchy.  Uses sub - function parsetag to break the individual
        lines into tags and the associated text.
        """
        infile = open(inputPseudo)
        # convert '>>>' alias for 'command>'
        xform = re.compile('^>>>\s*')
        for line in infile:
            line = line.strip()
            line = xform.sub('command>', line)
            (tag, tail, level) = self.parsetag(line)
            # build line into tree.
            # Add a little formatting - so it isn't all one line
            if level == 'root':
                root = ET.Element(tag)
                root.text = tail
                root.tail = "\n  "
            elif level == 'level1':
                elLev1 = ET.SubElement(root, tag)
                elLev1.text = tail
                elLev1.tail = "\n    "
            elif level == 'level2':
                elLev2 = ET.SubElement(elLev1, tag)
                elLev2.text = tail
                elLev2.tail = "\n      "
        tree = ET.ElementTree(root)
        return tree
    #
    def gentree(self):
        """\tRead all of the *.def files in the named xml directory.  For
        each flow *.def psuedo code file, read it into a tree.  Append
        the flow xml trees together into a combined tree.  Uses sub - 
        function psuedo2Xml to covert individual *.def into xml.
        """
        filePath = self.setPath()
        (fileDir, fileName) = os.path.split(filePath)
        root = ET.Element('combined')
        root.text = 'Definition' + "\n  "
        try:
            fileList = os.listdir(fileDir)
        except OSError:
            print "******** could not find " + fileDir
        for fname in fileList:
            if fname.count('.def') > 0:
                fname = os.path.join(fileDir, fname)
                subTree = self.psuedo2Xml(fname)
                subNode = subTree.getroot()
                root.append(subNode)
        tree = ET.ElementTree(root)
        tree.write(filePath)
        #return tree

    def GenCommanderXml(self):
        """\tA method to write the Commander xml to a file.  It takes no
        arguments and does not return anything.  It sets the variables for
        the Commander xml write and then calls the 'gentree' method.
        """
        self.srcType = 'cmdr'
        self.fglob = '.def'
        self.rootList = ['commander']
        self.lev1List = ['command', 'comment']
        self.lev2List = []
        self.gentree()

    def GenFlowXml(self):
        """\tA method to write the Flow xml to a file.  It takes no
        arguments and does not return anything.  It sets the variables for
        the Flow xml write and then calls the 'gentree' method.
        """
        self.srcType = 'flow'
        self.fglob = '.def'
        self.rootList = ['flow']
        self.lev1List = ['step']
        self.lev2List = ['command', 'comment']
        self.gentree()

    def GenPropertyXml(self):
        """\tA method to write the Property xml to a file.  It takes no
        arguments and does not return anything.  It sets the variables for
        the Property xml write and then calls the 'gentree' method.
        """
        self.srcType = 'prop'
        self.fglob = '.def'
        self.rootList = ['flags']
        self.lev1List = ['property']
        self.lev2List = ['default', 'option', 'comment']
        self.gentree()


class TestBench(object):
    """Exercises the classes XmlGenerator and BaseXmlReader
    """

    def __init__(self):
        #self._srcDirectory = ''
        pass

    def ListFunctions(self):
        print "XmlGenerator Methods\n"
        print "   GenCommanderXml"
        print "   GenFlowXml"
        print "   GenPropertyXml"
        print "\nBaseXmlReader Methods\n"
        print "   CommanderExtract"
        print "   CommanderMacros\n"
        print "   FlowExtract"
        print "   FlowFirstNameDict"
        print "   FlowNames"
        print "   FlowTree\n"
        print "   PropertyDefaults"
        print "   PropertyNames"
        print "   PropertyOption"
        print "\nTestBench Methods\n"
        print "   ListFunctions"
        print "   PrintClassDocs"
        print "   "

    def PrintClassDocs(self):
        print "*** XmlGenerator"
        print XmlGenerator.__doc__
        print "\n*** BaseXmlReader"
        print BaseXmlReader.__doc__
        print "\n*** TestBench"
        print TestBench.__doc__

    def TestXmlGen(self):
        print "*** Testing the XmlGenerator Class"
        print "\nWriting commander xml file"
        xmlObj = XmlGenerator()
        xmlObj.GenCommanderXml()
        print "\nWriting flow xml file"
        xmlObj.GenFlowXml()
        print "\nWriting property xml file"
        print "\nDone."
        xmlObj.GenPropertyXml()
        print "Check the time / date stamp of the xml files in the:"
        print "  .../myXml/flow"
        print "  .../myXml/commander"
        print "  .../myXml/property"
        print "directories.  myXml is under the {home}/.gimp-x.x directory"
        print "\nCheck the correctness of the content by exercising the"
        print "TestXmlRead method which reads the xml and prints the"
        print "output of each method."


    def TestXmlRead(self):
        print "*** Testing the BaseXmlReader Class"
        print ""
        xmlObj = BaseXmlReader()
        print "\n** Commander BaseXmlReader method CommanderMacros() **:\n%s"\
            % xmlObj.CommanderMacros()
        print "\n** Commander BaseXmlReader method CommanderExtract() **:\n%s"\
            % xmlObj.CommanderExtract('Centered Grid')
        print""
        #xmlObj = BaseXmlReader()
        print "\n** Property BaseXmlReader Property Names **: %s" % xmlObj.PropertyNames()
        print "\n** Property BaseXmlReader method Tree **" 
        newtree = xmlObj.PropertyTree()
        newroot = newtree.getroot()
        for L1 in newroot:
            for L2 in L1:
                print L2.text
                for L3 in L2:
                    if L3.tag == 'default':
                        print "   default value =>  " + L3.text
                    if L3.tag == 'option':
                        print "   option value  ->  " + L3.text
        print "\nProperty Specific BaseXmlReader Property Options: %s" % xmlObj.PropertyOption('EnhanceContrastLevel')
        print "\nProperty Specific BaseXmlReadr Property Default (tuples): %s" % xmlObj.PropertyDefaults()
        print
        xmlObj = BaseXmlReader()
        print "\n** Flow Specific BaseXmlReader Flow Names**: %s" % xmlObj.FlowNames()
        print "\n** Flow Specific BaseXmlReader Flow Tree **"
        flowTree = xmlObj.FlowTree()
        flowRoot = flowTree.getroot()
        for flowName in flowRoot:
            print flowName.text
            for flowStep in flowName:
                print '  Step -> ' + flowStep.text
                for Command in flowStep:
                    if Command.tag == 'command':
                        print "    Command => " + Command.text
                    if Command.tag == 'comment':
                        print "    Comment -- " + Command.text
        print
        cmdList, nStep = xmlObj.FlowExtract('Standard', 'DynamicRange')
        print "\n** Flow Specific BaseXmlReader FlowExtract Next Name: %s" % nStep
        print "\n** Flow Specific BaseXmlReader FlowExtract Command List: %s" % cmdList
        print "\n** Flow Specific BaseXmlReader Flow First Name Dict: %s" % xmlObj.FlowFirstNameDict()        


