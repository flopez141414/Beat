# Creates, retreive(read), updates, and Destroy Text files
import os
def createFile():
    cwd = os.getcwd()
    print(cwd)
    print("Enter Name of new File")
    userInput = input()
    f = open(userInput, "w+")

def readFile(File_object):
    cwd = os.getcwd()
    print(cwd)
    try:
        file = open(File_object, "r")
        print(file.read())
    except:
        print(File_object, " Not Found.")

def updateFile(File_object):
    print("updating file")
    try:
        file = open(File_object,"w")
        userInput = input()
        file.write(userInput)
        file.close()  # to change file access modes
    except:
        print("could not open file")

def delFile(fileToDel):
    #address = os.getcwd()
    try:
        os.remove(fileToDel)
        print(fileToDel," File removed")
    except:
        print("File not found")

createFile()
updateFile("tester.txt")
readFile("tester.txt")
delFile("tester.txt")