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
        print('OK clicked')


def confirm_deletion(message, title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Question)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    # msgBox.setStandardButtons(QMessageBox.No)
    # msgBox.setStandardButtons(QMessageBox.Cancel)
    msgBox.setSizeIncrement(1, 1)
    msgBox.setSizeGripEnabled(True)
    # msgBox.buttonClicked.connect(msgButtonClick)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Yes:
        print("Yes clicked")
        return True
    elif returnValue == QMessageBox.No:
        print("No clicked")
        return False


def infoToast(message, title):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.setSizeIncrement(1, 1)
    msgBox.setSizeGripEnabled(True)
    returnValue = msgBox.exec()
