import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtCore import *

app = QApplication(sys.argv)
web = QWebView()
web.settings().setAttribute(QWebSettings.PluginsEnabled, True)
web.show()
web.load(QUrl('file:///C:\Users\begv1\Desktop\Beat-Team-12\documentation\BEAT-doc.df)) # Path to actual file.
sys.exit(app.exec_())