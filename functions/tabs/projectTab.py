import json

import r2pipe
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QWidget, QPushButton, QLabel, QGridLayout, QTextEdit, \
    QLineEdit, QListWidget, QFileDialog


class ProjectTab(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QGridLayout()
        leftLayout = QGridLayout()
        rightLayout = QGridLayout()
        mainlayout.addLayout(leftLayout, 1, 0, 6, 1)
        mainlayout.addLayout(rightLayout, 1, 1, 6, 5)

        # Left panel
        searchBox = QLineEdit()
        searchButton = QPushButton('Search')
        newButton = QPushButton('New')
        searchList = QListWidget()
        leftPanelLabel = QLabel('Project View')
        leftPanelLabel.setAlignment(Qt.AlignCenter)

        leftLayout.addWidget(leftPanelLabel, 0, 0, 1, 4)
        leftLayout.addWidget(searchBox, 1, 0, 1, 3)
        leftLayout.addWidget(searchButton, 1, 3, 1, 1)
        leftLayout.addWidget(searchList, 2, 0, 1, 4)

        leftLayout.addWidget(newButton, 6, 0)

        # Right panel
        rightPanelLabel = QLabel('Detailed Project View')
        rightPanelLabel.setAlignment(Qt.AlignCenter)
        projNameArea = QTextEdit()
        projDescriptionArea = QTextEdit()
        self.binaryFilePath = QTextEdit()
        self.binaryFileProp = QTableWidget()
        self.binaryFileProp.horizontalHeader().setStretchLastSection(True)
        self.binaryFileProp.verticalHeader().setVisible(False)
        self.binaryFileProp.horizontalHeader().setVisible(False)
        self.binaryFileProp.setAlternatingRowColors(True)
        browseButton = QPushButton('Browse')
        browseButton.clicked.connect(self.OpenFile)

        rightLayout.addWidget(rightPanelLabel, 0, 0, 1, 14)
        rightLayout.addWidget(projNameArea, 1, 2, 10, 10)
        rightLayout.addWidget(projDescriptionArea, 2, 2, 5, 10)
        rightLayout.addWidget(self.binaryFilePath, 4, 2, 10, 10)
        rightLayout.addWidget(self.binaryFileProp, 6, 2, 8, 10)
        rightLayout.addWidget(browseButton, 4, 12)
        
        rightLayout.addWidget(QLabel('Project Name'), 1, 1, 1, 1)
        rightLayout.addWidget(QLabel('Project Description'), 2, 1, 1, 1)
        rightLayout.addWidget(QLabel('Binary File Path'), 6, 1, 1, 1)
        rightLayout.addWidget(QLabel('Binary File Properties'), 5, 1, 1, 1)

        deleteButton = QPushButton('Delete')
        saveButton = QPushButton('Save')
        rightLayout.addWidget(saveButton, 15, 8)
        rightLayout.addWidget(deleteButton, 15, 1)

        button = QPushButton("My Button")
        deleteButton.clicked.connect(self.staticAnalysis)
        self.setLayout(mainlayout)

        self.binaryFileProp.setRowCount(12)
        self.binaryFileProp.setColumnCount(2)
        self.binaryFileProp.setItem(0, 0, QTableWidgetItem("OS"))
        self.binaryFileProp.setItem(1, 0, QTableWidgetItem("Binary Type"))
        self.binaryFileProp.setItem(2, 0, QTableWidgetItem("Machine"))
        self.binaryFileProp.setItem(3, 0, QTableWidgetItem("Class"))
        self.binaryFileProp.setItem(4, 0, QTableWidgetItem("Bits"))
        self.binaryFileProp.setItem(5, 0, QTableWidgetItem("Canary"))
        self.binaryFileProp.setItem(6, 0, QTableWidgetItem("Crypto"))
        self.binaryFileProp.setItem(7, 0, QTableWidgetItem("Nx"))
        self.binaryFileProp.setItem(8, 0, QTableWidgetItem("Pic"))
        self.binaryFileProp.setItem(9, 0, QTableWidgetItem("Relocs"))
        self.binaryFileProp.setItem(10, 0, QTableWidgetItem("Relro"))
        self.binaryFileProp.setItem(11, 0, QTableWidgetItem("Stripped"))
        self.binaryFileProp.doubleClicked.connect(self.on_click)

    def clickEvent(self):
        print("Clicked")

    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.infoTable.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


#     def staticAnalysis(self):
#         rlocal = r2pipe.open("/bin/ping")
#         binInfo = rlocal.cmd('ij')
#         data = json.loads(binInfo)
# #         myvalue = (data['core']['file'])
# #         print(myvalue)
# 
#         myvalue = (data['core']['file'])
#         for key in data:
#             print(data['core']['file'])
#             
#         self.infoTable.setItem(1,1,QTableWidgetItem(myvalue))
# 
# #     def populateBinaryInfo(self):
#     def OpenFile(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.DontUseNativeDialog
#         fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
#                                                   "All Files (*);;Python Files (*.py)", options=options)
#         if fileName:
#             print(fileName)
            
    def staticAnalysis(self, filename):
        binPropertiesList = ["os", "bintype", "machine", "class", "bits", "canary", "crypto", "nx", "pic", "relocs",
                             "relro", "stripped"]

        # filename = self.OpenFile()
        rlocal = r2pipe.open(filename)
        # list1 = rlocal.cmd('iI')
        binInfo = rlocal.cmd('iI').splitlines()
        # print(binInfo)

        colNum = 0
        for item in binPropertiesList:
            matchingline = [s for s in binInfo if item in s]
            print(matchingline)
            a = matchingline[0].split()
            self.binaryFileProp.setItem(colNum, 1, QTableWidgetItem(a[1]))
            colNum += 1

    def OpenFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.binaryFilePath.setText(fileName)
            self.staticAnalysis(fileName)
            return fileName

        return "not found"
