import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget

from functions.PluginManagementTab import PluginManagementTab
from functions.tabs.PointsOfInterestTab import PointsOfInterestTab



def main():
    #initialinze stuff
    app = QApplication([])
    mainWindow = QMainWindow()

    tabWidget = QTabWidget()
    #tabWidget.addTab(ProjectTab(), "project tab")
   # tabWidget.addTab(AnalysisTab(), "AnalysisTab")
    #tabWidget.addTab(PluginManagementTab(), "PluginManagementTab")
    tabWidget.addTab(PointsOfInterestTab(), "PointsOfInterestTab")
   # tabWidget.addTab(DocumentationTab(), "DocumentationTab")

    mainWindow.setWindowTitle("BEAT: Behavior Extraction and Analysis Tool")
    mainWindow.setCentralWidget(tabWidget)
    mainWindow.show()
    sys.exit(app.exec())
    
    
main()