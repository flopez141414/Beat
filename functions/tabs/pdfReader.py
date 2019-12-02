import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

app = QApplication(sys.argv)
web = QWebView()
web.settings().setAttribute(QWebSettings.PluginsEnabled, True)
web.load(QUrl("BEAT-doc.pdf"))
web.show()
app.exec_()