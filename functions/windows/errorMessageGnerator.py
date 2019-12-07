import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


def showDialog(message, title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.setSizeIncrement(1, 1)
    msgBox.setSizeGripEnabled(True)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        pass

def confirmDeletion(message, title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Question)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msgBox.setSizeIncrement(1, 1)
    msgBox.setSizeGripEnabled(True)
    
    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Yes:
        return True
    elif returnValue == QMessageBox.No:
        return False
