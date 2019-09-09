# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CommentView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(689, 433)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit_CommView = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_CommView.setObjectName("plainTextEdit_CommView")
        self.gridLayout.addWidget(self.plainTextEdit_CommView, 1, 1, 1, 3)
        self.pushButtonSave = QtWidgets.QPushButton(Dialog)
        self.pushButtonSave.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout.addWidget(self.pushButtonSave, 2, 2, 1, 1)
        self.pushButtonClear = QtWidgets.QPushButton(Dialog)
        self.pushButtonClear.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.gridLayout.addWidget(self.pushButtonClear, 2, 3, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 1, 3, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Comment View"))
        self.pushButtonSave.setText(_translate("Dialog", "Save"))
        self.pushButtonClear.setText(_translate("Dialog", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
