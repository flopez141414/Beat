import r2pipe
import json
import projectTab

# opens binary file and extracts variables, strings, imports, functions, packet info, and struct info
from PyQt5.QtWidgets import QFileDialog

rlocal = r2pipe.open(projectTab.myFileName)
#     global variableInfo = rlocal.cmd()
stringInfo = rlocal.cmd('izzj')
dllInfo = rlocal.cmd('iij')
functionInfo = rlocal.cmd('aaa ; aflj')
# binaryInfo = rlocal.cmd('iI').splitlines()
#     global packetInfo = rlocal.cmd('afl')
#     global structInfo = rlocal.cmd('afl')

# parse strings and store them in our database
def parseStrings(r2str):
    myr2str = json.loads(r2str)
    myStrings = []
#     print(myr2str['strings'][0]['string'])
    for key in myr2str['strings']:
#         print(key['string'])
        myStrings.append(key['string'])
        
    #for finding duplicate strings    
#     myStrings.sort()
#     for i in range(len(myStrings)-1):
#         if myStrings[i] == myStrings[i+1]:
#             print('FOUND ONE', myStrings[i])
    print(myStrings)

def parseDll(r2dll):
    print(r2dll)
    
def parseFunction(r2func):
    print(r2func)
    
def parseBinaryInfo(r2binfo):
#     for i in r2binfo:
    print(type(r2binfo[0]))
    
    

#method to open file explorer
def OpenFile(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                              "All Files (*);;Python Files (*.py)", options=options)
    if fileName:
        print(fileName)
        return fileName

    return "not found"

def runStringAnalysis:
    parseStrings(r2str)
