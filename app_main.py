
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from app import Ui_MainWindow

# IMPORT FUNCTIONS
from app_function import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # UIFunctions.home_page_fun(self)

        self.ui.home.clicked.connect(lambda: UIFunctions.home_page_fun(self))

        # PAGE 2
        self.ui.stations.clicked.connect(lambda: UIFunctions.stations_page_fun(self))

        # PAGE 3
        self.ui.report.clicked.connect(lambda: UIFunctions.report_page_fun(self))

        #
        # self.ui.security.clicked.connect(lambda: UIFunctions.security_page_fun(self))

        # PAGE 2
        self.ui.my_account.clicked.connect(lambda: UIFunctions.account_page_fun(self))

        # PAGE 3
        self.ui.settings.clicked.connect(lambda: UIFunctions.settings_page_fun(self))

        #
        self.ui.About.clicked.connect(lambda: UIFunctions.about_page_fun(self))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(1400, 900)
    sys.exit(app.exec_())
