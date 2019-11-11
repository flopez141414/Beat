import sys
import r2pipe
import pymongo

sys.path.append("../DB")
import xmlUploader
# from xmlUploader import uploadXml


from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget
from PyQt5.QtGui import QPalette
from PyQt5.Qt import QColor

from PluginManagementTab import PluginManagementTab
from DocumentationTab import DocumentationTab
from analysisTab import AnalysisTab
from projectTab import ProjectTab
from PointsOfInterestTab import PointsOfInterestTab

def main():
    # initialize stuff
    app = QApplication([])
    mainWindow = QMainWindow()
    
    # dark theme
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53,53,53))
    palette.setColor(QPalette.WindowText, QColor(255,255,255))
    palette.setColor(QPalette.WindowText, QColor(255,255,255))
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, QColor(255,255,255))
    palette.setColor(QPalette.ToolTipText, QColor(255,255,255))
    palette.setColor(QPalette.Text, QColor(255,255,255))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor(255,255,255))
    palette.setColor(QPalette.BrightText, QColor(255,0,0))
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, QColor(0,0,0))
    app.setPalette(palette)

    tabWidget = QTabWidget()
    tabWidget.addTab(ProjectTab(), "Project tab")
    tabWidget.addTab(PluginManagementTab(), "PluginManagementTab")
    tabWidget.addTab(AnalysisTab(), "Analysis Tab")
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
