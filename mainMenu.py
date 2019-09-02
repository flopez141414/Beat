import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "BEAT: Behavior Extraction and Analysis Tool"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("icon.png")) # add icon

        self.InitWindow()

    def InitWindow(self):
        mainMenu = self.menuBar() # init menuBar

        projectMenu = mainMenu.addMenu("Project")
        analysisMenu = mainMenu.addMenu("Analysis")
        pluginMenu = mainMenu.addMenu("Plugin Management")
        POImenu = mainMenu.addMenu("Points of Interest")
        docMenu = mainMenu.addMenu("Documentation")


        # QAction to exit using ctrl + E
        #Deje esto aqui nomas para testing, esto agrega opciones para menubar
        #Lo que queremos aser es que los botones de menu bar cambien la vista del panel
        exitButton = QAction(QIcon("exit.png"), 'Exit', self) # image name, label, self
        exitButton.setShortcut("Ctrl+E")
        exitButton.setStatusTip("Exit Application")
        exitButton.triggered.connect(self.close)
        projectMenu.addAction(exitButton)


        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())