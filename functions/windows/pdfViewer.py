import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

app = QApplication(sys.argv)
web = QWebView()
web.settings().setAttribute(QWebSettings.PluginsEnabled, True)
web.load(QUrl("chapter1.pdf"))
web.show()
app.exec_()
