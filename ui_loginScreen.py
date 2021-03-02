# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginScreenEmAcqf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import nike_app_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(900, 460)
        LoginWindow.setMinimumSize(QSize(900, 460))
        LoginWindow.setMaximumSize(QSize(900, 460))
        LoginWindow.setStyleSheet(u"background-color: #876645;\n"
"border-radius:30px;\n"
"")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #876645;\n"
"border-radius:30px;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"Qframe{\n"
"border-radius:30px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: #876645;\n"
"}\n"
"QLabel{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 3px solid #7289da;\n"
"	border-radius:35px;\n"
"}\n"
"QLineEdit{\n"
"	background-color: 	#424549;\n"
"	border-radius: 20px;\n"
"	padding:10px;\n"
"	border:2px solid #7289da;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 35px;\n"
"	border: 3px solid #7289da;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 120, 201, 211))
        self.label_4.setStyleSheet(u"image: url(:/icons2/icons2/login.png);\n"
"border:none;\n"
"background-color: #876645;\n"
"")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.login_res_frame = QFrame(self.frame_2)
        self.login_res_frame.setObjectName(u"login_res_frame")
        self.login_res_frame.setGeometry(QRect(20, 40, 391, 231))
        self.login_res_frame.setMinimumSize(QSize(0, 0))
        self.login_res_frame.setMaximumSize(QSize(600, 300))
        self.login_res_frame.setStyleSheet(u"QFrame{\n"
"color: rgb(0, 0, 0);\n"
"background-color: #f2e3d0;\n"
"border: 2px solid rgb(66, 69, 73);\n"
"border-radius: 30px;\n"
"}\n"
"QPushButton{\n"
"	background-color: #4e6a50;\n"
"	border-radius: 25px;\n"
"	border: 3px solid rgb(66, 69, 73);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QLabel{\n"
"padding: 10px;\n"
"border: none;\n"
"background-color: 	#f0dabe;\n"
"}\n"
"                                                                        ")
        self.login_res_frame.setFrameShape(QFrame.StyledPanel)
        self.login_res_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.login_res_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.login_res_msg = QLabel(self.login_res_frame)
        self.login_res_msg.setObjectName(u"login_res_msg")
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_res_msg.setFont(font)
        self.login_res_msg.setScaledContents(False)
        self.login_res_msg.setAlignment(Qt.AlignCenter)
        self.login_res_msg.setWordWrap(True)
        self.login_res_msg.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_17.addWidget(self.login_res_msg)

        self.login_res_ok_btn = QPushButton(self.login_res_frame)
        self.login_res_ok_btn.setObjectName(u"login_res_ok_btn")
        self.login_res_ok_btn.setMinimumSize(QSize(80, 50))
        self.login_res_ok_btn.setMaximumSize(QSize(80, 50))
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.login_res_ok_btn.setFont(font1)
        self.login_res_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_17.addWidget(self.login_res_ok_btn, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-140, -140, 200, 200))
        self.label_3.setStyleSheet(u"border:none;\n"
"border-radius:100px;\n"
"background-color:	#f0ca8f;")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-140, 370, 200, 200))
        self.label_6.setStyleSheet(u"border:none;\n"
"border-radius:100px;\n"
"background-color:	#f0ca8f;")

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: #876645;\n"
"}\n"
"QLabel{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 3px solid #7289da;\n"
"	border-radius:35px;\n"
"}\n"
"QLineEdit{\n"
"	background-color: 	#424549;\n"
"	border-radius: 30px;\n"
"	padding:10px;\n"
"	border:2px solid #7289da;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 35px;\n"
"	border: 3px solid #7289da;\n"
"}\n"
"QPushButton:hover{	\n"
"	border: 3px solid rgb(160, 178, 191);\n"
"}\n"
"QCheckBox{\n"
"	background-color: #876645;\n"
"}\n"
"QCheckBox::indicator {\n"
"image: url(:/icons/icons/cil-lock-locked.png);\n"
"background-color: rgb(66, 69, 73);\n"
"width: 40px;\n"
"height: 40px;\n"
"border-radius:20px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	image: url(:/icons/icons/cil-lock-unlocked.png);\n"
"}\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 20, 100, 70))
        font2 = QFont()
        font2.setFamily(u"Comic Sans MS")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: #876645;\n"
"border: none;\n"
"image: url(:/icons/icons/user.png);\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QRect(270, 360, 41, 51))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"border:none;\n"
"image: url(:/icons/icons/enter.png);")
        self.pushButton_3.setIconSize(QSize(24, 24))
        self.login_button = QPushButton(self.frame_3)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(100, 350, 241, 71))
        font3 = QFont()
        font3.setFamily(u"Comic Sans MS")
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setWeight(75)
        self.login_button.setFont(font3)
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_button.setStyleSheet(u"")
        self.login_button.setIconSize(QSize(24, 24))
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 130, 321, 71))
        self.lineEdit.setFont(font1)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 130, 71, 71))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u":/icons/icons/profile-user.png"))
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 240, 311, 71))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 240, 71, 71))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u":/icons/icons/password (1).png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(370, -140, 200, 200))
        self.label_8.setStyleSheet(u"border:none;\n"
"border-radius:100px;\n"
"background-color:	#f0ca8f;")
        self.close_btn = QPushButton(self.frame_3)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(400, 0, 40, 40))
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"border-radius:20px;\n"
"border: none;\n"
"background-color:	#f0ca8f;\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(24, 24))
        self.pass_show_hide = QCheckBox(self.frame_3)
        self.pass_show_hide.setObjectName(u"pass_show_hide")
        self.pass_show_hide.setGeometry(QRect(350, 250, 41, 61))
        self.pass_show_hide.setMinimumSize(QSize(0, 0))
        self.pass_show_hide.setMaximumSize(QSize(210, 100))
        self.pass_show_hide.setFont(font)
        self.pass_show_hide.setCursor(QCursor(Qt.ArrowCursor))
        self.login_button.raise_()
        self.label_5.raise_()
        self.pushButton_3.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()
        self.label_8.raise_()
        self.close_btn.raise_()
        self.pass_show_hide.raise_()

        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        self.close_btn.clicked.connect(LoginWindow.close)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.login_res_msg.setText(QCoreApplication.translate("LoginWindow", u"TextLabel", None))
        self.login_res_ok_btn.setText(QCoreApplication.translate("LoginWindow", u"OK", None))
        self.label_3.setText("")
        self.label_6.setText("")
        self.label_5.setText("")
        self.pushButton_3.setText("")
        self.login_button.setText(QCoreApplication.translate("LoginWindow", u"LOGIN", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.label.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.label_2.setText("")
        self.label_8.setText("")
        self.close_btn.setText("")
        self.pass_show_hide.setText("")
    # retranslateUi

