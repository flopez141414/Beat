import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget

import r2pipe
import pymongo

from PluginManagementTab import PluginManagementTab
from DocumentationTab import DocumentationTab
from analysisTab import AnalysisTab
from projectTab import ProjectTab
from PointsOfInterestTab import PointsOfInterestTab
# import functions.tabs.PluginManagementTab

#from PluginManagementTab import PluginManagementTab
# from functions.tabs.DocumentationTab import DocumentationTab
# from functions.tabs.analysisTab import AnalysisTab
# from functions.tabs.projectTab import ProjectTab


def main():
    # initialize stuff
    app = QApplication([])
    mainWindow = QMainWindow()

    tabWidget = QTabWidget()
    tabWidget.addTab(ProjectTab(), "Project tab")
    tabWidget.addTab(AnalysisTab(), "Analysis Tab")
    tabWidget.addTab(PluginManagementTab(), "PluginManagementTab")
    tabWidget.addTab(PointsOfInterestTab(), "Points Of Interest Tab")
    tabWidget.addTab(DocumentationTab(), "Documentation Tab")

    mainWindow.setWindowTitle("BEAT: Behavior Extraction and Analysis Tool")
    mainWindow.setWindowIcon(QtGui.QIcon('BEAT-logo.png'))
    mainWindow.setFont(QtGui.QFont('Helvetica', 12))
    mainWindow.setAutoFillBackground(True)
    mainWindow.setCentralWidget(tabWidget)
    mainWindow.show()
    sys.exit(app.exec())


main()
