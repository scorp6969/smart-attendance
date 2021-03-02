# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nike_main_windowheWMtM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import nike_app_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 900)
        MainWindow.setMinimumSize(QSize(1280, 900))
        MainWindow.setMaximumSize(QSize(1280, 900))
        MainWindow.setStyleSheet(u"background-color: rgb(116, 85, 68);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QToolTip{\n"
"border: 2px solid #e7e1dd;\n"
"color: rgb(255, 255, 255);\n"
"background-color:#4d392f;\n"
"}\n"
"QWidget{\n"
"background-color: 	#745544;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMinimumSize(QSize(0, 60))
        self.main_header.setMaximumSize(QSize(16777215, 75))
        self.main_header.setStyleSheet(u"QFrame{\n"
"background-color:rgb(116, 85, 68);\n"
"}\n"
"                            ")
        self.main_header.setFrameShape(QFrame.WinPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tittle_bar_container = QFrame(self.main_header)
        self.tittle_bar_container.setObjectName(u"tittle_bar_container")
        self.tittle_bar_container.setStyleSheet(u"")
        self.tittle_bar_container.setFrameShape(QFrame.StyledPanel)
        self.tittle_bar_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.tittle_bar_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle = QFrame(self.tittle_bar_container)
        self.left_menu_toggle.setObjectName(u"left_menu_toggle")
        self.left_menu_toggle.setMinimumSize(QSize(60, 0))
        self.left_menu_toggle.setMaximumSize(QSize(60, 16777215))
        self.left_menu_toggle.setStyleSheet(u"QFrame{\n"
"background-color:	rgb(116, 85, 68);\n"
"}\n"
"QPushButton{\n"
"padding: 5px 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"background-color:	#876645;\n"
"color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #514f69;\n"
"}\n"
"")
        self.left_menu_toggle.setFrameShape(QFrame.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle_btn = QPushButton(self.left_menu_toggle)
        self.left_menu_toggle_btn.setObjectName(u"left_menu_toggle_btn")
        self.left_menu_toggle_btn.setMinimumSize(QSize(0, 50))
        self.left_menu_toggle_btn.setMaximumSize(QSize(60, 16777215))
        self.left_menu_toggle_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.left_menu_toggle_btn.setIcon(icon)
        self.left_menu_toggle_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.left_menu_toggle_btn)


        self.horizontalLayout_5.addWidget(self.left_menu_toggle)

        self.tittle_bar = QFrame(self.tittle_bar_container)
        self.tittle_bar.setObjectName(u"tittle_bar")
        self.tittle_bar.setStyleSheet(u"QLabel{\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"")
        self.tittle_bar.setFrameShape(QFrame.StyledPanel)
        self.tittle_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.tittle_bar)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_11 = QLabel(self.tittle_bar)
        self.label_11.setObjectName(u"label_11")
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_11)


        self.horizontalLayout_5.addWidget(self.tittle_bar)


        self.horizontalLayout_2.addWidget(self.tittle_bar_container)

        self.top_right_btns = QFrame(self.main_header)
        self.top_right_btns.setObjectName(u"top_right_btns")
        self.top_right_btns.setMinimumSize(QSize(0, 0))
        self.top_right_btns.setMaximumSize(QSize(130, 16777215))
        self.top_right_btns.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"padding: 6px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #514f69;\n"
"}\n"
"")
        self.top_right_btns.setFrameShape(QFrame.StyledPanel)
        self.top_right_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.top_right_btns)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon1)
        self.minimizeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.closeButton = QPushButton(self.top_right_btns)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout_2.addWidget(self.top_right_btns)


        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"background-color: 	#f2e3d0;")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMaximumSize(QSize(65, 16777215))
        self.left_side_menu.setStyleSheet(u"QFrame{\n"
"background-color:rgb(116, 85, 68);\n"
"}\n"
"QPushButton{\n"
"padding: 30px 8px;\n"
"border: none;\n"
"border-left: 2px solid transparent;\n"
"border-bottom: 2px solid transparent;\n"
"border-radius: 10px;\n"
"background-color:rgb(116, 85, 68);\n"
"color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: 	#514f69;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: 	#304053;\n"
"}\n"
"")
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(7, 0, 0, 0)
        self.left_menu_top_buttons = QFrame(self.left_side_menu)
        self.left_menu_top_buttons.setObjectName(u"left_menu_top_buttons")
        self.left_menu_top_buttons.setStyleSheet(u"")
        self.left_menu_top_buttons.setFrameShape(QFrame.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.home_button = QPushButton(self.left_menu_top_buttons)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setMinimumSize(QSize(100, 0))
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.home_button.setFont(font1)
        self.home_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_button.setStyleSheet(u"background-image:\n"
"                                                                    url(:/icons/icons/cil-home.png);\n"
"                                                                    background-repeat: none;\n"
"                                                                    padding-left: 150px;\n"
"                                                                    background-position: center left;\n"
"                                                                ")
        self.home_button.setIconSize(QSize(22, 22))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.home_button)

        self.account_button = QPushButton(self.left_menu_top_buttons)
        self.account_button.setObjectName(u"account_button")
        self.account_button.setMinimumSize(QSize(100, 0))
        self.account_button.setFont(font1)
        self.account_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.account_button.setStyleSheet(u"background-image:url(:/icons/icons/cil-user.png);\n"
"background-repeat: none;\n"
"padding-left: 115px;\n"
"background-position: center left;\n"
"")
        self.account_button.setIconSize(QSize(22, 22))

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.account_button)

        self.take_attendance = QPushButton(self.left_menu_top_buttons)
        self.take_attendance.setObjectName(u"take_attendance")
        self.take_attendance.setMinimumSize(QSize(110, 0))
        self.take_attendance.setFont(font1)
        self.take_attendance.setCursor(QCursor(Qt.PointingHandCursor))
        self.take_attendance.setStyleSheet(u"background-image:url(:/icons/icons/cil-camera.png);\n"
"background-repeat: none;\n"
"padding-left: 60px;\n"
"background-position: center left;\n"
"")
        self.take_attendance.setIconSize(QSize(22, 22))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.take_attendance)

        self.show_attendance = QPushButton(self.left_menu_top_buttons)
        self.show_attendance.setObjectName(u"show_attendance")
        self.show_attendance.setMinimumSize(QSize(110, 0))
        self.show_attendance.setFont(font1)
        self.show_attendance.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_attendance.setStyleSheet(u"background-image:url(:/icons/icons/cil-view-quilt.png);\n"
"background-repeat: none;\n"
"padding-left: 60px;\n"
"background-position: center left;\n"
"")
        self.show_attendance.setIconSize(QSize(22, 22))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.show_attendance)

        self.profile_button = QPushButton(self.left_menu_top_buttons)
        self.profile_button.setObjectName(u"profile_button")
        self.profile_button.setMinimumSize(QSize(110, 0))
        self.profile_button.setFont(font1)
        self.profile_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile_button.setStyleSheet(u"background-image: url(:/icons/icons/cil-description.png);\n"
"background-repeat: none;\n"
"padding-left: 60px;\n"
"background-position: center left;\n"
"\n"
"\n"
"                                                                ")
        self.profile_button.setIconSize(QSize(22, 22))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.profile_button)

        self.download_button = QPushButton(self.left_menu_top_buttons)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setMinimumSize(QSize(100, 0))
        self.download_button.setFont(font1)
        self.download_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.download_button.setStyleSheet(u"background-image: url(:/icons/icons/cil-envelope-closed.png);\n"
"background-repeat: none;\n"
"padding-left: 110px;\n"
"background-position: center left;\n"
"")
        self.download_button.setIconSize(QSize(22, 22))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.download_button)

        self.chart_button = QPushButton(self.left_menu_top_buttons)
        self.chart_button.setObjectName(u"chart_button")
        self.chart_button.setMinimumSize(QSize(100, 0))
        self.chart_button.setFont(font1)
        self.chart_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.chart_button.setStyleSheet(u"background-image:\n"
"                                                                    url(:/icons/icons/cil-chart-line.png);\n"
"                                                                    background-repeat: none;\n"
"                                                                    padding-left: 140px;\n"
"                                                                    background-position: center left;\n"
"                                                                ")
        self.chart_button.setIconSize(QSize(22, 22))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.chart_button)

        self.logout_button = QPushButton(self.left_menu_top_buttons)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setMinimumSize(QSize(110, 0))
        self.logout_button.setFont(font1)
        self.logout_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout_button.setStyleSheet(u"background-image: url(:/icons/icons/cil-power-standby.png);\n"
"background-repeat: none;\n"
"padding-left: 60px;\n"
"background-position: center left;\n"
"\n"
"\n"
"                                                                ")
        self.logout_button.setIconSize(QSize(22, 22))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.logout_button)


        self.verticalLayout_3.addWidget(self.left_menu_top_buttons)


        self.horizontalLayout.addWidget(self.left_side_menu)

        self.center_main_items = QFrame(self.main_body)
        self.center_main_items.setObjectName(u"center_main_items")
        self.center_main_items.setStyleSheet(u"")
        self.center_main_items.setFrameShape(QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center_main_items)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.home_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.home_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 0, 151, 41))
        font2 = QFont()
        font2.setFamily(u"Comic Sans MS")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px;\n"
"padding:5px;\n"
"background-position: center left;\n"
"")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_30 = QLabel(self.frame_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(220, 210, 411, 111))
        font3 = QFont()
        font3.setFamily(u"Digital-7")
        font3.setPointSize(45)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.label_30.setFont(font3)
        self.label_30.setStyleSheet(u"background-color: rgb(35, 39, 42);\n"
"border: 3px solid rgb(116, 85, 68);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"")
        self.label_30.setFrameShape(QFrame.NoFrame)
        self.label_30.setFrameShadow(QFrame.Plain)
        self.label_30.setLineWidth(1)
        self.label_30.setAlignment(Qt.AlignCenter)
        self.label_30.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_31 = QLabel(self.frame_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(340, 190, 161, 91))
        self.label_31.setFont(font3)
        self.label_31.setStyleSheet(u"background-color:rgb(116, 85, 68);\n"
"border:none;\n"
"border-radius:10px;\n"
"\n"
"padding:5px;\n"
"")
        self.label_31.setFrameShape(QFrame.NoFrame)
        self.label_31.setFrameShadow(QFrame.Plain)
        self.label_31.setLineWidth(1)
        self.label_31.setAlignment(Qt.AlignCenter)
        self.label_31.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_32 = QLabel(self.frame_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(270, 220, 311, 91))
        font4 = QFont()
        font4.setFamily(u"Digital-7")
        font4.setPointSize(50)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.label_32.setFont(font4)
        self.label_32.setStyleSheet(u"background-color: rgb(65, 90, 78);\n"
"font: 50pt \"Digital-7\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"padding:5px;\n"
"")
        self.label_32.setFrameShape(QFrame.NoFrame)
        self.label_32.setAlignment(Qt.AlignCenter)
        self.label_32.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_33 = QLabel(self.frame_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(270, 260, 61, 91))
        self.label_33.setFont(font3)
        self.label_33.setStyleSheet(u"background-color: rgb(116, 85, 68);\n"
"border:none;\n"
"border-radius:25px;\n"
"padding:5px;\n"
"")
        self.label_33.setFrameShape(QFrame.NoFrame)
        self.label_33.setFrameShadow(QFrame.Plain)
        self.label_33.setLineWidth(1)
        self.label_33.setAlignment(Qt.AlignCenter)
        self.label_33.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_34 = QLabel(self.frame_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(520, 260, 61, 91))
        self.label_34.setFont(font3)
        self.label_34.setStyleSheet(u"background-color:rgb(116, 85, 68);\n"
"border:none;\n"
"border-radius:25px;\n"
"\n"
"padding:5px;\n"
"")
        self.label_34.setFrameShape(QFrame.NoFrame)
        self.label_34.setFrameShadow(QFrame.Plain)
        self.label_34.setLineWidth(1)
        self.label_34.setAlignment(Qt.AlignCenter)
        self.label_34.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_35 = QLabel(self.frame_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(230, 230, 30, 30))
        self.label_35.setFont(font3)
        self.label_35.setStyleSheet(u"background-color: rgb(242, 227, 208);\n"
"border-radius:15px;\n"
"border: none;\n"
"padding:5px;")
        self.label_35.setFrameShape(QFrame.NoFrame)
        self.label_35.setFrameShadow(QFrame.Plain)
        self.label_35.setLineWidth(1)
        self.label_35.setAlignment(Qt.AlignCenter)
        self.label_35.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_36 = QLabel(self.frame_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(230, 270, 30, 30))
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"background-color: rgb(242, 227, 208);\n"
"border-radius:15px;\n"
"border: none;\n"
"padding:5px;")
        self.label_36.setFrameShape(QFrame.NoFrame)
        self.label_36.setFrameShadow(QFrame.Plain)
        self.label_36.setLineWidth(1)
        self.label_36.setAlignment(Qt.AlignCenter)
        self.label_36.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_37 = QLabel(self.frame_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(590, 270, 30, 30))
        self.label_37.setFont(font3)
        self.label_37.setStyleSheet(u"background-color: rgb(242, 227, 208);\n"
"border-radius:15px;\n"
"border: none;\n"
"padding:5px;\n"
"")
        self.label_37.setFrameShape(QFrame.NoFrame)
        self.label_37.setFrameShadow(QFrame.Plain)
        self.label_37.setLineWidth(1)
        self.label_37.setAlignment(Qt.AlignCenter)
        self.label_37.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_39 = QLabel(self.frame_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(590, 230, 30, 30))
        self.label_39.setFont(font3)
        self.label_39.setStyleSheet(u"background-color: rgb(242, 227, 208);\n"
"border-radius:15px;\n"
"border: none;\n"
"padding:5px;\n"
"")
        self.label_39.setFrameShape(QFrame.NoFrame)
        self.label_39.setFrameShadow(QFrame.Plain)
        self.label_39.setLineWidth(1)
        self.label_39.setAlignment(Qt.AlignCenter)
        self.label_39.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_40 = QLabel(self.frame_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(670, 180, 201, 81))
        font5 = QFont()
        font5.setFamily(u"Comic Sans MS")
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.label_40.setFont(font5)
        self.label_40.setStyleSheet(u"background-color:rgb(240, 202, 143);\n"
"border: 3px solid #67593d;\n"
"border-radius:10px;\n"
"padding:5px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_40.setFrameShape(QFrame.NoFrame)
        self.label_40.setFrameShadow(QFrame.Plain)
        self.label_40.setLineWidth(1)
        self.label_40.setAlignment(Qt.AlignCenter)
        self.label_40.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_41 = QLabel(self.frame_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(670, 260, 201, 161))
        self.label_41.setFont(font3)
        self.label_41.setStyleSheet(u"background-color:rgb(240, 202, 143);\n"
"border: 3px solid #67593d;\n"
"border-radius:10px;\n"
"padding:5px;\n"
"")
        self.label_41.setFrameShape(QFrame.NoFrame)
        self.label_41.setFrameShadow(QFrame.Plain)
        self.label_41.setLineWidth(1)
        self.label_41.setAlignment(Qt.AlignCenter)
        self.label_41.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_42 = QLabel(self.frame_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(680, 370, 181, 41))
        font6 = QFont()
        font6.setFamily(u"Comic Sans MS")
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.label_42.setFont(font6)
        self.label_42.setStyleSheet(u"background-color: 	#f0dabe;\n"
"border-radius:20px;\n"
"padding:5px;\n"
"color: rgb(0, 0, 0);")
        self.label_42.setFrameShape(QFrame.NoFrame)
        self.label_42.setFrameShadow(QFrame.Plain)
        self.label_42.setLineWidth(1)
        self.label_42.setAlignment(Qt.AlignCenter)
        self.label_42.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_43 = QLabel(self.frame_2)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(680, 270, 121, 91))
        font7 = QFont()
        font7.setFamily(u"Comic Sans MS")
        font7.setPointSize(50)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.label_43.setFont(font7)
        self.label_43.setStyleSheet(u"background-color:rgb(240, 202, 143);\n"
"padding:5px;\n"
"color: rgb(0, 0, 0);")
        self.label_43.setFrameShape(QFrame.NoFrame)
        self.label_43.setFrameShadow(QFrame.Plain)
        self.label_43.setLineWidth(1)
        self.label_43.setAlignment(Qt.AlignCenter)
        self.label_43.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_44 = QLabel(self.frame_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(800, 320, 61, 41))
        font8 = QFont()
        font8.setFamily(u"Comic Sans MS")
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(50)
        self.label_44.setFont(font8)
        self.label_44.setStyleSheet(u"background-color:rgb(240, 202, 143);\n"
"padding:5px;\n"
"color:rgb(0, 0, 0);")
        self.label_44.setFrameShape(QFrame.NoFrame)
        self.label_44.setFrameShadow(QFrame.Plain)
        self.label_44.setLineWidth(1)
        self.label_44.setAlignment(Qt.AlignCenter)
        self.label_44.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_45 = QLabel(self.frame_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(680, 200, 181, 51))
        font9 = QFont()
        font9.setFamily(u"Comic Sans MS")
        font9.setPointSize(18)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setWeight(75)
        self.label_45.setFont(font9)
        self.label_45.setStyleSheet(u"background-color: 	#f0dabe;\n"
"border-radius:20px;\n"
"padding:5px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_45.setFrameShape(QFrame.NoFrame)
        self.label_45.setFrameShadow(QFrame.Plain)
        self.label_45.setLineWidth(1)
        self.label_45.setAlignment(Qt.AlignCenter)
        self.label_45.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_38 = QLabel(self.frame_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(700, 150, 30, 51))
        self.label_38.setFont(font3)
        self.label_38.setStyleSheet(u"background-color: rgb(116, 85, 68);\n"
"border-radius:15px;\n"
"border: none;\n"
"padding:5px;\n"
"")
        self.label_38.setFrameShape(QFrame.NoFrame)
        self.label_38.setFrameShadow(QFrame.Plain)
        self.label_38.setLineWidth(1)
        self.label_38.setAlignment(Qt.AlignCenter)
        self.label_38.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_46 = QLabel(self.frame_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(810, 150, 30, 51))
        self.label_46.setFont(font3)
        self.label_46.setStyleSheet(u"background-color:rgb(116, 85, 68);\n"
"border-radius:15px;\n"
"border: none;\n"
"padding:5px;\n"
"\n"
"")
        self.label_46.setFrameShape(QFrame.NoFrame)
        self.label_46.setFrameShadow(QFrame.Plain)
        self.label_46.setLineWidth(1)
        self.label_46.setAlignment(Qt.AlignCenter)
        self.label_46.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_47 = QLabel(self.frame_2)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(710, 160, 20, 40))
        self.label_47.setFont(font3)
        self.label_47.setStyleSheet(u"background-color: rgb(242, 227, 208);\n"
"border-radius:10px;\n"
"border: 3px solid rgb(103, 89, 61);\n"
"padding:5px;\n"
"")
        self.label_47.setFrameShape(QFrame.NoFrame)
        self.label_47.setFrameShadow(QFrame.Plain)
        self.label_47.setLineWidth(1)
        self.label_47.setAlignment(Qt.AlignCenter)
        self.label_47.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_48 = QLabel(self.frame_2)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(820, 160, 20, 40))
        self.label_48.setFont(font3)
        self.label_48.setStyleSheet(u"background-color: rgb(242, 227, 208);\n"
"border-radius:10px;\n"
"border: 3px solid rgb(103, 89, 61);\n"
"padding:5px;\n"
"")
        self.label_48.setFrameShape(QFrame.NoFrame)
        self.label_48.setFrameShadow(QFrame.Plain)
        self.label_48.setLineWidth(1)
        self.label_48.setAlignment(Qt.AlignCenter)
        self.label_48.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_49 = QLabel(self.frame_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(530, 260, 51, 41))
        self.label_49.setFont(font6)
        self.label_49.setStyleSheet(u"background-color: #415a4e;\n"
"padding:5px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_49.setFrameShape(QFrame.NoFrame)
        self.label_49.setFrameShadow(QFrame.Plain)
        self.label_49.setLineWidth(1)
        self.label_49.setAlignment(Qt.AlignCenter)
        self.label_49.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_50 = QLabel(self.frame_2)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(270, 220, 261, 91))
        self.label_50.setFont(font4)
        self.label_50.setStyleSheet(u"background-color: #415a4e;\n"
"font: 50pt \"Digital-7\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_50.setFrameShape(QFrame.NoFrame)
        self.label_50.setAlignment(Qt.AlignCenter)
        self.label_50.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_52 = QLabel(self.frame_2)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(70, 540, 481, 111))
        font10 = QFont()
        font10.setFamily(u"Comic Sans MS")
        font10.setPointSize(22)
        font10.setBold(True)
        font10.setItalic(False)
        font10.setWeight(75)
        self.label_52.setFont(font10)
        self.label_52.setStyleSheet(u"background-color: 	#f0ca8f;\n"
"border: 3px solid rgb(116, 85, 68);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_52.setFrameShape(QFrame.NoFrame)
        self.label_52.setFrameShadow(QFrame.Plain)
        self.label_52.setLineWidth(1)
        self.label_52.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_52.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_53 = QLabel(self.frame_2)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(370, 550, 171, 91))
        self.label_53.setFont(font4)
        self.label_53.setStyleSheet(u"background-color: rgb(116, 85, 68);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"padding:5px;\n"
"")
        self.label_53.setFrameShape(QFrame.NoFrame)
        self.label_53.setAlignment(Qt.AlignCenter)
        self.label_53.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_56 = QLabel(self.frame_2)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(840, 550, 161, 91))
        self.label_56.setFont(font4)
        self.label_56.setStyleSheet(u"background-color: rgb(116, 85, 68);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"padding:5px;\n"
"\n"
"")
        self.label_56.setFrameShape(QFrame.NoFrame)
        self.label_56.setAlignment(Qt.AlignCenter)
        self.label_56.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_54 = QLabel(self.frame_2)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(630, 540, 381, 111))
        self.label_54.setFont(font10)
        self.label_54.setStyleSheet(u"background-color: 	#f0ca8f;\n"
"border: 3px solid rgb(116, 85, 68);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_54.setFrameShape(QFrame.NoFrame)
        self.label_54.setFrameShadow(QFrame.Plain)
        self.label_54.setLineWidth(1)
        self.label_54.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_54.setTextInteractionFlags(Qt.NoTextInteraction)
        self.refresh_db_button = QPushButton(self.frame_2)
        self.refresh_db_button.setObjectName(u"refresh_db_button")
        self.refresh_db_button.setGeometry(QRect(550, 560, 80, 80))
        self.refresh_db_button.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"image: url(:/icons/icons/cil-reload.png);\n"
"background-color: #4e6a50;\n"
"border:none;\n"
"border-radius: 40px;\n"
"border: 3px solid rgb(103, 89, 61);\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid rgb(242, 227, 208);\n"
"}")
        self.label_58 = QLabel(self.frame_2)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(460, 30, 351, 61))
        font11 = QFont()
        font11.setFamily(u"Forte")
        font11.setPointSize(28)
        font11.setBold(False)
        font11.setItalic(False)
        font11.setWeight(50)
        self.label_58.setFont(font11)
        self.label_58.setStyleSheet(u"background-color: rgb(116, 85, 68);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"")
        self.label_58.setFrameShape(QFrame.NoFrame)
        self.label_58.setAlignment(Qt.AlignCenter)
        self.label_58.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_59 = QLabel(self.frame_2)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(340, 20, 481, 81))
        self.label_59.setFont(font10)
        self.label_59.setStyleSheet(u"background-color: 	#f0ca8f;\n"
"\n"
"border-radius:10px;\n"
"padding:5px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_59.setFrameShape(QFrame.NoFrame)
        self.label_59.setFrameShadow(QFrame.Plain)
        self.label_59.setLineWidth(1)
        self.label_59.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_59.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_33.raise_()
        self.label_34.raise_()
        self.label_31.raise_()
        self.label_19.raise_()
        self.label_30.raise_()
        self.label_32.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.label_37.raise_()
        self.label_39.raise_()
        self.label_40.raise_()
        self.label_41.raise_()
        self.label_42.raise_()
        self.label_43.raise_()
        self.label_44.raise_()
        self.label_45.raise_()
        self.label_38.raise_()
        self.label_46.raise_()
        self.label_47.raise_()
        self.label_48.raise_()
        self.label_49.raise_()
        self.label_50.raise_()
        self.label_52.raise_()
        self.label_53.raise_()
        self.label_54.raise_()
        self.label_56.raise_()
        self.refresh_db_button.raise_()
        self.label_59.raise_()
        self.label_58.raise_()

        self.verticalLayout_13.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.home_page)
        self.accounts_page = QWidget()
        self.accounts_page.setObjectName(u"accounts_page")
        self.accounts_page.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.accounts_page)
        self.verticalLayout_12.setSpacing(7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.register_frame = QFrame(self.accounts_page)
        self.register_frame.setObjectName(u"register_frame")
        self.register_frame.setFrameShape(QFrame.StyledPanel)
        self.register_frame.setFrameShadow(QFrame.Raised)
        self.register_input_field_frame = QFrame(self.register_frame)
        self.register_input_field_frame.setObjectName(u"register_input_field_frame")
        self.register_input_field_frame.setGeometry(QRect(530, 210, 461, 501))
        self.register_input_field_frame.setStyleSheet(u"QFrame{\n"
"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"background-color: 	#f0ca8f;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}\n"
"QLabel{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: rgb(240, 202, 143);\n"
"}\n"
"QComboBox{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 202, 143);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}\n"
"QListView{\n"
"background-color: rgb(56, 108, 128);"
                        "\n"
"border: 3px solid rgb(70, 85, 134);\n"
"padding-top: 10px;\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"}\n"
"QComboBox:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"")
        self.register_input_field_frame.setFrameShape(QFrame.StyledPanel)
        self.register_input_field_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.register_input_field_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.register_button = QPushButton(self.register_input_field_frame)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setMinimumSize(QSize(280, 70))
        self.register_button.setMaximumSize(QSize(280, 70))
        font12 = QFont()
        font12.setFamily(u"Comic Sans MS")
        font12.setPointSize(14)
        font12.setBold(True)
        font12.setWeight(75)
        self.register_button.setFont(font12)
        self.register_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.register_button, 7, 1, 1, 1)

        self.take_photo_attend = QPushButton(self.register_input_field_frame)
        self.take_photo_attend.setObjectName(u"take_photo_attend")
        self.take_photo_attend.setMinimumSize(QSize(110, 45))
        self.take_photo_attend.setMaximumSize(QSize(150, 45))
        font13 = QFont()
        font13.setFamily(u"Comic Sans MS")
        font13.setPointSize(10)
        font13.setBold(False)
        font13.setWeight(50)
        self.take_photo_attend.setFont(font13)
        self.take_photo_attend.setCursor(QCursor(Qt.PointingHandCursor))
        self.take_photo_attend.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.take_photo_attend, 7, 0, 1, 1)

        self.label_20 = QLabel(self.register_input_field_frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(140, 60))
        self.label_20.setMaximumSize(QSize(140, 60))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_20, 4, 0, 1, 1)

        self.profile_icon_frame = QFrame(self.register_input_field_frame)
        self.profile_icon_frame.setObjectName(u"profile_icon_frame")
        self.profile_icon_frame.setMinimumSize(QSize(80, 80))
        self.profile_icon_frame.setMaximumSize(QSize(80, 80))
        self.profile_icon_frame.setStyleSheet(u"image:url(:/icons/icons/cil-user-follow.png);\n"
"background-color: rgb(116, 85, 68);\n"
"border-radius: 40px;\n"
"border: 2px solid rgb(0, 0, 0);\n"
"")
        self.profile_icon_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_icon_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.profile_icon_frame, 0, 0, 1, 1)

        self.username = QLineEdit(self.register_input_field_frame)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(280, 60))
        self.username.setMaximumSize(QSize(280, 60))
        font14 = QFont()
        font14.setFamily(u"Comic Sans MS")
        font14.setPointSize(11)
        self.username.setFont(font14)
        self.username.setStyleSheet(u"")
        self.username.setText(u"")
        self.username.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.username, 1, 1, 1, 1)

        self.comboBox_5 = QComboBox(self.register_input_field_frame)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(280, 60))
        self.comboBox_5.setMaximumSize(QSize(280, 60))
        self.comboBox_5.setFont(font14)

        self.gridLayout_3.addWidget(self.comboBox_5, 4, 1, 1, 1)

        self.label_21 = QLabel(self.register_input_field_frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(140, 60))
        self.label_21.setMaximumSize(QSize(140, 60))
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_21, 5, 0, 1, 1)

        self.label_23 = QLabel(self.register_input_field_frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(140, 60))
        self.label_23.setMaximumSize(QSize(280, 75))
        font15 = QFont()
        font15.setFamily(u"Comic Sans MS")
        font15.setPointSize(14)
        font15.setBold(False)
        font15.setWeight(50)
        self.label_23.setFont(font15)
        self.label_23.setStyleSheet(u"background-color: #386c80;\n"
"color: rgb(255, 255, 255);")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_23, 0, 1, 1, 2)

        self.comboBox_6 = QComboBox(self.register_input_field_frame)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(280, 60))
        self.comboBox_6.setMaximumSize(QSize(280, 60))
        self.comboBox_6.setFont(font14)

        self.gridLayout_3.addWidget(self.comboBox_6, 5, 1, 1, 1)

        self.label_2 = QLabel(self.register_input_field_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(140, 60))
        self.label_2.setMaximumSize(QSize(140, 60))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.generate_button = QPushButton(self.register_input_field_frame)
        self.generate_button.setObjectName(u"generate_button")
        self.generate_button.setMinimumSize(QSize(130, 55))
        self.generate_button.setMaximumSize(QSize(130, 55))
        self.generate_button.setFont(font13)
        self.generate_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.generate_button.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.generate_button, 3, 2, 1, 1)

        self.std_roll = QLineEdit(self.register_input_field_frame)
        self.std_roll.setObjectName(u"std_roll")
        self.std_roll.setEnabled(False)
        self.std_roll.setMinimumSize(QSize(145, 60))
        self.std_roll.setMaximumSize(QSize(145, 60))
        self.std_roll.setFont(font14)
        self.std_roll.setStyleSheet(u"")
        self.std_roll.setText(u"")
        self.std_roll.setAlignment(Qt.AlignCenter)
        self.std_roll.setReadOnly(False)

        self.gridLayout_3.addWidget(self.std_roll, 3, 1, 1, 1)

        self.label_3 = QLabel(self.register_input_field_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(140, 60))
        self.label_3.setMaximumSize(QSize(140, 60))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)

        self.register_res_frame = QFrame(self.register_frame)
        self.register_res_frame.setObjectName(u"register_res_frame")
        self.register_res_frame.setGeometry(QRect(230, 10, 700, 151))
        self.register_res_frame.setMinimumSize(QSize(700, 100))
        self.register_res_frame.setMaximumSize(QSize(700, 300))
        self.register_res_frame.setStyleSheet(u"QFrame{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 218, 190);\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 30px;\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 85, 64);\n"
"border:none;\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(116, 85, 68);\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid rgb(193, 97, 93);\n"
"}\n"
"QLabel{\n"
"padding: 10px;\n"
"border: none;\n"
"}\n"
"")
        self.register_res_frame.setFrameShape(QFrame.StyledPanel)
        self.register_res_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.register_res_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.register_res_msg = QLabel(self.register_res_frame)
        self.register_res_msg.setObjectName(u"register_res_msg")
        font16 = QFont()
        font16.setFamily(u"Comic Sans MS")
        font16.setPointSize(14)
        self.register_res_msg.setFont(font16)
        self.register_res_msg.setStyleSheet(u"")
        self.register_res_msg.setAlignment(Qt.AlignCenter)
        self.register_res_msg.setWordWrap(True)
        self.register_res_msg.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_6.addWidget(self.register_res_msg)

        self.register_res_msg_ok_btn = QPushButton(self.register_res_frame)
        self.register_res_msg_ok_btn.setObjectName(u"register_res_msg_ok_btn")
        self.register_res_msg_ok_btn.setMinimumSize(QSize(75, 55))
        self.register_res_msg_ok_btn.setMaximumSize(QSize(75, 55))
        font17 = QFont()
        font17.setFamily(u"Comic Sans MS")
        font17.setPointSize(12)
        font17.setBold(True)
        font17.setWeight(75)
        self.register_res_msg_ok_btn.setFont(font17)
        self.register_res_msg_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.register_res_msg_ok_btn.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.register_res_msg_ok_btn)

        self.register_input_field_frame_2 = QFrame(self.register_frame)
        self.register_input_field_frame_2.setObjectName(u"register_input_field_frame_2")
        self.register_input_field_frame_2.setGeometry(QRect(40, 190, 451, 541))
        self.register_input_field_frame_2.setStyleSheet(u"QFrame{\n"
"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"background-color: 	#f0ca8f;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}\n"
"QLabel{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: rgb(240, 202, 143);\n"
"}\n"
"QCheckBox{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"background-color:rgb(240, 202, 143);\n"
"color: rgb(0, 0, 0);\n"
"spacing: 20px;\n"
"}\n"
"QCheckBox:"
                        ":indicator {\n"
"width: 24px;\n"
"height: 24px;\n"
"border-radius:12px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background-color: rgb(35, 39, 42);\n"
"image: url(:/icons/icons/cil-check.png);\n"
"}\n"
"\n"
"")
        self.register_input_field_frame_2.setFrameShape(QFrame.StyledPanel)
        self.register_input_field_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.register_input_field_frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.create_an_account_button = QPushButton(self.register_input_field_frame_2)
        self.create_an_account_button.setObjectName(u"create_an_account_button")
        self.create_an_account_button.setMinimumSize(QSize(280, 70))
        self.create_an_account_button.setMaximumSize(QSize(280, 70))
        self.create_an_account_button.setFont(font12)
        self.create_an_account_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.create_an_account_button, 9, 1, 1, 1)

        self.confirm_password_label = QLineEdit(self.register_input_field_frame_2)
        self.confirm_password_label.setObjectName(u"confirm_password_label")
        self.confirm_password_label.setMinimumSize(QSize(280, 60))
        self.confirm_password_label.setMaximumSize(QSize(280, 60))
        self.confirm_password_label.setFont(font14)
        self.confirm_password_label.setStyleSheet(u"")
        self.confirm_password_label.setText(u"")
        self.confirm_password_label.setEchoMode(QLineEdit.Password)
        self.confirm_password_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.confirm_password_label, 4, 1, 1, 1)

        self.admin_username = QLineEdit(self.register_input_field_frame_2)
        self.admin_username.setObjectName(u"admin_username")
        self.admin_username.setMinimumSize(QSize(280, 60))
        self.admin_username.setMaximumSize(QSize(280, 60))
        self.admin_username.setFont(font14)
        self.admin_username.setStyleSheet(u"")
        self.admin_username.setText(u"")
        self.admin_username.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.admin_username, 1, 1, 1, 1)

        self.label_6 = QLabel(self.register_input_field_frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(140, 60))
        self.label_6.setMaximumSize(QSize(140, 60))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)

        self.password_label = QLineEdit(self.register_input_field_frame_2)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setMinimumSize(QSize(280, 60))
        self.password_label.setMaximumSize(QSize(280, 60))
        self.password_label.setFont(font14)
        self.password_label.setStyleSheet(u"")
        self.password_label.setText(u"")
        self.password_label.setEchoMode(QLineEdit.Password)
        self.password_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.password_label, 3, 1, 1, 1)

        self.profile_icon_frame_4 = QFrame(self.register_input_field_frame_2)
        self.profile_icon_frame_4.setObjectName(u"profile_icon_frame_4")
        self.profile_icon_frame_4.setMinimumSize(QSize(80, 80))
        self.profile_icon_frame_4.setMaximumSize(QSize(80, 80))
        self.profile_icon_frame_4.setStyleSheet(u"image:url(:/icons/icons/cil-user-follow.png);\n"
"background-color: rgb(116, 85, 68);\n"
"border-radius: 40px;\n"
"border: 2px solid rgb(0, 0, 0);")
        self.profile_icon_frame_4.setFrameShape(QFrame.StyledPanel)
        self.profile_icon_frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.profile_icon_frame_4, 0, 0, 1, 1)

        self.label_8 = QLabel(self.register_input_field_frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(140, 60))
        self.label_8.setMaximumSize(QSize(140, 60))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_27 = QLabel(self.register_input_field_frame_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(140, 60))
        self.label_27.setMaximumSize(QSize(280, 75))
        self.label_27.setFont(font15)
        self.label_27.setStyleSheet(u"background-color: #386c80;\n"
"color: rgb(255, 255, 255);")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_27, 0, 1, 1, 2)

        self.label_25 = QLabel(self.register_input_field_frame_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(140, 80))
        self.label_25.setMaximumSize(QSize(140, 80))
        self.label_25.setFont(font2)
        self.label_25.setStyleSheet(u"")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_25.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_25, 4, 0, 1, 1)

        self.checkBox = QCheckBox(self.register_input_field_frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(210, 60))
        self.checkBox.setMaximumSize(QSize(210, 60))
        self.checkBox.setFont(font2)
        self.checkBox.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout_4.addWidget(self.checkBox, 5, 1, 1, 1, Qt.AlignHCenter)

        self.password_generator = QPushButton(self.register_input_field_frame_2)
        self.password_generator.setObjectName(u"password_generator")
        self.password_generator.setMinimumSize(QSize(140, 60))
        self.password_generator.setMaximumSize(QSize(140, 60))
        self.password_generator.setFont(font13)
        self.password_generator.setCursor(QCursor(Qt.PointingHandCursor))
        self.password_generator.setStyleSheet(u"padding: 5px;\n"
"                                                                                    ")

        self.gridLayout_4.addWidget(self.password_generator, 9, 0, 1, 1)

        self.register_res_msg_2 = QLabel(self.register_input_field_frame_2)
        self.register_res_msg_2.setObjectName(u"register_res_msg_2")
        self.register_res_msg_2.setMinimumSize(QSize(0, 60))
        font18 = QFont()
        font18.setFamily(u"Comic Sans MS")
        font18.setPointSize(10)
        font18.setBold(False)
        font18.setItalic(True)
        font18.setWeight(50)
        self.register_res_msg_2.setFont(font18)
        self.register_res_msg_2.setStyleSheet(u"color: rgb(243, 243, 243);\n"
"background-color: rgb(135, 102, 69);\n"
"border:none;\n"
"padding: 10px;\n"
"                                                                                    ")
        self.register_res_msg_2.setScaledContents(False)
        self.register_res_msg_2.setAlignment(Qt.AlignCenter)
        self.register_res_msg_2.setWordWrap(True)
        self.register_res_msg_2.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_4.addWidget(self.register_res_msg_2, 6, 0, 1, 2)

        self.label_9 = QLabel(self.register_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 211, 41))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px;\n"
"padding:5px;\n"
"background-position: center left;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_12.addWidget(self.register_frame)

        self.stackedWidget.addWidget(self.accounts_page)
        self.take_attend_page = QWidget()
        self.take_attend_page.setObjectName(u"take_attend_page")
        self.take_attend_page.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.take_attend_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.take_attend_frame = QFrame(self.take_attend_page)
        self.take_attend_frame.setObjectName(u"take_attend_frame")
        self.take_attend_frame.setStyleSheet(u"")
        self.take_attend_frame.setFrameShape(QFrame.StyledPanel)
        self.take_attend_frame.setFrameShadow(QFrame.Raised)
        self.manual_attend_frame = QFrame(self.take_attend_frame)
        self.manual_attend_frame.setObjectName(u"manual_attend_frame")
        self.manual_attend_frame.setGeometry(QRect(440, 277, 571, 461))
        self.manual_attend_frame.setStyleSheet(u"QFrame{\n"
"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"background-color: 	#f0ca8f;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}\n"
"QLabel{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: rgb(240, 202, 143);\n"
"}\n"
"")
        self.manual_attend_frame.setFrameShape(QFrame.StyledPanel)
        self.manual_attend_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.manual_attend_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.submit_button = QPushButton(self.manual_attend_frame)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setMinimumSize(QSize(300, 60))
        self.submit_button.setMaximumSize(QSize(350, 16777215))
        self.submit_button.setFont(font12)
        self.submit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.submit_button.setCheckable(False)

        self.gridLayout.addWidget(self.submit_button, 5, 1, 1, 2)

        self.username_3 = QLineEdit(self.manual_attend_frame)
        self.username_3.setObjectName(u"username_3")
        self.username_3.setMinimumSize(QSize(220, 40))
        self.username_3.setMaximumSize(QSize(220, 16777215))
        font19 = QFont()
        font19.setFamily(u"Comic Sans MS")
        font19.setPointSize(12)
        self.username_3.setFont(font19)
        self.username_3.setStyleSheet(u"")
        self.username_3.setText(u"")
        self.username_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.username_3, 1, 1, 1, 2)

        self.label_16 = QLabel(self.manual_attend_frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(155, 40))
        self.label_16.setMaximumSize(QSize(16777215, 16777215))
        self.label_16.setFont(font17)
        self.label_16.setStyleSheet(u"")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 3, 0, 1, 1)

        self.label_12 = QLabel(self.manual_attend_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(155, 40))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        self.label_12.setFont(font17)
        self.label_12.setStyleSheet(u"")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_17 = QLabel(self.manual_attend_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(185, 0))
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"background-color: #386c80;\n"
"color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_15 = QLabel(self.manual_attend_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(155, 40))
        self.label_15.setMaximumSize(QSize(16777215, 16777215))
        self.label_15.setFont(font17)
        self.label_15.setStyleSheet(u"")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)

        self.date_fill = QLineEdit(self.manual_attend_frame)
        self.date_fill.setObjectName(u"date_fill")
        self.date_fill.setMinimumSize(QSize(220, 40))
        self.date_fill.setMaximumSize(QSize(220, 16777215))
        self.date_fill.setFont(font19)
        self.date_fill.setStyleSheet(u"")
        self.date_fill.setText(u"")
        self.date_fill.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.date_fill, 2, 1, 1, 1)

        self.time_fill = QLineEdit(self.manual_attend_frame)
        self.time_fill.setObjectName(u"time_fill")
        self.time_fill.setMinimumSize(QSize(220, 40))
        self.time_fill.setMaximumSize(QSize(220, 16777215))
        self.time_fill.setFont(font19)
        self.time_fill.setStyleSheet(u"")
        self.time_fill.setText(u"")
        self.time_fill.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.time_fill, 3, 1, 1, 1)

        self.auto_fill_button = QPushButton(self.manual_attend_frame)
        self.auto_fill_button.setObjectName(u"auto_fill_button")
        self.auto_fill_button.setMinimumSize(QSize(100, 50))
        self.auto_fill_button.setMaximumSize(QSize(100, 16777215))
        font20 = QFont()
        font20.setFamily(u"Comic Sans MS")
        font20.setPointSize(9)
        font20.setBold(True)
        font20.setWeight(75)
        self.auto_fill_button.setFont(font20)
        self.auto_fill_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.auto_fill_button, 2, 2, 2, 1)

        self.profile_icon_frame_2 = QFrame(self.manual_attend_frame)
        self.profile_icon_frame_2.setObjectName(u"profile_icon_frame_2")
        self.profile_icon_frame_2.setMinimumSize(QSize(80, 80))
        self.profile_icon_frame_2.setMaximumSize(QSize(80, 80))
        self.profile_icon_frame_2.setStyleSheet(u"image:url(:/icons/icons/cil-user-follow.png);\n"
"background-color: rgb(116, 85, 68);\n"
"border-radius: 40px;\n"
"border: 2px solid rgb(0, 0, 0);                                                ")
        self.profile_icon_frame_2.setFrameShape(QFrame.StyledPanel)
        self.profile_icon_frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.profile_icon_frame_2, 0, 1, 1, 1)

        self.auto_attend_frame = QFrame(self.take_attend_frame)
        self.auto_attend_frame.setObjectName(u"auto_attend_frame")
        self.auto_attend_frame.setGeometry(QRect(40, 394, 381, 221))
        self.auto_attend_frame.setStyleSheet(u"QFrame{\n"
"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}")
        self.auto_attend_frame.setFrameShape(QFrame.StyledPanel)
        self.auto_attend_frame.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.auto_attend_frame)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(11)
        self.formLayout_3.setVerticalSpacing(11)
        self.profile_icon_frame_3 = QFrame(self.auto_attend_frame)
        self.profile_icon_frame_3.setObjectName(u"profile_icon_frame_3")
        self.profile_icon_frame_3.setMinimumSize(QSize(80, 80))
        self.profile_icon_frame_3.setMaximumSize(QSize(80, 80))
        self.profile_icon_frame_3.setStyleSheet(u"image:url(:/icons/icons/cil-user-follow.png);\n"
"background-color: rgb(116, 85, 68);\n"
"border-radius: 40px;\n"
"border: 2px solid rgb(0, 0, 0);")
        self.profile_icon_frame_3.setFrameShape(QFrame.StyledPanel)
        self.profile_icon_frame_3.setFrameShadow(QFrame.Raised)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.profile_icon_frame_3)

        self.take_A_butn = QPushButton(self.auto_attend_frame)
        self.take_A_butn.setObjectName(u"take_A_butn")
        self.take_A_butn.setMinimumSize(QSize(300, 60))
        self.take_A_butn.setMaximumSize(QSize(350, 16777215))
        self.take_A_butn.setFont(font12)
        self.take_A_butn.setCursor(QCursor(Qt.PointingHandCursor))
        self.take_A_butn.setStyleSheet(u"QToolTip{\n"
"                                                                                        border: 2px solid rgb(114, 137,\n"
"                                                                                        218);\n"
"                                                                                        color: rgb(255, 255, 255);\n"
"                                                                                        background-color:rgb(44, 47,\n"
"                                                                                        51);\n"
"                                                                                        }\n"
"                                                                                    ")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.take_A_butn)

        self.take_attend_res_frame = QFrame(self.take_attend_frame)
        self.take_attend_res_frame.setObjectName(u"take_attend_res_frame")
        self.take_attend_res_frame.setGeometry(QRect(60, 60, 911, 191))
        self.take_attend_res_frame.setMinimumSize(QSize(400, 100))
        self.take_attend_res_frame.setMaximumSize(QSize(1000, 300))
        self.take_attend_res_frame.setStyleSheet(u"QFrame{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 218, 190);\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 30px;\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 85, 64);\n"
"border:none;\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(116, 85, 68);\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid rgb(193, 97, 93);\n"
"}\n"
"QLabel{\n"
"padding: 10px;\n"
"border: none;\n"
"}\n"
"")
        self.take_attend_res_frame.setFrameShape(QFrame.StyledPanel)
        self.take_attend_res_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.take_attend_res_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.take_attend_res_msg = QLabel(self.take_attend_res_frame)
        self.take_attend_res_msg.setObjectName(u"take_attend_res_msg")
        self.take_attend_res_msg.setFont(font19)
        self.take_attend_res_msg.setAlignment(Qt.AlignCenter)
        self.take_attend_res_msg.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.take_attend_res_msg)

        self.take_attend_res_ok_btn = QPushButton(self.take_attend_res_frame)
        self.take_attend_res_ok_btn.setObjectName(u"take_attend_res_ok_btn")
        self.take_attend_res_ok_btn.setMinimumSize(QSize(80, 50))
        self.take_attend_res_ok_btn.setMaximumSize(QSize(80, 50))
        self.take_attend_res_ok_btn.setFont(font17)
        self.take_attend_res_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_17.addWidget(self.take_attend_res_ok_btn, 0, Qt.AlignHCenter)

        self.label = QLabel(self.take_attend_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 191, 41))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px;\n"
"padding:5px;\n"
"background-position: center left;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_11.addWidget(self.take_attend_frame)

        self.stackedWidget.addWidget(self.take_attend_page)
        self.show_attend_page = QWidget()
        self.show_attend_page.setObjectName(u"show_attend_page")
        self.show_attend_page.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.show_attend_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.show_attend_frame = QFrame(self.show_attend_page)
        self.show_attend_frame.setObjectName(u"show_attend_frame")
        self.show_attend_frame.setFrameShape(QFrame.StyledPanel)
        self.show_attend_frame.setFrameShadow(QFrame.Raised)
        self.show_attend_res_frame = QFrame(self.show_attend_frame)
        self.show_attend_res_frame.setObjectName(u"show_attend_res_frame")
        self.show_attend_res_frame.setGeometry(QRect(40, 50, 900, 60))
        self.show_attend_res_frame.setMinimumSize(QSize(900, 60))
        self.show_attend_res_frame.setMaximumSize(QSize(900, 60))
        self.show_attend_res_frame.setStyleSheet(u"QFrame{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 218, 190);\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 30px;\n"
"}\n"
"QLabel{\n"
"padding: 5px;\n"
"border: none;\n"
"}")
        self.show_attend_res_frame.setFrameShape(QFrame.StyledPanel)
        self.show_attend_res_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.show_attend_res_frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.show_attend_res_msg = QLabel(self.show_attend_res_frame)
        self.show_attend_res_msg.setObjectName(u"show_attend_res_msg")
        self.show_attend_res_msg.setFont(font19)
        self.show_attend_res_msg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.show_attend_res_msg)

        self.show_attend_input_field_frame = QFrame(self.show_attend_frame)
        self.show_attend_input_field_frame.setObjectName(u"show_attend_input_field_frame")
        self.show_attend_input_field_frame.setGeometry(QRect(40, 120, 761, 161))
        self.show_attend_input_field_frame.setMinimumSize(QSize(0, 0))
        self.show_attend_input_field_frame.setMaximumSize(QSize(16777215, 16777215))
        self.show_attend_input_field_frame.setStyleSheet(u"QFrame{\n"
"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"background-color: 	#f0ca8f;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}\n"
"QLabel{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: rgb(240, 202, 143);\n"
"}\n"
"QComboBox{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 202, 143);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}\n"
"QListView{\n"
"background-color: rgb(56, 108, 128);"
                        "\n"
"border: 3px solid rgb(70, 85, 134);\n"
"padding-top: 10px;\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"}\n"
"QComboBox:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}")
        self.show_attend_input_field_frame.setFrameShape(QFrame.StyledPanel)
        self.show_attend_input_field_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.show_attend_input_field_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.show_attend_input_field_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(200, 50))
        self.label_18.setMaximumSize(QSize(200, 50))
        self.label_18.setFont(font20)
        self.label_18.setStyleSheet(u"")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_18, 1, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.show_attend_input_field_frame)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(250, 50))
        self.comboBox_4.setMaximumSize(QSize(250, 50))
        self.comboBox_4.setFont(font19)

        self.gridLayout_2.addWidget(self.comboBox_4, 1, 1, 1, 1)

        self.label_5 = QLabel(self.show_attend_input_field_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(200, 50))
        self.label_5.setMaximumSize(QSize(200, 50))
        self.label_5.setFont(font20)
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.show_attend_semsester_btn = QPushButton(self.show_attend_input_field_frame)
        self.show_attend_semsester_btn.setObjectName(u"show_attend_semsester_btn")
        self.show_attend_semsester_btn.setMinimumSize(QSize(100, 50))
        self.show_attend_semsester_btn.setMaximumSize(QSize(100, 50))
        self.show_attend_semsester_btn.setFont(font12)
        self.show_attend_semsester_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.show_attend_semsester_btn, 1, 2, 1, 1)

        self.show_attend_faculty_btn = QPushButton(self.show_attend_input_field_frame)
        self.show_attend_faculty_btn.setObjectName(u"show_attend_faculty_btn")
        self.show_attend_faculty_btn.setMinimumSize(QSize(100, 50))
        self.show_attend_faculty_btn.setMaximumSize(QSize(100, 50))
        self.show_attend_faculty_btn.setFont(font12)
        self.show_attend_faculty_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.show_attend_faculty_btn, 0, 2, 1, 1)

        self.comboBox_3 = QComboBox(self.show_attend_input_field_frame)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(250, 50))
        self.comboBox_3.setMaximumSize(QSize(250, 50))
        self.comboBox_3.setFont(font19)

        self.gridLayout_2.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.show_attend_table_frame = QFrame(self.show_attend_frame)
        self.show_attend_table_frame.setObjectName(u"show_attend_table_frame")
        self.show_attend_table_frame.setGeometry(QRect(40, 298, 950, 451))
        self.show_attend_table_frame.setMinimumSize(QSize(950, 400))
        self.show_attend_table_frame.setMaximumSize(QSize(950, 500))
        self.show_attend_table_frame.setStyleSheet(u"QFrame{\n"
"background-color:	#f0ca8f;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(116, 85, 68);\n"
"}\n"
"")
        self.show_attend_table_frame.setFrameShape(QFrame.StyledPanel)
        self.show_attend_table_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.show_attend_table_frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.show_attend_table_frame)
        self.tableWidget.setObjectName(u"tableWidget")
        font21 = QFont()
        font21.setFamily(u"Comic Sans MS")
        font21.setPointSize(10)
        self.tableWidget.setFont(font21)
        self.tableWidget.setStyleSheet(u"background-color: 	#f0ca8f;\n"
"color:rgb(0, 0, 0);\n"
"                                                                                    ")
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)

        self.verticalLayout_18.addWidget(self.tableWidget)

        self.label_22 = QLabel(self.show_attend_frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(0, 0, 191, 41))
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px;\n"
"padding:5px;\n"
"background-position: center left;")
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_22.setTextInteractionFlags(Qt.NoTextInteraction)
        self.convert_to_csv = QPushButton(self.show_attend_frame)
        self.convert_to_csv.setObjectName(u"convert_to_csv")
        self.convert_to_csv.setGeometry(QRect(810, 120, 171, 81))
        self.convert_to_csv.setMinimumSize(QSize(0, 0))
        self.convert_to_csv.setMaximumSize(QSize(16777215, 16777215))
        self.convert_to_csv.setFont(font12)
        self.convert_to_csv.setCursor(QCursor(Qt.PointingHandCursor))
        self.convert_to_csv.setStyleSheet(u"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}")
        self.convert_to_csv.setInputMethodHints(Qt.ImhMultiLine)
        self.convert_to_csv_2 = QPushButton(self.show_attend_frame)
        self.convert_to_csv_2.setObjectName(u"convert_to_csv_2")
        self.convert_to_csv_2.setGeometry(QRect(810, 200, 171, 81))
        self.convert_to_csv_2.setMinimumSize(QSize(0, 0))
        self.convert_to_csv_2.setMaximumSize(QSize(16777215, 16777215))
        self.convert_to_csv_2.setFont(font12)
        self.convert_to_csv_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.convert_to_csv_2.setStyleSheet(u"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}")
        self.convert_to_csv_2.setInputMethodHints(Qt.ImhMultiLine)

        self.verticalLayout_10.addWidget(self.show_attend_frame)

        self.stackedWidget.addWidget(self.show_attend_page)
        self.charts_page = QWidget()
        self.charts_page.setObjectName(u"charts_page")
        self.charts_page.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.charts_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.charts_page_frame = QFrame(self.charts_page)
        self.charts_page_frame.setObjectName(u"charts_page_frame")
        self.charts_page_frame.setFrameShape(QFrame.StyledPanel)
        self.charts_page_frame.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.charts_page_frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(0, 0, 111, 41))
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px;\n"
"padding:5px;\n"
"background-position: center left;")
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setTextInteractionFlags(Qt.NoTextInteraction)
        self.show_chart_button = QPushButton(self.charts_page_frame)
        self.show_chart_button.setObjectName(u"show_chart_button")
        self.show_chart_button.setGeometry(QRect(410, 10, 200, 200))
        self.show_chart_button.setMinimumSize(QSize(0, 0))
        self.show_chart_button.setMaximumSize(QSize(16777215, 16777215))
        self.show_chart_button.setFont(font12)
        self.show_chart_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_chart_button.setStyleSheet(u"background-color:#f0dabe;\n"
"background-image: url(:/icons/icons2/statistics.png);\n"
"background-repeat:none;\n"
"background-position:center;\n"
"border-radius:100px;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons2/statistics.png", QSize(), QIcon.Normal, QIcon.Off)
        self.show_chart_button.setIcon(icon3)
        self.show_chart_button.setIconSize(QSize(180, 180))
        self.chart_frame_3 = QFrame(self.charts_page_frame)
        self.chart_frame_3.setObjectName(u"chart_frame_3")
        self.chart_frame_3.setGeometry(QRect(70, 310, 871, 381))
        self.chart_frame_3.setStyleSheet(u"QFrame{\n"
"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"background-color: 	#f0ca8f;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}\n"
"QLabel{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: rgb(240, 202, 143);\n"
"}\n"
"QComboBox{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 202, 143);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}\n"
"QListView{\n"
"background-color: rgb(56, 108, 128);"
                        "\n"
"border: 3px solid rgb(70, 85, 134);\n"
"padding-top: 10px;\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"}\n"
"QComboBox:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"\n"
"")
        self.chart_frame_3.setFrameShape(QFrame.StyledPanel)
        self.chart_frame_3.setFrameShadow(QFrame.Raised)
        self.chart_frame_2 = QFrame(self.chart_frame_3)
        self.chart_frame_2.setObjectName(u"chart_frame_2")
        self.chart_frame_2.setGeometry(QRect(110, 20, 601, 101))
        self.chart_frame_2.setStyleSheet(u"QFrame{\n"
"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"background-color: 	#f0ca8f;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}\n"
"QLabel{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: rgb(240, 202, 143);\n"
"}\n"
"QComboBox{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 202, 143);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}\n"
"QListView{\n"
"background-color: rgb(56, 108, 128);"
                        "\n"
"border: 3px solid rgb(70, 85, 134);\n"
"padding-top: 10px;\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"}\n"
"QComboBox:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"\n"
"")
        self.chart_frame_2.setFrameShape(QFrame.StyledPanel)
        self.chart_frame_2.setFrameShadow(QFrame.Raised)
        self.show_chart_button_2 = QPushButton(self.chart_frame_2)
        self.show_chart_button_2.setObjectName(u"show_chart_button_2")
        self.show_chart_button_2.setGeometry(QRect(340, 20, 111, 60))
        self.show_chart_button_2.setMinimumSize(QSize(0, 0))
        self.show_chart_button_2.setMaximumSize(QSize(16777215, 16777215))
        self.show_chart_button_2.setFont(font12)
        self.show_chart_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_chart_button_2.setStyleSheet(u"QToolTip{\n"
"                                                                                        border: 2px solid rgb(114, 137,\n"
"                                                                                        218);\n"
"                                                                                        color: rgb(255, 255, 255);\n"
"                                                                                        background-color:rgb(44, 47,\n"
"                                                                                        51);\n"
"                                                                                        }\n"
"                                                                                    ")
        self.label_55 = QLabel(self.chart_frame_2)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(20, 20, 271, 61))
        self.label_55.setFont(font17)
        self.show_chart_button_3 = QPushButton(self.chart_frame_2)
        self.show_chart_button_3.setObjectName(u"show_chart_button_3")
        self.show_chart_button_3.setGeometry(QRect(470, 20, 111, 60))
        self.show_chart_button_3.setMinimumSize(QSize(0, 0))
        self.show_chart_button_3.setMaximumSize(QSize(16777215, 16777215))
        self.show_chart_button_3.setFont(font12)
        self.show_chart_button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_chart_button_3.setStyleSheet(u"QToolTip{\n"
"                                                                                        border: 2px solid rgb(114, 137,\n"
"                                                                                        218);\n"
"                                                                                        color: rgb(255, 255, 255);\n"
"                                                                                        background-color:rgb(44, 47,\n"
"                                                                                        51);\n"
"                                                                                        }\n"
"                                                                                    ")
        self.chart_frame_4 = QFrame(self.chart_frame_3)
        self.chart_frame_4.setObjectName(u"chart_frame_4")
        self.chart_frame_4.setGeometry(QRect(140, 140, 541, 101))
        self.chart_frame_4.setStyleSheet(u"QFrame{\n"
"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"background-color: 	#f0ca8f;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}\n"
"QLabel{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: rgb(240, 202, 143);\n"
"}\n"
"QComboBox{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 202, 143);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}\n"
"QListView{\n"
"background-color: rgb(56, 108, 128);"
                        "\n"
"border: 3px solid rgb(70, 85, 134);\n"
"padding-top: 10px;\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"}\n"
"QComboBox:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"\n"
"")
        self.chart_frame_4.setFrameShape(QFrame.StyledPanel)
        self.chart_frame_4.setFrameShadow(QFrame.Raised)
        self.show_chart_button_4 = QPushButton(self.chart_frame_4)
        self.show_chart_button_4.setObjectName(u"show_chart_button_4")
        self.show_chart_button_4.setGeometry(QRect(280, 20, 111, 60))
        self.show_chart_button_4.setMinimumSize(QSize(0, 0))
        self.show_chart_button_4.setMaximumSize(QSize(16777215, 16777215))
        self.show_chart_button_4.setFont(font12)
        self.show_chart_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_chart_button_4.setStyleSheet(u"QToolTip{\n"
"                                                                                        border: 2px solid rgb(114, 137,\n"
"                                                                                        218);\n"
"                                                                                        color: rgb(255, 255, 255);\n"
"                                                                                        background-color:rgb(44, 47,\n"
"                                                                                        51);\n"
"                                                                                        }\n"
"                                                                                    ")
        self.label_57 = QLabel(self.chart_frame_4)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(20, 20, 211, 61))
        self.label_57.setFont(font17)
        self.show_chart_button_5 = QPushButton(self.chart_frame_4)
        self.show_chart_button_5.setObjectName(u"show_chart_button_5")
        self.show_chart_button_5.setGeometry(QRect(410, 20, 111, 60))
        self.show_chart_button_5.setMinimumSize(QSize(0, 0))
        self.show_chart_button_5.setMaximumSize(QSize(16777215, 16777215))
        self.show_chart_button_5.setFont(font12)
        self.show_chart_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_chart_button_5.setStyleSheet(u"QToolTip{\n"
"                                                                                        border: 2px solid rgb(114, 137,\n"
"                                                                                        218);\n"
"                                                                                        color: rgb(255, 255, 255);\n"
"                                                                                        background-color:rgb(44, 47,\n"
"                                                                                        51);\n"
"                                                                                        }\n"
"                                                                                    ")
        self.chart_frame_5 = QFrame(self.chart_frame_3)
        self.chart_frame_5.setObjectName(u"chart_frame_5")
        self.chart_frame_5.setGeometry(QRect(140, 260, 541, 101))
        self.chart_frame_5.setStyleSheet(u"QFrame{\n"
"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"background-color: 	#f0ca8f;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}\n"
"QLabel{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: rgb(240, 202, 143);\n"
"}\n"
"QComboBox{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 202, 143);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}\n"
"QListView{\n"
"background-color: rgb(56, 108, 128);"
                        "\n"
"border: 3px solid rgb(70, 85, 134);\n"
"padding-top: 10px;\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"}\n"
"QComboBox:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"\n"
"")
        self.chart_frame_5.setFrameShape(QFrame.StyledPanel)
        self.chart_frame_5.setFrameShadow(QFrame.Raised)
        self.show_chart_button_6 = QPushButton(self.chart_frame_5)
        self.show_chart_button_6.setObjectName(u"show_chart_button_6")
        self.show_chart_button_6.setGeometry(QRect(280, 20, 111, 60))
        self.show_chart_button_6.setMinimumSize(QSize(0, 0))
        self.show_chart_button_6.setMaximumSize(QSize(16777215, 16777215))
        self.show_chart_button_6.setFont(font12)
        self.show_chart_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_chart_button_6.setStyleSheet(u"QToolTip{\n"
"                                                                                        border: 2px solid rgb(114, 137,\n"
"                                                                                        218);\n"
"                                                                                        color: rgb(255, 255, 255);\n"
"                                                                                        background-color:rgb(44, 47,\n"
"                                                                                        51);\n"
"                                                                                        }\n"
"                                                                                    ")
        self.label_60 = QLabel(self.chart_frame_5)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(20, 20, 211, 61))
        self.label_60.setFont(font17)
        self.show_chart_button_7 = QPushButton(self.chart_frame_5)
        self.show_chart_button_7.setObjectName(u"show_chart_button_7")
        self.show_chart_button_7.setGeometry(QRect(410, 20, 111, 60))
        self.show_chart_button_7.setMinimumSize(QSize(0, 0))
        self.show_chart_button_7.setMaximumSize(QSize(16777215, 16777215))
        self.show_chart_button_7.setFont(font12)
        self.show_chart_button_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_chart_button_7.setStyleSheet(u"QToolTip{\n"
"                                                                                        border: 2px solid rgb(114, 137,\n"
"                                                                                        218);\n"
"                                                                                        color: rgb(255, 255, 255);\n"
"                                                                                        background-color:rgb(44, 47,\n"
"                                                                                        51);\n"
"                                                                                        }\n"
"                                                                                    ")
        self.label_62 = QLabel(self.charts_page_frame)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(460, 210, 101, 41))
        self.label_62.setFont(font17)
        self.label_62.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_62.setAlignment(Qt.AlignCenter)
        self.label_62.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_63 = QLabel(self.charts_page_frame)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(620, 150, 60, 60))
        self.label_63.setStyleSheet(u"image: url(:/icons/icons2/diagram (1).png);\n"
"")
        self.label_64 = QLabel(self.charts_page_frame)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(320, 30, 60, 60))
        self.label_64.setStyleSheet(u"image: url(:/icons/icons2/line-chart.png);\n"
"")

        self.verticalLayout_9.addWidget(self.charts_page_frame)

        self.stackedWidget.addWidget(self.charts_page)
        self.download_page = QWidget()
        self.download_page.setObjectName(u"download_page")
        self.download_page.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.download_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.download_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 161, 41))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px;\n"
"padding:5px;\n"
"background-position: center left;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setTextInteractionFlags(Qt.NoTextInteraction)
        self.send_email_frame = QFrame(self.frame)
        self.send_email_frame.setObjectName(u"send_email_frame")
        self.send_email_frame.setGeometry(QRect(50, 180, 861, 571))
        self.send_email_frame.setStyleSheet(u"QFrame{\n"
"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"background-color: 	#f0ca8f;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}\n"
"QLabel{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: rgb(240, 202, 143);\n"
"}\n"
"QComboBox{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 202, 143);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}\n"
"QListView{\n"
"background-color: rgb(56, 108, 128);"
                        "\n"
"border: 3px solid rgb(70, 85, 134);\n"
"padding-top: 10px;\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"}\n"
"QComboBox:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"\n"
"")
        self.send_email_frame.setFrameShape(QFrame.StyledPanel)
        self.send_email_frame.setFrameShadow(QFrame.Raised)
        self.send_email_button = QPushButton(self.send_email_frame)
        self.send_email_button.setObjectName(u"send_email_button")
        self.send_email_button.setGeometry(QRect(420, 480, 161, 70))
        self.send_email_button.setMinimumSize(QSize(0, 0))
        self.send_email_button.setMaximumSize(QSize(16777215, 16777215))
        self.send_email_button.setFont(font12)
        self.send_email_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.email_address = QLineEdit(self.send_email_frame)
        self.email_address.setObjectName(u"email_address")
        self.email_address.setGeometry(QRect(280, 20, 441, 61))
        self.email_address.setMinimumSize(QSize(0, 0))
        self.email_address.setMaximumSize(QSize(16777215, 16777215))
        self.email_address.setFont(font14)
        self.email_address.setStyleSheet(u"")
        self.email_address.setText(u"")
        self.email_address.setAlignment(Qt.AlignCenter)
        self.textEdit = QTextEdit(self.send_email_frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(60, 180, 741, 211))
        font22 = QFont()
        font22.setFamily(u"Comic Sans MS")
        font22.setPointSize(12)
        font22.setBold(False)
        font22.setWeight(50)
        self.textEdit.setFont(font22)
        self.textEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"")
        self.textEdit.setCursorWidth(3)
        self.file_name = QLabel(self.send_email_frame)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setGeometry(QRect(60, 410, 581, 41))
        self.file_name.setFont(font21)
        self.browse_button = QPushButton(self.send_email_frame)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setGeometry(QRect(650, 410, 151, 41))
        self.browse_button.setMinimumSize(QSize(0, 0))
        self.browse_button.setMaximumSize(QSize(16777215, 16777215))
        self.browse_button.setFont(font17)
        self.browse_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.browse_button.setStyleSheet(u"padding:5px;\n"
"")
        self.subject = QLineEdit(self.send_email_frame)
        self.subject.setObjectName(u"subject")
        self.subject.setGeometry(QRect(280, 100, 441, 61))
        self.subject.setMinimumSize(QSize(0, 0))
        self.subject.setMaximumSize(QSize(16777215, 16777215))
        self.subject.setFont(font14)
        self.subject.setStyleSheet(u"")
        self.subject.setText(u"")
        self.subject.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.send_email_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 20, 201, 61))
        self.label_7.setFont(font17)
        self.label_14 = QLabel(self.send_email_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(60, 100, 201, 61))
        self.label_14.setFont(font17)
        self.clear_all_field = QPushButton(self.send_email_frame)
        self.clear_all_field.setObjectName(u"clear_all_field")
        self.clear_all_field.setGeometry(QRect(250, 480, 161, 70))
        self.clear_all_field.setMinimumSize(QSize(0, 0))
        self.clear_all_field.setMaximumSize(QSize(16777215, 16777215))
        self.clear_all_field.setFont(font12)
        self.clear_all_field.setCursor(QCursor(Qt.PointingHandCursor))
        self.email_res_frame = QFrame(self.frame)
        self.email_res_frame.setObjectName(u"email_res_frame")
        self.email_res_frame.setGeometry(QRect(50, 50, 861, 121))
        self.email_res_frame.setStyleSheet(u"QFrame{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 218, 190);\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 30px;\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 85, 64);\n"
"border:none;\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(116, 85, 68);\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid rgb(193, 97, 93);\n"
"}\n"
"QLabel{\n"
"border:none;\n"
"}\n"
"")
        self.email_res_frame.setFrameShape(QFrame.StyledPanel)
        self.email_res_frame.setFrameShadow(QFrame.Raised)
        self.email_res_ok_btn = QPushButton(self.email_res_frame)
        self.email_res_ok_btn.setObjectName(u"email_res_ok_btn")
        self.email_res_ok_btn.setGeometry(QRect(780, 30, 71, 60))
        self.email_res_ok_btn.setMinimumSize(QSize(0, 0))
        self.email_res_ok_btn.setMaximumSize(QSize(16777215, 16777215))
        self.email_res_ok_btn.setFont(font12)
        self.email_res_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.email_res_ok_btn.setStyleSheet(u"QToolTip{\n"
"                                                                                        border: 2px solid rgb(114, 137,\n"
"                                                                                        218);\n"
"                                                                                        color: rgb(255, 255, 255);\n"
"                                                                                        background-color:rgb(44, 47,\n"
"                                                                                        51);\n"
"                                                                                        }\n"
"                                                                                    ")
        self.label_26 = QLabel(self.email_res_frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 10, 761, 101))
        self.label_26.setFont(font16)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.frame)

        self.stackedWidget.addWidget(self.download_page)
        self.std_profile_page = QWidget()
        self.std_profile_page.setObjectName(u"std_profile_page")
        self.std_profile_page.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.std_profile_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.std_profile_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.show_attend_input_field_frame_3 = QFrame(self.frame_3)
        self.show_attend_input_field_frame_3.setObjectName(u"show_attend_input_field_frame_3")
        self.show_attend_input_field_frame_3.setGeometry(QRect(30, 140, 681, 111))
        self.show_attend_input_field_frame_3.setMinimumSize(QSize(0, 0))
        self.show_attend_input_field_frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.show_attend_input_field_frame_3.setStyleSheet(u"QFrame{\n"
"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: 	#f0ca8f;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}\n"
"QLabel{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: rgb(240, 202, 143);\n"
"}\n"
"QComboBox{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 202, 143);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}\n"
"QListView{\n"
"background-color: rgb(56, 108, 128);\n"
""
                        "border: 3px solid rgb(70, 85, 134);\n"
"padding-top: 10px;\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"}\n"
"QComboBox:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}")
        self.show_attend_input_field_frame_3.setFrameShape(QFrame.StyledPanel)
        self.show_attend_input_field_frame_3.setFrameShadow(QFrame.Raised)
        self.label_61 = QLabel(self.show_attend_input_field_frame_3)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(20, 30, 200, 50))
        self.label_61.setMinimumSize(QSize(200, 50))
        self.label_61.setMaximumSize(QSize(200, 50))
        self.label_61.setFont(font20)
        self.label_61.setStyleSheet(u"")
        self.label_61.setAlignment(Qt.AlignCenter)
        self.show_attend_faculty_btn_3 = QPushButton(self.show_attend_input_field_frame_3)
        self.show_attend_faculty_btn_3.setObjectName(u"show_attend_faculty_btn_3")
        self.show_attend_faculty_btn_3.setGeometry(QRect(560, 20, 100, 71))
        self.show_attend_faculty_btn_3.setMinimumSize(QSize(0, 0))
        self.show_attend_faculty_btn_3.setMaximumSize(QSize(16777215, 16777215))
        self.show_attend_faculty_btn_3.setFont(font12)
        self.show_attend_faculty_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.lineEdit_2 = QLineEdit(self.show_attend_input_field_frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(227, 17, 321, 71))
        self.lineEdit_2.setFont(font17)
        self.show_attend_table_frame_3 = QFrame(self.frame_3)
        self.show_attend_table_frame_3.setObjectName(u"show_attend_table_frame_3")
        self.show_attend_table_frame_3.setGeometry(QRect(30, 270, 950, 491))
        self.show_attend_table_frame_3.setMinimumSize(QSize(950, 400))
        self.show_attend_table_frame_3.setMaximumSize(QSize(950, 500))
        self.show_attend_table_frame_3.setStyleSheet(u"QFrame{\n"
"background-color:	#f0ca8f;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(116, 85, 68);\n"
"}\n"
"")
        self.show_attend_table_frame_3.setFrameShape(QFrame.StyledPanel)
        self.show_attend_table_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.show_attend_table_frame_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_3 = QTableWidget(self.show_attend_table_frame_3)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setFont(font21)
        self.tableWidget_3.setStyleSheet(u"background-color: 	#f0ca8f;\n"
"color:rgb(0, 0, 0);\n"
"                                                                                    ")
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(180)

        self.verticalLayout_21.addWidget(self.tableWidget_3)

        self.show_attend_input_field_frame_4 = QFrame(self.frame_3)
        self.show_attend_input_field_frame_4.setObjectName(u"show_attend_input_field_frame_4")
        self.show_attend_input_field_frame_4.setGeometry(QRect(300, 10, 681, 111))
        self.show_attend_input_field_frame_4.setMinimumSize(QSize(0, 0))
        self.show_attend_input_field_frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.show_attend_input_field_frame_4.setStyleSheet(u"QFrame{\n"
"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: 	#f0ca8f;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}\n"
"QLabel{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 30px;\n"
"padding: 5px;\n"
"background-color: rgb(240, 202, 143);\n"
"}\n"
"QComboBox{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 202, 143);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}\n"
"QListView{\n"
"background-color: rgb(56, 108, 128);\n"
""
                        "border: 3px solid rgb(70, 85, 134);\n"
"padding-top: 10px;\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"}\n"
"QComboBox:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}")
        self.show_attend_input_field_frame_4.setFrameShape(QFrame.StyledPanel)
        self.show_attend_input_field_frame_4.setFrameShadow(QFrame.Raised)
        self.show_attend_faculty_btn_4 = QPushButton(self.show_attend_input_field_frame_4)
        self.show_attend_faculty_btn_4.setObjectName(u"show_attend_faculty_btn_4")
        self.show_attend_faculty_btn_4.setGeometry(QRect(560, 20, 100, 71))
        self.show_attend_faculty_btn_4.setMinimumSize(QSize(0, 0))
        self.show_attend_faculty_btn_4.setMaximumSize(QSize(16777215, 16777215))
        self.show_attend_faculty_btn_4.setFont(font12)
        self.show_attend_faculty_btn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_4 = QLabel(self.show_attend_input_field_frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 531, 91))
        self.label_4.setFont(font19)
        self.label_4.setStyleSheet(u"border:none;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setTextInteractionFlags(Qt.NoTextInteraction)
        self.convert_tocsv_name = QPushButton(self.frame_3)
        self.convert_tocsv_name.setObjectName(u"convert_tocsv_name")
        self.convert_tocsv_name.setGeometry(QRect(730, 160, 241, 71))
        self.convert_tocsv_name.setMinimumSize(QSize(0, 0))
        self.convert_tocsv_name.setMaximumSize(QSize(16777215, 16777215))
        self.convert_tocsv_name.setFont(font12)
        self.convert_tocsv_name.setCursor(QCursor(Qt.PointingHandCursor))
        self.convert_tocsv_name.setStyleSheet(u"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}")
        self.label_51 = QLabel(self.frame_3)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(0, 0, 291, 41))
        self.label_51.setFont(font2)
        self.label_51.setStyleSheet(u"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px;\n"
"padding:5px;\n"
"background-position: center left;")
        self.label_51.setAlignment(Qt.AlignCenter)
        self.label_51.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_7.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.std_profile_page)
        self.logout_page = QWidget()
        self.logout_page.setObjectName(u"logout_page")
        self.logout_page.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.logout_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.logout_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.exit_icon_btn = QPushButton(self.frame_4)
        self.exit_icon_btn.setObjectName(u"exit_icon_btn")
        self.exit_icon_btn.setGeometry(QRect(410, 50, 220, 220))
        self.exit_icon_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_icon_btn.setStyleSheet(u"background-image: url(:/icons/icons2/exit.png);\n"
"background-repeat:none;\n"
"background-position:center;\n"
"background-color:	#f0ca8f;\n"
"border:2px solid 	#745544;\n"
"border-radius:110px;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons2/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_icon_btn.setIcon(icon4)
        self.exit_icon_btn.setIconSize(QSize(200, 200))
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 0, 161, 41))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px;\n"
"padding:5px;\n"
"background-position: center left;")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setTextInteractionFlags(Qt.NoTextInteraction)
        self.logout_frame = QFrame(self.frame_4)
        self.logout_frame.setObjectName(u"logout_frame")
        self.logout_frame.setGeometry(QRect(160, 310, 741, 421))
        self.logout_frame.setMinimumSize(QSize(0, 0))
        self.logout_frame.setMaximumSize(QSize(16777215, 16777215))
        self.logout_frame.setStyleSheet(u"QFrame{\n"
"background-color: 	#f0dabe;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"border: 3px solid rgb(135, 102, 69);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(116, 85, 68);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: 	#f0ca8f;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"border: 3px solid #b84a4a;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: #4e6a50;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border: 3px solid #29201b;\n"
"}\n"
"QLabel{\n"
"border-radius: 40px;\n"
"padding: 5px;\n"
"background-color: rgb(240, 202, 143);\n"
"}\n"
"QComboBox{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 202, 143);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}\n"
"QListView{\n"
"background-color: rgb(56, 108, 128);\n"
"border: 3px solid rgb(70, 85, 134);\n"
""
                        "padding-top: 10px;\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"}\n"
"QComboBox:hover{\n"
"border: 3px solid rgb(81, 79, 105);\n"
"}")
        self.logout_frame.setFrameShape(QFrame.StyledPanel)
        self.logout_frame.setFrameShadow(QFrame.Raised)
        self.logout_yes_btn = QPushButton(self.logout_frame)
        self.logout_yes_btn.setObjectName(u"logout_yes_btn")
        self.logout_yes_btn.setGeometry(QRect(240, 320, 141, 71))
        self.logout_yes_btn.setMinimumSize(QSize(0, 0))
        self.logout_yes_btn.setMaximumSize(QSize(16777215, 16777215))
        self.logout_yes_btn.setFont(font12)
        self.logout_yes_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout_no_btn = QPushButton(self.logout_frame)
        self.logout_no_btn.setObjectName(u"logout_no_btn")
        self.logout_no_btn.setGeometry(QRect(400, 320, 141, 71))
        self.logout_no_btn.setMinimumSize(QSize(0, 0))
        self.logout_no_btn.setMaximumSize(QSize(16777215, 16777215))
        self.logout_no_btn.setFont(font12)
        self.logout_no_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_28 = QLabel(self.logout_frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 20, 110, 110))
        self.label_28.setStyleSheet(u"image: url(:/icons2/icons2/question.png);\n"
"background-color: rgb(240, 218, 190);\n"
"border-radius:55px;\n"
"border:none;")
        self.label_29 = QLabel(self.logout_frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(160, 60, 451, 241))
        font23 = QFont()
        font23.setFamily(u"Comic Sans MS")
        font23.setPointSize(30)
        font23.setBold(True)
        font23.setWeight(75)
        self.label_29.setFont(font23)
        self.label_29.setStyleSheet(u"border:none;")
        self.label_29.setAlignment(Qt.AlignCenter)
        self.label_29.setWordWrap(True)
        self.label_29.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_6.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.logout_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_page.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.settings_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.center_main_items)

        self.right_side_menu = QFrame(self.main_body)
        self.right_side_menu.setObjectName(u"right_side_menu")
        self.right_side_menu.setMinimumSize(QSize(0, 850))
        self.right_side_menu.setMaximumSize(QSize(100, 850))
        self.right_side_menu.setStyleSheet(u"background-color: rgb(242, 227, 208);\n"
"")
        self.right_side_menu.setFrameShape(QFrame.NoFrame)
        self.right_side_menu.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.right_side_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(11, 0, -1, 0)

        self.horizontalLayout.addWidget(self.right_side_menu)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMinimumSize(QSize(0, 30))
        self.main_footer.setMaximumSize(QSize(16777215, 30))
        self.main_footer.setCursor(QCursor(Qt.ForbiddenCursor))
        self.main_footer.setStyleSheet(u"QFrame{\n"
"background-color: rgb(116, 85, 68);\n"
"border-top-color: solid 2px #000;\n"
"}\n"
"QLabel{\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"")
        self.main_footer.setFrameShape(QFrame.StyledPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)
        self.version_label = QLabel(self.main_footer)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setGeometry(QRect(1190, 0, 60, 30))
        self.version_label.setFont(font8)
        self.version_label.setStyleSheet(u"QLabel{\n"
"                                    color:rgb(255, 255, 255);\n"
"                                    }\n"
"                                ")
        self.version_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.main_footer, 0, Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMinimumSize(QSize(0, 28))
        self.statusBar.setMaximumSize(QSize(16777215, 28))
        font24 = QFont()
        font24.setFamily(u"Comic Sans MS")
        font24.setPointSize(10)
        font24.setItalic(True)
        self.statusBar.setFont(font24)
        self.statusBar.setCursor(QCursor(Qt.ForbiddenCursor))
        self.statusBar.setLayoutDirection(Qt.LeftToRight)
        self.statusBar.setStyleSheet(u"color: rgb(153, 170, 181);")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.minimizeButton.clicked.connect(MainWindow.showMinimized)
        self.closeButton.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.left_menu_toggle_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle Menu", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.left_menu_toggle_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Toogle Left Pane Menu", None))
#endif // QT_CONFIG(statustip)
        self.left_menu_toggle_btn.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"SMART ATTENDANCE", None))
#if QT_CONFIG(tooltip)
        self.minimizeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.minimizeButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Minimize Screen", None))
#endif // QT_CONFIG(statustip)
        self.minimizeButton.setText("")
#if QT_CONFIG(tooltip)
        self.closeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.closeButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Exit Application", None))
#endif // QT_CONFIG(statustip)
        self.closeButton.setText("")
#if QT_CONFIG(statustip)
        self.home_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Home Page", None))
#endif // QT_CONFIG(statustip)
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
#if QT_CONFIG(statustip)
        self.account_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Account Page", None))
#endif // QT_CONFIG(statustip)
        self.account_button.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT", None))
#if QT_CONFIG(statustip)
        self.take_attendance.setStatusTip(QCoreApplication.translate("MainWindow", u"Take Attendance", None))
#endif // QT_CONFIG(statustip)
        self.take_attendance.setText(QCoreApplication.translate("MainWindow", u"TAKE ATTENDANCE", None))
#if QT_CONFIG(statustip)
        self.show_attendance.setStatusTip(QCoreApplication.translate("MainWindow", u"Show Attendance", None))
#endif // QT_CONFIG(statustip)
        self.show_attendance.setText(QCoreApplication.translate("MainWindow", u"SHOW ATTENDANCE", None))
#if QT_CONFIG(statustip)
        self.profile_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Students profile", None))
#endif // QT_CONFIG(statustip)
        self.profile_button.setText(QCoreApplication.translate("MainWindow", u"STUDENT", None))
#if QT_CONFIG(statustip)
        self.download_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Send Email", None))
#endif // QT_CONFIG(statustip)
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"SEND EMAIL", None))
#if QT_CONFIG(statustip)
        self.chart_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Charts Page", None))
#endif // QT_CONFIG(statustip)
        self.chart_button.setText(QCoreApplication.translate("MainWindow", u"CHARTS", None))
#if QT_CONFIG(statustip)
        self.logout_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Students profile", None))
#endif // QT_CONFIG(statustip)
        self.logout_button.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>-&gt;\n"
"                                                                            Homepage</p></body></html>\n"
"                                                                        ", None))
        self.label_40.setText("")
        self.label_49.setText("")
        self.label_50.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Total Students</p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Attendees</p></body></html>", None))
#if QT_CONFIG(statustip)
        self.refresh_db_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Refresh Database", None))
#endif // QT_CONFIG(statustip)
        self.refresh_db_button.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Welcome</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.register_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Register to database", None))
#endif // QT_CONFIG(statustip)
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"Resgister", None))
#if QT_CONFIG(statustip)
        self.take_photo_attend.setStatusTip(QCoreApplication.translate("MainWindow", u"Take photo", None))
#endif // QT_CONFIG(statustip)
        self.take_photo_attend.setText(QCoreApplication.translate("MainWindow", u"Take Photo", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Faculty\n"
"                                                                                        <span style=\"\n"
"                                                                                        color:#ff0000;\">*</span></p></body></html>\n"
"                                                                                    ", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Bsc.CSIT", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"BCA", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"BIM", None))

        self.comboBox_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Faculty", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Semester\n"
"                                                                                        <span style=\"\n"
"                                                                                        color:#ff0000;\">*</span></p></body></html>\n"
"                                                                                    ", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Student Registration", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"CSIT(First)", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"CSIT(Second)", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"CSIT(Third)", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("MainWindow", u"BCA(First)", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("MainWindow", u"BCA(Second)", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("MainWindow", u"BCA(Third)", None))
        self.comboBox_6.setItemText(6, QCoreApplication.translate("MainWindow", u"BIM(First)", None))
        self.comboBox_6.setItemText(7, QCoreApplication.translate("MainWindow", u"BIM(Second)", None))
        self.comboBox_6.setItemText(8, QCoreApplication.translate("MainWindow", u"BIM(Third)", None))

        self.comboBox_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Semester", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Full\n"
"                                                                                        Name <span style=\"\n"
"                                                                                        color:#ff0000;\">*</span></p></body></html>\n"
"                                                                                    ", None))
#if QT_CONFIG(statustip)
        self.generate_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Generate 4 digit student id", None))
#endif // QT_CONFIG(statustip)
        self.generate_button.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.std_roll.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Student Id", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Std Id: <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.register_res_msg.setText("")
        self.register_res_msg_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
#if QT_CONFIG(statustip)
        self.create_an_account_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Create an account", None))
#endif // QT_CONFIG(statustip)
        self.create_an_account_button.setText(QCoreApplication.translate("MainWindow", u"Create an account", None))
        self.confirm_password_label.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.admin_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Username\n"
"                                                                                        <span style=\"\n"
"                                                                                        color:#ff0000;\">*</span></p></body></html>\n"
"                                                                                    ", None))
        self.password_label.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Password\n"
"                                                                                        <span style=\"\n"
"                                                                                        color:#ff0000;\">*</span></p></body></html>\n"
"                                                                                    ", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Admin Registration", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Confirm\n"
"                                                                                        Password <span style=\"\n"
"                                                                                        color:#ff0000;\">*</span></p></body></html>\n"
"                                                                                    ", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Show Password", None))
#if QT_CONFIG(statustip)
        self.password_generator.setStatusTip(QCoreApplication.translate("MainWindow", u"Generate 10 digits random password", None))
#endif // QT_CONFIG(statustip)
        self.password_generator.setText(QCoreApplication.translate("MainWindow", u"Generate Pass", None))
        self.register_res_msg_2.setText(QCoreApplication.translate("MainWindow", u"(Password must be at least 6 character long)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>-&gt;\n"
"                                                                            Accounts / Register</p><p><br/></p></body></html>\n"
"                                                                        ", None))
#if QT_CONFIG(statustip)
        self.submit_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Submit to Database", None))
#endif // QT_CONFIG(statustip)
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.username_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Student Id", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Time\n"
"                                                                                        <span style=\"\n"
"                                                                                        color:#ff0000;\">*</span></p></body></html>\n"
"                                                                                    ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Student\n"
"                                                                                        Id <span style=\"\n"
"                                                                                        color:#ff0000;\">*</span></p></body></html>\n"
"                                                                                    ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Manual</p><p>Attendance</p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Date\n"
"                                                                                        <span style=\"\n"
"                                                                                        color:#ff0000;\">*</span></p></body></html>\n"
"                                                                                    ", None))
        self.date_fill.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.time_fill.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Time", None))
#if QT_CONFIG(statustip)
        self.auto_fill_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Auto fill date and time field", None))
#endif // QT_CONFIG(statustip)
        self.auto_fill_button.setText(QCoreApplication.translate("MainWindow", u"Auto Fill", None))
#if QT_CONFIG(statustip)
        self.take_A_butn.setStatusTip(QCoreApplication.translate("MainWindow", u"Face Recognition Attendance System", None))
#endif // QT_CONFIG(statustip)
        self.take_A_butn.setText(QCoreApplication.translate("MainWindow", u"Smart Attendance", None))
        self.take_attend_res_msg.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.take_attend_res_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>-&gt;\n"
"                                                                            Take Attendance</p></body></html>\n"
"                                                                        ", None))
        self.show_attend_res_msg.setText(QCoreApplication.translate("MainWindow", u"Please select either faculty / semester.", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Attendance by semester", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"CSIT(First)", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"CSIT(Second)", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"CSIT(Third)", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"BCA(First)", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"BCA(Second)", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"BCA(Third)", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", u"BIM(First)", None))
        self.comboBox_4.setItemText(7, QCoreApplication.translate("MainWindow", u"BIM(Second)", None))
        self.comboBox_4.setItemText(8, QCoreApplication.translate("MainWindow", u"BIM(Third)", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Attendance by faculty", None))
        self.show_attend_semsester_btn.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.show_attend_faculty_btn.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"CSIT", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"BCA", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"BIM", None))

        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>-&gt;\n"
"                                                                            Show Attendance</p></body></html>\n"
"                                                                        ", None))
        self.convert_to_csv.setText(QCoreApplication.translate("MainWindow", u"Convert to \n"
"CSV", None))
        self.convert_to_csv_2.setText(QCoreApplication.translate("MainWindow", u"Convert to \n"
"CSV", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>-&gt;\n"
"                                                                            Charts</p></body></html>\n"
"                                                                        ", None))
        self.show_chart_button.setText("")
        self.show_chart_button_2.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"By Students Name/Id ->", None))
        self.show_chart_button_3.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.show_chart_button_4.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"By Faculty ->", None))
        self.show_chart_button_5.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.show_chart_button_6.setText(QCoreApplication.translate("MainWindow", u"Bar", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"By Semester ->", None))
        self.show_chart_button_7.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Charts", None))
        self.label_63.setText("")
        self.label_64.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>-&gt; Send Email</p></body></html>", None))
        self.send_email_button.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.email_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email Address", None))
        self.textEdit.setMarkdown("")
        self.file_name.setText("")
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.subject.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Subject", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Email Address : <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Subject : <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.clear_all_field.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.email_res_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_26.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Student Name <span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.show_attend_faculty_btn_3.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.show_attend_faculty_btn_4.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_4.setText("")
        self.convert_tocsv_name.setText(QCoreApplication.translate("MainWindow", u"Convert to\n"
"CSV", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>-&gt; Individual Attendance sheet</p></body></html>", None))
        self.exit_icon_btn.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>-&gt; Log out</p></body></html>", None))
        self.logout_yes_btn.setText(QCoreApplication.translate("MainWindow", u"YES", None))
        self.logout_no_btn.setText(QCoreApplication.translate("MainWindow", u"NO", None))
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Are you sure? You want to logout!", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"v 1.1", None))
#if QT_CONFIG(statustip)
        self.statusBar.setStatusTip("")
#endif // QT_CONFIG(statustip)
    # retranslateUi

