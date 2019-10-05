import sys
import r2pipe
import pymongo
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QFileDialog, QSplitter, QHBoxLayout, QFrame, QGridLayout, QTabWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore

class ProjectTab(QWidget):
    def __init__(self):
        super().__init__()
        
        mainlayout = QGridLayout()
        leftLayout = QGridLayout()
        rightLayout = QGridLayout()
        mainlayout.addLayout(leftLayout, 0, 0, 6, 1)
        mainlayout.addLayout(rightLayout, 0, 1, 6, 5) 
        leftLayout.addWidget(QLabel('left'))
        rightLayout.addWidget(QLabel('left'))

        self.setLayout(mainlayout)
    