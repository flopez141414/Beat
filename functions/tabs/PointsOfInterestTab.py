import sys
import r2pipe
import pymongo
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QFileDialog, QSplitter, \
    QHBoxLayout, QFrame, QGridLayout, QTabWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QListWidget, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore


class PointsOfInterestTab(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QGridLayout()
        leftLayout = QGridLayout()
        rightLayout = QGridLayout()

        mainlayout.addLayout(leftLayout, 1, 0, 6, 1)
        mainlayout.addLayout(rightLayout, 1, 1, 6, 1)

        # Top layout elements

        # Left panel
        searchBox = QLineEdit()
        newButtonPOI = QPushButton('New')
        poiList = QListWidget()
        leftPanelLabel = QLabel('Points of Interest View')
        leftPanelLabel.setAlignment(Qt.AlignCenter)

        leftLayout.addWidget(leftPanelLabel, 0, 0, 1, 5)
        leftLayout.addWidget(poiList, 2, 0, 1, 5)
        leftLayout.addWidget(searchBox, 1, 0, 1, 4) # l , r,
        leftLayout.addWidget(newButtonPOI, 11, 1)

        # Right panel
        pluginDropdown = QComboBox()
        delButtonPOI = QPushButton('Delete')
        saveButtonPOI = QPushButton('Save')

        rightPanelLabel = QLabel('Detailed Point of Interest View')
        pluginLabel = QLabel('Plugin')
        POILabel = QLabel('asdg')

        rightPanelLabel.setAlignment(Qt.AlignCenter)
        pluginLabel.setAlignment(Qt.AlignLeft)
        POILabel.setAlignment(Qt.AlignCenter)

        poiContentArea = QTextEdit()
        rightLayout.addWidget(pluginDropdown, 0, 1, 1, 2)
        rightLayout.addWidget(rightPanelLabel, 0, 0, 1, 1)
       # rightLayout.addWidget(pluginLabel, 0, 0, 0, 1)
        rightLayout.addWidget(POILabel, 0, 0, 7, 7)

        rightLayout.addWidget(poiContentArea, 1, 0, 10, 8)

        rightLayout.addWidget(delButtonPOI, 11, 1)
        rightLayout.addWidget(saveButtonPOI, 11, 7)

        button = QPushButton("My Button")
        button.clicked.connect(self.clickEvent)
        self.setLayout(mainlayout)

    def clickEvent(self):
        print("Clicked")