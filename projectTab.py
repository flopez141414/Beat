import sys
import r2pipe
import pymongo
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QFileDialog, QSplitter, QHBoxLayout, QFrame, QGridLayout, QTabWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore
import json

from scripts import parseStrings

class ProjectTab(QWidget):
    def __init__(self):
        super().__init__()
        
        mainlayout = QGridLayout()
        leftLayout = QGridLayout()
        rightLayout = QGridLayout()
        mainlayout.addLayout(leftLayout, 0, 0, 6, 1)
        mainlayout.addLayout(rightLayout, 0, 1, 6, 5) 
        leftLayout.addWidget(QLabel('left'))
        rightLayout.addWidget(QLabel('right'))
        
        staticAnalysisButton = QPushButton("Static Analysis")
        rightLayout.addWidget(staticAnalysisButton, 1, 1, 1, 1)
        staticAnalysisButton.clicked.connect(self.staticAnalysis)
        
        self.infoTable = QTableWidget()
        self.infoTable.setRowCount(2)
        self.infoTable.setColumnCount(2)
        self.infoTable.setItem(0, 0, QTableWidgetItem("OS"))
        self.infoTable.setItem(1, 0, QTableWidgetItem("Binary Type"))
        self.infoTable.doubleClicked.connect(self.on_click)


        self.test = QLabel("hi")
        leftLayout.addWidget(self.test, 2, 2, 2, 2)

        rightLayout.addWidget(self.infoTable)
        
        
        self.setLayout(mainlayout)
        
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.infoTable.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
        self.test.setText("testtesetteset")
            
    

    def staticAnalysis(self):
        rlocal = r2pipe.open("/bin/ping")
        binInfo = rlocal.cmd('ij')
        data = json.loads(binInfo)
#         myvalue = (data['core']['file'])
#         print(myvalue)
  
        myvalue = (data['core']['file'])
        for key in data:
            print(data['core']['file'])
            
        self.infoTable.setItem(1,1,QTableWidgetItem(myvalue))

#     def populateBinaryInfo(self):
         
        
        