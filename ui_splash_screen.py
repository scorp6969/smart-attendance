# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenAtIuNf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(720, 450)
        SplashScreen.setMinimumSize(QSize(720, 450))
        SplashScreen.setMaximumSize(QSize(720, 450))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        self.dropShadowFrame.setFont(font)
        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
"background-color: #745544;\n"
"color: #ffffff;\n"
"border-radius: 20px;\n"
"}\n"
"QLabel{\n"
"color:#f0dabe;\n"
"}\n"
"")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(20, 50, 661, 91))
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(45)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: #ffffff;")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(20, 150, 661, 41))
        font2 = QFont()
        font2.setFamily(u"Comic Sans MS")
        font2.setPointSize(16)
        self.label_description.setFont(font2)
        self.label_description.setStyleSheet(u"")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 280, 611, 31))
        font3 = QFont()
        font3.setFamily(u"Comic Sans MS")
        font3.setPointSize(10)
        self.progressBar.setFont(font3)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"background-color: rgb(173, 203, 227);\n"
"color: #0e1111;\n"
"border-style: none;\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523,\n"
"stop:0 #386c80, stop:1 rgb(242,227,208));\n"
"}\n"
"")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(20, 310, 661, 31))
        font4 = QFont()
        font4.setFamily(u"Comic Sans MS")
        font4.setPointSize(13)
        self.label_loading.setFont(font4)
        self.label_loading.setStyleSheet(u"")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(70, 390, 621, 31))
        font5 = QFont()
        font5.setFamily(u"Comic Sans MS")
        font5.setPointSize(11)
        self.label_credits.setFont(font5)
        self.label_credits.setStyleSheet(u"")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\"\n"
"                                    font-weight:600;\">S</span>mart<span style=\" font-weight:600;\">\n"
"                                    A</span>ttendance</p></body></html>\n"
"                                ", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\"\n"
"                                    font-weight:600;\">F</span>ace <span style=\" font-weight:600;\">R</span>ecognition\n"
"                                    <span style=\" font-weight:600;\">A</span>ttendance <span\n"
"                                    style=\" font-weight:600;\">S</span>ystem</p></body></html>\n"
"                                ", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\"\n"
"                                    font-weight:600;\">Created By</span>: Dipesh, Sayal, Shekhar, Prince</p></body></html>\n"
"                                ", None))
    # retranslateUi

