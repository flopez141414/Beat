# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnalysisResultView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(295, 387)
        self.pushButton_Delete = QtWidgets.QPushButton(Dialog)
        self.pushButton_Delete.setGeometry(QtCore.QRect(10, 350, 93, 28))
        self.pushButton_Delete.setObjectName("pushButton_Delete")
        self.pushButton_Save = QtWidgets.QPushButton(Dialog)
        self.pushButton_Save.setGeometry(QtCore.QRect(190, 350, 93, 28))
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 10, 21, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 10, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 51, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_Name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Name.setGeometry(QtCore.QRect(70, 190, 211, 22))
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.PlanTextEdit_DescrBox = QtWidgets.QPlainTextEdit(Dialog)
        self.PlanTextEdit_DescrBox.setGeometry(QtCore.QRect(70, 220, 211, 121))
        self.PlanTextEdit_DescrBox.setObjectName("PlanTextEdit_DescrBox")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 170, 91, 16))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 160, 271, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_New = QtWidgets.QPushButton(Dialog)
        self.pushButton_New.setGeometry(QtCore.QRect(190, 130, 93, 28))
        self.pushButton_New.setObjectName("pushButton_New")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 70, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 90, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(100, 110, 81, 16))
        self.label_7.setObjectName("label_7")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(260, 40, 21, 21))
        self.toolButton.setObjectName("toolButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 241, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_Delete.setText(_translate("Dialog", "Delete"))
        self.pushButton_Save.setText(_translate("Dialog", "Save"))
        self.pushButton_3.setText(_translate("Dialog", "X"))
        self.label.setText(_translate("Dialog", "Analysis Result View"))
        self.label_2.setText(_translate("Dialog", " Name"))
        self.label_3.setText(_translate("Dialog", "Description"))
        self.label_4.setText(_translate("Dialog", "Analysis Result Area"))
        self.pushButton_New.setText(_translate("Dialog", "New"))
        self.label_5.setText(_translate("Dialog", "Analysis Result A"))
        self.label_6.setText(_translate("Dialog", "Analysis Result B"))
        self.label_7.setText(_translate("Dialog", "Analysis Result C"))
        self.toolButton.setText(_translate("Dialog", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
