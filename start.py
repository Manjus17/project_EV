
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

################################################################################################
# LOGIN AND SIGNUP GUI FILE IMPORT
################################################################################################
from ui_start import Ui_StartWindow

################################################################################################
# APPLICATION PAGE GUI FILE IMPORT
################################################################################################
from app import Ui_MainWindow

################################################################################################
# IMPORT APP FUNCTIONS
################################################################################################
from app_function import *


# import total_chargers and in_use_cahrgers
from app import total_chargers, in_use_chargers

class MainWindow(QMainWindow):
    ################################################################################################
    # APPLICATION PAGE 
    ################################################################################################
    def appstart(self):
        print('in appstart')
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        # hide the login and signup window as the application window is open
        MainWindow.hide(self)

        # normal window size
        self.window.resize(1400, 900)

        # deaclaring the scope of the variable
        global total_chargers
        global in_use_chargers

        # setting the range of the progress bar
        self.ui.prg_in.rpb_setRange(0, 100)
        self.ui.prg_in.rpb_setBarStyle('Pizza')  # progress bar style

        # storing value returned from progress bar function
        value = UIFunctions.progress_bar_value(in_use_chargers, total_chargers)
        self.ui.prg_in.rpb_setValue(value) # set the returned value in progress bar

        # calculation of available chargers 
        Available_chargers = UIFunctions.available(total_chargers, in_use_chargers)
        self.ui.lcdNumber_3.setProperty("intValue", Available_chargers) # add value to lcd display
        
        # Home page
        self.ui.home.clicked.connect(lambda: UIFunctions.home_page_fun(self))

        # stations page
        self.ui.stations.clicked.connect(lambda: UIFunctions.stations_page_fun(self))

        # report page
        self.ui.report.clicked.connect(lambda: UIFunctions.report_page_fun(self))

        # my account page
        self.ui.my_account.clicked.connect(lambda: UIFunctions.account_page_fun(self))

        # settings page
        self.ui.settings.clicked.connect(lambda: UIFunctions.settings_page_fun(self))

        # about page
        self.ui.About.clicked.connect(lambda: UIFunctions.about_page_fun(self))

        # show window
        self.window.show()





    ################################################################################################
    # LOGIN AND SIGNUP PAGE
    ################################################################################################
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self)

        # giving window fixed width and height
        self.setFixedHeight(900)
        self.setFixedWidth(1300)

        # open appliction after creating account
        self.ui.pushButton_6.clicked.connect(self.appstart)

        # open application after logging in
        self.ui.pushButton_7.clicked.connect(self.appstart)

        # link main i.e, first page to create account page
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # link main i.e, first page to login page
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##



########################################################################
# EXECUTION 
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.resize(1400, 900)
    sys.exit(app.exec_())