# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QFileDialog, QSplitter, \
    QHBoxLayout, QFrame, QGridLayout, QTabWidget, QVBoxLayout, QHBoxLayout, QListWidget, QComboBox, QLineEdit, QTextEdit
from PyQt5.QtWidgets import QListWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(689, 433)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        self.searchBox = QLineEdit()
        #self.doc_view_label = QLabel('Document View')
        #detail_doc_view_label = QLabel('Detail Document View')


        #self.gridLayout.addWidget(self.detail2_doc_view_label, 0, 1, 1, 1)
        # Search box
        self.gridLayout.addWidget(self.searchBox, 0, 0, 1,7)

        # Text Edit
        self.plainTextEdit_CommView = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_CommView.setObjectName("plainTextEdit_CommView")
        self.gridLayout.addWidget(self.plainTextEdit_CommView, 1, 5, 1, 7)

        # list
        self.searchDocList = QListWidget()
        self.gridLayout.addWidget(self.searchDocList, 1, 0, 1, 5)





        # Save Button
        self.pushButtonSave = QtWidgets.QPushButton(Dialog)
        self.pushButtonSave.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout.addWidget(self.pushButtonSave, 2, 1, 1, 1)
        #Clear Button
        self.pushButtonClear = QtWidgets.QPushButton(Dialog)
        self.pushButtonClear.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.gridLayout.addWidget(self.pushButtonClear, 2, 2, 1, 1)
        #Search Button
        self.pushButtonSearch = QtWidgets.QPushButton(Dialog)
        self.pushButtonSearch.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.gridLayout.addWidget(self.pushButtonSearch, 3, 1,1,1)

        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # self.gridLayout.addWidget(self.frame, 3, 1, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Comment View"))
        self.pushButtonSave.setText(_translate("Dialog", "Save"))
        self.pushButtonClear.setText(_translate("Dialog", "Clear"))
        self.pushButtonSearch.setText(_translate("Dialog", "Search"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
