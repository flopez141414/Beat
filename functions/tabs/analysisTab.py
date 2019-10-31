import sys

import r2pipe
import pymongo
import json

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QFileDialog, QSplitter, \
    QHBoxLayout, QFrame, QGridLayout, QTabWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QListWidget, QTextEdit
from PyQt5.QtCore import pyqtSlot, Qt
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
        self.stopDynamic = QPushButton('Stop')

        # TODO: Using this button to test terminal temporarily: remove comment from setEnabled call after finished
#         self.stopDynamic.setEnabled(False)
        # TODO: Disable this connection after testing is finished and create a new button to grab input from terminal 
        self.stopDynamic.clicked.connect(self.sendTextToTerminal)

        topLayout.addWidget(QLabel('Plugin'), 0, 0)
        topLayout.addWidget(pluginDropdown, 0, 1, 1, 2)
        topLayout.addWidget(QLabel('Static Analysis'), 1, 0)
        topLayout.addWidget(runStatic, 1, 1, 1, 1)
        topLayout.addWidget(QLabel('Point of Interest Type'), 2, 0)
        topLayout.addWidget(self.poiDropdown, 2, 1, 1, 2)
        topLayout.addWidget(QLabel('Dynamic Analysis'), 1, 5, 1, 1)
        topLayout.addWidget(runDynamic, 1, 6)
        topLayout.addWidget(self.stopDynamic, 1, 7)
        topLayout.addWidget(QLabel(), 0, 3, 1, 15)

        # Left panel
        searchBox = QLineEdit()
        searchButton = QPushButton('Search')

        self.poiList = QListWidget()
        leftPanelLabel = QLabel('Point of Interest View')
#         leftPanelLabel.setStyleSheet("background-color: rgba(173,216,230 ,1 )")
        leftPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        leftPanelLabel.setAlignment(Qt.AlignCenter)

        leftLayout.addWidget(leftPanelLabel, 0, 0, 1, 4)
        leftLayout.addWidget(searchBox, 1, 0, 1, 3)
        leftLayout.addWidget(searchButton, 1, 3, 1, 1)
        leftLayout.addWidget(self.poiList, 2, 0, 1, 4)

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
        self.connectedClient = False # flag to continue step into dynamic analysis
        self.initialized = False # flag to see if we have already initiated dynamic analysis

        self.poiDropdown.activated[str].connect(self.displayPOI)
        runStatic.clicked.connect(self.clickStaticAnalysis)
        self.setLayout(mainlayout)

    def displayPOI(self,option):
        if option=="Strings":
            self.poiList.clear()
            for item in stringsPOI:
                item2=item.split()
                self.poiList.addItem(item2[2])
            #self.poiContentArea.setText(stringsPOI)
        elif option == "Variables":
            self.poiList.clear()
            #for item in variablesPOI:
             #   self.poiList.addItem(item)
            #self.poiContentArea.setText(variablesPOI)
        elif option == "Functions":
            self.poiList.clear()
            for item in functionsPOI:
                item2=item.split()
                if item2[3]=="->":
                    self.poiList.addItem(item2[5])
                else:
                    self.poiList.addItem(item2[3])
            #self.poiContentArea.setText(functionsPOI)
        elif option == "Structures":
            self.poiList.clear()
            #for item in structuresPOI:
             #   self.poiList.addItem(item)
            #self.poiContentArea.setText(structuresPOI)
        elif option == "Dlls":
            self.poiContentArea.setText(dllsPOI)
            self.poiList.clear()
            for item in dllsPOI[2:]:
                item2=item.split()
                self.poiList.addItem(item2[4])
            #self.poiContentArea.setText(dllsPOI)
            
    def onActivated(self,option):
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

    def clickStaticAnalysis(self):
        import projectTab
        bina = r2pipe.open(projectTab.myFileName)
        self.terminal.setText("Running Static Analysis..")
        global stringsPOI
        global variablesPOI
        global functionsPOI
        global dllsPOI
        global structuresPOI

        stringsPOI = bina.cmd("f;~str.").splitlines()
        dllsPOI = bina.cmd("ii").splitlines()
        functionsPOI = bina.cmd("aaa;afl").splitlines()
        #structuresPOI = bina.cmd("").splitlines()
        #variablesPOI = bina.cmd("").splitlines()
        self.terminal.append("Static Analysis done!")
    
    def dynamicAnalysis(self):
        # only do the initializing of breakpoints/opening file/running in debug mode once
        if(self.initialized is False):
            programToAnalyze = "server.out"
            functionName = "sym.imp.recv"
            global r2
            r2 = r2pipe.open("server.out") # Open program to be analyzed by radare2
            r2.cmd("aaa") # Perform static analysis on program 
            r2.cmd("doo 12344") # Re open program in debug/background mode
            self.initialized = True
            print("initialized dynamic analysis; connect the client now")
#         references = r2.cmd("axtj sym.imp.strncmp") # Find all references to functionName in binary

#         r2.cmd("db 0x401548") # hardcoded breakpoint to sym.imp.recv reference in main
#         print(references)
# #         for i in range(len(references)):
# #             self.terminal.append(references[i])# display references to sym.imp.strncmp on GUI
        
#         for i in range(len(references)):
#             breakpoint = 'db ' + hex(references[i]["from"]) # Create add breakpoint command
#             r2.cmd(breakpoint) # Add breakpoints at references locations
# #             print(breakpoint)
        else:
            if(self.connectedClient):
                debugData = r2.cmdj('axtj sym.imp.recv')
                
                breakpoint = 'db ' + hex(debugData[0]["from"])
                
                r2.cmd(breakpoint)
                self.terminal.append("set breakpoint at %s" % breakpoint)
                
                terminalData = r2.cmd("dc") # this will pause the program till you connect the client
                self.terminal.append(terminalData)

                terminalData = r2.cmd("dso") # once client is connected, proceed to step over the function
                self.terminal.append(terminalData)
                
                # retreive data that server.out recieved
                messageAddr = r2.cmd("dr rsi")
                getPayloadCommand = "psz @" + messageAddr
                payload = r2.cmd(getPayloadCommand)
                
                # r2 output
                self.terminal.append("found payload: %s" % payload)
                self.terminal.append("at: %s" % messageAddr)
# 
#                 breakpoints = r2.cmd("db")
#                 print(breakpoints)
#                 r2.cmd("dc")


        
#         whie True:
#             r2.cmd("dso") # step over recv function
# #         ripAddress = r2.cmd("dr rsi")
#             payload = r2.cmd("pxj @ 0x7ffff1111dc0")
#             print(payload)
#             break
             
             
    
    def sendTextToTerminal(self):
#         binary = r2.open("hello")
#         commandToSend = self.terminal.toPlainText() # grabbing user input from text edit to send to radare2
#         print(commandToSend)
        
#         myText = binary.cmd(commandToSend)
#         print(myText)   
#         
        self.connectedClient = True

        
        

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
