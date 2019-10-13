import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget

import r2pipe
import pymongo

from PointsOfInterestTab import PointsOfInterestTab
from DocumentationTab import DocumentationTab
from projectTab import ProjectTab
from analysisTab import AnalysisTab
# from PluginManagementTab import PluginManagementTab

def main():
    #initialize stuff
    app = QApplication([])
    mainWindow = QMainWindow()

    tabWidget = QTabWidget()
    tabWidget.addTab(ProjectTab(), "Project tab")
    tabWidget.addTab(AnalysisTab(), "Analysis Tab")
#     tabWidget.addTab(PluginManagementTab(), "PluginManagementTab")
    tabWidget.addTab(PointsOfInterestTab(), "Points Of Interest Tab")
    tabWidget.addTab(DocumentationTab(), "Documentation Tab")

    mainWindow.setWindowTitle("BEAT: Behavior Extraction and Analysis Tool")
    mainWindow.setCentralWidget(tabWidget)
    mainWindow.show()
    sys.exit(app.exec())
    
    
main()