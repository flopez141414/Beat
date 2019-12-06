#!/usr/bin/env python3
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QFileDialog, QSplitter, \
    QHBoxLayout, QFrame, QGridLayout, QTabWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QListWidget, QTextEdit
import pymongo
import r2pipe


class PointsOfInterestTab(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QGridLayout()
        leftLayout = QGridLayout()
        rightLayout = QGridLayout()

        mainlayout.addLayout(leftLayout, 1, 0, 6, 1)
        mainlayout.addLayout(rightLayout, 1, 1, 6, 5)

        # Top layout elements

        # Left panel
        searchBox = QLineEdit()
        newButtonPOI = QPushButton('New')
        poiList = QListWidget()
        leftPanelLabel = QLabel('Points of Interest View')
        leftPanelLabel.setAlignment(Qt.AlignCenter)
#         leftPanelLabel.setStyleSheet("background-color: rgba(173,216,230 ,1 )")
        leftPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))

        leftLayout.addWidget(leftPanelLabel, 0, 0, 1, 5)
        leftLayout.addWidget(poiList, 2, 0, 1, 5)
        leftLayout.addWidget(searchBox, 1, 0, 1, 5) # l , r,
        leftLayout.addWidget(newButtonPOI, 11, 1)

        # Right panel
        pluginDropdown = QComboBox()
        poiType = QComboBox()
        delButtonPOI = QPushButton('Delete')
        saveButtonPOI = QPushButton('Save')

        rightPanelLabel = QLabel('Detailed Point of Interest View')
#         rightPanelLabel.setStyleSheet("background-color: rgba(173,216,230 ,1 )")
        rightPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        pluginLabel = QLabel('Plugin')
        POILabel = QLabel('Point of Interest Type')

        rightPanelLabel.setAlignment(Qt.AlignCenter)
        pluginLabel.setAlignment(Qt.AlignLeft)
        POILabel.setAlignment(Qt.AlignCenter)

        poiContentArea = QTextEdit()
        rightLayout.addWidget(rightPanelLabel, 0, 1, 1, 5)
        rightLayout.addWidget(pluginDropdown, 0, 1, 2, 2)
        rightLayout.addWidget(pluginLabel, 0, 0, 0, 1)
        rightLayout.addWidget(POILabel, 2, 0, 7, 7)

        rightLayout.addWidget(poiContentArea, 3, 0, 7, 8)

        rightLayout.addWidget(delButtonPOI, 11, 1)
        rightLayout.addWidget(saveButtonPOI, 11, 7)

        button = QPushButton("My Button")
        button.clicked.connect(self.clickEvent)
        self.setLayout(mainlayout)

    def clickEvent(self):
        print("Clicked")