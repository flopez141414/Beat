import sys

from pymongo import MongoClient

import r2pipe
import pymongo
import json
import projectTab as pt
from PyQt5.QtWidgets import QMainWindow,QLabel, QApplication,QFormLayout, QWidget, QPushButton, QAction, QLabel, QFileDialog, QSplitter, \
    QHBoxLayout, QFrame, QGridLayout, QTabWidget, QVBoxLayout,QScrollArea, QHBoxLayout, QComboBox, QLineEdit, QListWidget, QTextEdit
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore, QtGui, QtWidgets

from CommentView import Ui_Dialog as comment_window
from AnalysisResultView import Ui_Dialog as analysis_window
from OutputFieldView import Ui_Dialog as output_Field_Window

#XML libraries
import xml.etree.ElementTree as ET
import xmltodict
import pprint
import json

sys.path.append("../DB")
sys.path.append("../windows")
import xmlUploader
import errorMessageGnerator
# from xmlUploader import uploadXml

import base64

import xml.dom.minidom

class AnalysisTab(QWidget):

    def __init__(self):
        super().__init__()
        stringsPOI = []
        functionsPOI = []
        variablesPOI = []
        protocolsPOI = []
        structuresPOI = []
        poiSuperList= []
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
        self.searchBox = QLineEdit()
        self.searchButton = QPushButton('Search')
        self.searchedWord=[]
        
        
        self.poiList = QListWidget()
        leftPanelLabel = QLabel('Point of Interest View')
#         leftPanelLabel.setStyleSheet("background-color: rgba(173,216,230 ,1 )")
        leftPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        leftPanelLabel.setAlignment(Qt.AlignCenter)

        leftLayout.addWidget(leftPanelLabel, 0, 0, 1, 4)
        leftLayout.addWidget(self.searchBox, 1, 0, 1, 3)
        leftLayout.addWidget(self.searchButton, 1, 3, 1, 1)
        leftLayout.addWidget(self.poiList, 2, 0, 1, 4)

        # Right panel
        rightPanelLabel = QLabel('Point of Interest View')
#         rightPanelLabel.setStyleSheet("background-color: rgba(173,216,230 ,1 )")
        rightPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        rightPanelLabel.setAlignment(Qt.AlignCenter)
        self.poiContentArea = QScrollArea()
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
        self.searchButton.clicked.connect(self.clickedSearch)
        self.setLayout(mainlayout)

    def clickedSearch(self):
        global poiSuperList
        target=self.searchBox.text()
        self.searchedWord=[s for s in poiSuperList if target in s]
        self.poiList.clear()
        for items in self.searchedWord:
            self.poiList.addItem(items)

    def displayPOIparam(self):
        content_widget=QWidget()
        self.poiContentArea.setWidget(content_widget)
        layoutForPOI= QGridLayout(content_widget)
        self.poiContentArea.setWidgetResizable(True)
        option= self.poiDropdown.currentText()
        if option=="Strings":
            for i in range(layoutForPOI.count()): layoutForPOI.itemAt(i).widget().close()
            value= QLabel('Value:')
            sectionInBinary=QLabel('Section In Binary:')
            self.valueLine=QLineEdit()
            self.sectionInBinaryLine= QLineEdit()
            layoutForPOI.addWidget(value,1,0)
            layoutForPOI.addWidget(self.valueLine,1,1)
            layoutForPOI.addWidget(sectionInBinary,2,0)
            layoutForPOI.addWidget(self.sectionInBinaryLine,2,1)
        elif option=="Functions":
            for i in range(layoutForPOI.count()): layoutForPOI.itemAt(i).widget().close()
        
            order= QLabel('Order of Parameters:')
            fpType=QLabel('Parameter Type:')
            fpValue=QLabel('Parameter Value:')
            frType=QLabel('Return Type:')
            frValue=QLabel('Return Value:')
            fRelativeOrder=QLabel('Order in Relation to :')
            
            self.orderLine=QLineEdit()
            self.fpTypeLine= QLineEdit()
            self.fpValueLine=QLineEdit()
            self.frValueLine= QLineEdit()
            self.frTypeLine=QLineEdit()
            self.fRelativeOrderLine= QLineEdit()
            
            layoutForPOI.addWidget(order,1,0)
            layoutForPOI.addWidget(self.orderLine,1,1)
            layoutForPOI.addWidget(fpType,2,0)
            layoutForPOI.addWidget(self.fpTypeLine,2,1)
            layoutForPOI.addWidget(frValue,3,0)
            layoutForPOI.addWidget(self.frValueLine,3,1)
            layoutForPOI.addWidget(fRelativeOrder,4,0)
            layoutForPOI.addWidget(self.fRelativeOrderLine,4,1)

        elif option=="Variables":
            for i in range(layoutForPOI.count()): layoutForPOI.itemAt(i).widget().close()
            variableType=QLabel('Variable Type:')
            value= QLabel('Value:')
            sectionInBinary=QLabel('Section In Binary:')
            variableTypeLine=QLineEdit()
            valueLine=QLineEdit()
            sectionInBinaryLine= QLineEdit()
            layoutForPOI.addWidget(variableType,1,0)
            layoutForPOI.addWidget(variableTypeLine,1,1)
            layoutForPOI.addWidget(value,2,0)
            layoutForPOI.addWidget(valueLine,2,1)
            layoutForPOI.addWidget(sectionInBinary,3,0)
            layoutForPOI.addWidget(sectionInBinaryLine,3,1)
        elif option=="Structures":
            for i in range(layoutForPOI.count()): layoutForPOI.itemAt(i).widget().close()
            memberOrder=QLabel('Member Order:')
            memberType= QLabel('Value:')
            sectionInBinary=QLabel('Section In Binary:')
            memberValue=QLabel('Member Value:')
            memberOrderLine=QLineEdit()
            memberTypeLine=QLineEdit()
            sectionInBinaryLine= QLineEdit()
            memberValueLine=QLineEdit()
            layoutForPOI.addWidget(sectionInBinary,1,0)
            layoutForPOI.addWidget(sectionInBinaryLine,1,1)
            layoutForPOI.addWidget(memberOrder,2,0)
            layoutForPOI.addWidget(memberOrderLine,2,1)
            layoutForPOI.addWidget(memberType,3,0)
            layoutForPOI.addWidget(memberTypeLine,3,1)
            layoutForPOI.addWidget(memberValue,4,0)
            layoutForPOI.addWidget(memberValueLine,4,1)
        elif option=="Protocols":
            for i in range(layoutForPOI.count()): layoutForPOI.itemAt(i).widget().close()
            pStructure=QLabel('Structure')
            pSize= QLabel('Size')
            sectionInBinary=QLabel('Section In Binary:')
            pSizeLine=QLineEdit()
            pStructureLine=QLineEdit()
            sectionInBinaryLine= QLineEdit()
            layoutForPOI.addWidget(sectionInBinary,1,0)
            layoutForPOI.addWidget(sectionInBinaryLine,1,1)
            layoutForPOI.addWidget(pStructure,2,0)
            layoutForPOI.addWidget(pStructureLine,2,1)
            layoutForPOI.addWidget(pSize,3,0)
            layoutForPOI.addWidget(pSizeLine,3,1)
        else:
            for i in range(layoutForPOI.count()): layoutForPOI.itemAt(i).widget().close()

    def makeStringTree(self, stringsData, parentRoot):
        stringHolderElement = parentRoot.find('./stringHolder')
        
        for index in range(len(stringsData)): # access each string
            myString = stringsData[index] # this dictionary contains one String POI
            tree = ET.parse('../xml/StringPointOfInterest.xml')
            root = tree.getroot()
            b2tf = root.find("./value")
            b2tf.text = str(base64.standard_b64decode(myString['string']))
            b2tf = root.find("./address")
            b2tf.text = str(hex(myString['vaddr']))
            b2tf = root.find("./section")
            b2tf.text = str(myString['section'])
            stringHolderElement.append(root)          
        
    def makeFunctionsTree(self, functionsData, parentRoot):
        functionHolderElement = parentRoot.find('./functionHolder')
        
        for index in range(len(functionsData)): # access each function
            myFunction = functionsData[index] # this dictionary contains one function POI
            tree = ET.parse('../xml/FunctionPointOfInterest.xml')
            root = tree.getroot()
            b2tf = root.find("./name")
            b2tf.text = str(myFunction['name'])
            b2tf = root.find("./address")
            b2tf.text = str(hex(myFunction['offset']))
            b2tf = root.find("./parameterType")
            b2tf.text = str(myFunction['signature'])
            functionHolderElement.append(root)      
    
    # TODO: link list item with expanded view of POI      
    def displayPOI(self,option):
        client = MongoClient('localhost', 27017) # client to access database
        db = client.pymongo_test # getting an instance of our DB
        dataCollection = db.dataSet # accessing a collection of documents in our DB
        dataSet = dataCollection.find()
        
        if option =="Strings":
            self.poiList.clear()
            for data in dataSet: # access a cursor object from database
                stringPois = data['pointOfInterestDataSet']['stringHolder']['stringPointOfInterest']
                for i in range(len(stringPois)): # access each individual string POI
                    self.poiList.addItem(stringPois[i]['value'])
        if option =="Functions":
            self.poiList.clear()
            for data in dataSet: # access a cursor object from database
                functionPois = data['pointOfInterestDataSet']['functionHolder']['functionPointOfInterest']
                for i in range(len(functionPois)): # access each individual function POI
                    self.poiList.addItem(functionPois[i]['name'])
            

                
    def parseNetworkItems(self):
        global poiSuperList
        target=['socket','send','rec','ipv','main']
        for i in target:
            self.searchedWord.append([s for s in poiSuperList if i in s])
            
        self.poiList.clear()
        poiSuperList=[]
        for items in self.searchedWord:
            for item2 in items:
                self.poiList.addItem(item2)
        self.searchedWord = []
        
#     def displayPOI(self,option):
#         global poiSuperList
#         if option=="Strings":
#             poiSuperList=[]
#             self.poiList.clear()
# #            target=['socket','send','rec','ipv','main']
#  #           for i in target:
#   #          self.searchedWord.append([s for s in poiSuperList if i in s])
#             for item in stringsPOI:
#                 item2=item.split()
#                 self.poiList.addItem(item2[2])
#                 poiSuperList.append(item2[2])
#             #self.poiContentArea.setText(stringsPOI)
#             #self.poiList.itemSelectionChanged.connect(self.poiSelected)
#         elif option == "Variables":
#             self.poiList.clear()
#             poiSuperList=[]
#             #for item in variablesPOI:
#              #   self.poiList.addItem(item)
#             #self.poiContentArea.setText(variablesPOI)
#         elif option == "Functions":
#             self.poiList.clear()
#             poiSuperList=[]
#             for item in functionsPOI:
#                 item2=item.split()
#                 if item2[3]=="->":
#                     self.poiList.addItem(item2[5])
#                     poiSuperList.append(item2[5])
#                 else:
#                     self.poiList.addItem(item2[3])
#                     poiSuperList.append(item2[3])
#             #self.poiContentArea.setText(functionsPOI)
#             #self.poiList.itemSelectionChanged.connect(self.displayPOIselected)
#         elif option == "Structures":
#             self.poiList.clear()
#             poiSuperList=[]
#             #for item in structuresPOI:
#              #   self.poiList.addItem(item)
#             #self.poiContentArea.setText(structuresPOI)
#             #self.poiList.itemSelectionChanged.connect(self.displayPOIselected)
#         elif option == "Protocols":
#             self.poiList.clear()
#             poiSuperList=[]
#            # for item in protocolsPOI[2:]:
#             #    item2=item.split()
#              #   self.poiList.addItem(item2[3])
#             #self.poiContentArea.setText(dllsPOI)
#             #self.poiList.itemSelectionChanged.connect(self.displayPOIselected)
#         self.displayPOIparam()
#         self.parseNetworkItems()
#         
    def onActivated(self,option):
        if option == "Network Plugin":
            self.poiDropdown.clear()
            self.poiDropdown.addItem("Select POI to display")
            self.poiDropdown.addItem("Strings")
            self.poiDropdown.addItem("Functions")
            self.poiDropdown.addItem("Variables")
            self.poiDropdown.addItem("Protocols")
            self.poiDropdown.addItem("Structures")
        elif option == "dummy":
            self.poiDropdown.clear()
            self.poiDropdown.addItem("opps")

    def clickStaticAnalysis(self):
        global stringsPOI
        global variablesPOI
        global functionsPOI
        global protocolsPOI
        global structuresPOI
        
        global parentRoot # holds all POIs from static analysis
        
        bina = r2pipe.open(pt.myFileName)
        bina.cmd("aaaa") # analyze binary in Radare2
        self.terminal.setText("Running Static Analysis..")
        
        # extracting POI data from Radare2 and storing as json dictionaries
        stringsPOI = bina.cmd("izj") 
        jsonStrings = json.loads(stringsPOI) 
        functionsPOI = bina.cmd("aflj")
        jsonFunctions = json.loads(functionsPOI)
        
        # get handle to POI holder xml, create POI xmls, and upload them to DB
        parentTree = ET.parse('../xml/pointOfInterestDataSet.xml')
        parentRoot = parentTree.getroot()
        self.makeStringTree(jsonStrings, parentRoot)
        self.makeFunctionsTree(jsonFunctions, parentRoot)
        parent_dict = ET.tostring(parentRoot, encoding='utf8').decode('utf8')
        xmlUploader.uploadDataSet(parent_dict) 
        
#       protocolsPOI = bina.cmd("ii").splitlines()
#       structuresPOI = bina.cmd("").splitlines()
#       variablesPOI = bina.cmd("").splitlines()
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
