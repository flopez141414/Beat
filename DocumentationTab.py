import sys
import r2pipe
import pymongo
import os

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QFileDialog, QSplitter, \
    QHBoxLayout, QFrame, QGridLayout, QTabWidget, QVBoxLayout, QHBoxLayout, QListWidget, QComboBox, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore, QtGui


class DocumentationTab(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QGridLayout()
        leftLayout = QGridLayout()
        rightLayout = QGridLayout()

        mainlayout.addLayout(leftLayout, 1, 0, 6, 1)
        mainlayout.addLayout(rightLayout, 1, 1, 6, 8)

        # Left panel
        searchBox = QLineEdit()
        searchButton = QPushButton('Search')

        self.searchDocList = QListWidget()
        #docList = QTextEdit()
        leftPanelLabel = QLabel('Document View')
        leftPanelLabel.setAlignment(Qt.AlignCenter)
#         leftPanelLabel.setStyleSheet("background-color: rgba(173,216,230 ,1 )")

        leftPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        leftLayout.addWidget(leftPanelLabel, 0, 0, 1, 5)
        leftLayout.addWidget(searchButton, 1, 4, 1, 1)
        leftLayout.addWidget(searchBox, 1, 0, 1, 3)
        leftLayout.addWidget(self.searchDocList, 2, 0, 1, 5)

        # Right panel
        rightPanelLabel = QLabel('Detail Document View')
        rightPanelLabel.setAlignment(Qt.AlignCenter)
#         rightPanelLabel.setStyleSheet("background-color: rgba(173,216,230 ,1 )")
        rightPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        self.docContentArea = QTextEdit()
        rightLayout.addWidget(rightPanelLabel, 0, 0, 1, 10)
        rightLayout.addWidget(self.docContentArea, 1, 1, 10, 8)

        self.searchDocList.doubleClicked.connect(self.readFile)

        self.setLayout(mainlayout)

        #display titles for docs
        docTitles = ["About BEAT" , "Add Plugin", "Delete Plugin", "Delete Project", "Make Project", "Set MongoDB"]
        for item in docTitles:
            self.searchDocList.addItem(item)

    # def clickEvent(self):
    #     print("Clicked")

    def readFile(self):
        current = ''
        for currentQTableWidgetItem in self.searchDocList.selectedItems():
            current = currentQTableWidgetItem.text()
        print(current)
        if current == 'About BEAT':
            self.fileOpener('About.txt')
        elif current == 'Add Plugin':
            self.fileOpener('AddPlugin.txt')
        elif current == 'Delete Plugin':
            self.fileOpener('DelPlugin.txt')
        elif current == 'Delete Project':
            self.fileOpener('DelProject.txt')
        elif current == 'Make Project':
            self.fileOpener('MkProject.txt')
        elif current == 'Set MongoDB':
            self.fileOpener('SetMongo.txt')

    def fileOpener(self,File_object):
        cwd = os.getcwd()
        self.docContentArea.setText("test")
        print(cwd)
        try:
            file = open(File_object, "r")
            doc = file.read()
            self.docContentArea.setText(doc)
            self.docContentArea.setEnabled(False)
            print(file.read())
        except:
             print(File_object, " Not Found.")