from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QTextEdit, QLineEdit, QListWidget
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QTextEdit, QLineEdit, QListWidget


class ProjectTab(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QGridLayout()
        leftLayout = QGridLayout()
        rightLayout = QGridLayout()
        mainlayout.addLayout(leftLayout, 1, 0, 6, 1)
        mainlayout.addLayout(rightLayout, 1, 1, 6, 1)

        # Left panel
        searchBox = QLineEdit()
        searchButton = QPushButton('Search')
        newButton = QPushButton('New')
        searchList = QListWidget()
        leftPanelLabel = QLabel('Project View')
        leftPanelLabel.setAlignment(Qt.AlignCenter)

        leftLayout.addWidget(leftPanelLabel, 0, 0, 1, 5)
        leftLayout.addWidget(searchBox, 1, 0, 1, 3)
        leftLayout.addWidget(searchButton, 1, 4, 1, 1)
        leftLayout.addWidget(searchList, 2, 0, 1, 5)
        leftLayout.addWidget(newButton, 6, 0)

        # Right panel
        rightPanelLabel = QLabel('Detailed Project View')
        rightPanelLabel.setAlignment(Qt.AlignCenter)
        projNameArea = QTextEdit()
        projDescriptionArea = QTextEdit()
        binaryFilePath = QTextEdit()
        binaryFileProp = QTextEdit()
        browseButton = QPushButton('Browse')


        rightLayout.addWidget(rightPanelLabel, 0, 0, 1, 10)
        rightLayout.addWidget(projNameArea, 1, 2, 10, 2)
        rightLayout.addWidget(projDescriptionArea, 2, 2, 10, 2)
        rightLayout.addWidget(binaryFilePath, 4, 2, 10, 2)
        rightLayout.addWidget(binaryFileProp, 5, 2, 10, 2)
        rightLayout.addWidget(browseButton, 3, 6)
        rightLayout.addWidget(QLabel('Project Name'), 1, 1, 1, 1)
        rightLayout.addWidget(QLabel('Project Description'), 2, 1, 1, 1)
        rightLayout.addWidget(QLabel('Binary File Path'), 4, 1, 1, 1)
        rightLayout.addWidget(QLabel('Binary File Properties'), 5, 1, 1, 1)

        deleteButton = QPushButton('Delete')
        saveButton = QPushButton('Save')
        rightLayout.addWidget(saveButton, 11, 7)
        rightLayout.addWidget(deleteButton, 11, 1)

        button = QPushButton("My Button")
        button.clicked.connect(self.clickEvent)
        self.setLayout(mainlayout)

    def clickEvent(self):
        print("Clicked")