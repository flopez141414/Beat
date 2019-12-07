import sys
import r2pipe
import pymongo
import xml.dom.minidom
import xml.etree.ElementTree as ET
import json
import xmltodict
import pprint
import urllib
import os.path
import os

sys.path.append("../DB")
sys.path.append("../windows")
from xmlManager import PluginXmlManager
import errorMessageGenerator

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QWidget, QPushButton, QLabel, QGridLayout, QTextEdit, \
    QLineEdit, QListWidget, QFileDialog, QMessageBox, QComboBox

# Global variables
xml1 = []
xml2 = []
nameH = ""
descH = ""
structH = ""
pdatasetH = ""
listCounter = 0


class PluginManagementTab(QWidget):
    def __init__(self):
        super().__init__()
        
        self.pluginManager = PluginXmlManager()

        global nameH
        global descH
        global structH
        global pdatasetH

        mainlayout = QGridLayout()
        leftLayout = QGridLayout()
        self.rightLayout = QGridLayout()
        mainlayout.addLayout(leftLayout, 1, 0, 6, 1)
        mainlayout.addLayout(self.rightLayout, 1, 1, 6, 5)

        # Left panel
        self.searchBox = QLineEdit()
        searchButton = QPushButton('Search')
        newButton = QPushButton('New')
        self.searchList = QListWidget()
        leftPanelLabel = QLabel('Plugin View')
        leftPanelLabel.setAlignment(Qt.AlignCenter)
        leftPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))

        leftLayout.addWidget(leftPanelLabel, 0, 0, 1, 5)
        leftLayout.addWidget(self.searchBox, 1, 0, 1, 3)
        leftLayout.addWidget(searchButton, 1, 4, 1, 1)
        leftLayout.addWidget(self.searchList, 2, 0, 1, 5)
        leftLayout.addWidget(newButton, 6, 0)

        # Right panel
        self.structureLabel = QLabel('Plugin Structure')
        self.datasetLabel = QLabel('Plugin Predefined Data Set')
        self.pluginNameLabel = QLabel('Plugin Name')
        self.pluginDescLabel = QLabel('Plugin Description')
        self.poisLabel = QLabel('Points of Interest')
        self.rightPanelLabel = QLabel('Detailed Plugin View')
        self.rightPanelLabel.setAlignment(Qt.AlignCenter)
        self.rightPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        self.pluginStructArea = QTextEdit()
        structH = self.pluginStructArea
        self.pluginDataSet = QTextEdit()
        pdatasetH = self.pluginDataSet
        self.pluginName = QTextEdit()
        nameH = self.pluginName
        self.pluginDesc = QTextEdit()
        descH = self.pluginDesc
        self.pointsOI = QListWidget()
        self.browseButton1 = QPushButton('Browse')
        self.browseButton2 = QPushButton('Browse')
        newButton.clicked.connect(self.createNew)
        self.deleteButton = QPushButton('Delete')
        self.saveButton = QPushButton('Save')
        self.updateButton = QPushButton('Update Description')
        button = QPushButton("My Button")
        self.setLayout(mainlayout)
        self.updateButton.clicked.connect(self.editExistingPlugin)
        self.browseButton1.clicked.connect(self.browse1)
        self.browseButton2.clicked.connect(self.browse2)
        self.searchList.doubleClicked.connect(self.selectPlugin)
        self.searchList.doubleClicked.connect(self.disableEditing)
        self.saveButton.clicked.connect(self.saveXml)
        self.deleteButton.clicked.connect(self.deletePluggin)
        searchButton.clicked.connect(self.clickedSearch)

        # retrieve plugin titles and display on list
        pluginList = self.pluginManager.getListOfPlugins()
        for item in pluginList:
            self.searchList.addItem(item)

    def loadRightLayout(self):
        self.clearRightLayout()
        self.rightLayout.addWidget(self.browseButton1, 1, 6)
        self.rightLayout.addWidget(self.browseButton2, 2, 6)
        self.rightLayout.addWidget(self.rightPanelLabel, 0, 0, 1, 10)
        self.rightLayout.addWidget(self.pluginStructArea, 1, 2, 2, 1)
        self.rightLayout.addWidget(self.pluginDataSet, 2, 2, 2, 1)
        self.rightLayout.addWidget(self.pluginName, 3, 2, 2, 1)
        self.rightLayout.addWidget(self.pluginDesc, 6, 2, 2, 1)
        self.rightLayout.addWidget(self.pointsOI, 8, 2, 4, 1)

        self.structureLabel = QLabel('Plugin Structure')
        self.datasetLabel = QLabel('Plugin Predefined Data Set')
        self.pluginNameLabel = QLabel('Plugin Name')
        self.pluginDescLabel = QLabel('Plugin Description')
        self.poisLabel = QLabel('Points of Interest')
        self.rightLayout.addWidget(self.structureLabel, 1, 1, 1, 1)
        self.rightLayout.addWidget(self.datasetLabel, 2, 1, 1, 1)
        self.rightLayout.addWidget(self.pluginNameLabel, 3, 1, 1, 1)
        self.rightLayout.addWidget(self.pluginDescLabel, 6, 1, 1, 1)
        self.rightLayout.addWidget(self.poisLabel, 8, 1, 1, 1)
        self.rightLayout.addWidget(self.saveButton, 15, 7)
        self.rightLayout.addWidget(self.deleteButton, 15, 1)
        self.rightLayout.addWidget(self.updateButton, 15, 7)
        self.updateButton.hide()

    def clearRightLayout(self):
        self.structureLabel.clear()
        self.datasetLabel.clear()
        self.pluginNameLabel.clear()
        self.pluginDescLabel.clear()
        self.poisLabel.clear()

    def clickedSearch(self):
        target = self.searchBox.text()
        pluginList = self.pluginManager.getListOfPlugins()
        self.searchedWord = [s for s in pluginList if target in s]
        self.searchList.clear()
        for items in self.searchedWord:
            self.searchList.addItem(items)
        if self.searchList.count() == 0:
            errorMessageGenerator.showDialog("A plugin with that name does not exist!", "Search Result")

    # aids in opening a file. Tells which button was clicked
    def browse1(self):
        self.openFile(1)

    def browse2(self):
        self.openFile(2)

    def selectPlugin(self):
        # for this mode we will load the right layout
        global plugin

        self.loadRightLayout()
        self.deleteButton.show()
        self.browseButton1.hide()
        self.browseButton2.hide()
        self.saveButton.hide()
        self.updateButton.show()

        plugins = [item.text() for item in self.searchList.selectedItems()]
        pluginName = ' '.join([str(elem) for elem in plugins])

        #get list from db
        plugin = self.pluginManager.getSelectedPlugin(pluginName)

        self.pluginName.setText(plugin['Plugin']['Plugin_name']['#text'])
        self.pluginDesc.setText(plugin['Plugin']['Plugin_Desc']['#text'])
        self.pluginStructArea.setText(plugin['Plugin']['structure_path']['#text'])
        self.pluginDataSet.setText(plugin['Plugin']['predefined_dataset_path']['#text'])
        list_of_poi = self.updatePoiList(plugin)
        self.updatePluginList()
        for item in list_of_poi:
            self.pointsOI.addItem(item)

    # checks which browse button was clicked. Sends address and button number
    myFileName = ""

    def openFile(self, caller):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            if caller == 1:
                if(self.pluginxmlhandler(fileName, 1)): # if xml is good
                    self.pluginStructArea.setText(fileName)
                    poi_list = retrievePoiList()
                    #add pois to gui list
                    for item in poi_list:
                        self.pointsOI.addItem(item)
            elif caller == 2:
                if (self.pluginxmlhandler(fileName, 2)):  # if xml is good
                    self.pluginDataSet.setText(fileName)
                    self.pluginxmlhandler(fileName, 2)

            global myFileName
            myFileName = fileName
            return fileName
        self.updatePluginList()

    # stores xml1 and xml2 from browse buttons
    def pluginxmlhandler(self, filePath, caller):
        global xml1
        global xml2
        if(self.checkXml(filePath,caller)): # if xml is good
            if caller == 1:
                tree = ET.parse(filePath)
                xml1 = tree.getroot()
                return True
            elif caller == 2:
                tree = ET.parse(filePath)
                xml2 = tree.getroot()
                return True
        return False # if xml is bad return false

    #check for errors on xml
    def checkXml(self,filePath,caller):
        #check if its an xml
        is_xml = True
        if caller == 1 or caller == 2:
            try:
                tree = ET.parse(filePath)
                xml = tree.getroot()
            except:
                errorMessageGenerator.showDialog("Please select a valid Plugin xml", 'Plugin error')
                return False
        if(is_xml and caller == 1):
            # check if it has specific branches
            try:
                x = xml.find("./DataInPlugin")
                if x is None:
                    errorMessageGenerator.showDialog("Invalid plugin. Please follow default architecture",
                       'Delete plugin')
                    return False
            except:
                errorMessageGenerator.showDialog("Invalid plugin. Please follow default architecture", 'Delete plugin')
                return False
            try:
                x = xml.find("./Filters")
                if x is None:
                    errorMessageGenerator.showDialog("Invalid plugin. Please follow default architecture",
                                                    'Delete plugin')
                    return False
            except:
                errorMessageGenerator.showDialog("Invalid plugin. Please follow default architecture", 'Delete plugin')
                return False

        return True

    def updatePluginList(self):
        self.searchList.clear()
        pluginList = self.pluginManager.getListOfPlugins()
        for item in pluginList:
            self.searchList.addItem(item)

    def updatePoiList(self,plugin):
        self.pointsOI.clear()

        # get poi list
        list_of_poi = []
        x = plugin['Plugin']['DataInPlugin']
        for y in x:
            list_of_poi.append(y)

        return list_of_poi

    def enableEditing(self):
        self.pluginStructArea.setEnabled(True)
        self.pluginDataSet.setEnabled(True)
        self.pluginName.setEnabled(True)

    def disableEditing(self):
        self.pluginStructArea.setEnabled(False)
        self.pluginDataSet.setEnabled(False)
        self.pluginName.setEnabled(False)

    def createNew(self):
        # load buttons and Layout
        self.loadRightLayout()
        self.deleteButton.hide()
        self.browseButton1.show()
        self.browseButton2.show()
        self.saveButton.show()
        # Clear
        self.pluginName.clear()
        self.pluginDesc.clear()
        self.pluginStructArea.clear()
        self.pluginDataSet.clear()
        self.pluginDataSet.setEnabled(True)
        self.pointsOI.clear()
        self.updatePluginList()
        self.enableEditing()

    def deletePluggin(self):
        global nameH
        toErase = nameH.toPlainText()
        if not toErase:
            errorMessageGenerator.showDialog("Please select a Plugin to delete", 'Delete plugin')

        delete = errorMessageGenerator.confirmDeletion("Are you sure you want to delete this plugin",
                                                       "Delete confirmation")
        if delete:
            self.pluginManager.deleteSelectedPlugin(toErase)
            for item in self.searchList.selectedItems():
                self.searchList.takeItem(self.searchList.row(item))
            self.updatePluginList()

    def saveXml(self):
        global xml1
        global xml2
        global nameH
        global descH
        global structH
        global pdatasetH

        pname = nameH.toPlainText()
        pdesc = descH.toPlainText()
        plugpath = structH.toPlainText()
        data = pdatasetH.toPlainText()

        if self.pluginManager.pluginExists(pname):
            errorMessageGenerator.showDialog("A plugin with that name already exists!", "Project Name Error")
        else:
            if pname != "" and pdesc != "" and plugpath != "" and data != "":
                xml1.attrib['nameOfPlugin']=pname

                b2tf = xml1.find("./Plugin_name")
                b2tf.text = pname
                b2tf = xml1.find("./Plugin_Desc")
                b2tf.text = pdesc
                b2tf = xml1.find("./structure_path")
                b2tf.text = plugpath
                b2tf = xml1.find("./predefined_dataset_path")
                with open(data, 'r') as file:
                    x = file.read().replace('\n', '')

                y=open("../xml/"+pname+"DataSet.xml","w")
                y.write(x)
                y.close()
                b2tf.text = data
                my_dict = ET.tostring(xml1, encoding='utf8').decode('utf8')
                newPlugin=open("../xml/"+pname+"plugin.xml",'w')
                newPlugin.write(my_dict)
                newPlugin.close()
                beatTree='../xml/Beat.xml'
                pluginTree="../xml/"+pname+"plugin.xml"
                system=self.pluginManager.xmlMerger('.//Plugins',beatTree,pluginTree)
                system.write('../xml/Beat.xml')
                self.pluginManager.deleteSystem()
                systemTree=ET.parse('../xml/Beat.xml')
                systemRoot=systemTree.getroot()
                self.pluginManager.uploadSystemOnSave(ET.tostring(systemRoot, encoding='utf8').decode('utf8'))
                self.pluginManager.uploadPlugin(my_dict)
                self.updatePluginList()
                self.disableEditing()
                errorMessageGenerator.showDialog("Please restart the system to finish setting up the new plugin",
                                                "Success")
            if pname == "":
                errorMessageGenerator.showDialog("Enter a Plugin name", "Plugin Name Error")
            if pdesc == "":
                errorMessageGenerator.showDialog("Enter a description for the Plugin", "Plugin File Error")
            if plugpath == "":
                errorMessageGenerator.showDialog("Enter an xml structure file", "Empty plugin structure")
            if data == "":
                errorMessageGenerator.showDialog("Enter a plugin dataset", "Missing dataset")

    def editExistingPlugin(self):
        global plugin
        global descH
        pdesc = descH.toPlainText()
        description = plugin['Plugin']['Plugin_Desc']['#text']
        self.pluginManager.updatePluginDescription(description, pdesc)
        errorMessageGenerator.showDialog("Description updated successfully", "Success")

#Returns a list of strings from XML1 only
def retrievePoiList():
    global xml1
    x = xml1.find("./DataInPlugin")
    list_of_poi = []

    for y in x:
        list_of_poi.append(str(y.attrib['name']))
    return list_of_poi
