import sys
import r2pipe
import pymongo
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QFileDialog, QSplitter, QHBoxLayout, QFrame, QTabWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore

from analysisTab import AnalysisTab
from projectTab import ProjectTab


def main():
    #initialinze stuff
    app = QApplication([])
    mainWindow = QMainWindow()
    
    tabWidget = QTabWidget()
    tabWidget.addTab(ProjectTab(), "project tab")
    tabWidget.addTab(AnalysisTab(), "AnalysisTab")
#     tabWidget.addTab(PluginManagementTab(), "PluginManagementTab")
#     tabWidget.addTab(PointsOfInterestTab(), "PointsOfInterestTab")
#     tabWidget.addTab(DocumentationTab(), "DocumentationTab")

    mainWindow.setCentralWidget(tabWidget)
    mainWindow.show()
    sys.exit(app.exec())
    
    
main()