# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainvuPnQY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar

import account_rc
import search_rc
import edit_rc
import line_rc
import plug_rc
import down_rc
import menu_rc
import noti_rc

total_chargers = 58
in_use_chargers = 43

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global total_chargers
        global in_use_chargers

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(894, 597)
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
        self.home_page_main_frame = QFrame(self.home_page)
        self.home_page_main_frame.setObjectName(u"home_page_main_frame")
        self.home_page_main_frame.setFrameShape(QFrame.StyledPanel)
        self.home_page_main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.home_page_main_frame)
        self.gridLayout_8.setSpacing(10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.home_page_main_frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setMidLineWidth(-4)
        self.gridLayout_9 = QGridLayout(self.frame_12)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.occupiedchargers_frame = QFrame(self.frame_12)
        self.occupiedchargers_frame.setObjectName(u"occupiedchargers_frame")
        self.occupiedchargers_frame.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.occupiedchargers_frame.setFrameShape(QFrame.StyledPanel)
        self.occupiedchargers_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.occupiedchargers_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, -1, -1, -1)
        self.occupied_chargers_label = QLabel(self.occupiedchargers_frame)
        self.occupied_chargers_label.setObjectName(u"occupied_chargers_label")
        self.occupied_chargers_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Calibri\";")

        self.horizontalLayout_6.addWidget(self.occupied_chargers_label, 0, Qt.AlignHCenter)

        self.occupied_chargers_lcdNumber = QLCDNumber(self.occupiedchargers_frame)
        self.occupied_chargers_lcdNumber.setObjectName(u"occupied_chargers_lcdNumber")
        self.occupied_chargers_lcdNumber.setDigitCount(2)
        self.occupied_chargers_lcdNumber.setProperty("intValue", in_use_chargers)

        self.horizontalLayout_6.addWidget(self.occupied_chargers_lcdNumber)


        self.gridLayout_9.addWidget(self.occupiedchargers_frame, 2, 0, 1, 1)

        self.total_chargers_frame = QFrame(self.frame_12)
        self.total_chargers_frame.setObjectName(u"total_chargers_frame")
        self.total_chargers_frame.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.total_chargers_frame.setFrameShape(QFrame.StyledPanel)
        self.total_chargers_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.total_chargers_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, 9, 9, 9)
        self.total_chargers_label = QLabel(self.total_chargers_frame)
        self.total_chargers_label.setObjectName(u"total_chargers_label")
        self.total_chargers_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Calibri\";")
        self.total_chargers_label.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.total_chargers_label, 0, Qt.AlignHCenter)

        self.total_chargers_lcdNumber = QLCDNumber(self.total_chargers_frame)
        self.total_chargers_lcdNumber.setObjectName(u"total_chargers_lcdNumber")
        self.total_chargers_lcdNumber.setDigitCount(2)
        self.total_chargers_lcdNumber.setProperty("intValue", total_chargers)

        self.horizontalLayout_5.addWidget(self.total_chargers_lcdNumber)


        self.gridLayout_9.addWidget(self.total_chargers_frame, 0, 0, 1, 1)

        self.available_chargers_frame = QFrame(self.frame_12)
        self.available_chargers_frame.setObjectName(u"available_chargers_frame")
        self.available_chargers_frame.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.available_chargers_frame.setFrameShape(QFrame.StyledPanel)
        self.available_chargers_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.available_chargers_frame)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(20, -1, -1, -1)
        self.available_chargers_label = QLabel(self.available_chargers_frame)
        self.available_chargers_label.setObjectName(u"available_chargers_label")
        self.available_chargers_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Calibri\";")

        self.horizontalLayout_66.addWidget(self.available_chargers_label)

        self.available_chargers_lcdNumber = QLCDNumber(self.available_chargers_frame)
        self.available_chargers_lcdNumber.setObjectName(u"available_chargers_lcdNumber")
        self.available_chargers_lcdNumber.setDigitCount(2)

        self.horizontalLayout_66.addWidget(self.available_chargers_lcdNumber)


        self.gridLayout_9.addWidget(self.available_chargers_frame, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_12, 0, 0, 1, 1)

        self.frame_13 = QFrame(self.home_page_main_frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_13)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.progressbar_frame = QFrame(self.frame_13)
        self.progressbar_frame.setObjectName(u"progressbar_frame")
        sizePolicy.setHeightForWidth(self.progressbar_frame.sizePolicy().hasHeightForWidth())
        self.progressbar_frame.setSizePolicy(sizePolicy)
        self.progressbar_frame.setFrameShape(QFrame.StyledPanel)
        self.progressbar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.progressbar_frame)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.progress = QFrame(self.progressbar_frame)
        self.progress.setObjectName(u"progress")
        self.progress.setMinimumSize(QSize(150, 150))
        self.progress.setMaximumSize(QSize(5000, 5000))
        self.progress.setStyleSheet(u"border: 2px solid;\n"
"border-radius: 75;\n"
"border-color: transparent;\n"
"")
        self.progress.setFrameShape(QFrame.StyledPanel)
        self.progress.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.progress)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.prg_in = roundProgressBar(self.progress)
        self.prg_in.setObjectName(u"prg_in")

        self.horizontalLayout_65.addWidget(self.prg_in)


        self.horizontalLayout_71.addWidget(self.progress)


        self.verticalLayout_24.addWidget(self.progressbar_frame)

        self.percentage_frame = QFrame(self.frame_13)
        self.percentage_frame.setObjectName(u"percentage_frame")
        self.percentage_frame.setFrameShape(QFrame.StyledPanel)
        self.percentage_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.percentage_frame)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.percentage_label = QLabel(self.percentage_frame)
        self.percentage_label.setObjectName(u"percentage_label")
        self.percentage_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Calibri\";")

        self.horizontalLayout_64.addWidget(self.percentage_label)


        self.verticalLayout_24.addWidget(self.percentage_frame, 0, Qt.AlignBottom)


        self.gridLayout_8.addWidget(self.frame_13, 0, 1, 1, 1)

        self.co2_frame = QFrame(self.home_page_main_frame)
        self.co2_frame.setObjectName(u"co2_frame")
        sizePolicy.setHeightForWidth(self.co2_frame.sizePolicy().hasHeightForWidth())
        self.co2_frame.setSizePolicy(sizePolicy)
        self.co2_frame.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.co2_frame.setFrameShape(QFrame.StyledPanel)
        self.co2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.co2_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.co2_heading_frame = QFrame(self.co2_frame)
        self.co2_heading_frame.setObjectName(u"co2_heading_frame")
        self.co2_heading_frame.setMinimumSize(QSize(0, 100))
        self.co2_heading_frame.setFrameShape(QFrame.StyledPanel)
        self.co2_heading_frame.setFrameShadow(QFrame.Raised)
        self.co2_heading_label = QLabel(self.co2_heading_frame)
        self.co2_heading_label.setObjectName(u"co2_heading_label")
        self.co2_heading_label.setGeometry(QRect(0, 0, 310, 96))
        self.co2_heading_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Gill Sans MT\";\n"
"padding-left: 20px;\n"
"")
        self.co2_heading_label.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.co2_heading_frame)

        self.co2_contents = QFrame(self.co2_frame)
        self.co2_contents.setObjectName(u"co2_contents")
        self.co2_contents.setFrameShape(QFrame.StyledPanel)
        self.co2_contents.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.co2_contents)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_6 = QLabel(self.co2_contents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.gridLayout_10.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_8 = QLabel(self.co2_contents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.gridLayout_10.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_7 = QLabel(self.co2_contents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.gridLayout_10.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_9 = QLabel(self.co2_contents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.gridLayout_10.addWidget(self.label_9, 1, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.co2_contents)


        self.gridLayout_8.addWidget(self.co2_frame, 1, 0, 1, 1)

        self.Monthly_revenue_frame = QFrame(self.home_page_main_frame)
        self.Monthly_revenue_frame.setObjectName(u"Monthly_revenue_frame")
        sizePolicy.setHeightForWidth(self.Monthly_revenue_frame.sizePolicy().hasHeightForWidth())
        self.Monthly_revenue_frame.setSizePolicy(sizePolicy)
        self.Monthly_revenue_frame.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
"")
        self.Monthly_revenue_frame.setFrameShape(QFrame.StyledPanel)
        self.Monthly_revenue_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Monthly_revenue_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.heading_frame_revenue = QFrame(self.Monthly_revenue_frame)
        self.heading_frame_revenue.setObjectName(u"heading_frame_revenue")
        self.heading_frame_revenue.setMinimumSize(QSize(0, 100))
        self.heading_frame_revenue.setFrameShape(QFrame.StyledPanel)
        self.heading_frame_revenue.setFrameShadow(QFrame.Raised)
        self.revenue_heading_label = QLabel(self.heading_frame_revenue)
        self.revenue_heading_label.setObjectName(u"revenue_heading_label")
        self.revenue_heading_label.setGeometry(QRect(0, 0, 310, 97))
        self.revenue_heading_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Gill Sans MT\";\n"
"padding-left: 20px;")
        self.revenue_heading_label.setWordWrap(False)

        self.verticalLayout_8.addWidget(self.heading_frame_revenue)

        self.frame_21 = QFrame(self.Monthly_revenue_frame)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_21)


        self.gridLayout_8.addWidget(self.Monthly_revenue_frame, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.home_page_main_frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.stations_page = QWidget()
        self.stations_page.setObjectName(u"stations_page")
        self.gridLayout_2 = QGridLayout(self.stations_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Station_main_frame = QFrame(self.stations_page)
        self.Station_main_frame.setObjectName(u"Station_main_frame")
        self.Station_main_frame.setFrameShape(QFrame.StyledPanel)
        self.Station_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Station_main_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.Station_main_frame)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(100, 35))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.stations_comboBox = QComboBox(self.frame_23)
        self.stations_comboBox.addItem("")
        self.stations_comboBox.addItem("")
        self.stations_comboBox.setObjectName(u"stations_comboBox")
        self.stations_comboBox.setGeometry(QRect(10, 0, 150, 40))
        self.stations_comboBox.setMinimumSize(QSize(150, 30))
        self.stations_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 162, 244);\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.frame_23, 0, Qt.AlignTop)

        self.chargers_frame = QFrame(self.Station_main_frame)
        self.chargers_frame.setObjectName(u"chargers_frame")
        sizePolicy.setHeightForWidth(self.chargers_frame.sizePolicy().hasHeightForWidth())
        self.chargers_frame.setSizePolicy(sizePolicy)
        self.chargers_frame.setFrameShape(QFrame.StyledPanel)
        self.chargers_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.chargers_frame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.chargers_frame)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(0, 70))
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
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.top_chargers_1 = QFrame(self.frame_24)
        self.top_chargers_1.setObjectName(u"top_chargers_1")
        self.top_chargers_1.setMinimumSize(QSize(0, 40))
        self.top_chargers_1.setFrameShape(QFrame.StyledPanel)
        self.top_chargers_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.top_chargers_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_30 = QFrame(self.top_chargers_1)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.location1_btn = QPushButton(self.frame_30)
        self.location1_btn.setObjectName(u"location1_btn")
        self.location1_btn.setMinimumSize(QSize(100, 30))
        self.location1_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 10;\n"
"padding: 3px 5px;")

        self.horizontalLayout_10.addWidget(self.location1_btn)

        self.camera1_btn = QPushButton(self.frame_30)
        self.camera1_btn.setObjectName(u"camera1_btn")
        self.camera1_btn.setMinimumSize(QSize(150, 30))
        self.camera1_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 10;\n"
"padding: 3px 5px;")

        self.horizontalLayout_10.addWidget(self.camera1_btn)


        self.horizontalLayout_9.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.top_chargers_1)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(200, 0))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.st1_charger_comboBox = QComboBox(self.frame_31)
        self.st1_charger_comboBox.addItem("")
        self.st1_charger_comboBox.addItem("")
        self.st1_charger_comboBox.setObjectName(u"st1_charger_comboBox")
        self.st1_charger_comboBox.setGeometry(QRect(40, 10, 150, 35))
        self.st1_charger_comboBox.setMinimumSize(QSize(150, 30))
        self.st1_charger_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 162, 244);")

        self.horizontalLayout_9.addWidget(self.frame_31, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.top_chargers_1, 0, Qt.AlignTop)

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
        self.charge_11 = QWidget()
        self.charge_11.setObjectName(u"charge_11")
        self.gridLayout_17 = QGridLayout(self.charge_11)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.charger_11_frame = QFrame(self.charge_11)
        self.charger_11_frame.setObjectName(u"charger_11_frame")
        self.charger_11_frame.setFrameShape(QFrame.StyledPanel)
        self.charger_11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.charger_11_frame)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ch11_left_frame = QFrame(self.charger_11_frame)
        self.ch11_left_frame.setObjectName(u"ch11_left_frame")
        self.ch11_left_frame.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.ch11_left_frame.setFrameShape(QFrame.StyledPanel)
        self.ch11_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.ch11_left_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.cname11_frame = QFrame(self.ch11_left_frame)
        self.cname11_frame.setObjectName(u"cname11_frame")
        self.cname11_frame.setFrameShape(QFrame.StyledPanel)
        self.cname11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.cname11_frame)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(9, 0, 0, 0)
        self.cname11_label = QLabel(self.cname11_frame)
        self.cname11_label.setObjectName(u"cname11_label")
        self.cname11_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_11.addWidget(self.cname11_label)

        self.cname11_value_label = QLabel(self.cname11_frame)
        self.cname11_value_label.setObjectName(u"cname11_value_label")
        self.cname11_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_11.addWidget(self.cname11_value_label, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.cname11_frame)

        self.ctype11_frame = QFrame(self.ch11_left_frame)
        self.ctype11_frame.setObjectName(u"ctype11_frame")
        self.ctype11_frame.setFrameShape(QFrame.StyledPanel)
        self.ctype11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.ctype11_frame)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(9, 0, 0, 0)
        self.ctype11_label = QLabel(self.ctype11_frame)
        self.ctype11_label.setObjectName(u"ctype11_label")
        self.ctype11_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_12.addWidget(self.ctype11_label)

        self.ctype11_value_label = QLabel(self.ctype11_frame)
        self.ctype11_value_label.setObjectName(u"ctype11_value_label")
        self.ctype11_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_12.addWidget(self.ctype11_value_label, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.ctype11_frame)

        self.cid11_frame = QFrame(self.ch11_left_frame)
        self.cid11_frame.setObjectName(u"cid11_frame")
        self.cid11_frame.setFrameShape(QFrame.StyledPanel)
        self.cid11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.cid11_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 0, 0, 0)
        self.cid11_label = QLabel(self.cid11_frame)
        self.cid11_label.setObjectName(u"cid11_label")
        self.cid11_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_13.addWidget(self.cid11_label)

        self.cid11_value_label = QLabel(self.cid11_frame)
        self.cid11_value_label.setObjectName(u"cid11_value_label")
        self.cid11_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_13.addWidget(self.cid11_value_label, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.cid11_frame)

        self.minc11_frame = QFrame(self.ch11_left_frame)
        self.minc11_frame.setObjectName(u"minc11_frame")
        self.minc11_frame.setFrameShape(QFrame.StyledPanel)
        self.minc11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.minc11_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, 0, 0)
        self.minc11_label = QLabel(self.minc11_frame)
        self.minc11_label.setObjectName(u"minc11_label")
        self.minc11_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_14.addWidget(self.minc11_label)

        self.minc11_value_label = QLabel(self.minc11_frame)
        self.minc11_value_label.setObjectName(u"minc11_value_label")
        self.minc11_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_14.addWidget(self.minc11_value_label, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.minc11_frame)

        self.maxc11_frame = QFrame(self.ch11_left_frame)
        self.maxc11_frame.setObjectName(u"maxc11_frame")
        self.maxc11_frame.setFrameShape(QFrame.StyledPanel)
        self.maxc11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.maxc11_frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, 0, 0)
        self.maxc11_label = QLabel(self.maxc11_frame)
        self.maxc11_label.setObjectName(u"maxc11_label")
        self.maxc11_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_15.addWidget(self.maxc11_label)

        self.maxc11_value_label = QLabel(self.maxc11_frame)
        self.maxc11_value_label.setObjectName(u"maxc11_value_label")
        self.maxc11_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_15.addWidget(self.maxc11_value_label, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.maxc11_frame)

        self.voltage11_frame = QFrame(self.ch11_left_frame)
        self.voltage11_frame.setObjectName(u"voltage11_frame")
        self.voltage11_frame.setFrameShape(QFrame.StyledPanel)
        self.voltage11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.voltage11_frame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, 0, 0)
        self.voltage11_label = QLabel(self.voltage11_frame)
        self.voltage11_label.setObjectName(u"voltage11_label")
        self.voltage11_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_16.addWidget(self.voltage11_label)

        self.voltage11_value_label = QLabel(self.voltage11_frame)
        self.voltage11_value_label.setObjectName(u"voltage11_value_label")
        self.voltage11_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_16.addWidget(self.voltage11_value_label, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.voltage11_frame)


        self.horizontalLayout_7.addWidget(self.ch11_left_frame)

        self.ch11_right_frame = QFrame(self.charger_11_frame)
        self.ch11_right_frame.setObjectName(u"ch11_right_frame")
        self.ch11_right_frame.setMinimumSize(QSize(0, 0))
        self.ch11_right_frame.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.ch11_right_frame.setFrameShape(QFrame.StyledPanel)
        self.ch11_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.ch11_right_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.evid11_frame = QFrame(self.ch11_right_frame)
        self.evid11_frame.setObjectName(u"evid11_frame")
        self.evid11_frame.setFrameShape(QFrame.StyledPanel)
        self.evid11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.evid11_frame)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.evid11_label = QLabel(self.evid11_frame)
        self.evid11_label.setObjectName(u"evid11_label")
        self.evid11_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_21.addWidget(self.evid11_label)

        self.evid11_value_label = QLabel(self.evid11_frame)
        self.evid11_value_label.setObjectName(u"evid11_value_label")
        self.evid11_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_21.addWidget(self.evid11_value_label)


        self.verticalLayout_12.addWidget(self.evid11_frame)

        self.cst11_frame = QFrame(self.ch11_right_frame)
        self.cst11_frame.setObjectName(u"cst11_frame")
        self.cst11_frame.setFrameShape(QFrame.StyledPanel)
        self.cst11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.cst11_frame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.cst11_label = QLabel(self.cst11_frame)
        self.cst11_label.setObjectName(u"cst11_label")
        self.cst11_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_22.addWidget(self.cst11_label)

        self.cst11_value_label = QLabel(self.cst11_frame)
        self.cst11_value_label.setObjectName(u"cst11_value_label")
        self.cst11_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_22.addWidget(self.cst11_value_label)


        self.verticalLayout_12.addWidget(self.cst11_frame)

        self.soc11_frame = QFrame(self.ch11_right_frame)
        self.soc11_frame.setObjectName(u"soc11_frame")
        self.soc11_frame.setFrameShape(QFrame.StyledPanel)
        self.soc11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.soc11_frame)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.soc11_label = QLabel(self.soc11_frame)
        self.soc11_label.setObjectName(u"soc11_label")
        self.soc11_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_23.addWidget(self.soc11_label)

        self.soc11_value_label = QLabel(self.soc11_frame)
        self.soc11_value_label.setObjectName(u"soc11_value_label")
        self.soc11_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_23.addWidget(self.soc11_value_label)


        self.verticalLayout_12.addWidget(self.soc11_frame)

        self.capacity11_frame = QFrame(self.ch11_right_frame)
        self.capacity11_frame.setObjectName(u"capacity11_frame")
        self.capacity11_frame.setFrameShape(QFrame.StyledPanel)
        self.capacity11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.capacity11_frame)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.capacity11_label = QLabel(self.capacity11_frame)
        self.capacity11_label.setObjectName(u"capacity11_label")
        self.capacity11_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_24.addWidget(self.capacity11_label)

        self.capacity11_value_label = QLabel(self.capacity11_frame)
        self.capacity11_value_label.setObjectName(u"capacity11_value_label")
        self.capacity11_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_24.addWidget(self.capacity11_value_label)


        self.verticalLayout_12.addWidget(self.capacity11_frame)

        self.ecet11_frame = QFrame(self.ch11_right_frame)
        self.ecet11_frame.setObjectName(u"ecet11_frame")
        self.ecet11_frame.setFrameShape(QFrame.StyledPanel)
        self.ecet11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.ecet11_frame)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.ecet11_label = QLabel(self.ecet11_frame)
        self.ecet11_label.setObjectName(u"ecet11_label")
        self.ecet11_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_25.addWidget(self.ecet11_label)

        self.ecet11_value_label = QLabel(self.ecet11_frame)
        self.ecet11_value_label.setObjectName(u"ecet11_value_label")
        self.ecet11_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_25.addWidget(self.ecet11_value_label)


        self.verticalLayout_12.addWidget(self.ecet11_frame)

        self.price11_frame = QFrame(self.ch11_right_frame)
        self.price11_frame.setObjectName(u"price11_frame")
        self.price11_frame.setFrameShape(QFrame.StyledPanel)
        self.price11_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.price11_frame)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.price11_label = QLabel(self.price11_frame)
        self.price11_label.setObjectName(u"price11_label")
        self.price11_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_26.addWidget(self.price11_label)

        self.price11_value_label = QLabel(self.price11_frame)
        self.price11_value_label.setObjectName(u"price11_value_label")
        self.price11_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_26.addWidget(self.price11_value_label)


        self.verticalLayout_12.addWidget(self.price11_frame)


        self.horizontalLayout_7.addWidget(self.ch11_right_frame)


        self.gridLayout_17.addWidget(self.charger_11_frame, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.charge_11)
        self.charge_12 = QWidget()
        self.charge_12.setObjectName(u"charge_12")
        self.gridLayout_18 = QGridLayout(self.charge_12)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.charger12_main_frame = QFrame(self.charge_12)
        self.charger12_main_frame.setObjectName(u"charger12_main_frame")
        self.charger12_main_frame.setFrameShape(QFrame.StyledPanel)
        self.charger12_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.charger12_main_frame)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.charger12_main_left_frame = QFrame(self.charger12_main_frame)
        self.charger12_main_left_frame.setObjectName(u"charger12_main_left_frame")
        self.charger12_main_left_frame.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.charger12_main_left_frame.setFrameShape(QFrame.StyledPanel)
        self.charger12_main_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.charger12_main_left_frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.cname12_frame = QFrame(self.charger12_main_left_frame)
        self.cname12_frame.setObjectName(u"cname12_frame")
        self.cname12_frame.setFrameShape(QFrame.StyledPanel)
        self.cname12_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.cname12_frame)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.cname12_label = QLabel(self.cname12_frame)
        self.cname12_label.setObjectName(u"cname12_label")
        self.cname12_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_37.addWidget(self.cname12_label)

        self.cname12_value_label = QLabel(self.cname12_frame)
        self.cname12_value_label.setObjectName(u"cname12_value_label")
        self.cname12_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_37.addWidget(self.cname12_value_label, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.cname12_frame)

        self.ctype12_frame = QFrame(self.charger12_main_left_frame)
        self.ctype12_frame.setObjectName(u"ctype12_frame")
        self.ctype12_frame.setFrameShape(QFrame.StyledPanel)
        self.ctype12_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.ctype12_frame)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.ctype12_label = QLabel(self.ctype12_frame)
        self.ctype12_label.setObjectName(u"ctype12_label")
        self.ctype12_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_38.addWidget(self.ctype12_label)

        self.ctype12_value_label = QLabel(self.ctype12_frame)
        self.ctype12_value_label.setObjectName(u"ctype12_value_label")
        self.ctype12_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_38.addWidget(self.ctype12_value_label, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.ctype12_frame)

        self.cid12_frame = QFrame(self.charger12_main_left_frame)
        self.cid12_frame.setObjectName(u"cid12_frame")
        self.cid12_frame.setFrameShape(QFrame.StyledPanel)
        self.cid12_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.cid12_frame)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.cid12_label = QLabel(self.cid12_frame)
        self.cid12_label.setObjectName(u"cid12_label")
        self.cid12_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_39.addWidget(self.cid12_label)

        self.cid12_value_label = QLabel(self.cid12_frame)
        self.cid12_value_label.setObjectName(u"cid12_value_label")
        self.cid12_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_39.addWidget(self.cid12_value_label, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.cid12_frame)

        self.minc12_frame = QFrame(self.charger12_main_left_frame)
        self.minc12_frame.setObjectName(u"minc12_frame")
        self.minc12_frame.setFrameShape(QFrame.StyledPanel)
        self.minc12_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.minc12_frame)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.minc12_label = QLabel(self.minc12_frame)
        self.minc12_label.setObjectName(u"minc12_label")
        self.minc12_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_40.addWidget(self.minc12_label)

        self.minc12_value_label = QLabel(self.minc12_frame)
        self.minc12_value_label.setObjectName(u"minc12_value_label")
        self.minc12_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_40.addWidget(self.minc12_value_label, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.minc12_frame)

        self.maxc12_frame = QFrame(self.charger12_main_left_frame)
        self.maxc12_frame.setObjectName(u"maxc12_frame")
        self.maxc12_frame.setFrameShape(QFrame.StyledPanel)
        self.maxc12_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.maxc12_frame)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.maxc12_label = QLabel(self.maxc12_frame)
        self.maxc12_label.setObjectName(u"maxc12_label")
        self.maxc12_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_41.addWidget(self.maxc12_label)

        self.maxc12_value_label = QLabel(self.maxc12_frame)
        self.maxc12_value_label.setObjectName(u"maxc12_value_label")
        self.maxc12_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_41.addWidget(self.maxc12_value_label, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.maxc12_frame)

        self.voltage12_frame = QFrame(self.charger12_main_left_frame)
        self.voltage12_frame.setObjectName(u"voltage12_frame")
        self.voltage12_frame.setFrameShape(QFrame.StyledPanel)
        self.voltage12_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.voltage12_frame)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.voltage12_label = QLabel(self.voltage12_frame)
        self.voltage12_label.setObjectName(u"voltage12_label")
        self.voltage12_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_42.addWidget(self.voltage12_label)

        self.voltage12_value_label = QLabel(self.voltage12_frame)
        self.voltage12_value_label.setObjectName(u"voltage12_value_label")
        self.voltage12_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_42.addWidget(self.voltage12_value_label, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.voltage12_frame)


        self.horizontalLayout_8.addWidget(self.charger12_main_left_frame)

        self.frame_37 = QFrame(self.charger12_main_frame)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_37)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_76 = QFrame(self.frame_37)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_59 = QLabel(self.frame_76)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_43.addWidget(self.label_59)

        self.label_60 = QLabel(self.frame_76)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_43.addWidget(self.label_60, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_76)

        self.frame_77 = QFrame(self.frame_37)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_61 = QLabel(self.frame_77)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_44.addWidget(self.label_61)

        self.label_62 = QLabel(self.frame_77)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_44.addWidget(self.label_62, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_77)

        self.frame_78 = QFrame(self.frame_37)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_63 = QLabel(self.frame_78)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_45.addWidget(self.label_63)

        self.label_64 = QLabel(self.frame_78)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_45.addWidget(self.label_64, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_78)

        self.frame_79 = QFrame(self.frame_37)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_65 = QLabel(self.frame_79)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_46.addWidget(self.label_65)

        self.label_66 = QLabel(self.frame_79)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_46.addWidget(self.label_66, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_79)

        self.frame_80 = QFrame(self.frame_37)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_57 = QLabel(self.frame_80)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_47.addWidget(self.label_57)

        self.label_58 = QLabel(self.frame_80)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_47.addWidget(self.label_58)


        self.verticalLayout_18.addWidget(self.frame_80)

        self.frame_81 = QFrame(self.frame_37)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_67 = QLabel(self.frame_81)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_48.addWidget(self.label_67)

        self.label_68 = QLabel(self.frame_81)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_48.addWidget(self.label_68, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_81)


        self.horizontalLayout_8.addWidget(self.frame_37)


        self.gridLayout_18.addWidget(self.charger12_main_frame, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.charge_12)

        self.gridLayout_16.addWidget(self.stackedWidget_3, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_29)


        self.gridLayout_12.addWidget(self.frame_24, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.station_1)
        self.station_2 = QWidget()
        self.station_2.setObjectName(u"station_2")
        self.gridLayout_13 = QGridLayout(self.station_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.station2_frame = QFrame(self.station_2)
        self.station2_frame.setObjectName(u"station2_frame")
        self.station2_frame.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.station2_frame.setFrameShape(QFrame.StyledPanel)
        self.station2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.station2_frame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.st1_top_frame = QFrame(self.station2_frame)
        self.st1_top_frame.setObjectName(u"st1_top_frame")
        self.st1_top_frame.setMinimumSize(QSize(0, 70))
        self.st1_top_frame.setSizeIncrement(QSize(0, 40))
        self.st1_top_frame.setFrameShape(QFrame.StyledPanel)
        self.st1_top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.st1_top_frame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(9, -1, -1, -1)
        self.frame_52 = QFrame(self.st1_top_frame)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.location2_btn = QPushButton(self.frame_52)
        self.location2_btn.setObjectName(u"location2_btn")
        self.location2_btn.setMinimumSize(QSize(100, 30))
        self.location2_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 10;\n"
"padding: 3px 5px;")

        self.horizontalLayout_19.addWidget(self.location2_btn)

        self.camera2_btn = QPushButton(self.frame_52)
        self.camera2_btn.setObjectName(u"camera2_btn")
        self.camera2_btn.setMinimumSize(QSize(150, 30))
        self.camera2_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 10;\n"
"padding: 3px 5px;")

        self.horizontalLayout_19.addWidget(self.camera2_btn)


        self.horizontalLayout_17.addWidget(self.frame_52)

        self.frame_51 = QFrame(self.st1_top_frame)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(200, 0))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.st2_charger_comboBox = QComboBox(self.frame_51)
        self.st2_charger_comboBox.addItem("")
        self.st2_charger_comboBox.addItem("")
        self.st2_charger_comboBox.setObjectName(u"st2_charger_comboBox")
        self.st2_charger_comboBox.setGeometry(QRect(40, 10, 150, 35))
        self.st2_charger_comboBox.setMinimumSize(QSize(150, 30))
        self.st2_charger_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 162, 244);")

        self.horizontalLayout_17.addWidget(self.frame_51, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.st1_top_frame, 0, Qt.AlignTop)

        self.frame_50 = QFrame(self.station2_frame)
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
        self.charger21_frame = QFrame(self.page)
        self.charger21_frame.setObjectName(u"charger21_frame")
        self.charger21_frame.setFrameShape(QFrame.StyledPanel)
        self.charger21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.charger21_frame)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.charger21_left_frame = QFrame(self.charger21_frame)
        self.charger21_left_frame.setObjectName(u"charger21_left_frame")
        self.charger21_left_frame.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.charger21_left_frame.setFrameShape(QFrame.StyledPanel)
        self.charger21_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.charger21_left_frame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.cname21_frame = QFrame(self.charger21_left_frame)
        self.cname21_frame.setObjectName(u"cname21_frame")
        self.cname21_frame.setFrameShape(QFrame.StyledPanel)
        self.cname21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.cname21_frame)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.cname21_label = QLabel(self.cname21_frame)
        self.cname21_label.setObjectName(u"cname21_label")
        self.cname21_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_28.addWidget(self.cname21_label)

        self.cname21_value_label = QLabel(self.cname21_frame)
        self.cname21_value_label.setObjectName(u"cname21_value_label")
        self.cname21_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_28.addWidget(self.cname21_value_label)


        self.verticalLayout_20.addWidget(self.cname21_frame)

        self.ctype21_frame = QFrame(self.charger21_left_frame)
        self.ctype21_frame.setObjectName(u"ctype21_frame")
        self.ctype21_frame.setFrameShape(QFrame.StyledPanel)
        self.ctype21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.ctype21_frame)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.ctype21_label = QLabel(self.ctype21_frame)
        self.ctype21_label.setObjectName(u"ctype21_label")
        self.ctype21_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_29.addWidget(self.ctype21_label)

        self.ctype21_value_label = QLabel(self.ctype21_frame)
        self.ctype21_value_label.setObjectName(u"ctype21_value_label")
        self.ctype21_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_29.addWidget(self.ctype21_value_label)


        self.verticalLayout_20.addWidget(self.ctype21_frame)

        self.cid21_frame = QFrame(self.charger21_left_frame)
        self.cid21_frame.setObjectName(u"cid21_frame")
        self.cid21_frame.setFrameShape(QFrame.StyledPanel)
        self.cid21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.cid21_frame)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.cid21_label = QLabel(self.cid21_frame)
        self.cid21_label.setObjectName(u"cid21_label")
        self.cid21_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_30.addWidget(self.cid21_label)

        self.cid21_value_label = QLabel(self.cid21_frame)
        self.cid21_value_label.setObjectName(u"cid21_value_label")
        self.cid21_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_30.addWidget(self.cid21_value_label)


        self.verticalLayout_20.addWidget(self.cid21_frame)

        self.minc21_frame = QFrame(self.charger21_left_frame)
        self.minc21_frame.setObjectName(u"minc21_frame")
        self.minc21_frame.setFrameShape(QFrame.StyledPanel)
        self.minc21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.minc21_frame)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.minc21_label = QLabel(self.minc21_frame)
        self.minc21_label.setObjectName(u"minc21_label")
        self.minc21_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_31.addWidget(self.minc21_label)

        self.minc21_value_label = QLabel(self.minc21_frame)
        self.minc21_value_label.setObjectName(u"minc21_value_label")
        self.minc21_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_31.addWidget(self.minc21_value_label)


        self.verticalLayout_20.addWidget(self.minc21_frame)

        self.maxc21_frame = QFrame(self.charger21_left_frame)
        self.maxc21_frame.setObjectName(u"maxc21_frame")
        self.maxc21_frame.setFrameShape(QFrame.StyledPanel)
        self.maxc21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.maxc21_frame)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.maxc21_label = QLabel(self.maxc21_frame)
        self.maxc21_label.setObjectName(u"maxc21_label")
        self.maxc21_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_32.addWidget(self.maxc21_label)

        self.maxc21_value_label = QLabel(self.maxc21_frame)
        self.maxc21_value_label.setObjectName(u"maxc21_value_label")
        self.maxc21_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_32.addWidget(self.maxc21_value_label)


        self.verticalLayout_20.addWidget(self.maxc21_frame)

        self.voltage21_frame = QFrame(self.charger21_left_frame)
        self.voltage21_frame.setObjectName(u"voltage21_frame")
        self.voltage21_frame.setFrameShape(QFrame.StyledPanel)
        self.voltage21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.voltage21_frame)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.voltage21_label = QLabel(self.voltage21_frame)
        self.voltage21_label.setObjectName(u"voltage21_label")
        self.voltage21_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_33.addWidget(self.voltage21_label)

        self.voltage21_value_label = QLabel(self.voltage21_frame)
        self.voltage21_value_label.setObjectName(u"voltage21_value_label")
        self.voltage21_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_33.addWidget(self.voltage21_value_label)


        self.verticalLayout_20.addWidget(self.voltage21_frame)


        self.horizontalLayout_18.addWidget(self.charger21_left_frame)

        self.charger21_right_frame = QFrame(self.charger21_frame)
        self.charger21_right_frame.setObjectName(u"charger21_right_frame")
        self.charger21_right_frame.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.charger21_right_frame.setFrameShape(QFrame.StyledPanel)
        self.charger21_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.charger21_right_frame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.evid21_frame = QFrame(self.charger21_right_frame)
        self.evid21_frame.setObjectName(u"evid21_frame")
        self.evid21_frame.setFrameShape(QFrame.StyledPanel)
        self.evid21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.evid21_frame)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.evid21_label = QLabel(self.evid21_frame)
        self.evid21_label.setObjectName(u"evid21_label")
        self.evid21_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_34.addWidget(self.evid21_label)

        self.evid21_value_label = QLabel(self.evid21_frame)
        self.evid21_value_label.setObjectName(u"evid21_value_label")
        self.evid21_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_34.addWidget(self.evid21_value_label)


        self.verticalLayout_21.addWidget(self.evid21_frame)

        self.cst21_frame = QFrame(self.charger21_right_frame)
        self.cst21_frame.setObjectName(u"cst21_frame")
        self.cst21_frame.setFrameShape(QFrame.StyledPanel)
        self.cst21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.cst21_frame)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.cst21_label = QLabel(self.cst21_frame)
        self.cst21_label.setObjectName(u"cst21_label")
        self.cst21_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_35.addWidget(self.cst21_label)

        self.cst21_value_label = QLabel(self.cst21_frame)
        self.cst21_value_label.setObjectName(u"cst21_value_label")
        self.cst21_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_35.addWidget(self.cst21_value_label)


        self.verticalLayout_21.addWidget(self.cst21_frame)

        self.soc21_frame = QFrame(self.charger21_right_frame)
        self.soc21_frame.setObjectName(u"soc21_frame")
        self.soc21_frame.setFrameShape(QFrame.StyledPanel)
        self.soc21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.soc21_frame)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.soc21_label = QLabel(self.soc21_frame)
        self.soc21_label.setObjectName(u"soc21_label")
        self.soc21_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_36.addWidget(self.soc21_label)

        self.soc21_value_label = QLabel(self.soc21_frame)
        self.soc21_value_label.setObjectName(u"soc21_value_label")
        self.soc21_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_36.addWidget(self.soc21_value_label)


        self.verticalLayout_21.addWidget(self.soc21_frame)

        self.capacity21_frame = QFrame(self.charger21_right_frame)
        self.capacity21_frame.setObjectName(u"capacity21_frame")
        self.capacity21_frame.setFrameShape(QFrame.StyledPanel)
        self.capacity21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.capacity21_frame)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.capacity21_label = QLabel(self.capacity21_frame)
        self.capacity21_label.setObjectName(u"capacity21_label")
        self.capacity21_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_49.addWidget(self.capacity21_label)

        self.capacity21_value_label = QLabel(self.capacity21_frame)
        self.capacity21_value_label.setObjectName(u"capacity21_value_label")
        self.capacity21_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_49.addWidget(self.capacity21_value_label)


        self.verticalLayout_21.addWidget(self.capacity21_frame)

        self.ecet21_frame = QFrame(self.charger21_right_frame)
        self.ecet21_frame.setObjectName(u"ecet21_frame")
        self.ecet21_frame.setFrameShape(QFrame.StyledPanel)
        self.ecet21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.ecet21_frame)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.ecet21_label = QLabel(self.ecet21_frame)
        self.ecet21_label.setObjectName(u"ecet21_label")
        self.ecet21_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_50.addWidget(self.ecet21_label)

        self.ecet21_value_label = QLabel(self.ecet21_frame)
        self.ecet21_value_label.setObjectName(u"ecet21_value_label")
        self.ecet21_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_50.addWidget(self.ecet21_value_label)


        self.verticalLayout_21.addWidget(self.ecet21_frame)

        self.price21_frame = QFrame(self.charger21_right_frame)
        self.price21_frame.setObjectName(u"price21_frame")
        self.price21_frame.setFrameShape(QFrame.StyledPanel)
        self.price21_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.price21_frame)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.price21_label = QLabel(self.price21_frame)
        self.price21_label.setObjectName(u"price21_label")
        self.price21_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_51.addWidget(self.price21_label)

        self.price21_value_label = QLabel(self.price21_frame)
        self.price21_value_label.setObjectName(u"price21_value_label")
        self.price21_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_51.addWidget(self.price21_value_label)


        self.verticalLayout_21.addWidget(self.price21_frame)


        self.horizontalLayout_18.addWidget(self.charger21_right_frame)


        self.gridLayout_24.addWidget(self.charger21_frame, 0, 0, 1, 1)

        self.stackedWidget_4.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_26 = QGridLayout(self.page_2)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.charger22_frame = QFrame(self.page_2)
        self.charger22_frame.setObjectName(u"charger22_frame")
        self.charger22_frame.setFrameShape(QFrame.StyledPanel)
        self.charger22_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.charger22_frame)
        self.horizontalLayout_27.setSpacing(10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.charger22_left_frame = QFrame(self.charger22_frame)
        self.charger22_left_frame.setObjectName(u"charger22_left_frame")
        self.charger22_left_frame.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.charger22_left_frame.setFrameShape(QFrame.StyledPanel)
        self.charger22_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.charger22_left_frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.cname22_frame = QFrame(self.charger22_left_frame)
        self.cname22_frame.setObjectName(u"cname22_frame")
        self.cname22_frame.setFrameShape(QFrame.StyledPanel)
        self.cname22_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.cname22_frame)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.cname22_label = QLabel(self.cname22_frame)
        self.cname22_label.setObjectName(u"cname22_label")
        self.cname22_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_52.addWidget(self.cname22_label)

        self.cname22_value_label = QLabel(self.cname22_frame)
        self.cname22_value_label.setObjectName(u"cname22_value_label")
        self.cname22_value_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_52.addWidget(self.cname22_value_label)


        self.verticalLayout_23.addWidget(self.cname22_frame)

        self.ctype22_frame = QFrame(self.charger22_left_frame)
        self.ctype22_frame.setObjectName(u"ctype22_frame")
        self.ctype22_frame.setFrameShape(QFrame.StyledPanel)
        self.ctype22_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.ctype22_frame)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_95 = QLabel(self.ctype22_frame)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_53.addWidget(self.label_95)

        self.label_96 = QLabel(self.ctype22_frame)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_53.addWidget(self.label_96)


        self.verticalLayout_23.addWidget(self.ctype22_frame)

        self.frame_99 = QFrame(self.charger22_left_frame)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_97 = QLabel(self.frame_99)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_54.addWidget(self.label_97)

        self.label_98 = QLabel(self.frame_99)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_54.addWidget(self.label_98)


        self.verticalLayout_23.addWidget(self.frame_99)

        self.frame_100 = QFrame(self.charger22_left_frame)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_99 = QLabel(self.frame_100)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_55.addWidget(self.label_99)

        self.label_100 = QLabel(self.frame_100)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_55.addWidget(self.label_100)


        self.verticalLayout_23.addWidget(self.frame_100)

        self.frame_101 = QFrame(self.charger22_left_frame)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_101 = QLabel(self.frame_101)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_56.addWidget(self.label_101)

        self.label_102 = QLabel(self.frame_101)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_56.addWidget(self.label_102)


        self.verticalLayout_23.addWidget(self.frame_101)

        self.frame_102 = QFrame(self.charger22_left_frame)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_103 = QLabel(self.frame_102)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_57.addWidget(self.label_103)

        self.label_104 = QLabel(self.frame_102)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_57.addWidget(self.label_104)


        self.verticalLayout_23.addWidget(self.frame_102)


        self.horizontalLayout_27.addWidget(self.charger22_left_frame)

        self.frame_96 = QFrame(self.charger22_frame)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_96)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_103 = QFrame(self.frame_96)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_105 = QLabel(self.frame_103)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_58.addWidget(self.label_105)

        self.label_106 = QLabel(self.frame_103)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_58.addWidget(self.label_106)


        self.verticalLayout_22.addWidget(self.frame_103)

        self.frame_104 = QFrame(self.frame_96)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_107 = QLabel(self.frame_104)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_59.addWidget(self.label_107)

        self.label_108 = QLabel(self.frame_104)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_59.addWidget(self.label_108)


        self.verticalLayout_22.addWidget(self.frame_104)

        self.frame_105 = QFrame(self.frame_96)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_109 = QLabel(self.frame_105)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_60.addWidget(self.label_109)

        self.label_110 = QLabel(self.frame_105)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_60.addWidget(self.label_110)


        self.verticalLayout_22.addWidget(self.frame_105)

        self.frame_106 = QFrame(self.frame_96)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_111 = QLabel(self.frame_106)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_61.addWidget(self.label_111)

        self.label_112 = QLabel(self.frame_106)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_61.addWidget(self.label_112)


        self.verticalLayout_22.addWidget(self.frame_106)

        self.frame_107 = QFrame(self.frame_96)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_107)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_113 = QLabel(self.frame_107)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_62.addWidget(self.label_113)

        self.label_114 = QLabel(self.frame_107)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_62.addWidget(self.label_114)


        self.verticalLayout_22.addWidget(self.frame_107)

        self.frame_108 = QFrame(self.frame_96)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_108)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_115 = QLabel(self.frame_108)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_63.addWidget(self.label_115)

        self.label_116 = QLabel(self.frame_108)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_63.addWidget(self.label_116)


        self.verticalLayout_22.addWidget(self.frame_108)


        self.horizontalLayout_27.addWidget(self.frame_96)


        self.gridLayout_26.addWidget(self.charger22_frame, 0, 0, 1, 1)

        self.stackedWidget_4.addWidget(self.page_2)

        self.gridLayout_23.addWidget(self.stackedWidget_4, 0, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_50)


        self.gridLayout_13.addWidget(self.station2_frame, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.station_2)

        self.gridLayout_11.addWidget(self.stackedWidget_2, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.chargers_frame)


        self.gridLayout_2.addWidget(self.Station_main_frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.stations_page)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.gridLayout_3 = QGridLayout(self.report_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_7 = QFrame(self.report_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_7)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.tabWidget = QTabWidget(self.frame_7)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
"border: none;")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.sales_tab = QWidget()
        self.sales_tab.setObjectName(u"sales_tab")
        self.gridLayout_20 = QGridLayout(self.sales_tab)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.sales_frame = QFrame(self.sales_tab)
        self.sales_frame.setObjectName(u"sales_frame")
        self.sales_frame.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.sales_frame.setFrameShape(QFrame.StyledPanel)
        self.sales_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.sales_frame)
        self.gridLayout_25.setObjectName(u"gridLayout_25")

        self.gridLayout_20.addWidget(self.sales_frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.sales_tab, "")
        self.managemet_cost_tab = QWidget()
        self.managemet_cost_tab.setObjectName(u"managemet_cost_tab")
        self.gridLayout_21 = QGridLayout(self.managemet_cost_tab)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.managemet_cost_frame = QFrame(self.managemet_cost_tab)
        self.managemet_cost_frame.setObjectName(u"managemet_cost_frame")
        self.managemet_cost_frame.setFrameShape(QFrame.StyledPanel)
        self.managemet_cost_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_21.addWidget(self.managemet_cost_frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.managemet_cost_tab, "")
        self.electricity_cost_tab = QWidget()
        self.electricity_cost_tab.setObjectName(u"electricity_cost_tab")
        self.gridLayout_22 = QGridLayout(self.electricity_cost_tab)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.electricity_cost_frame = QFrame(self.electricity_cost_tab)
        self.electricity_cost_frame.setObjectName(u"electricity_cost_frame")
        self.electricity_cost_frame.setFrameShape(QFrame.StyledPanel)
        self.electricity_cost_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_22.addWidget(self.electricity_cost_frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.electricity_cost_tab, "")

        self.gridLayout_19.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.report_page)
        self.account_page_2 = QWidget()
        self.account_page_2.setObjectName(u"account_page_2")
        self.gridLayout_4 = QGridLayout(self.account_page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.account_main_frame = QFrame(self.account_page_2)
        self.account_main_frame.setObjectName(u"account_main_frame")
        self.account_main_frame.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.account_main_frame.setFrameShape(QFrame.StyledPanel)
        self.account_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.account_main_frame)
        self.verticalLayout_14.setSpacing(8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.account_main_frame)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.top_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.top_header_frame = QFrame(self.top_frame)
        self.top_header_frame.setObjectName(u"top_header_frame")
        self.top_header_frame.setMinimumSize(QSize(0, 50))
        self.top_header_frame.setFrameShape(QFrame.StyledPanel)
        self.top_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.top_header_frame)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.frame_22 = QFrame(self.top_header_frame)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(250, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label = QLabel(self.frame_22)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(35, 35))
        self.label.setStyleSheet(u"border-image: url(:/newPrefix/\ud83e\udd86 icon _User Circle_.png);")

        self.horizontalLayout_68.addWidget(self.label)

        self.label_2 = QLabel(self.frame_22)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"")

        self.horizontalLayout_68.addWidget(self.label_2)


        self.horizontalLayout_67.addWidget(self.frame_22, 0, Qt.AlignLeft)

        self.frame_20 = QFrame(self.top_header_frame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(50, 0))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_20)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.pushButton = QPushButton(self.frame_20)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(50, 50))
        self.pushButton.setStyleSheet(u"border-image: url(:/newPrefix/\ud83e\udd86 icon _User Edit_.png);")

        self.gridLayout_14.addWidget(self.pushButton, 0, 0, 1, 1)


        self.horizontalLayout_67.addWidget(self.frame_20, 0, Qt.AlignRight)


        self.verticalLayout_16.addWidget(self.top_header_frame, 0, Qt.AlignTop)

        self.info_frame = QFrame(self.top_frame)
        self.info_frame.setObjectName(u"info_frame")
        sizePolicy.setHeightForWidth(self.info_frame.sizePolicy().hasHeightForWidth())
        self.info_frame.setSizePolicy(sizePolicy)
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.info_frame)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.info_left_frame = QFrame(self.info_frame)
        self.info_left_frame.setObjectName(u"info_left_frame")
        self.info_left_frame.setFrameShape(QFrame.StyledPanel)
        self.info_left_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.info_left_frame)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_name = QLabel(self.info_left_frame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"Consolas\";")

        self.gridLayout_15.addWidget(self.label_name, 0, 0, 1, 1)

        self.label_name_value = QLabel(self.info_left_frame)
        self.label_name_value.setObjectName(u"label_name_value")
        self.label_name_value.setStyleSheet(u"background-color: rgb(34, 34, 34);\n"
"border: none;\n"
"border-radius: 10;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Consolas\";")
        self.label_name_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_name_value, 0, 1, 1, 1)

        self.label_sid = QLabel(self.info_left_frame)
        self.label_sid.setObjectName(u"label_sid")
        self.label_sid.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"Consolas\";")

        self.gridLayout_15.addWidget(self.label_sid, 1, 0, 1, 1)

        self.label_sid_value = QLabel(self.info_left_frame)
        self.label_sid_value.setObjectName(u"label_sid_value")
        self.label_sid_value.setStyleSheet(u"background-color: rgb(34, 34, 34);\n"
"border: none;\n"
"border-radius: 10;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Consolas\";")
        self.label_sid_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_sid_value, 1, 1, 1, 1)

        self.label_mail = QLabel(self.info_left_frame)
        self.label_mail.setObjectName(u"label_mail")
        self.label_mail.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"Consolas\";")

        self.gridLayout_15.addWidget(self.label_mail, 2, 0, 1, 1)

        self.label_mail_value = QLabel(self.info_left_frame)
        self.label_mail_value.setObjectName(u"label_mail_value")
        self.label_mail_value.setStyleSheet(u"background-color: rgb(34, 34, 34);\n"
"border: none;\n"
"border-radius: 10;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Consolas\";")
        self.label_mail_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_mail_value, 2, 1, 1, 1)

        self.label_status = QLabel(self.info_left_frame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"Consolas\";")

        self.gridLayout_15.addWidget(self.label_status, 3, 0, 1, 1)

        self.label_status_value = QLabel(self.info_left_frame)
        self.label_status_value.setObjectName(u"label_status_value")
        self.label_status_value.setStyleSheet(u"background-color: rgb(34, 34, 34);\n"
"border: none;\n"
"border-radius: 10;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Consolas\";")
        self.label_status_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_status_value, 3, 1, 1, 1)


        self.horizontalLayout_73.addWidget(self.info_left_frame)

        self.info_right_frame = QFrame(self.info_frame)
        self.info_right_frame.setObjectName(u"info_right_frame")
        self.info_right_frame.setFrameShape(QFrame.StyledPanel)
        self.info_right_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.info_right_frame)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_total_stations = QLabel(self.info_right_frame)
        self.label_total_stations.setObjectName(u"label_total_stations")
        self.label_total_stations.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"Consolas\";")

        self.gridLayout_27.addWidget(self.label_total_stations, 0, 0, 1, 1)

        self.label_otal_stations_value = QLabel(self.info_right_frame)
        self.label_otal_stations_value.setObjectName(u"label_otal_stations_value")
        self.label_otal_stations_value.setStyleSheet(u"background-color: rgb(34, 34, 34);\n"
"border: none;\n"
"border-radius: 5;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Consolas\";")
        self.label_otal_stations_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.label_otal_stations_value, 0, 1, 1, 1)

        self.view_map_button = QPushButton(self.info_right_frame)
        self.view_map_button.setObjectName(u"view_map_button")
        self.view_map_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"Consolas\";\n"
"background-color: rgb(50, 162, 244);\n"
"border: none;\n"
"border-radius: 5;\n"
"padding: 3px 5px;")

        self.gridLayout_27.addWidget(self.view_map_button, 0, 2, 1, 1)

        self.frame_toshow_stations = QFrame(self.info_right_frame)
        self.frame_toshow_stations.setObjectName(u"frame_toshow_stations")
        self.frame_toshow_stations.setFrameShape(QFrame.StyledPanel)
        self.frame_toshow_stations.setFrameShadow(QFrame.Raised)

        self.gridLayout_27.addWidget(self.frame_toshow_stations, 1, 0, 1, 3)


        self.horizontalLayout_73.addWidget(self.info_right_frame)


        self.verticalLayout_16.addWidget(self.info_frame)


        self.verticalLayout_14.addWidget(self.top_frame)

        self.bottom_frame = QFrame(self.account_main_frame)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_20.setSpacing(8)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.bleft_frame = QFrame(self.bottom_frame)
        self.bleft_frame.setObjectName(u"bleft_frame")
        self.bleft_frame.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.bleft_frame.setFrameShape(QFrame.StyledPanel)
        self.bleft_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.bleft_frame)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_16 = QFrame(self.bleft_frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 50))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_4 = QLabel(self.frame_16)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";")

        self.horizontalLayout_70.addWidget(self.label_4)


        self.verticalLayout_25.addWidget(self.frame_16, 0, Qt.AlignTop)

        self.frame_18 = QFrame(self.bleft_frame)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMinimumSize(QSize(0, 0))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.frame_18)


        self.horizontalLayout_20.addWidget(self.bleft_frame)

        self.bright_frame = QFrame(self.bottom_frame)
        self.bright_frame.setObjectName(u"bright_frame")
        self.bright_frame.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.bright_frame.setFrameShape(QFrame.StyledPanel)
        self.bright_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.bright_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_17 = QFrame(self.bright_frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_3 = QLabel(self.frame_17)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"")

        self.horizontalLayout_69.addWidget(self.label_3)

        self.frame_25 = QFrame(self.frame_17)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(230, 40))
        self.frame_25.setStyleSheet(u"background-color: rgb(34, 34, 34);\n"
"border: none;\n"
"border-radius: 15;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.pushButton_2 = QPushButton(self.frame_25)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(10, 10))
        self.pushButton_2.setMaximumSize(QSize(20, 20))
        self.pushButton_2.setStyleSheet(u"border-image: url(:/newPrefix/\ud83e\udd86 icon _Search_.png);")

        self.horizontalLayout_72.addWidget(self.pushButton_2)

        self.lineEdit = QLineEdit(self.frame_25)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_72.addWidget(self.lineEdit)


        self.horizontalLayout_69.addWidget(self.frame_25)


        self.verticalLayout_17.addWidget(self.frame_17, 0, Qt.AlignTop)

        self.frame_19 = QFrame(self.bright_frame)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.frame_19)


        self.horizontalLayout_20.addWidget(self.bright_frame)


        self.verticalLayout_14.addWidget(self.bottom_frame)


        self.gridLayout_4.addWidget(self.account_main_frame, 0, 0, 1, 1)

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
        self.frame_62.setMinimumSize(QSize(0, 100))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.label_25 = QLabel(self.frame_62)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 10, 631, 100))
        self.label_25.setMinimumSize(QSize(0, 100))
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 36pt \"MS Shell Dlg 2\";")

        self.verticalLayout_15.addWidget(self.frame_62, 0, Qt.AlignTop)

        self.frame_63 = QFrame(self.frame_61)
        self.frame_63.setObjectName(u"frame_63")
        sizePolicy.setHeightForWidth(self.frame_63.sizePolicy().hasHeightForWidth())
        self.frame_63.setSizePolicy(sizePolicy)
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_63)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_26 = QLabel(self.frame_63)
        self.label_26.setObjectName(u"label_26")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy1)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Calibri\";")
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_26.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.label_26)


        self.verticalLayout_15.addWidget(self.frame_63)


        self.gridLayout_7.addWidget(self.frame_61, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.about_page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.main_bar)


        self.verticalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.st1_charger_comboBox.currentIndexChanged.connect(self.stackedWidget_3.setCurrentIndex)
        self.stations_comboBox.currentIndexChanged.connect(self.stackedWidget_2.setCurrentIndex)
        self.st2_charger_comboBox.currentIndexChanged.connect(self.stackedWidget_4.setCurrentIndex)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(2)


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
        self.occupied_chargers_label.setText(QCoreApplication.translate("MainWindow", u"Occupied Chargers", None))
        self.total_chargers_label.setText(QCoreApplication.translate("MainWindow", u"Total Chargers", None))
        self.available_chargers_label.setText(QCoreApplication.translate("MainWindow", u"Available Chargers", None))
        self.percentage_label.setText(QCoreApplication.translate("MainWindow", u"Percentage of Chargers in use ", None))
        self.co2_heading_label.setText(QCoreApplication.translate("MainWindow", u"Carbon Foot print Reduction", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CO2 Saved", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"10 Units", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Fuel Replaced", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"20 Units", None))
        self.revenue_heading_label.setText(QCoreApplication.translate("MainWindow", u"Monthly Revenue", None))
        self.stations_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Station 1", None))
        self.stations_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Station 2", None))

        self.location1_btn.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.camera1_btn.setText(QCoreApplication.translate("MainWindow", u"Camera View", None))
        self.st1_charger_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Charger 1", None))
        self.st1_charger_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Charger 2", None))

        self.cname11_label.setText(QCoreApplication.translate("MainWindow", u"Charger Name", None))
        self.cname11_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.ctype11_label.setText(QCoreApplication.translate("MainWindow", u"Charger Type", None))
        self.ctype11_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.cid11_label.setText(QCoreApplication.translate("MainWindow", u"Charger ID", None))
        self.cid11_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.minc11_label.setText(QCoreApplication.translate("MainWindow", u"Minimum Current", None))
        self.minc11_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.maxc11_label.setText(QCoreApplication.translate("MainWindow", u"Maximum Current", None))
        self.maxc11_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.voltage11_label.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.voltage11_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.evid11_label.setText(QCoreApplication.translate("MainWindow", u"EV ID", None))
        self.evid11_value_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cst11_label.setText(QCoreApplication.translate("MainWindow", u"Charging start Time", None))
        self.cst11_value_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.soc11_label.setText(QCoreApplication.translate("MainWindow", u"Current SOC", None))
        self.soc11_value_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.capacity11_label.setText(QCoreApplication.translate("MainWindow", u"Total Capacity", None))
        self.capacity11_value_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ecet11_label.setText(QCoreApplication.translate("MainWindow", u"Expected Charging End Time", None))
        self.ecet11_value_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.price11_label.setText(QCoreApplication.translate("MainWindow", u"Expected Price", None))
        self.price11_value_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cname12_label.setText(QCoreApplication.translate("MainWindow", u"Charger name", None))
        self.cname12_value_label.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.ctype12_label.setText(QCoreApplication.translate("MainWindow", u"Charger Type", None))
        self.ctype12_value_label.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.cid12_label.setText(QCoreApplication.translate("MainWindow", u"Charger ID", None))
        self.cid12_value_label.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.minc12_label.setText(QCoreApplication.translate("MainWindow", u"Minimum Current", None))
        self.minc12_value_label.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.maxc12_label.setText(QCoreApplication.translate("MainWindow", u"Maximum Current", None))
        self.maxc12_value_label.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.voltage12_label.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.voltage12_value_label.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"EV ID", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Charging start Time", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Current SOC", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Total Capacity", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Expected Charging End Time", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Expected Price", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.location2_btn.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.camera2_btn.setText(QCoreApplication.translate("MainWindow", u"Camera View", None))
        self.st2_charger_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Charger 1", None))
        self.st2_charger_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Charger 2", None))

        self.cname21_label.setText(QCoreApplication.translate("MainWindow", u"Charger Name", None))
        self.cname21_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.ctype21_label.setText(QCoreApplication.translate("MainWindow", u"Charger Type", None))
        self.ctype21_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.cid21_label.setText(QCoreApplication.translate("MainWindow", u"Charger ID", None))
        self.cid21_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.minc21_label.setText(QCoreApplication.translate("MainWindow", u"Minimum Current", None))
        self.minc21_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.maxc21_label.setText(QCoreApplication.translate("MainWindow", u"Maximum Current", None))
        self.maxc21_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.voltage21_label.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.voltage21_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.evid21_label.setText(QCoreApplication.translate("MainWindow", u"EV ID", None))
        self.evid21_value_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cst21_label.setText(QCoreApplication.translate("MainWindow", u"Chrging Start Time", None))
        self.cst21_value_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.soc21_label.setText(QCoreApplication.translate("MainWindow", u"Current SOC", None))
        self.soc21_value_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.capacity21_label.setText(QCoreApplication.translate("MainWindow", u"Total Capacity", None))
        self.capacity21_value_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ecet21_label.setText(QCoreApplication.translate("MainWindow", u"Expected Charging End Time", None))
        self.ecet21_value_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.price21_label.setText(QCoreApplication.translate("MainWindow", u"Expected Price", None))
        self.price21_value_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cname22_label.setText(QCoreApplication.translate("MainWindow", u"Charger Name", None))
        self.cname22_value_label.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Charger Type", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Charger ID", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Minimum Current", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Maximum Current", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"EV ID", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Charging Start Time", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Current SOC", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Total Capacity", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Expected Charging End Time", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Expected Price", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sales_tab), QCoreApplication.translate("MainWindow", u"Sales", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.managemet_cost_tab), QCoreApplication.translate("MainWindow", u"Management Cost", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.electricity_cost_tab), QCoreApplication.translate("MainWindow", u"Electricity Cost", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.pushButton.setText("")
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_name_value.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_sid.setText(QCoreApplication.translate("MainWindow", u"Seller Id", None))
        self.label_sid_value.setText(QCoreApplication.translate("MainWindow", u"12345", None))
        self.label_mail.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_mail_value.setText(QCoreApplication.translate("MainWindow", u"abc@gmail.com", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Account Status", None))
        self.label_status_value.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.label_total_stations.setText(QCoreApplication.translate("MainWindow", u"Stations Managed", None))
        self.label_otal_stations_value.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.view_map_button.setText(QCoreApplication.translate("MainWindow", u"View Map", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Recent Updates", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.pushButton_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Our Mission", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"In the next 20 years, EVs will replace ICE vehicles as the main way that people move around. We are living through a revolution in not only how we move, but how we store and use energy. 25% of all end-use global energy is spent on transportation (37% in North America). Switching from gas to electric fuel for transportation will require the largest global infrastructure overhaul of our lives\u2014from new renewable power generation, to how we transmit, distribute, store, and use electricity.\n"
"\u200d\n"
"EV Charge\u2019s mission is to build EV charging solutions that scale. This means making EV charger deployment fast and affordable. And making charging easy and reliable for every EV driver.\n"
"\u200d\n"
"EV Charge sits at the nexus point between vehicles, building owners, and the grid. With software, we can help buildings, communities, and entire cities charge more EVs than their infrastructure would otherwise allow. We can optimize charging for grid capacity, cost, or carbon impact. And we can enable bi-di"
                        "rectional communication between individual EVs and the grid.", None))
    # retranslateUi

