from PyQt5 import QtCore, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.id_le = QtWidgets.QLineEdit("")
        self.id_le.installEventFilter(self)
        self.dob_le = QtWidgets.QLineEdit()
        btn = QtWidgets.QPushButton(
            text="Enter",
            clicked=self.conversion
        )
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QFormLayout(central_widget)
        lay.addRow("Field 1", self.id_le)
        lay.addRow("Field 2", self.dob_le)
        lay.addRow(btn)

    def eventFilter(self, obj, event):
        if self.id_le == obj and event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Tab:
                QtCore.QTimer.singleShot(0, self.conversion)
        return super(MainWindow, self).eventFilter(obj, event)

    def conversion(self):
        id_value = self.id_le.text()
        if len(id_value) > 7:
            text = id_value[1:7]
            dt = QtCore.QDateTime.fromString(text, "yyddMM")
            if dt.isValid():
                self.dob_le.setText(dt.toString("dd/MM/yyyy"))
                return
        print("Invalid conversion")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())