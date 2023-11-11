
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

################################################################################################
# MAP FILE IMPORT
################################################################################################
from camera_and_map.map import MapWindow, MapDialog

################################################################################################
# CAMERA FILE IMPORT
################################################################################################
from camera_and_map.camera import MaincamWindow

################################################################################################
# VIEW MAP FILE IMPORT
################################################################################################
from camera_and_map.view_map import ViewMapWindow, ViewMapDialog

################################################################################################
# LOGIN AND SIGNUP GUI FILE IMPORT
################################################################################################
from ui_main import Ui_StartWindow

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
import firebase_admin
import pyrebase
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("./service.json")
firebase_admin.initialize_app(cred)
# app = firebase_admin.initialize_app()
firestore_client = firestore.client()

class MainWindow(QMainWindow):
    #########################################################################################################
    # MAP LINKING FUNCTION
    #########################################################################################################
    # def maplink(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Map_in_App()
    #     # self.ui.setupUi(self.window)
    #     self.window.show()


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

        # show window
        self.window.show()


    #######################################################################################################
    # FIREBASE AUTHENTICATION
    #######################################################################################################
    def loginfunction(self, auth):
        email=self.ui.username.text()
        password=self.ui.password_login.text()
        try:
            # auth = firebase.auth()
            auth.sign_in_with_email_and_password(email,password)
            self.appstart()
        except:
            print("Couldn't Sign in Please reacheck email or password")
            

    def createaccfunction(self, auth):
        email = self.ui.email.text()
        name = self.ui.name.text()
        seller_id = self.ui.seller_id.text()

        if self.ui.password.text()==self.ui.cnf_password.text():
            password=self.ui.password.text()
            try:
                # auth = firebase.auth()
                print('inside the try block of creating account')
                user = auth.create_user_with_email_and_password(email,password)
                user_id = user['idToken']
                doc_ref=firestore_client.collection("stations").document(user_id)
                doc_ref.set({
                    "email":email,
                    "name":name,
                    "sellerid":seller_id
                })
                # print(user_id)

                # # db = firebase.database()
                # db.child("Sellers").child(user_id).set({"name": name, "seller_id": seller_id , "email": email})
                # # db.child("users").child(email).set({"name": name, "seller_id": seller_id, "email": email })
                # print('the account created for seller_id ' + seller_id)
                # self.appstart()
            except Exception as e:
                print(e)
                # print("This account already exist")
    
    def add_chargers_fn(self, total_ch):
        if total_ch == int(self.ui.no_chargers.text()):
            self.ui.stackedWidget.setCurrentWidget(self.ui.add_charger)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.add_charger)


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
        # self.ui.ca_next.clicked.connect(lambda: self.createaccfunction(auth))
        # self.ui.ca_next.clicked.connect(lambda: login(self))

        self.ui.ca_next.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.add_station))
        self.ui.add_station_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.add_charger))

        t_ch = self.ui.no_chargers.text()
        # print(type(int(t_ch)))
        # total_ch = int(t_ch)

        # while total_ch > 0:
        #     self.ui.add_charger_page_btn.clicked.connect(lambda: self.add_chargers_fn(self, total_ch))
        #     total_ch = total_ch - 1

        self.ui.add_charger_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.added_st_btn.clicked.connect(self.appstart)
        


        # open application after logging in
        self.ui.loginpg_next_btn.clicked.connect(lambda: self.loginfunction(auth))

        # link main i.e, first page to create account page
        self.ui.create_account_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.creat_account_page))

        # link main i.e, first page to login page
        self.ui.log_in_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login_page))

        firebaseConfig = {
            "apiKey": "AIzaSyCxe5iXVQujXMltkX7Lcc06Xp16qRCzi1Y",
            "authDomain": "ev-station-management-e64ee.firebaseapp.com",
            "databaseURL": "https://ev-station-management-e64ee.firebaseio.com/",
            "projectId": "ev-station-management-e64ee",
            "storageBucket": "ev-station-management-e64ee.appspot.com",
            "messagingSenderId": "361415870891",
            "appId": "1:361415870891:web:173208fcd67f36eea46aee",
            "measurementId": "G-9HD0M30NVD",
            "databaseURL": ""
        }

        firebase = pyrebase.initialize_app(firebaseConfig)
        auth=firebase.auth()

        # db = firebase.database()

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