import sys
import r2pipe
import pymongo
import os
# import webbrowser as wb #--new line to import pdf
from pymongo import MongoClient
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QFileDialog, QSplitter, \
    QHBoxLayout, QFrame, QGridLayout, QTabWidget, QVBoxLayout, QHBoxLayout, QListWidget, QComboBox, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore, QtGui


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidget


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(689, 433)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        self.plainTextEdit_CommView = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_CommView.setObjectName("plainTextEdit_CommView")
        self.gridLayout.addWidget(self.plainTextEdit_CommView, 0, 1, 1, 1)

        self.searchDocList = QListWidget()
        self.gridLayout.addWidget(self.searchDocList, 0, 0, 1, 1)

        self.pushButtonSave = QtWidgets.QPushButton(Dialog)
        self.pushButtonSave.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout.addWidget(self.pushButtonSave, 1, 1, 1, 1)
        self.pushButtonSave.clicked.connect(self.display_comments)

        self.pushButtonClear = QtWidgets.QPushButton(Dialog)
        self.pushButtonClear.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.gridLayout.addWidget(self.pushButtonClear, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Comment View"))
        self.pushButtonSave.setText(_translate("Dialog", "Save"))
        self.pushButtonClear.setText(_translate("Dialog", "Clear"))

    def displayPOI(self, option):
        client = MongoClient('localhost', 27017)  # client to access database
        db = client.beat  # getting an instance of our DB
        dataCollection = db.Project  # accessing a collection of documents in our DB
        dataSet = dataCollection.find()
        strings = pois['Project']['StaticAnalysis']['stringPointOfInterest']
        for i in range(len(strings)):
            self.searchDocList.addItem(strings[i]['value'])
        functions = pois['Project']['StaticAnalysis']['functionPointOfInterest']
        for i in range(len(functions)):
            self.searchDocList.addItem(functions[i]['name'])

    def display_comments(self):
        client = MongoClient('localhost', 27017)
        db = client.beat
        dataSet = db.Project
        collection = dataSet.find()[1]
        print(collection['Project'])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.displayPOI()
    Dialog.show()
    sys.exit(app.exec_())
