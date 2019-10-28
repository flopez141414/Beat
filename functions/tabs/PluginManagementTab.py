import sys
import r2pipe
import pymongo
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QFileDialog, QSplitter, \
    QHBoxLayout, QFrame, QGridLayout, QTabWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QListWidget, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore, QtGui

pluginNameN = ''
pluginDescH = ''
poiH = ''

class PluginManagementTab(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QGridLayout()
        leftLayout = QGridLayout()
        rightLayout = QGridLayout()
        mainlayout.addLayout(leftLayout, 1, 0, 6, 1)
        mainlayout.addLayout(rightLayout, 1, 1, 6, 1)

        # Left panel
        searchBox = QLineEdit()
        searchButton = QPushButton('Search')
        newButton = QPushButton('New')
        searchList = QListWidget()
        leftPanelLabel = QLabel('Plugin View')
        leftPanelLabel.setAlignment(Qt.AlignCenter)
#         leftPanelLabel.setStyleSheet("background-color: rgba(173,216,230 ,1 )")
        leftPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))

        leftLayout.addWidget(leftPanelLabel, 0, 0, 1, 5)
        leftLayout.addWidget(searchBox, 1, 0, 1, 3)
        leftLayout.addWidget(searchButton, 1, 4, 1, 1)
        leftLayout.addWidget(searchList, 2, 0, 1, 5)
        leftLayout.addWidget(newButton, 6, 0)

        # Right panel
        rightPanelLabel = QLabel('Detailed Plugin View')
        rightPanelLabel.setAlignment(Qt.AlignCenter)
#         rightPanelLabel.setStyleSheet("background-color: rgba(173,216,230 ,1 )")
        rightPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        self.pluginStructArea = QTextEdit()
        self.pluginDataSet = QTextEdit()
        self.pluginName = QTextEdit()
        pluginDesc = QTextEdit()
        self.pointsOI = QTextEdit()
        defaultOutDropdown = QComboBox()

        browseButton1 = QPushButton('Browse')
        browseButton1.clicked.connect(self.OpenPluginFile)

        browseButton2 = QPushButton('Browse')
        browseButton2.clicked.connect(self.OpenPluginFile)

        rightLayout.addWidget(browseButton1, 1, 6)
        rightLayout.addWidget(browseButton2, 2, 6)

        rightLayout.addWidget(rightPanelLabel, 0, 0, 1, 10)
        rightLayout.addWidget(self.pluginStructArea, 1, 2, 2, 1)
        rightLayout.addWidget(self.pluginDataSet, 2, 2, 2, 1)
        rightLayout.addWidget(self.pluginName, 3, 2, 2, 1)
        rightLayout.addWidget(pluginDesc, 4, 2, 2, 1)
        rightLayout.addWidget(defaultOutDropdown, 5, 2, 1, 1)
        rightLayout.addWidget(self.pointsOI, 6, 2, 4, 1)

        rightLayout.addWidget(QLabel('Plugin Structure'), 1, 1, 1, 1)
        rightLayout.addWidget(QLabel('Plugin Predefined Data Set'), 2, 1, 1, 1)
        rightLayout.addWidget(QLabel('Plugin Name'), 3, 1, 1, 1)
        rightLayout.addWidget(QLabel('Plugin Description'), 4, 1, 1, 1)
        rightLayout.addWidget(QLabel('Default Output Field'), 5, 1, 1, 1)
        rightLayout.addWidget(QLabel('Points of Interest'), 6, 1, 1, 1)

        deleteButton = QPushButton('Delete')
        saveButton = QPushButton('Save')
        rightLayout.addWidget(saveButton, 15, 7)
        rightLayout.addWidget(deleteButton, 15, 1)

        button = QPushButton("My Button")
        button.clicked.connect(self.clickEvent)
        self.setLayout(mainlayout)

    def clickEvent(self):
        print("Clicked")


    def OpenPluginFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "All Files (*);;Python Files (*.xml)", options=options)
        if fileName:
            print('test')
            self.pluginStructArea.setText('Hello!')
            self.pluginDataSet.setText('world')
            self.pluginName.setText('asaa')
            self.pointsOI.setText('list of pois go heres')
            #global myFileName
            #myFileName = fileName

            #return fileName

        #return "not found"