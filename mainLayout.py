from PyQt5.QtWidgets import QDesktopWidget, QTabWidget, QMainWindow


from tabs import documentation_tab



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.tabBuilder()
        self.buildWindow()

    def tabBuilder(self):
        # TODO: Add tab implementations
        self.tabs = QTabWidget()
        self.tabs.addTab(documentation_tab(), "Documentation")

    def buildWindow(self):
        # Tabs
        self.setCentralWidget(self.tabs)

        # Setup
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        #qtRectangle.setWidth(constants.WIDTH)
        #qtRectangle.setHeight(constants.HEIGHT)
        qtRectangle.moveCenter(centerPoint)
       # self.setWindowTitle(constants.SYSTEM_TITLE)
        self.setGeometry(qtRectangle)
        self.show()