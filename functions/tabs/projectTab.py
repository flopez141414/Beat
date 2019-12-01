#!/usr/bin/env python3

import json
import r2pipe
import sys
# XML libraries
import xml.etree.ElementTree as ET
import xmltodict
import pprint
import json
import analysisTab as aT
from typing import Any

sys.path.append("../DB")
sys.path.append("../windows")
import xmlUploader
import errorMessageGnerator
# from xmlUploader import uploadXml

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QWidget, QPushButton, QLabel, QGridLayout, QTextEdit, \
    QLineEdit, QListWidget, QFileDialog, QMessageBox

# Global Variables to Save Project
projectNameHolder = ''
projectDescHolder = ''
projectPathHolder = ''
fileProperties = []
project = []  # type: Any
projectSelected = False
listCounter = 0

class ProjectTab(QWidget):
    def __init__(self):
        super().__init__()

        global projectNameHolder
        global projectDescHolder
        global projectPathHolder

        mainlayout = QGridLayout()
        leftLayout = QGridLayout()
        self.rightLayout = QGridLayout()
        mainlayout.addLayout(leftLayout, 1, 0, 6, 1)
        mainlayout.addLayout(self.rightLayout, 1, 1, 6, 5)

        # Left panel
        searchBox = QLineEdit()
        searchButton = QPushButton('Search')
        newButton = QPushButton('New')
        self.searchList = QListWidget()
        self.leftPanelLabel = QLabel('Project View')
        self.leftPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        self.leftPanelLabel.setAlignment(Qt.AlignCenter)
        leftLayout.addWidget(self.leftPanelLabel, 0, 0, 1, 4)
        leftLayout.addWidget(searchBox, 1, 0, 1, 3)
        leftLayout.addWidget(searchButton, 1, 3, 1, 1)
        leftLayout.addWidget(self.searchList, 2, 0, 1, 4)
        leftLayout.addWidget(newButton, 6, 0)

        # Right panel
        self.rightPanelLabel = QLabel('Detailed Project View')
        self.rightPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        # rightPanelLabel.hide()
        self.rightPanelLabel.setAlignment(Qt.AlignCenter)
        self.projNameArea = QTextEdit()
        projectNameHolder = self.projNameArea  # storing global
        self.projDescriptionArea = QTextEdit()
        projectDescHolder = self.projDescriptionArea
        self.binaryFilePath = QTextEdit()
        projectPathHolder = self.binaryFilePath

        self.binaryFileProp = QTableWidget()
        self.binaryFileProp.horizontalHeader().setStretchLastSection(True)
        self.binaryFileProp.verticalHeader().setVisible(False)
        self.binaryFileProp.horizontalHeader().setVisible(False)
        self.binaryFileProp.setAlternatingRowColors(True)
        self.browseButton = QPushButton('Browse')
        self.LoadButton = QPushButton('Load Current PM')

        self.LoadButton.clicked.connect(self.setCurrentProject)
        self.browseButton.clicked.connect(self.OpenFile)
        self.deleteButton = QPushButton('Delete')
        self.saveButton = QPushButton('Save')
        self.updateButton = QPushButton('Update Description')
        self.saveButton.toggle()
        self.saveButton.clicked.connect(self.saveFile)
        self.updateButton.clicked.connect(self.edit_existing_project)

        newButton.clicked.connect(self.createNew)

        self.deleteButton.clicked.connect(self.deleteProject)
        self.setLayout(mainlayout)

        self.binaryFileProp.setRowCount(13)
        self.binaryFileProp.setColumnCount(2)
        self.binaryFileProp.setItem(0, 0, QTableWidgetItem("OS"))
        self.binaryFileProp.setItem(1, 0, QTableWidgetItem("Binary Type"))
        self.binaryFileProp.setItem(2, 0, QTableWidgetItem("Machine"))
        self.binaryFileProp.setItem(3, 0, QTableWidgetItem("Class"))
        self.binaryFileProp.setItem(4, 0, QTableWidgetItem("Bits"))
        self.binaryFileProp.setItem(5, 0, QTableWidgetItem("Language"))
        self.binaryFileProp.setItem(6, 0, QTableWidgetItem("Canary"))
        self.binaryFileProp.setItem(7, 0, QTableWidgetItem("Crypto"))
        self.binaryFileProp.setItem(8, 0, QTableWidgetItem("Nx"))
        self.binaryFileProp.setItem(9, 0, QTableWidgetItem("Pic"))
        self.binaryFileProp.setItem(10, 0, QTableWidgetItem("Relocs"))
        self.binaryFileProp.setItem(11, 0, QTableWidgetItem("Relro"))
        self.binaryFileProp.setItem(12, 0, QTableWidgetItem("Stripped"))
        self.binaryFileProp.setEnabled(False)
        # self.binaryFileProp.doubleClicked.connect(self.on_click)
        self.searchList.doubleClicked.connect(self.select_project)
        self.searchList.doubleClicked.connect(self.disableEditing)

        projectList = xmlUploader.retrieve_list_of_projects()
        for item in projectList:
            self.searchList.addItem(item)

    def disableEditing(self):
        self.browseButton.setEnabled(False)
        self.projNameArea.setEnabled(False)
        self.binaryFilePath.setEnabled(False)
        self.binaryFileProp.setEnabled(False)

    def staticAnalysis(self, filename):
        global fileProperties
        binPropertiesList = ["os", "bintype", "machine", "class", "bits", "lang", "canary", "crypto", "nx", "pic",
                             "relocs",
                             "relro", "stripped"]
        rlocal = r2pipe.open(filename)
        colNum = 0
        binInfo = rlocal.cmd('iI').splitlines()
        for item in binPropertiesList:
            matchingline = [s for s in binInfo if item in s]
            a = matchingline[0].split()
            fileProperties.append(a[1])
            self.binaryFileProp.setItem(colNum, 1, QTableWidgetItem(a[1]))
            colNum += 1
        self.updateProjectList()

    # global.py
    myFileName = ""

    def OpenFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.binaryFilePath.setText(fileName)
            self.staticAnalysis(fileName)
            #             self.myFilename = fileName
            global myFileName
            myFileName = fileName
            return fileName
        self.updateProjectList()
        return "not found"

    def getFileName(self):
        return self.myFilename

    def saveFile(self):
        global projectNameHolder
        global projectDescHolder
        global projectPathHolder
        global projectSelected
        global project
        # self.turnOff()
        pname = projectNameHolder.toPlainText()
        pdesc = projectDescHolder.toPlainText()
        ppath = projectPathHolder.toPlainText()

        if xmlUploader.project_exists(pname):
            errorMessageGnerator.showDialog("A project with that name already exists!", "Project Name Error")
        else:
            if pname != "" and pdesc != "" and ppath != "":
                # Adding to XMl
                tree = ET.parse('../xml/practiceXml.xml')
                root = tree.getroot()
                b2tf = root.find("./Project_name")
                b2tf.text = pname
                b2tf = root.find("./projectDescription")
                b2tf.text = pdesc
                b2tf = root.find("./BinaryFilePath")
                b2tf.text = ppath
                b2tf = root.find("./StaticDataSet/OS")
                b2tf.text = fileProperties[0]
                b2tf = root.find("./StaticDataSet/BinaryType")
                b2tf.text = fileProperties[1]
                b2tf = root.find("./StaticDataSet/Machine")
                b2tf.text = fileProperties[2]
                b2tf = root.find("./StaticDataSet/Class")
                b2tf.text = fileProperties[3]
                b2tf = root.find("./StaticDataSet/Bits")
                b2tf.text = fileProperties[4]
                b2tf = root.find("./StaticDataSet/Language")
                b2tf.text = fileProperties[5]
                b2tf = root.find("./StaticDataSet/Canary")
                b2tf.text = fileProperties[6]
                b2tf = root.find("./StaticDataSet/Crypto")
                b2tf.text = fileProperties[7]
                b2tf = root.find("./StaticDataSet/NX")
                b2tf.text = fileProperties[8]
                b2tf = root.find("./StaticDataSet/Pic")
                b2tf.text = fileProperties[9]
                b2tf = root.find("./StaticDataSet/Relocs")
                b2tf.text = fileProperties[10]
                b2tf = root.find("./StaticDataSet/Relro")
                b2tf.text = fileProperties[11]
                b2tf = root.find("./StaticDataSet/Stripped")
                b2tf.text = fileProperties[12]
                my_dict = ET.tostring(root, encoding='utf8').decode('utf8')
                xmlUploader.uploadXML(my_dict)
                project = xmlUploader.retrieve_selected_project(pname)
                self.disableEditing()
                self.browseButton.hide()
            elif pname == "":
                errorMessageGnerator.showDialog("Enter a project name", "Project Name Error")
            elif pdesc == "":
                errorMessageGnerator.showDialog("Enter a description for the project", "Project File Error")
            elif ppath == "":
                errorMessageGnerator.showDialog("Cannot create a project without a binary file", "Binary File Error")
            self.updateProjectList()
            self.searchList.setCurrentItem(self.searchList.setCurrentRow(listCounter))
            self.searchList.item(listCounter)
            projectSelected = True
            return pname

    # loads right side
    def loadRightLayout(self):
        self.rightLayout.addWidget(self.rightPanelLabel, 0, 0, 1, 14)
        self.rightLayout.addWidget(self.projNameArea, 1, 2, 10, 10)
        self.rightLayout.addWidget(self.projDescriptionArea, 2, 2, 5, 10)
        self.rightLayout.addWidget(self.binaryFilePath, 4, 2, 10, 10)
        self.rightLayout.addWidget(self.binaryFileProp, 6, 2, 8, 10)
        self.rightLayout.addWidget(self.browseButton, 4, 12)
        self.rightLayout.addWidget(self.LoadButton, 4, 12)
        self.LoadButton.hide()
        self.deleteButton.show()

        self.rightLayout.addWidget(QLabel('Project Name'), 1, 1, 1, 1)
        self.rightLayout.addWidget(QLabel('Project Description'), 2, 1, 1, 1)
        self.rightLayout.addWidget(QLabel('Binary File Path'), 5, 1, 1, 1)
        self.rightLayout.addWidget(QLabel('Binary File Properties'), 6, 1, 1, 1)
        self.rightLayout.addWidget(self.saveButton, 15, 8)
        self.rightLayout.addWidget(self.deleteButton, 15, 1)
        self.rightLayout.addWidget(self.updateButton, 15, 8)
        self.updateButton.hide()


    def select_project(self):
        global project
        # for this mode we will load the right layout
        self.loadRightLayout()
        # disable buttons not needed
        self.saveButton.hide()
        self.browseButton.hide()
        self.LoadButton.show()
        self.updateButton.show()

        project = [item.text() for item in self.searchList.selectedItems()]
        projectName = ' '.join([str(elem) for elem in project])
        project = xmlUploader.retrieve_selected_project(projectName)

        self.projNameArea.setText(project['Project']['Project_name']['#text'])
        self.projDescriptionArea.setText(project['Project']['projectDescription']['#text'])
        self.binaryFilePath.setText(project['Project']['BinaryFilePath']['#text'])
        self.binaryFileProp.setItem(0, 1, QTableWidgetItem(project['Project']['StaticDataSet']['OS']))
        self.binaryFileProp.setItem(1, 1, QTableWidgetItem(project['Project']['StaticDataSet']['BinaryType']))
        self.binaryFileProp.setItem(2, 1, QTableWidgetItem(project['Project']['StaticDataSet']['Machine']))
        self.binaryFileProp.setItem(3, 1, QTableWidgetItem(project['Project']['StaticDataSet']['Class']))
        self.binaryFileProp.setItem(4, 1, QTableWidgetItem(project['Project']['StaticDataSet']['Bits']))
        self.binaryFileProp.setItem(5, 1, QTableWidgetItem(project['Project']['StaticDataSet']['Language']))
        self.binaryFileProp.setItem(6, 1, QTableWidgetItem(project['Project']['StaticDataSet']['Canary']))
        self.binaryFileProp.setItem(7, 1, QTableWidgetItem(project['Project']['StaticDataSet']['Crypto']))
        self.binaryFileProp.setItem(8, 1, QTableWidgetItem(project['Project']['StaticDataSet']['NX']))
        self.binaryFileProp.setItem(9, 1, QTableWidgetItem(project['Project']['StaticDataSet']['Pic']))
        self.binaryFileProp.setItem(10, 1, QTableWidgetItem(project['Project']['StaticDataSet']['Relocs']))
        self.binaryFileProp.setItem(11, 1, QTableWidgetItem(project['Project']['StaticDataSet']['Relro']))
        self.binaryFileProp.setItem(12, 1, QTableWidgetItem(project['Project']['StaticDataSet']['Stripped']))
        self.updateProjectList()
        self.updateButton.show()
        return True

    def createNew(self):
        # enable buttons
        self.saveButton.show()
        self.browseButton.show()
        # disable Button
        self.deleteButton.hide()

        self.loadRightLayout()
        self.projDescriptionArea.clear()
        self.projNameArea.clear()
        self.binaryFilePath.clear()
        self.binaryFileProp.setItem(0, 1, QTableWidgetItem(""))
        self.binaryFileProp.setItem(1, 1, QTableWidgetItem(""))
        self.binaryFileProp.setItem(2, 1, QTableWidgetItem(""))
        self.binaryFileProp.setItem(3, 1, QTableWidgetItem(""))
        self.binaryFileProp.setItem(4, 1, QTableWidgetItem(""))
        self.binaryFileProp.setItem(5, 1, QTableWidgetItem(""))
        self.binaryFileProp.setItem(6, 1, QTableWidgetItem(""))
        self.binaryFileProp.setItem(7, 1, QTableWidgetItem(""))
        self.binaryFileProp.setItem(8, 1, QTableWidgetItem(""))
        self.binaryFileProp.setItem(9, 1, QTableWidgetItem(""))
        self.binaryFileProp.setItem(10, 1, QTableWidgetItem(""))
        self.binaryFileProp.setItem(11, 1, QTableWidgetItem(""))
        self.binaryFileProp.setItem(12, 1, QTableWidgetItem(""))
        self.browseButton.setEnabled(True)
        self.projNameArea.setEnabled(True)
        self.binaryFilePath.setEnabled(True)
        self.binaryFileProp.setEnabled(True)
        self.updateProjectList()

    def deleteProject(self):
        global projectNameHolder
        toErase = projectNameHolder.toPlainText()
        if not toErase:
            errorMessageGnerator.showDialog("Please select a project to delete")

        delete = errorMessageGnerator.confirm_deletion("Are you sure you want to delete this project",
                                                       "Delete confirmation")
        if delete:
            xmlUploader.delete_selected_project(toErase)
            for item in self.searchList.selectedItems():
                self.searchList.takeItem(self.searchList.row(item))
            self.updateProjectList()
            self.createNew()
        else:
            pass

    def turnOn(self):
        self.saveButton.show()

    def turnOff(self):
        self.saveButton.hide()

    def updateProjectList(self):
        global project
        global listCounter
        listCounter = 0
        self.searchList.clear()
        projectList = xmlUploader.retrieve_list_of_projects()
        for item in projectList:
            self.searchList.addItem(item)
            listCounter += 1

    def edit_existing_project(self):
        global project
        global projectDescHolder
        pdesc = projectDescHolder.toPlainText()
        name = project['Project']['Project_name']['#text']
        description = project['Project']['projectDescription']['#text']
        xmlUploader.update_proj_description(description, pdesc)

    '''''
    We want to store the current project name.
    Using the current project name we can retrieve the project XML from the DB
    '''''

    def setCurrentProject(self):
        global projectNameHolder
        toStore = projectNameHolder.toPlainText()
        errorMessageGnerator.infoToast(' Current Project is ' + toStore, 'Current Project')

    '''''
    This is to test merger
        tree = ET.parse('practiceXml.xml')
        xml1 = tree.getroot()
        tree = ET.parse('testplugin.xml')
        xml2 = tree.getroot()
        xmlUploader.xmlmerger('PluginHolder',xml1,xml2)
    '''''
