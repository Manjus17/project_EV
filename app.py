# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmQhmHb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import account_rc
import plug_rc
import down_rc
import menu_rc
import noti_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(894, 544)
        MainWindow.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menu = QPushButton(self.frame)
        self.menu.setObjectName(u"menu")
        icon = QIcon()
        icon.addFile(u":/newPrefix/\ud83e\udd86 icon _Bars_.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.menu)

        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"padding-bottom: 2px;")

        self.horizontalLayout_3.addWidget(self.title, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.notification = QPushButton(self.frame_2)
        self.notification.setObjectName(u"notification")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/\ud83e\udd86 icon _bell_.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notification.setIcon(icon1)
        self.notification.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.notification)

        self.account = QPushButton(self.frame_2)
        self.account.setObjectName(u"account")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/\ud83e\udd86 icon _User Circle_.png", QSize(), QIcon.Normal, QIcon.Off)
        self.account.setIcon(icon2)
        self.account.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.account)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.main)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 7, 0, 0)
        self.left_menu = QWidget(self.main)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(180, 0))
        self.left_menu.setMaximumSize(QSize(300, 16777215))
        self.left_menu.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
"border: none;\n"
"border-radius: 25;")
        self.verticalLayout_3 = QVBoxLayout(self.left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.left_menu)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.home = QPushButton(self.frame_3)
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 10;\n"
"padding: 3px 5px;")

        self.verticalLayout_4.addWidget(self.home)

        self.stations = QPushButton(self.frame_3)
        self.stations.setObjectName(u"stations")
        self.stations.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"padding: 3px 5px;")

        self.verticalLayout_4.addWidget(self.stations)

        self.report = QPushButton(self.frame_3)
        self.report.setObjectName(u"report")
        self.report.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"padding: 3px 5px;")

        self.verticalLayout_4.addWidget(self.report)

        self.my_account = QPushButton(self.frame_3)
        self.my_account.setObjectName(u"my_account")
        self.my_account.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"padding: 3px 5px;")

        self.verticalLayout_4.addWidget(self.my_account)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.settings = QPushButton(self.frame_4)
        self.settings.setObjectName(u"settings")
        self.settings.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"padding: 3px 5px;")

        self.verticalLayout_5.addWidget(self.settings)

        self.About = QPushButton(self.frame_4)
        self.About.setObjectName(u"About")
        self.About.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"padding: 3px 5px;")

        self.verticalLayout_5.addWidget(self.About)


        self.verticalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_4.addWidget(self.left_menu)

        self.main_bar = QWidget(self.main)
        self.main_bar.setObjectName(u"main_bar")
        self.main_bar.setStyleSheet(u"background-color: rgb(34, 34, 34);\n"
"border: none;\n"
"border-radius: 25;")
        self.verticalLayout_2 = QVBoxLayout(self.main_bar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.gridLayout = QGridLayout(self.home_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(self.home_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_5)
        self.gridLayout_8.setSpacing(10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setMidLineWidth(-4)
        self.gridLayout_9 = QGridLayout(self.frame_12)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_12)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, -1, -1, -1)
        self.label_3 = QLabel(self.frame_18)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Calibri\";")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.lcdNumber_2 = QLCDNumber(self.frame_18)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setDigitCount(2)
        self.lcdNumber_2.setProperty("intValue", 40)

        self.horizontalLayout_6.addWidget(self.lcdNumber_2)


        self.gridLayout_9.addWidget(self.frame_18, 1, 0, 1, 1)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, 9, 9, 9)
        self.label = QLabel(self.frame_16)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Calibri\";")
        self.label.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter)

        self.lcdNumber = QLCDNumber(self.frame_16)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setProperty("intValue", 10)

        self.horizontalLayout_5.addWidget(self.lcdNumber)


        self.gridLayout_9.addWidget(self.frame_16, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_12, 0, 0, 1, 1)

        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.frame_13, 0, 1, 1, 1)

        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_14)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_17)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 281, 81))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Gill Sans MT\";\n"
"")
        self.label_5.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_19)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_6 = QLabel(self.frame_19)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.gridLayout_10.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.gridLayout_10.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame_19)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.gridLayout_10.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_9 = QLabel(self.frame_19)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.gridLayout_10.addWidget(self.label_9, 1, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_19)


        self.gridLayout_8.addWidget(self.frame_14, 1, 0, 1, 1)

        self.frame_15 = QFrame(self.frame_5)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_20)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(60, 30, 201, 41))
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Gill Sans MT\";")
        self.label_10.setWordWrap(False)

        self.verticalLayout_8.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_15)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_21)


        self.gridLayout_8.addWidget(self.frame_15, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.stations_page = QWidget()
        self.stations_page.setObjectName(u"stations_page")
        self.gridLayout_2 = QGridLayout(self.stations_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_6 = QFrame(self.stations_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_6)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(100, 35))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.comboBox = QComboBox(self.frame_23)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 0, 150, 40))
        self.comboBox.setMinimumSize(QSize(150, 30))
        self.comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 162, 244);\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.frame_23, 0, Qt.AlignTop)

        self.frame_22 = QFrame(self.frame_6)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_22)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_22)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.station_1 = QWidget()
        self.station_1.setObjectName(u"station_1")
        self.gridLayout_12 = QGridLayout(self.station_1)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_24 = QFrame(self.station_1)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_24)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_28 = QFrame(self.frame_24)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 40))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton = QPushButton(self.frame_30)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 30))
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 10;\n"
"padding: 3px 5px;")

        self.horizontalLayout_10.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_30)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 10;\n"
"padding: 3px 5px;")

        self.horizontalLayout_10.addWidget(self.pushButton_2)


        self.horizontalLayout_9.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_28)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(200, 0))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.comboBox_2 = QComboBox(self.frame_31)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(30, 10, 150, 40))
        self.comboBox_2.setMinimumSize(QSize(150, 30))
        self.comboBox_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 162, 244);")

        self.horizontalLayout_9.addWidget(self.frame_31, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.frame_28, 0, Qt.AlignTop)

        self.frame_29 = QFrame(self.frame_24)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_29)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = QStackedWidget(self.frame_29)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.charge_1 = QWidget()
        self.charge_1.setObjectName(u"charge_1")
        self.gridLayout_17 = QGridLayout(self.charge_1)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.frame_32 = QFrame(self.charge_1)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_33)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_41 = QFrame(self.frame_33)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(9, 0, 0, 0)
        self.label_2 = QLabel(self.frame_41)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_11.addWidget(self.label_2)

        self.label_4 = QLabel(self.frame_41)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_11.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_33)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(9, 0, 0, 0)
        self.label_11 = QLabel(self.frame_42)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_42)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_12.addWidget(self.label_12, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_33)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 0, 0, 0)
        self.label_13 = QLabel(self.frame_43)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_13.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_43)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_13.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_33)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, 0, 0)
        self.label_15 = QLabel(self.frame_44)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_14.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_44)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_14.addWidget(self.label_16, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.frame_33)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, 0, 0)
        self.label_17 = QLabel(self.frame_45)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_15.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_45)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_15.addWidget(self.label_18, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_33)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, 0, 0)
        self.label_19 = QLabel(self.frame_46)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_16.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_46)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_16.addWidget(self.label_20, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_46)


        self.horizontalLayout_7.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 0))
        self.frame_34.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_34)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_48 = QFrame(self.frame_34)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(200, 60))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.label_21 = QLabel(self.frame_48)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 0, 211, 71))
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 20pt \"Calibri\";")
        self.label_21.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.frame_48, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_47 = QFrame(self.frame_34)
        self.frame_47.setObjectName(u"frame_47")
        sizePolicy.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy)
        self.frame_47.setMinimumSize(QSize(200, 0))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.label_22 = QLabel(self.frame_47)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(40, 20, 181, 131))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        self.label_22.setStyleSheet(u"border-image: url(:/newPrefix/plug.png);")

        self.verticalLayout_12.addWidget(self.frame_47)


        self.horizontalLayout_7.addWidget(self.frame_34)


        self.gridLayout_17.addWidget(self.frame_32, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.charge_1)
        self.charge_2 = QWidget()
        self.charge_2.setObjectName(u"charge_2")
        self.gridLayout_18 = QGridLayout(self.charge_2)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.frame_35 = QFrame(self.charge_2)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_37)


        self.gridLayout_18.addWidget(self.frame_35, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.charge_2)

        self.gridLayout_16.addWidget(self.stackedWidget_3, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_29)


        self.gridLayout_12.addWidget(self.frame_24, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.station_1)
        self.station_2 = QWidget()
        self.station_2.setObjectName(u"station_2")
        self.gridLayout_13 = QGridLayout(self.station_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_25 = QFrame(self.station_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_25)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_49 = QFrame(self.frame_25)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(0, 68))
        self.frame_49.setSizeIncrement(QSize(0, 40))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(9, -1, -1, -1)
        self.frame_52 = QFrame(self.frame_49)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_3 = QPushButton(self.frame_52)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 30))
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 10;\n"
"padding: 3px 5px;")

        self.horizontalLayout_19.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_52)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(150, 30))
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 10;\n"
"padding: 3px 5px;")

        self.horizontalLayout_19.addWidget(self.pushButton_4)


        self.horizontalLayout_17.addWidget(self.frame_52)

        self.frame_51 = QFrame(self.frame_49)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(200, 0))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.comboBox_3 = QComboBox(self.frame_51)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(40, 10, 131, 41))
        self.comboBox_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 162, 244);")

        self.horizontalLayout_17.addWidget(self.frame_51, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.frame_49, 0, Qt.AlignTop)

        self.frame_50 = QFrame(self.frame_25)
        self.frame_50.setObjectName(u"frame_50")
        sizePolicy.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy)
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_50)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_4 = QStackedWidget(self.frame_50)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_24 = QGridLayout(self.page)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.frame_53 = QFrame(self.page)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_54 = QFrame(self.frame_53)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.frame_53)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frame_55)


        self.gridLayout_24.addWidget(self.frame_53, 0, 0, 1, 1)

        self.stackedWidget_4.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_4.addWidget(self.page_2)

        self.gridLayout_23.addWidget(self.stackedWidget_4, 0, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_50)


        self.gridLayout_13.addWidget(self.frame_25, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.station_2)
        self.station_3 = QWidget()
        self.station_3.setObjectName(u"station_3")
        self.gridLayout_14 = QGridLayout(self.station_3)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_26 = QFrame(self.station_3)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.gridLayout_14.addWidget(self.frame_26, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.station_3)
        self.station_4 = QWidget()
        self.station_4.setObjectName(u"station_4")
        self.gridLayout_15 = QGridLayout(self.station_4)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_27 = QFrame(self.station_4)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.gridLayout_15.addWidget(self.frame_27, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.station_4)

        self.gridLayout_11.addWidget(self.stackedWidget_2, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_22)


        self.gridLayout_2.addWidget(self.frame_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.stations_page)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.gridLayout_3 = QGridLayout(self.report_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_7 = QFrame(self.report_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_7)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.tabWidget = QTabWidget(self.frame_7)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_20 = QGridLayout(self.tab)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.frame_38 = QFrame(self.tab)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_38)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.tableWidget = QTableWidget(self.frame_38)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_25.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame_38, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_21 = QGridLayout(self.tab_2)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frame_39 = QFrame(self.tab_2)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)

        self.gridLayout_21.addWidget(self.frame_39, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_22 = QGridLayout(self.tab_3)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_40 = QFrame(self.tab_3)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)

        self.gridLayout_22.addWidget(self.frame_40, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_19.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.report_page)
        self.account_page_2 = QWidget()
        self.account_page_2.setObjectName(u"account_page_2")
        self.gridLayout_4 = QGridLayout(self.account_page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_8 = QFrame(self.account_page_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_56 = QFrame(self.frame_8)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_56)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_11 = QFrame(self.frame_56)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 250))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.frame_11)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(50, 40, 191, 171))
        self.label_24.setStyleSheet(u"border-image: url(:/newPrefix/\ud83e\udd86 icon _User Circle_.png);")

        self.verticalLayout_16.addWidget(self.frame_11)

        self.frame_58 = QFrame(self.frame_56)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 26pt \"MS Shell Dlg 2\";")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.label_23 = QLabel(self.frame_58)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 0, 241, 121))
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_23.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.frame_58)


        self.horizontalLayout_20.addWidget(self.frame_56)

        self.frame_57 = QFrame(self.frame_8)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_57)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_59 = QFrame(self.frame_57)
        self.frame_59.setObjectName(u"frame_59")
        sizePolicy.setHeightForWidth(self.frame_59.sizePolicy().hasHeightForWidth())
        self.frame_59.setSizePolicy(sizePolicy)
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_59)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_64 = QFrame(self.frame_59)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.label_27 = QLabel(self.frame_64)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(50, 20, 47, 14))
        self.label_28 = QLabel(self.frame_64)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(170, 20, 47, 14))
        self.label_29 = QLabel(self.frame_64)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(50, 50, 47, 14))
        self.label_30 = QLabel(self.frame_64)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(170, 50, 47, 14))
        self.label_31 = QLabel(self.frame_64)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(50, 80, 47, 14))
        self.label_32 = QLabel(self.frame_64)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(170, 80, 47, 14))
        self.label_33 = QLabel(self.frame_64)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(50, 110, 47, 14))
        self.label_34 = QLabel(self.frame_64)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(170, 110, 47, 14))

        self.verticalLayout_17.addWidget(self.frame_64)

        self.frame_65 = QFrame(self.frame_59)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.frame_65)


        self.verticalLayout_14.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_57)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 70))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_60, 0, Qt.AlignBottom)


        self.horizontalLayout_20.addWidget(self.frame_57)


        self.gridLayout_4.addWidget(self.frame_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.account_page_2)
        self.settings_page_2 = QWidget()
        self.settings_page_2.setObjectName(u"settings_page_2")
        self.gridLayout_5 = QGridLayout(self.settings_page_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_9 = QFrame(self.settings_page_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.settings_page_2)
        self.about_page_2 = QWidget()
        self.about_page_2.setObjectName(u"about_page_2")
        self.gridLayout_6 = QGridLayout(self.about_page_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_10 = QFrame(self.about_page_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_10)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_61 = QFrame(self.frame_10)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_61)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_62 = QFrame(self.frame_61)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(0, 70))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.label_25 = QLabel(self.frame_62)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 10, 631, 41))
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 36pt \"MS Shell Dlg 2\";")

        self.verticalLayout_15.addWidget(self.frame_62, 0, Qt.AlignTop)

        self.frame_63 = QFrame(self.frame_61)
        self.frame_63.setObjectName(u"frame_63")
        sizePolicy.setHeightForWidth(self.frame_63.sizePolicy().hasHeightForWidth())
        self.frame_63.setSizePolicy(sizePolicy)
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.label_26 = QLabel(self.frame_63)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 20, 591, 331))
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")
        self.label_26.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.frame_63)


        self.gridLayout_7.addWidget(self.frame_61, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.about_page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.main_bar)


        self.verticalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox_2.currentIndexChanged.connect(self.stackedWidget_3.setCurrentIndex)
        self.comboBox.currentIndexChanged.connect(self.stackedWidget_2.setCurrentIndex)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"EV Charge", None))
        self.notification.setText("")
        self.account.setText("")
        self.home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.stations.setText(QCoreApplication.translate("MainWindow", u"Stations", None))
        self.report.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.my_account.setText(QCoreApplication.translate("MainWindow", u"My Account", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.About.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total Chargers", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total Stations", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Carbon Foot print Reduction", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CO2 Saved", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"10 Units", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Fuel Replaced", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"20 Units", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Monthly Revenue", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Station 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Station 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Station 3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Station 4", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Camera View", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Charger 1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Charger 2", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Charger Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Charger Type", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Charger ID", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Minimum Current", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Maximum Current", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"EV Not Connected", None))
        self.label_22.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Camera View", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Charger 1", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Charger 2", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Sales", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Management Cost", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Electricity Cost", None))
        self.label_24.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Account Holders  Name", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Our Mission", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"In the next 20 years, EVs will replace ICE vehicles as the main way that people move around. We are living through a revolution in not only how we move, but how we store and use energy. 25% of all end-use global energy is spent on transportation (37% in North America). Switching from gas to electric fuel for transportation will require the largest global infrastructure overhaul of our lives\u2014from new renewable power generation, to how we transmit, distribute, store, and use electricity.\n"
"\u200d\n"
"EV Charge\u2019s mission is to build EV charging solutions that scale. This means making EV charger deployment fast and affordable. And making charging easy and reliable for every EV driver.\n"
"\u200d\n"
"EV Charge sits at the nexus point between vehicles, building owners, and the grid. With software, we can help buildings, communities, and entire cities charge more EVs than their infrastructure would otherwise allow. We can optimize charging for grid capacity, cost, or carbon impact. And we can enable bi-di"
                        "rectional communication between individual EVs and the grid.\n"
"\n"
"EV Charge is building for scale because our planet needs millions more EVs, and consumers want millions more EVs. Automobiles have been powered by petrol since 1892. The switch to electric vehicles is a once-per-century economic and cultural shift. We are pioneers for the new era of transportation and energy.", None))
    # retranslateUi

