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
        Dialog.resize(487, 551)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_Name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.gridLayout.addWidget(self.lineEdit_Name, 9, 1, 1, 4)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 4)
        self.pushButton_Delete = QtWidgets.QPushButton(Dialog)
        self.pushButton_Delete.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_Delete.setObjectName("pushButton_Delete")
        self.gridLayout.addWidget(self.pushButton_Delete, 12, 0, 1, 3)
        self.pushButton_New = QtWidgets.QPushButton(Dialog)
        self.pushButton_New.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_New.setObjectName("pushButton_New")
        self.gridLayout.addWidget(self.pushButton_New, 5, 4, 1, 1)
        self.PlanTextEdit_DescrBox = QtWidgets.QPlainTextEdit(Dialog)
        self.PlanTextEdit_DescrBox.setObjectName("PlanTextEdit_DescrBox")
        self.gridLayout.addWidget(self.PlanTextEdit_DescrBox, 10, 1, 1, 4)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 4)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setMaxLength(65001)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 10, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 5)
        self.pushButton_Save = QtWidgets.QPushButton(Dialog)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.gridLayout.addWidget(self.pushButton_Save, 12, 4, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Analysis Result View"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Analysis Result A</p></body></html>"))
        self.pushButton_Delete.setText(_translate("Dialog", "Delete"))
        self.pushButton_New.setText(_translate("Dialog", "New"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Analysis Result C</p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Analysis Result"))
        self.label_2.setText(_translate("Dialog", " Name"))
        self.label_3.setText(_translate("Dialog", "Description"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Analysis Result B</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Analysis Result Area</span></p></body></html>"))
        self.pushButton_Save.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
