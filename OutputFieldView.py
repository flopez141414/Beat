# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OutputFieldView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(292, 315)
        self.pushButton_Browse = QtWidgets.QPushButton(Dialog)
        self.pushButton_Browse.setGeometry(QtCore.QRect(190, 250, 93, 28))
        self.pushButton_Browse.setObjectName("pushButton_Browse")
        self.pushButton_Generate = QtWidgets.QPushButton(Dialog)
        self.pushButton_Generate.setGeometry(QtCore.QRect(190, 280, 93, 28))
        self.pushButton_Generate.setObjectName("pushButton_Generate")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 10, 21, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 10, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 51, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_Name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Name.setGeometry(QtCore.QRect(70, 60, 211, 22))
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.plainTextEdit_Description = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_Description.setGeometry(QtCore.QRect(70, 100, 211, 101))
        self.plainTextEdit_Description.setObjectName("plainTextEdit_Description")
        self.lineEdit_Location = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Location.setGeometry(QtCore.QRect(70, 220, 211, 22))
        self.lineEdit_Location.setObjectName("lineEdit_Location")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_Browse.setText(_translate("Dialog", "Browse"))
        self.pushButton_Generate.setText(_translate("Dialog", "Generate"))
        self.pushButton_3.setText(_translate("Dialog", "X"))
        self.label.setText(_translate("Dialog", "Output Field View"))
        self.label_2.setText(_translate("Dialog", " Name"))
        self.label_3.setText(_translate("Dialog", "Description"))
        self.label_4.setText(_translate("Dialog", "    Location"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
