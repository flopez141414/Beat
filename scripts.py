import r2pipe
import json
# opens binary file and extracts variables, strings, imports, functions, packet info, and struct info
rlocal = r2pipe.open("/bin/ping") 
#     global variableInfo = rlocal.cmd()
stringInfo = rlocal.cmd('izzj')
dllInfo = rlocal.cmd('iij')
functionInfo = rlocal.cmd('aaa ; aflj')
binaryInfo = rlocal.cmd('iI').splitlines()
#     global packetInfo = rlocal.cmd('afl')
#     global structInfo = rlocal.cmd('afl')

# 
#   "strings": [
#     {
#       "vaddr": 52,
#       "paddr": 52,
#       "ordinal": 0,
#       "size": 12,
#       "length": 5,
#       "section": "LOAD0",
#       "type": "utf16le",
#       "string": "QDhcdEBcZQ=="
#     },
    
def parseStrings(r2str):
    myr2str = json.loads(r2str)
    mystuff = []
#     print(myr2str['strings'][0]['string'])
    for key in myr2str['strings']:
#         print(key['string'])
        mystuff.append(key['string'])
        
    #for finding duplicate strings    
    mystuff.sort()
    for i in range(len(mystuff)-1):
        if mystuff[i] == mystuff[i+1]:
            print('FOUND ONE', mystuff[i])
#     print(mystuff)

def parseDll(r2dll):
    print(r2dll)
    
def parseFunction(r2func):
    print(r2func)
    
def parseBinaryInfo(r2binfo):
#     for i in r2binfo:
    print(type(r2binfo[0]))
    
    
# parseStrings(stringInfo)

parseBinaryInfo(binaryInfo)
    