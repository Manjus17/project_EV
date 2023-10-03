
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_start import Ui_StartWindow
from app import Ui_MainWindow
from app_function import *
# import app_function.total_chargers
from app import total_chargers, in_use_chargers

# IMPORT FUNCTIONS
# from app_function import *

class MainWindow(QMainWindow):
    def appstart(self):
        print('in appstart')
        # MainWindow.hide(MainWindow)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide(self)
        self.window.resize(1400, 900)
        global total_chargers
        global in_use_chargers
        # print(total_chargers)
        self.ui.prg_in.rpb_setRange(0, 100)
        self.ui.prg_in.rpb_setBarStyle('Pizza') 
        value = UIFunctions.progress_bar_value(in_use_chargers, total_chargers)
        self.ui.prg_in.rpb_setValue(value)

        Available_chargers = UIFunctions.available(total_chargers, in_use_chargers)
        self.ui.lcdNumber_3.setProperty("intValue", Available_chargers)
        

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


        # MainWindow.hide()
        self.window.show()


    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self)
        self.setFixedHeight(900)
        self.setFixedWidth(1300)

        # UIFunctions.home_page_fun(self)

        
        self.ui.pushButton_6.clicked.connect(self.appstart)
        self.ui.pushButton_7.clicked.connect(self.appstart)


        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))


        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.resize(1400, 900)
    sys.exit(app.exec_())