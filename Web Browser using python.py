import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PY-Browser")
        self.setWindowIcon(QIcon("icons/python.gif"))
        self.setGeometry(200, 200, 900, 600)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon("icons/home.png"))
        self.homeButton.setIconSize(QSize(36, 36))
        self.homeButton.clicked.connect(self.homebtn)
        toolbar.addWidget(self.homeButton)

        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("icons/back.png"))
        self.backButton.setIconSize(QSize(36,36))
        self.backButton.clicked.connect(self.backbtn)
        toolbar.addWidget(self.backButton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("icons/forward.png"))
        self.forwardButton.setIconSize(QSize(36, 36))
        self.forwardButton.clicked.connect(self.forwardbtn)
        toolbar.addWidget(self.forwardButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("icons/reload.png"))
        self.reloadButton.setIconSize(QSize(36, 36))
        self.reloadButton.clicked.connect(self.reloadbtn)
        toolbar.addWidget(self.reloadButton)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("Sanserif",18))
        self.addressLineEdit.returnPressed.connect(self.searchbtn)
        toolbar.addWidget(self.addressLineEdit)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon("icons/search.png"))
        self.searchButton.setIconSize(QSize(36, 36))
        self.searchButton.clicked.connect(self.searchbtn)
        toolbar.addWidget(self.searchButton)

        self.webEngineview = QWebEngineView()
        self.setCentralWidget(self.webEngineview)
        initialUrl = 'https://www.google.com/'
        self.addressLineEdit.setText(initialUrl)
        self.webEngineview.load(QUrl(initialUrl))

    def searchbtn(self):
        myurl = self.addressLineEdit.text()
        try:
            url = QUrl(myurl)
            if not url.isValid() or url.scheme() == '':
                url = QUrl('http://' + myurl)
            self.webEngineview.load(url)
        except Exception as e:
            print(f"Error loading URL: {e}")

    def backbtn(self):
        self.webEngineview.back()

    def forwardbtn(self):
        self.webEngineview.forward()

    def reloadbtn(self):
        self.webEngineview.reload()

    def homebtn(self):
        self.webEngineview.load(QUrl('https://www.google.com/'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
