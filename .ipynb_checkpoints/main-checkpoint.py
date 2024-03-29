
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
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("./service.json")
firebase_admin.initialize_app(cred)
firestore_client = firestore.client()

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
    def loginfunction(self):
        email=self.ui.username.text()
        password=self.ui.password_login.text()
        try:
            auth.sign_in_with_email_and_password(email,password)
            self.appstart()
        except Exception as e:
                print(e)
            

    def createaccfunction(self):
        email = self.ui.email.text()
        name = self.ui.name.text()
        seller_id = self.ui.seller_id.text()

        if self.ui.password.text()==self.ui.cnf_password.text():
            password=self.ui.password.text()
            try:
                print('inside the try block of creating account')
                user = auth.create_user_with_email_and_password(email,password)
                user_id = user['idToken']
                doc_ref=firestore_client.collection("Admins").document(user_id)
                doc_ref.set({
                    "email":email,
                    "name":name,
                    "sellerid":seller_id
                })

                UIFunctions.store_email(email, user_id)
                
            except Exception as e:
                print(e)


    #############################################################################################################################
    # all added station and charger page function
    #############################################################################################################################
    def added_stn_chargers(self, user_id, station_id):
        charger_name = self.ui.charger_name.text()
        charger_id = self.ui.charger_id.text()
        charger_type = self.ui.charger_type.text()
        maximum_current = int(self.ui.maximum_current.text())
        minimum_current = int(self.ui.minimum_current.text())
        voltage = int(self.ui.voltage.text())
        power = int(self.ui.power.text())
        self.ui.stackedWidget.setCurrentWidget(self.ui.added_chargers)

        doc_ref=firestore_client.collection("Admins").document(user_id).collection("Stations").document(station_id).collection("Chargers").document(charger_id)
        doc_ref.set({
            "Charger name": charger_name,
            "Charger type": charger_type,
            "Minimum Current": minimum_current,
            "Maximum Current": maximum_current,
            "Voltage": voltage,
            "Power": power
        })

        self.ui.added_st_btn.clicked.connect(lambda: self.appstart)
        self.ui.add_more_stn_btn.clicked.connect(lambda: self.add_station)

        
    #############################################################################################################################
    # add charger function
    #############################################################################################################################
    def add_another_charger(self, user_id, station_id):

        # extract values
        charger_name = self.ui.charger_name.text()
        charger_id = self.ui.charger_id.text()
        charger_type = self.ui.charger_type.text()
        maximum_current = int(self.ui.maximum_current.text())
        minimum_current = int(self.ui.minimum_current.text())
        voltage = int(self.ui.voltage.text())
        power = int(self.ui.power.text())

        # clear the values
        self.ui.charger_name.clear()
        self.ui.charger_id.clear()
        self.ui.charger_type.clear()
        self.ui.maximum_current.clear()
        self.ui.minimum_current.clear()
        self.ui.voltage.clear()
        self.ui.power.clear()

        doc_ref=firestore_client.collection("Admins").document(user_id).collection("Stations").document(station_id).collection("Chargers").document(charger_id)
        doc_ref.set({
            "Charger name": charger_name,
            "Charger type": charger_type,
            "Minimum Current": minimum_current,
            "Maximum Current": maximum_current,
            "Voltage": voltage,
            "Power": power
        })

        self.ui.add_charger_page_btn.clicked.connect(lambda: self.added_stn_chargers)
        self.ui.add_more_charger_btn.clicked.connect(lambda: self.add_another_charger(user_id, station_id))




    #############################################################################################################################
    # add charger function
    #############################################################################################################################
    def add_chargers_fn(self, user_id):
        station_name = self.ui.station_name.text()
        station_loc = self.ui.station_location.text()
        latitude = float(self.ui.Latitude.text())
        longitude = float(self.ui.longitude.text())

        station_id = self.generate_id()
        print(station_id)

        doc_ref_st=firestore_client.collection("Admins").document(user_id).collection("Stations").document(station_id)
        doc_ref_st.set({
            "Station name": station_name,
            "Station Location": station_loc,
            "Latitude": latitude,
            "Longitude": longitude
        })

        self.ui.stackedWidget.setCurrentWidget(self.ui.add_charger)

        print("inside the add chargers block")

        self.ui.add_charger_page_btn.clicked.connect(lambda: self.added_stn_chargers())
        self.ui.add_more_charger_btn.clicked.connect(lambda: self.add_another_charger(user_id, station_id))

        
        

    #############################################################################################################################
    # unique station id generator
    #############################################################################################################################
    def generate_id(self):
        current_time = datetime.now()
        id_str = str(current_time)
        id_str = self.remove_non_numeric_characters(id_str)
        n = int(id_str)
        fi = format(n, 'x')
        return fi

    def remove_non_numeric_characters(self, input_str):
        return ''.join(char for char in input_str if char.isdigit())
    


    ###############################################################################################################################
    # add station 
    ###############################################################################################################################
    def add_station(self, user_id):
        self.ui.stackedWidget.setCurrentWidget(self.ui.add_station)

        print("inside the add station block")

        self.ui.add_station_page_btn.clicked.connect(lambda: self.add_chargers_fn(user_id))



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
        self.ui.ca_next.clicked.connect(lambda: self.createaccfunction())
        self.ui.add_station_page_btn.clicked.connect(self.add_chargers_fn)

        self.ui.added_st_btn.clicked.connect(self.appstart)
        


        # open application after logging in
        self.ui.loginpg_next_btn.clicked.connect(lambda: self.loginfunction())

        # link main i.e, first page to create account page
        self.ui.create_account_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.creat_account_page))

        # link main i.e, first page to login page
        self.ui.log_in_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login_page))

        # firebaseConfig = {
        #     "apiKey": "AIzaSyCxe5iXVQujXMltkX7Lcc06Xp16qRCzi1Y",
        #     "authDomain": "ev-station-management-e64ee.firebaseapp.com",
        #     "databaseURL": "https://ev-station-management-e64ee.firebaseio.com/",
        #     "projectId": "ev-station-management-e64ee",
        #     "storageBucket": "ev-station-management-e64ee.appspot.com",
        #     "messagingSenderId": "361415870891",
        #     "appId": "1:361415870891:web:173208fcd67f36eea46aee",
        #     "measurementId": "G-9HD0M30NVD",
        #     "databaseURL": ""
        # }

        # firebase = pyrebase.initialize_app(firebaseConfig)
        # auth=firebase.auth()

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