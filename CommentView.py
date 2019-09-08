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
        Dialog.resize(286, 215)
        self.pushButtonSave = QtWidgets.QPushButton(Dialog)
        self.pushButtonSave.setGeometry(QtCore.QRect(90, 180, 93, 28))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonClear = QtWidgets.QPushButton(Dialog)
        self.pushButtonClear.setGeometry(QtCore.QRect(190, 180, 93, 28))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 10, 91, 16))
        self.label.setObjectName("label")
        self.plainTextEdit_CommView = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_CommView.setGeometry(QtCore.QRect(10, 40, 271, 131))
        self.plainTextEdit_CommView.setObjectName("plainTextEdit_CommView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonSave.setText(_translate("Dialog", "Save"))
        self.pushButtonClear.setText(_translate("Dialog", "Clear"))
        self.label.setText(_translate("Dialog", "Comment View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
