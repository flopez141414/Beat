#code generated by QtCreator:
from PySide import QtCore, QtGui
import sys
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.webView = QtWebKit.QWebView(self.centralWidget)
        self.webView.setGeometry(QtCore.QRect(10, 20, 380, 270))
        self.webView.setUrl(QtCore.QUrl("file:///C:/Users/Rocio/Desktop/extra%20credit.pdf"))
        self.webView.setObjectName("webView")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit

# My code:
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    APP = QtGui.QApplication(sys.argv)
    MW = MainWindow()
    MW.show()

    sys.exit(APP.exec_())