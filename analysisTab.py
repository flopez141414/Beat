import sys
import r2pipe
import pymongo
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QFileDialog, QSplitter, \
    QHBoxLayout, QFrame, QGridLayout, QTabWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QListWidget, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore


class AnalysisTab(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QGridLayout()
        leftLayout = QGridLayout()
        rightLayout = QGridLayout()
        topLayout = QGridLayout()
        mainlayout.addLayout(topLayout, 0, 0, 1, 6)
        mainlayout.addLayout(leftLayout, 1, 0, 6, 1)
        mainlayout.addLayout(rightLayout, 1, 1, 6, 5)

        # Top layout elements
        pluginDropdown = QComboBox()
        runStatic = QPushButton('Run')
        poiDropdown = QComboBox()
        runDynamic = QPushButton('Run')
        stopDynamic = QPushButton('Stop')

        topLayout.addWidget(QLabel('Plugin'), 0, 0)
        topLayout.addWidget(pluginDropdown, 0, 1, 1, 2)
        topLayout.addWidget(QLabel('Static Analysis'), 1, 0)
        topLayout.addWidget(runStatic, 1, 1, 1, 1)
        topLayout.addWidget(QLabel('Point of Interest Type'), 2, 0)
        topLayout.addWidget(poiDropdown, 2, 1, 1, 2)
        topLayout.addWidget(QLabel('Dynamic Analysis'), 1, 5, 1, 1)
        topLayout.addWidget(runDynamic, 1, 6)
        topLayout.addWidget(stopDynamic, 1, 7)
        topLayout.addWidget(QLabel(), 0, 3, 1, 15)

        # Left panel
        searchBox = QLineEdit()
        searchButton = QPushButton('Search')
        poiList = QListWidget()
        leftPanelLabel = QLabel('Point of Interest View')
        leftPanelLabel.setAlignment(Qt.AlignCenter)

        leftLayout.addWidget(leftPanelLabel, 0, 0, 1, 5)
        leftLayout.addWidget(searchBox, 1, 0, 1, 3)
        leftLayout.addWidget(searchButton, 1, 4, 1, 1)
        leftLayout.addWidget(poiList, 2, 0, 1, 5)

        # Right panel
        rightPanelLabel = QLabel('Point of Interest View')
        rightPanelLabel.setAlignment(Qt.AlignCenter)
        poiContentArea = QTextEdit()
        terminal = QTextEdit()
        commentButton = QPushButton('C')
        outputButton = QPushButton('O')
        analysisButton = QPushButton('A')

        rightLayout.addWidget(rightPanelLabel, 0, 0, 1, 10)
        rightLayout.addWidget(poiContentArea, 1, 0, 10, 8)
        rightLayout.addWidget(terminal, 11, 0, 10, 8)
        rightLayout.addWidget(analysisButton, 1, 9)
        rightLayout.addWidget(outputButton, 2, 9)
        rightLayout.addWidget(commentButton, 2, 8)

        button = QPushButton("My Button")
        button.clicked.connect(self.clickEvent)
        self.setLayout(mainlayout)

    def clickEvent(self):
        print("Clicked")
