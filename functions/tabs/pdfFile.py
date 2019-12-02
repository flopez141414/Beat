import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

PDFJS = 'file:///path/to/pdfjs-1.9.426-dist/web/viewer.html'
# PDFJS = 'file:///usr/share/pdf.js/web/viewer.html'
PDF = 'file:///path/to/my/sample.pdf'

class Window(QtWebEngineWidgets.QWebEngineView):
    def __init__(self):
        super(Window, self).__init__()
        self.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (PDFJS, PDF)))

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 50, 800, 600)
    window.show()
    sys.exit(app.exec_())