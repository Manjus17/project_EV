
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

## ui file is in icons folder named as main.ui

################################################################################################
# MAP FILE IMPORT
################################################################################################
from map import MapWindow, MapDialog

################################################################################################
# CAMERA FILE IMPORT
################################################################################################
from camera import MaincamWindow

################################################################################################
# GUI FILE IMPORT
################################################################################################
from app import Ui_MainWindow

################################################################################################
# VIEW MAP FILE IMPORT
################################################################################################
from view_map import ViewMapWindow, ViewMapDialog

################################################################################################
# IMPORT FUNCTIONS
################################################################################################
from app_function import *


################################################################################################
# import total_chargers and in_use_chargers for progress bar algo
################################################################################################
from app import total_chargers, in_use_chargers, total_capacity, current_soc, power, charging_start_time


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # deaclaring the scope of the variable
        global total_chargers
        global in_use_chargers

        # setting the range of the progress bar
        self.ui.prg_in.rpb_setRange(0, 100)
        self.ui.prg_in.rpb_setBarStyle('Pizza')  # progress bar style

        in_use_progress = [
            {"percentage": 20, "power_use":7.82 },
            {"percentage": 30, "power_use":7.6 },
            {"percentage": 30, "power_use":5.9 },
            {"percentage": 20, "power_use":6.2 }
        ]

        not_in_use_progress = [
            {"percentage": 50, "power_use":8.2 },
            {"percentage": 50, "power_use":5.66 },
        ]

        # storing value returned from progress bar function
        value = UIFunctions.progress_bar_value(in_use_progress, not_in_use_progress)
        self.ui.prg_in.rpb_setValue(value) # set the returned value in progress bar

        # calculation of available chargers 
        Available_chargers = UIFunctions.available(total_chargers, in_use_chargers)
        self.ui.available_chargers_lcdNumber.setProperty("intValue", Available_chargers) # add value to lcd display
        
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

        # connect location button of station 1 with its location passing latitude longitude station name and location as parameters
        self.ui.location1_btn.clicked.connect(lambda: MapWindow.open_map_window(self, 26.8640, 75.8108, "Station 1", "Malaviya National Institute of Technology, jaipur"))

        # connect location button of station 2 with its location passing latitude longitude station name and location as parameters
        self.ui.location2_btn.clicked.connect(lambda: MapWindow.open_map_window(self, 26.8416, 75.8014, "Station 2", "Patrika Gate, Jaipur"))

        # all Managed stations locations to be shown on on the map
        locations = [
            {"name": "Station 1", "lat": 26.8640, "lon": 75.8108, "popup": "Malaviya National Institute of Technology, jaipur"},
            {"name": "Station 2", "lat": 26.8416, "lon": 75.8014, "popup": "Patrika Gate, Jaipur"}
        ]

        # connect the view map button to the map passing the locations
        self.ui.view_map_button.clicked.connect(lambda: ViewMapWindow.open_map_window(self, 26.9124, 75.7873, locations))

        # link camera using opencv
        self.ui.camera1_btn.clicked.connect(lambda: MaincamWindow.open_camera_window(self))
        self.ui.camera2_btn.clicked.connect(lambda: MaincamWindow.open_camera_window(self))

        ecet11 = UIFunctions.calculate_charging_end_time(charging_start_time, current_soc, total_capacity, power)
        self.ui.ecet11_value_label.setText(str(ecet11))


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
    window.resize(1400, 900)
    sys.exit(app.exec_())
