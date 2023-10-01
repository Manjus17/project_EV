# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startnanqsj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import logo_rc
import google_rc
import apple_rc
import add_rc
import next_rc
import log_in_rc
import sign_in_rc

class Ui_StartWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(844, 511)
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
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(400, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(600, 16777215))
        self.label.setStyleSheet(u"border-image: url(:/newPrefix/image1.png);")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_2)

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
        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_7 = QFrame(self.frame_6)
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

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, -1, 0)
        self.pushButton = QPushButton(self.frame_8)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 55))
        self.pushButton.setMaximumSize(QSize(250, 16777215))
        self.pushButton.setStyleSheet(u"border-image: url(:/newPrefix/create_account.png);")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(80, 50))
        self.pushButton_2.setMaximumSize(QSize(100, 16777215))
        self.pushButton_2.setStyleSheet(u"border-image: url(:/newPrefix/button_2.png);")

        self.horizontalLayout_2.addWidget(self.pushButton_2, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame_8, 0, Qt.AlignTop)


        self.gridLayout_6.addWidget(self.frame_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_7 = QGridLayout(self.page_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_10 = QFrame(self.page_3)
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
        self.label_5 = QLabel(self.frame_15)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 338, 60))
        self.label_5.setMinimumSize(QSize(0, 60))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 26pt \"MS Shell Dlg 2\";\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.frame_15, 0, Qt.AlignTop)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lineEdit = QLineEdit(self.frame_16)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 60))
        self.lineEdit.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 6px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_16)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 60))
        self.lineEdit_2.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 6px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame_16)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 60))
        self.lineEdit_3.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 6px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.lineEdit_3)

        self.lineEdit_5 = QLineEdit(self.frame_16)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 60))
        self.lineEdit_5.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 6px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.lineEdit_5)

        self.lineEdit_4 = QLineEdit(self.frame_16)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 60))
        self.lineEdit_4.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 6px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.lineEdit_4)


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

        self.pushButton_3 = QPushButton(self.frame_14)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(30, 30))
        self.pushButton_3.setStyleSheet(u"border-image: url(:/newPrefix/button_4.png);")

        self.horizontalLayout_4.addWidget(self.pushButton_3, 0, Qt.AlignLeft)

        self.pushButton_6 = QPushButton(self.frame_14)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(100, 65))
        self.pushButton_6.setStyleSheet(u"border-image: url(:/newPrefix/button_1.png);")

        self.horizontalLayout_4.addWidget(self.pushButton_6)


        self.verticalLayout_4.addWidget(self.frame_14)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"border-top: 2px solid white;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_4 = QPushButton(self.frame_12)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 45))
        self.pushButton_4.setMaximumSize(QSize(45, 16777215))
        self.pushButton_4.setStyleSheet(u"border-image: url(:/newPrefix/apple.png);")

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_12)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 40))
        self.pushButton_5.setMaximumSize(QSize(40, 16777215))
        self.pushButton_5.setStyleSheet(u"border-image: url(:/newPrefix/google.png);")

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_4.addWidget(self.frame_12)


        self.verticalLayout_5.addWidget(self.frame_11)


        self.gridLayout_7.addWidget(self.frame_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_8 = QGridLayout(self.page_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_17 = QFrame(self.page_4)
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
        self.label_6 = QLabel(self.frame_18)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 342, 70))
        self.label_6.setMinimumSize(QSize(0, 70))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 26pt \"MS Shell Dlg 2\";")
        self.label_6.setAlignment(Qt.AlignCenter)

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
        self.lineEdit_6 = QLineEdit(self.frame_19)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 70))
        self.lineEdit_6.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_8.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.frame_19)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 70))
        self.lineEdit_7.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"padding-left: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_8.addWidget(self.lineEdit_7)


        self.verticalLayout_7.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(200, 80))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_20)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_7 = QPushButton(self.frame_20)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(100, 65))
        self.pushButton_7.setMaximumSize(QSize(120, 70))
        self.pushButton_7.setStyleSheet(u"border-image: url(:/newPrefix/button_1.png);")

        self.gridLayout_9.addWidget(self.pushButton_7, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_20, 0, Qt.AlignTop)


        self.gridLayout_8.addWidget(self.frame_17, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)

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
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Plug Into Better", None))
        self.pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Already have an account", None))
        self.pushButton_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seller Id", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Add Image", None))
        self.pushButton_3.setText("")
        self.pushButton_6.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton_7.setText("")
    # retranslateUi

