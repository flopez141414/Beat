#!/usr/bin/env python3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(670, 538)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.PlanTextEdit_DescrBox = QtWidgets.QPlainTextEdit(Dialog)
        self.PlanTextEdit_DescrBox.setObjectName("PlanTextEdit_DescrBox")
        self.gridLayout.addWidget(self.PlanTextEdit_DescrBox, 3, 1, 1, 1)
        self.lineEdit_Name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.gridLayout.addWidget(self.lineEdit_Name, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.pushButton_Save = QtWidgets.QPushButton(Dialog)
        self.pushButton_Save.setMaximumSize(QtCore.QSize(100, 16777212))
        self.pushButton_Save.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_Save.setAutoDefault(True)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.gridLayout.addWidget(self.pushButton_Save, 5, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.pushButton_Delete = QtWidgets.QPushButton(Dialog)
        self.pushButton_Delete.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_Delete.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_Delete.setObjectName("pushButton_Delete")
        self.gridLayout.addWidget(self.pushButton_Delete, 6, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Output Field View"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"> Name</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Location</p></body></html>"))
        self.pushButton_Save.setText(_translate("Dialog", "Generate"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Description</p></body></html>"))
        self.pushButton_Delete.setText(_translate("Dialog", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())