# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1149, 846)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 891, 801))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.projectTab = QtWidgets.QWidget()
        self.projectTab.setObjectName("projectTab")
        self.pushButton = QtWidgets.QPushButton(self.projectTab)
        self.pushButton.setGeometry(QtCore.QRect(110, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.projectTab)
        self.label.setGeometry(QtCore.QRect(20, 40, 47, 14))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.projectTab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.projectTab)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 47, 14))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.projectTab)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 47, 14))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.projectTab)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 47, 14))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.projectTab, "")
        self.analysisTab = QtWidgets.QWidget()
        self.analysisTab.setObjectName("analysisTab")
        self.pushButton_2 = QtWidgets.QPushButton(self.analysisTab)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 480, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.analysisTab, "")
        self.pluginTab = QtWidgets.QWidget()
        self.pluginTab.setObjectName("pluginTab")
        self.pushButton_3 = QtWidgets.QPushButton(self.pluginTab)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 450, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.pluginTab, "")
        self.PoiTab = QtWidgets.QWidget()
        self.PoiTab.setObjectName("PoiTab")
        self.pushButton_4 = QtWidgets.QPushButton(self.PoiTab)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 430, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.PoiTab, "")
        self.documentationTab = QtWidgets.QWidget()
        self.documentationTab.setObjectName("documentationTab")
        self.pushButton_5 = QtWidgets.QPushButton(self.documentationTab)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 50, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.documentationTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1149, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.projectTab), _translate("MainWindow", "Project"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analysisTab), _translate("MainWindow", "Analysis "))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pluginTab), _translate("MainWindow", "Plugin Management"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PoiTab), _translate("MainWindow", "Points of Interest"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.documentationTab), _translate("MainWindow", "Documentation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
