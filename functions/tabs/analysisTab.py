import sys

import r2pipe
import pymongo
import json

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QFileDialog, QSplitter, \
    QHBoxLayout, QFrame, QGridLayout, QTabWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QListWidget, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore
from PyQt5.uic.properties import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets

from CommentView import Ui_Dialog as comment_window
from AnalysisResultView import Ui_Dialog as analysis_window
from OutputFieldView import Ui_Dialog as output_Field_Window




class AnalysisTab(QWidget):

    def __init__(self):
        super().__init__()
        stringsPOI = []
        functionsPOI = []
        variablesPOI = []
        dllsPOI = []
        structuresPOI = []

        mainlayout = QGridLayout()
        leftLayout = QGridLayout()
        rightLayout = QGridLayout()
        topLayout = QGridLayout()
        mainlayout.addLayout(topLayout, 0, 0, 1, 6)
        mainlayout.addLayout(leftLayout, 1, 0, 6, 1)
        mainlayout.addLayout(rightLayout, 1, 1, 6, 5)

        # Top layout elements
        pluginDropdown = QComboBox()
        runStatic = QPushButton('Run')
        self.poiDropdown = QComboBox()
        runDynamic = QPushButton('Run')
        stopDynamic = QPushButton('Stop')

        topLayout.addWidget(QLabel('Plugin'), 0, 0)
        topLayout.addWidget(pluginDropdown, 0, 1, 1, 2)
        topLayout.addWidget(QLabel('Static Analysis'), 1, 0)
        topLayout.addWidget(runStatic, 1, 1, 1, 1)
        topLayout.addWidget(QLabel('Point of Interest Type'), 2, 0)
        topLayout.addWidget(self.poiDropdown, 2, 1, 1, 2)
        topLayout.addWidget(QLabel('Dynamic Analysis'), 1, 5, 1, 1)
        topLayout.addWidget(runDynamic, 1, 6)
        topLayout.addWidget(stopDynamic, 1, 7)
        topLayout.addWidget(QLabel(), 0, 3, 1, 15)

        # Left panel
        searchBox = QLineEdit()
        searchButton = QPushButton('Search')

        poiList = QListWidget()
        leftPanelLabel = QLabel('Point of Interest View')
#         leftPanelLabel.setStyleSheet("background-color: rgba(173,216,230 ,1 )")
        leftPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        leftPanelLabel.setAlignment(Qt.AlignCenter)

        leftLayout.addWidget(leftPanelLabel, 0, 0, 1, 4)
        leftLayout.addWidget(searchBox, 1, 0, 1, 3)
        leftLayout.addWidget(searchButton, 1, 3, 1, 1)
        leftLayout.addWidget(poiList, 2, 0, 1, 4)

        # Right panel
        rightPanelLabel = QLabel('Point of Interest View')
#         rightPanelLabel.setStyleSheet("background-color: rgba(173,216,230 ,1 )")
        rightPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        rightPanelLabel.setAlignment(Qt.AlignCenter)
        self.poiContentArea = QTextEdit()
        self.terminal = QTextEdit()
        self.commentButton = QPushButton('Comments')
        self.outputButton = QPushButton('Output')
        self.analysisButton = QPushButton('Analysis')

        rightLayout.addWidget(rightPanelLabel, 0, 0, 1, 10)
        rightLayout.addWidget(self.poiContentArea, 1, 0, 10, 8)
        rightLayout.addWidget(self.terminal, 11, 0, 10, 8)
        rightLayout.addWidget(self.analysisButton, 1, 9)
        rightLayout.addWidget(self.outputButton, 2, 9)
        rightLayout.addWidget(self.commentButton, 2, 8)

        #Functionality
        self.commentButton.clicked.connect(self.openCommentWindow)
        self.analysisButton.clicked.connect(self.openAnalysisWindow)
        self.outputButton.clicked.connect(self.openOutputWindow)

        # set Plugin name
        pluginDropdown.addItem("Select Plugin")
        pluginDropdown.addItem("Network Plugin")
        pluginDropdown.addItem("dummy")
        pluginDropdown.activated[str].connect(self.onActivated)
        
        #dynamic analysis run event listener
        runDynamic.clicked.connect(self.dynamicAnalysis)

        self.poiDropdown.activated[str].connect(self.displayPOI)
        runStatic.clicked.connect(self.clickEvent)
        self.setLayout(mainlayout)

    def displayPOI(self, option):
        if option == "Strings":
            self.poiContentArea.setText(stringsPOI)
        elif option == "Variables":
            self.poiContentArea.setText(variablesPOI)
        elif option == "Functions":
            self.poiContentArea.setText(functionsPOI)
        elif option == "Structures":
            self.poiContentArea.setText(structuresPOI)
        elif option == "Dlls":
            self.poiContentArea.setText(dllsPOI)

    def onActivated(self, option):
        if option == "Network Plugin":
            self.poiDropdown.clear()
            self.poiDropdown.addItem("Select POI to display")
            self.poiDropdown.addItem("Strings")
            self.poiDropdown.addItem("Functions")
            self.poiDropdown.addItem("Variables")
            self.poiDropdown.addItem("Dlls")
            self.poiDropdown.addItem("Structures")
        elif option == "dummy":
            self.poiDropdown.clear()
            self.poiDropdown.addItem("opps")

    def clickEvent(self):
#         bina = r2pipe.open("hello")

        import projectTab
        bina = r2pipe.open(projectTab.myFileName)
        
        self.terminal.setText("Running Static Analysis..")
        global stringsPOI
        global variablesPOI
        global functionsPOI
        global dllsPOI
        global structuresPOI
        stringsPOI = bina.cmd("f;~str.")
        dllsPOI = bina.cmd("ii")
        functionsPOI = bina.cmd("pdf;~call")
        structuresPOI = bina.cmd("")
        variablesPOI = bina.cmd("")
        self.terminal.append("Static Analysis done!")
    
    
    def dynamicAnalysis(self):
        programToAnalyze = "ping"
        functionName = "sym.imp.recv"
        
        r2 = r2pipe.open("ping") # Open program to be analyzed by radare2
        r2.cmd('e bin.maxstrbuf=0xfffff09c5e400ba8') # Increase the buffer size 
        r2.cmd('e dbg.bpinmaps=0') # disable cannot set breakpoint on unmapped memory
        r2.cmd("aaa") # Perform static analysis on program 
        r2.cmd("doo arg1=127.0.0.1") # Re open program in debug/background mode
        references = r2.cmd("axtj sym.imp.strncmp") # Find all references to functionName in binary

        print(references)
#         for i in range(len(references)):
#             self.terminal.append(references[i])# display references to sym.imp.strncmp on GUI
        
        for i in range(len(references)):
            breakpoint = 'db ' + hex(references[i]["from"]) # Create add breakpoint command
            r2.cmd(breakpoint) # Add breakpoints at references locations
#             print(breakpoint)
            
        
             
#         while True:
#             r2.cmd("dc") # Continue until breakpoint is hit 'debug continue execution'
#             r2.cmd("dso") # Execute over the breakpoint 'debug step over'
         
# #             rax = 0x00000000
# #             rbx = 0x00000000
# #             rcx = 0x00000000
# #             rdx = 0x00000000
# #             rsi = 0x00000000
# #             rdi = 0x00000000
# #             r8 = 0x00000000
# #             r9 = 0x00000000
# #             r10 = 0x00000000
# #             r11 = 0x00000000
# #             r12 = 0x00000000
# #             r13 = 0x00000000
# #             r14 = 0x00000000
# #             r15 = 0x00000000
# #             rip = 0x00003c80
# #             rbp = 0x00000000
# #             rflags = 0x00000000
# #             rsp = 0x00000000
#             payloadAddr = r2.cmd("dr") # values at registers 'debug show register'
#             print(payloadAddr)
#                
#             break

# Methods to open windows
    def openCommentWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = comment_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAnalysisWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = analysis_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def openOutputWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = output_Field_Window()
        self.ui.setupUi(self.window)
        self.window.show()
