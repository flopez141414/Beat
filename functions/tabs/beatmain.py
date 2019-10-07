import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget

import r2pipe
import pymongo
from PointsOfInterestTab import PointsOfInterestTab
from DocumentationTab import DocumentationTab
from projectTab import ProjectTab
from analysisTab import AnalysisTab

def main():
    #initialize stuff
    app = QApplication([])
    mainWindow = QMainWindow()

    tabWidget = QTabWidget()
    tabWidget.addTab(ProjectTab(), "project tab")
    tabWidget.addTab(AnalysisTab(), "AnalysisTab")
    #tabWidget.addTab(PluginManagementTab(), "PluginManagementTab")
    tabWidget.addTab(PointsOfInterestTab(), "PointsOfInterestTab")
    tabWidget.addTab(DocumentationTab(), "DocumentationTab")

    mainWindow.setWindowTitle("BEAT: Behavior Extraction and Analysis Tool")
    mainWindow.setCentralWidget(tabWidget)
    mainWindow.show()
    sys.exit(app.exec())
    
    
main()