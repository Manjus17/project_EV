# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startBmWhhR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import qrc_pyfiles.logo_rc as logo_rc
import qrc_pyfiles.google_rc as google_rc
import qrc_pyfiles.apple_rc as apple_rc
import qrc_pyfiles.add_rc as add_rc
import qrc_pyfiles.next_rc as next_rc
import qrc_pyfiles.log_in_rc as log_in_rc
import qrc_pyfiles.sign_in_rc as sign_in_rc

class Ui_StartWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(844, 696)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo_frame = QFrame(self.frame)
        self.logo_frame.setObjectName(u"logo_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo_frame.sizePolicy().hasHeightForWidth())
        self.logo_frame.setSizePolicy(sizePolicy1)
        self.logo_frame.setMinimumSize(QSize(400, 0))
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.logo_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_4 = QFrame(self.logo_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.logo_label = QLabel(self.frame_4)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setMaximumSize(QSize(600, 16777215))
        self.logo_label.setStyleSheet(u"border-image: url(:/newPrefix/image1.png);")

        self.gridLayout_3.addWidget(self.logo_label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.logo_frame)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMinimumSize(QSize(400, 0))
        self.frame_3.setMaximumSize(QSize(700, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setMinimumSize(QSize(400, 0))
        self.frame_5.setMaximumSize(QSize(600, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_6 = QGridLayout(self.page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.first_right_frame = QFrame(self.page)
        self.first_right_frame.setObjectName(u"first_right_frame")
        self.first_right_frame.setFrameShape(QFrame.StyledPanel)
        self.first_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.first_right_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_7 = QFrame(self.first_right_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(300, 200))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 311, 151))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 40pt \"Calibri\";")
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.frame_7, 0, Qt.AlignBottom)

        self.frame_8 = QFrame(self.first_right_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, -1, 0)
        self.create_account_button = QPushButton(self.frame_8)
        self.create_account_button.setObjectName(u"create_account_button")
        self.create_account_button.setMinimumSize(QSize(100, 55))
        self.create_account_button.setMaximumSize(QSize(250, 16777215))
        self.create_account_button.setStyleSheet(u"border-image: url(:/newPrefix/create_account.png);")

        self.verticalLayout_2.addWidget(self.create_account_button)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.login_label = QLabel(self.frame_9)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";")

        self.horizontalLayout_2.addWidget(self.login_label)

        self.log_in_button = QPushButton(self.frame_9)
        self.log_in_button.setObjectName(u"log_in_button")
        self.log_in_button.setMinimumSize(QSize(110, 60))
        self.log_in_button.setMaximumSize(QSize(100, 16777215))
        self.log_in_button.setStyleSheet(u"border-image: url(:/newPrefix/button_2.png);")

        self.horizontalLayout_2.addWidget(self.log_in_button, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame_8, 0, Qt.AlignTop)


        self.gridLayout_6.addWidget(self.first_right_frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.creat_account_page = QWidget()
        self.creat_account_page.setObjectName(u"creat_account_page")
        self.gridLayout_7 = QGridLayout(self.creat_account_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_10 = QFrame(self.creat_account_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_13)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 60))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.create_account_label = QLabel(self.frame_15)
        self.create_account_label.setObjectName(u"create_account_label")
        self.create_account_label.setGeometry(QRect(0, 0, 338, 60))
        self.create_account_label.setMinimumSize(QSize(0, 60))
        self.create_account_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 26pt \"MS Shell Dlg 2\";\n"
"")
        self.create_account_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.frame_15, 0, Qt.AlignTop)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.name = QLineEdit(self.frame_16)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(0, 60))
        self.name.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 6px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.name)

        self.email = QLineEdit(self.frame_16)
        self.email.setObjectName(u"email")
        self.email.setMinimumSize(QSize(0, 60))
        self.email.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 6px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.email)

        self.seller_id = QLineEdit(self.frame_16)
        self.seller_id.setObjectName(u"seller_id")
        self.seller_id.setMinimumSize(QSize(0, 60))
        self.seller_id.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 6px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.seller_id)

        self.password = QLineEdit(self.frame_16)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 60))
        self.password.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 6px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.password)

        self.cnf_password = QLineEdit(self.frame_16)
        self.cnf_password.setObjectName(u"cnf_password")
        self.cnf_password.setMinimumSize(QSize(0, 60))
        self.cnf_password.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 6px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.cnf_password)


        self.verticalLayout_3.addWidget(self.frame_16)


        self.verticalLayout_4.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_4.addWidget(self.label_4, 0, Qt.AlignRight)

        self.add_image_btn = QPushButton(self.frame_14)
        self.add_image_btn.setObjectName(u"add_image_btn")
        self.add_image_btn.setMinimumSize(QSize(30, 30))
        self.add_image_btn.setStyleSheet(u"border-image: url(:/newPrefix/button_4.png);")

        self.horizontalLayout_4.addWidget(self.add_image_btn, 0, Qt.AlignLeft)

        self.ca_next = QPushButton(self.frame_14)
        self.ca_next.setObjectName(u"ca_next")
        self.ca_next.setMinimumSize(QSize(110, 80))
        self.ca_next.setStyleSheet(u"border-image: url(:/newPrefix/button_1.png);")

        self.horizontalLayout_4.addWidget(self.ca_next)


        self.verticalLayout_4.addWidget(self.frame_14)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"border-top: 2px solid white;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.apple_btn = QPushButton(self.frame_12)
        self.apple_btn.setObjectName(u"apple_btn")
        self.apple_btn.setMinimumSize(QSize(0, 45))
        self.apple_btn.setMaximumSize(QSize(45, 16777215))
        self.apple_btn.setStyleSheet(u"border-image: url(:/newPrefix/apple.png);")

        self.horizontalLayout_3.addWidget(self.apple_btn)

        self.google_btn = QPushButton(self.frame_12)
        self.google_btn.setObjectName(u"google_btn")
        self.google_btn.setMinimumSize(QSize(0, 40))
        self.google_btn.setMaximumSize(QSize(40, 16777215))
        self.google_btn.setStyleSheet(u"border-image: url(:/newPrefix/google.png);")

        self.horizontalLayout_3.addWidget(self.google_btn)


        self.verticalLayout_4.addWidget(self.frame_12)


        self.verticalLayout_5.addWidget(self.frame_11)


        self.gridLayout_7.addWidget(self.frame_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.creat_account_page)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.gridLayout_8 = QGridLayout(self.login_page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_17 = QFrame(self.login_page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_17)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 70))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.login_label_2 = QLabel(self.frame_18)
        self.login_label_2.setObjectName(u"login_label_2")
        self.login_label_2.setGeometry(QRect(0, 0, 342, 70))
        self.login_label_2.setMinimumSize(QSize(0, 70))
        self.login_label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 26pt \"MS Shell Dlg 2\";")
        self.login_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.frame_18, 0, Qt.AlignBottom)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy1.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy1)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_19)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 30)
        self.username = QLineEdit(self.frame_19)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 70))
        self.username.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_8.addWidget(self.username)

        self.password_login = QLineEdit(self.frame_19)
        self.password_login.setObjectName(u"password_login")
        self.password_login.setMinimumSize(QSize(0, 70))
        self.password_login.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_8.addWidget(self.password_login)


        self.verticalLayout_7.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(200, 80))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_20)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.loginpg_next_btn = QPushButton(self.frame_20)
        self.loginpg_next_btn.setObjectName(u"loginpg_next_btn")
        self.loginpg_next_btn.setMinimumSize(QSize(110, 75))
        self.loginpg_next_btn.setMaximumSize(QSize(180, 120))
        self.loginpg_next_btn.setStyleSheet(u"border-image: url(:/newPrefix/button_1.png);")

        self.gridLayout_9.addWidget(self.loginpg_next_btn, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_20, 0, Qt.AlignTop)


        self.gridLayout_8.addWidget(self.frame_17, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.login_page)
        self.add_station = QWidget()
        self.add_station.setObjectName(u"add_station")
        self.gridLayout_10 = QGridLayout(self.add_station)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_2 = QFrame(self.add_station)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 120))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 26pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_21 = QFrame(self.frame_2)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_21)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.station_name = QLineEdit(self.frame_21)
        self.station_name.setObjectName(u"station_name")
        self.station_name.setMinimumSize(QSize(120, 60))
        self.station_name.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_10.addWidget(self.station_name)

        self.station_location = QLineEdit(self.frame_21)
        self.station_location.setObjectName(u"station_location")
        self.station_location.setMinimumSize(QSize(120, 65))
        self.station_location.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_10.addWidget(self.station_location)

        self.Latitude = QLineEdit(self.frame_21)
        self.Latitude.setObjectName(u"Latitude")
        self.Latitude.setMinimumSize(QSize(120, 65))
        self.Latitude.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_10.addWidget(self.Latitude)

        self.longitude = QLineEdit(self.frame_21)
        self.longitude.setObjectName(u"longitude")
        self.longitude.setMinimumSize(QSize(120, 65))
        self.longitude.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_10.addWidget(self.longitude)

        self.no_chargers = QLineEdit(self.frame_21)
        self.no_chargers.setObjectName(u"no_chargers")
        self.no_chargers.setMinimumSize(QSize(120, 65))
        self.no_chargers.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_10.addWidget(self.no_chargers)


        self.verticalLayout_9.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 100))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_22)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.add_station_page_btn = QPushButton(self.frame_22)
        self.add_station_page_btn.setObjectName(u"add_station_page_btn")
        self.add_station_page_btn.setMinimumSize(QSize(0, 0))
        self.add_station_page_btn.setMaximumSize(QSize(120, 55))
        self.add_station_page_btn.setStyleSheet(u"padding: 3px 5px;\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 10;\n"
"font: 14pt \"Consolas\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_12.addWidget(self.add_station_page_btn, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_22)


        self.gridLayout_10.addWidget(self.frame_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.add_station)
        self.add_charger = QWidget()
        self.add_charger.setObjectName(u"add_charger")
        self.gridLayout_13 = QGridLayout(self.add_charger)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_23 = QFrame(self.add_charger)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_23)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 120))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_24)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_3 = QLabel(self.frame_24)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 26pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_3, 0, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_24, 0, Qt.AlignTop)

        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setMaximumSize(QSize(16777214, 16777215))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_25)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.charger_name = QLineEdit(self.frame_25)
        self.charger_name.setObjectName(u"charger_name")
        self.charger_name.setMinimumSize(QSize(0, 55))
        self.charger_name.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_12.addWidget(self.charger_name)

        self.charger_type = QLineEdit(self.frame_25)
        self.charger_type.setObjectName(u"charger_type")
        self.charger_type.setMinimumSize(QSize(0, 55))
        self.charger_type.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_12.addWidget(self.charger_type)

        self.charger_id = QLineEdit(self.frame_25)
        self.charger_id.setObjectName(u"charger_id")
        self.charger_id.setMinimumSize(QSize(0, 55))
        self.charger_id.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_12.addWidget(self.charger_id)

        self.minimum_current = QLineEdit(self.frame_25)
        self.minimum_current.setObjectName(u"minimum_current")
        self.minimum_current.setMinimumSize(QSize(0, 55))
        self.minimum_current.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_12.addWidget(self.minimum_current)

        self.maximum_current = QLineEdit(self.frame_25)
        self.maximum_current.setObjectName(u"maximum_current")
        self.maximum_current.setMinimumSize(QSize(0, 55))
        self.maximum_current.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_12.addWidget(self.maximum_current)

        self.voltage = QLineEdit(self.frame_25)
        self.voltage.setObjectName(u"voltage")
        self.voltage.setMinimumSize(QSize(0, 55))
        self.voltage.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_12.addWidget(self.voltage)

        self.power = QLineEdit(self.frame_25)
        self.power.setObjectName(u"power")
        self.power.setMinimumSize(QSize(0, 55))
        self.power.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_12.addWidget(self.power)


        self.verticalLayout_11.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_23)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 100))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_26)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.add_charger_page_btn = QPushButton(self.frame_26)
        self.add_charger_page_btn.setObjectName(u"add_charger_page_btn")
        self.add_charger_page_btn.setMaximumSize(QSize(250, 60))
        self.add_charger_page_btn.setStyleSheet(u"padding: 3px 5px;\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 10;\n"
"font: 14pt \"Consolas\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_15.addWidget(self.add_charger_page_btn, 0, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_26, 0, Qt.AlignBottom)


        self.gridLayout_13.addWidget(self.frame_23, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.add_charger)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_16 = QGridLayout(self.page_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_27 = QFrame(self.page_3)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_27)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_30 = QFrame(self.frame_27)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 120))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_30)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_5 = QLabel(self.frame_30)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 26pt \"MS Shell Dlg 2\";")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_5, 0, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_30, 0, Qt.AlignTop)

        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_28)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.station_frame = QFrame(self.frame_28)
        self.station_frame.setObjectName(u"station_frame")
        self.station_frame.setMaximumSize(QSize(250, 100))
        self.station_frame.setStyleSheet(u"padding: 3px 5px;\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 10;\n"
"font: 8pt \"Consolas\";\n"
"color: rgb(255, 255, 255);")
        self.station_frame.setFrameShape(QFrame.StyledPanel)
        self.station_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.station_frame)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setSizeConstraint(QLayout.SetFixedSize)
        self.station_n = QLabel(self.station_frame)
        self.station_n.setObjectName(u"station_n")

        self.gridLayout_19.addWidget(self.station_n, 0, 0, 1, 1)

        self.station_value = QLabel(self.station_frame)
        self.station_value.setObjectName(u"station_value")

        self.gridLayout_19.addWidget(self.station_value, 0, 1, 1, 1)

        self.charger_n = QLabel(self.station_frame)
        self.charger_n.setObjectName(u"charger_n")

        self.gridLayout_19.addWidget(self.charger_n, 1, 0, 1, 1)

        self.charger_value = QLabel(self.station_frame)
        self.charger_value.setObjectName(u"charger_value")

        self.gridLayout_19.addWidget(self.charger_value, 1, 1, 1, 1)


        self.gridLayout_20.addWidget(self.station_frame, 0, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 100))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_29)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.added_st_btn = QPushButton(self.frame_29)
        self.added_st_btn.setObjectName(u"added_st_btn")
        self.added_st_btn.setMaximumSize(QSize(120, 50))
        self.added_st_btn.setStyleSheet(u"padding: 3px 5px;\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 10;\n"
"font: 14pt \"Consolas\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_18.addWidget(self.added_st_btn, 0, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_29, 0, Qt.AlignBottom)


        self.gridLayout_16.addWidget(self.frame_27, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_5, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Plug Into Better", None))
        self.create_account_button.setText("")
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"Already have an account", None))
        self.log_in_button.setText("")
        self.create_account_label.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.seller_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seller Id", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.cnf_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Add Image", None))
        self.add_image_btn.setText("")
        self.ca_next.setText("")
        self.apple_btn.setText("")
        self.google_btn.setText("")
        self.login_label_2.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginpg_next_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add Station", None))
        self.station_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Station Name", None))
        self.station_location.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Station Location", None))
        self.Latitude.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.longitude.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.no_chargers.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Number of Chargers in the station", None))
        self.add_station_page_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Add charger", None))
        self.charger_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chrager Name", None))
        self.charger_type.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Charger Type", None))
        self.charger_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Charger Id", None))
        self.minimum_current.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Minimum Current", None))
        self.maximum_current.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Maximum Current", None))
        self.voltage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.power.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Power in kWh", None))
        self.add_charger_page_btn.setText(QCoreApplication.translate("MainWindow", u"Add charger", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Added Stations", None))
        self.station_n.setText(QCoreApplication.translate("MainWindow", u"Station 1", None))
        self.station_value.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.charger_n.setText(QCoreApplication.translate("MainWindow", u"Chargers", None))
        self.charger_value.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.added_st_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

