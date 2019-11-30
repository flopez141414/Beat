import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtCore import *

app = QApplication(sys.argv)
web = QWebView()
web.settings().setAttribute(QWebSettings.PluginsEnabled, True)
web.show()
print("line before path")
web.load(QUrl('file:///C:/Users/begv1/Desktop/Beat-Team-12/documentation/BEAT-doc.pdf')) # Path to actual file.
print("line after path")
sys.exit(app.exec_())