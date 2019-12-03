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
        global project
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
        self.leftPanelLabel = QLabel('Project View')
        self.leftPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        self.leftPanelLabel.setAlignment(Qt.AlignCenter)
        leftLayout.addWidget(self.leftPanelLabel, 0, 0, 1, 4)
        leftLayout.addWidget(self.searchBox, 1, 0, 1, 3)
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
        self.projectNameLabel = QLabel('Project Name')
        self.projectdescLabel = QLabel('Project Description')
        self.binFileLabel = QLabel('Binary File Path')
        self.binFilePropLabel = QLabel('Binary File Properties')

        self.binaryFileProp = QTableWidget()
        self.binaryFileProp.horizontalHeader().setStretchLastSection(True)
        self.binaryFileProp.verticalHeader().setVisible(False)
        self.binaryFileProp.horizontalHeader().setVisible(False)
        self.binaryFileProp.setAlternatingRowColors(True)
        self.browseButton = QPushButton('Browse')
        self.browseButton.clicked.connect(self.OpenFile)
        self.deleteButton = QPushButton('Delete')
        self.saveButton = QPushButton('Save')
        self.updateButton = QPushButton('Update Description')
        self.saveButton.toggle()
        self.saveButton.clicked.connect(self.saveFile)
        self.updateButton.clicked.connect(self.edit_existing_project)

        searchButton.clicked.connect(self.clickedSearch)
        newButton.clicked.connect(self.createNew)

        self.deleteButton.clicked.connect(self.deleteProject)
        self.setLayout(mainlayout)

        self.binaryFileProp.setRowCount(13)
        self.binaryFileProp.setColumnCount(2)
        self.fillBinaryFileProperties()
        self.binaryFileProp.setEnabled(False)
        self.searchList.doubleClicked.connect(self.select_project)
        self.searchList.doubleClicked.connect(self.disableEditing)

        projectList = xmlUploader.retrieve_list_of_projects()
        for item in projectList:
            self.searchList.addItem(item)

    def fillBinaryFileProperties(self):
        tree = ET.parse('../xml/Project.xml')
        project = tree.getroot()
        projectProperties = project.find('StaticDataSet')
        c = 0
        for item in projectProperties.iter():
            if item.tag != 'StaticDataSet':
                self.binaryFileProp.setItem(c, 0, QTableWidgetItem(item.tag))
                c += 1

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
            global myFileName
            myFileName = fileName
            return fileName
        self.updateProjectList()

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
                tree = ET.parse('../xml/Project.xml')
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
                errorMessageGnerator.showDialog("Project created successfully", "Success")
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
        return pname

    def clickedSearch(self):
        target = self.searchBox.text()
        projectList = xmlUploader.retrieve_list_of_projects()
        self.searchedWord = [s for s in projectList if target in s]
        self.searchList.clear()
        for items in self.searchedWord:
            self.searchList.addItem(items)
        if self.searchList.count() == 0:
            errorMessageGnerator.showDialog("A project with that name does not exist!", "Search Result")

    # loads right side
    def loadRightLayout(self):
        self.clearRightlayout()

        self.rightPanelLabel = QLabel('Detailed Project View')
        self.rightPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        self.rightPanelLabel.setAlignment(Qt.AlignCenter)
        self.rightLayout.addWidget(self.rightPanelLabel, 0, 0, 1, 14)
        self.rightLayout.addWidget(self.projNameArea, 1, 2, 10, 10)
        self.rightLayout.addWidget(self.projDescriptionArea, 2, 2, 5, 10)
        self.rightLayout.addWidget(self.binaryFilePath, 4, 2, 10, 10)
        self.rightLayout.addWidget(self.binaryFileProp, 6, 2, 8, 10)
        self.rightLayout.addWidget(self.browseButton, 4, 12)
        self.deleteButton.show()

        self.projectNameLabel = QLabel('Project Name')
        self.projectdescLabel = QLabel('Project Description')
        self.binFileLabel = QLabel('Binary File Path')
        self.binFilePropLabel = QLabel('Binary File Properties')
        self.rightLayout.addWidget(self.projectNameLabel, 1, 1, 1, 1)
        self.rightLayout.addWidget(self.projectdescLabel, 2, 1, 1, 1)
        self.rightLayout.addWidget(self.binFileLabel, 4, 1, 1, 1)
        self.rightLayout.addWidget(self.binFilePropLabel, 6, 1, 1, 1)
        self.rightLayout.addWidget(self.saveButton, 15, 8)
        self.rightLayout.addWidget(self.deleteButton, 15, 1)
        self.rightLayout.addWidget(self.updateButton, 15, 8)
        self.updateButton.hide()

    def clearRightlayout(self):
        self.rightPanelLabel.clear()
        self.projectNameLabel.clear()
        self.projectdescLabel.clear()
        self.binFileLabel.clear()
        self.binFilePropLabel.clear()

    def select_project(self):
        global project
        # for this mode we will load the right layout
        self.loadRightLayout()
        # disable buttons not needed
        self.saveButton.hide()
        self.browseButton.hide()
        self.updateButton.show()
        self.searchBox.setText("")

        project = [item.text() for item in self.searchList.selectedItems()]
        projectName = ' '.join([str(elem) for elem in project])
        project = xmlUploader.retrieve_selected_project(projectName)
        self.projNameArea.setText(project['Project']['Project_name']['#text'])
        self.projDescriptionArea.setText(project['Project']['projectDescription']['#text'])
        self.binaryFilePath.setText(project['Project']['BinaryFilePath']['#text'])
        c = 0
        for item in project['Project']['StaticDataSet']:
            self.binaryFileProp.setItem(c, 1, QTableWidgetItem(project['Project']['StaticDataSet'][item]))
            c += 1
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
        i = 0
        for i in range(13):
            self.binaryFileProp.setItem(i, 1, QTableWidgetItem(""))
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

    def edit_existing_project(self):
        global project
        global projectDescHolder
        pdesc = projectDescHolder.toPlainText()
        name = project['Project']['Project_name']['#text']
        description = project['Project']['projectDescription']['#text']
        xmlUploader.update_proj_description(description, pdesc)

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
        description = project['Project']['projectDescription']['#text']
        xmlUploader.update_proj_description(description, pdesc)
        errorMessageGnerator.showDialog("Description updated successfully", "Success")
