# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainaHqoUu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import account_rc
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
        self.left_menu = QCustomSlideMenu(self.main)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(180, 0))
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

        self.security = QPushButton(self.frame_3)
        self.security.setObjectName(u"security")
        self.security.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";\n"
"padding: 3px 5px;")

        self.verticalLayout_4.addWidget(self.security)

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
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.main_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.main_bar)


        self.verticalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

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
        self.security.setText(QCoreApplication.translate("MainWindow", u"Security", None))
        self.my_account.setText(QCoreApplication.translate("MainWindow", u"My Account", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.About.setText(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

