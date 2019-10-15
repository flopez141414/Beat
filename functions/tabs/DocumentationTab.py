import sys
import r2pipe
import pymongo
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QFileDialog, QSplitter, \
    QHBoxLayout, QFrame, QGridLayout, QTabWidget, QVBoxLayout, QHBoxLayout, QListWidget, QComboBox, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore, QtGui


class DocumentationTab(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QGridLayout()
        leftLayout = QGridLayout()
        rightLayout = QGridLayout()

        mainlayout.addLayout(leftLayout, 1, 0, 6, 1)
        mainlayout.addLayout(rightLayout, 1, 1, 6, 8)

        # Left panel
        searchBox = QLineEdit()

        poiList = QListWidget()
        leftPanelLabel = QLabel('Document View')
        leftPanelLabel.setAlignment(Qt.AlignCenter)
        leftPanelLabel.setStyleSheet("background-color: rgba(173,216,230 ,1 )")
        leftPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))

        leftLayout.addWidget(leftPanelLabel, 0, 0, 1, 5)
        leftLayout.addWidget(searchBox, 1, 0, 1, 3)

        leftLayout.addWidget(poiList, 2, 0, 1, 5)

        # Right panel
        rightPanelLabel = QLabel('Detail Document View')
        rightPanelLabel.setAlignment(Qt.AlignCenter)
        rightPanelLabel.setStyleSheet("background-color: rgba(173,216,230 ,1 )")
        rightPanelLabel.setFont(QtGui.QFont('Arial', 12, weight=QtGui.QFont().Bold))
        poiContentArea = QTextEdit()
        rightLayout.addWidget(rightPanelLabel, 0, 0)
        rightLayout.addWidget(poiContentArea, 1, 0, 10, 8)
        button = QPushButton("My Button")
        button.clicked.connect(self.clickEvent)
        self.setLayout(mainlayout)

    def clickEvent(self):
        print("Clicked")