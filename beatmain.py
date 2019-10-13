import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget

# from projectTab import ProjectTab
# from PointsOfInterestTab import PointsOfInterestTab
from DocumentationTab import DocumentationTab
from PluginManagementTab import PluginManagementTab
from projectTab import ProjectTab


def main():
    #initialinze stuff
    app = QApplication([])
    mainWindow = QMainWindow()
    
    tabWidget = QTabWidget()
    tabWidget.addTab(ProjectTab(), "project tab")
   # tabWidget.addTab(AnalysisTab(), "AnalysisTab")
    tabWidget.addTab(PluginManagementTab(), "PluginManagementTab")
   # tabWidget.addTab(PointsOfInterestTab(), "PointsOfInterestTab")
    tabWidget.addTab(DocumentationTab(), "DocumentationTab")

    mainWindow.setCentralWidget(tabWidget)
    mainWindow.show()
    sys.exit(app.exec())

main()