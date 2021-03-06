import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

import re
import datetime
import random
import string
import sys
import cv2
import os
import matplotlib
import platform

import pandas
from PyQt5.QtCore import pyqtSlot
from matplotlib import pyplot as plt, pyplot
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as navi

import numpy as np
import face_recognition as face

import pymysql
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# Import user interface file
from ui_nike_main_window import *

# Global value for the windows status
WINDOW_SIZE = 0


# This will help us determine if the window is minimized or maximized

# Main class
class MainWindow(QMainWindow):
    @pyqtSlot()
    def getAdminUsername(self, adUsername):
        self.ui.label_58.setText(adUsername)

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global successStyle, errorStyle

        self._new_window = None

        # Remove window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.image1path = 'icons2/exit.png'
        self.image2path = 'icons2/question.png'
        self.image3path = 'icons2/statistics.png'
        self.image4path = 'icons2/line-chart.png'
        self.image5path = 'icons2/diagram (1).png'

        self.image1 = QtGui.QImage(self.image1path)
        self.image2 = QtGui.QImage(self.image2path)
        self.image3 = QtGui.QImage(self.image3path)
        self.image4 = QtGui.QImage(self.image4path)
        self.image5 = QtGui.QImage(self.image5path)

        self.ui.exit_icon_btn.setIcon(QtGui.QPixmap.fromImage(self.image1))
        self.ui.exit_icon_btn.setGeometry(410, 50, 220, 220)
        self.ui.show_chart_button.setIcon(QtGui.QPixmap.fromImage(self.image3))
        self.ui.show_chart_button.setGeometry(410, 10, 200, 200)
        self.ui.label_28.setPixmap(QtGui.QPixmap.fromImage(self.image2))
        self.ui.label_28.setScaledContents(True)
        self.ui.label_64.setPixmap(QtGui.QPixmap.fromImage(self.image4))
        self.ui.label_64.setScaledContents(True)
        self.ui.label_63.setPixmap(QtGui.QPixmap.fromImage(self.image5))
        self.ui.label_63.setScaledContents(True)
        self.ui.logout_frame.hide()
        self.ui.exit_icon_btn.clicked.connect(lambda: self.ui.logout_frame.show())

        # ###############################################
        # home page --> clock
        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)

        # Button click events to our top bar buttons
        # Minimize window
        # self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        # Close window
        # self.ui.closeButton.clicked.connect(lambda: self.close())
        # Restore/Maximize window
        # self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())

        # ###############################################
        # clear all the field button on email page
        self.ui.clear_all_field.clicked.connect(lambda: self.clearAllField())

        # ###############################################
        # show attendance by student name
        self.ui.show_attend_faculty_btn_3.clicked.connect(lambda: self.ShowAttendByName())

        self.ui.show_attend_input_field_frame_4.hide()
        self.ui.show_attend_faculty_btn_4.clicked.connect(lambda: self.ui.show_attend_input_field_frame_4.hide())

        # ###############################################
        # covert to csv button
        self.ui.convert_to_csv.hide()
        self.ui.convert_to_csv.clicked.connect(lambda: self.convertToCsvFaculty())
        self.ui.convert_to_csv_2.hide()
        self.ui.convert_to_csv_2.clicked.connect(lambda: self.convertToCsvSemester())
        self.ui.convert_tocsv_name.hide()
        self.ui.convert_tocsv_name.clicked.connect(lambda: self.convertToCsvName())

        # ###############################################
        # browse button file dialogue
        self.ui.browse_button.clicked.connect(lambda: self.browseFile())

        # ###############################################
        # register page register frame
        self.ui.email_res_frame.hide()
        self.ui.email_res_ok_btn.clicked.connect(lambda: self.ui.email_res_frame.hide())

        # ###############################################
        # register page register frame
        self.ui.register_res_frame.hide()
        self.ui.register_res_msg_ok_btn.clicked.connect(lambda: self.registerResMsgOk())

        self.showDate()

        # ###############################################
        # take attend button
        self.ui.take_A_butn.clicked.connect(lambda: self.markAttendance())

        # ###############################################
        # show chart button
        self.ui.chart_frame_3.hide()
        self.ui.show_chart_button.clicked.connect(lambda: self.ui.chart_frame_3.show())
        self.ui.show_chart_button_2.clicked.connect(lambda: self.showChart())
        self.ui.show_chart_button_3.clicked.connect(lambda: self.chartStudentLine())
        self.ui.show_chart_button_4.clicked.connect(lambda: self.chartFacultyBar())
        self.ui.show_chart_button_5.clicked.connect(lambda: self.chartFacultyLine())

        self.ui.show_chart_button_6.clicked.connect(lambda: self.chartSemesterBar())
        self.ui.show_chart_button_7.clicked.connect(lambda: self.chartSemesterLine())

        # ###############################################
        # show attend button
        # Move window on mouse drag event on the tittle bar
        def moveWindow(e):
            # Detect if the window is  normal size
            if self.isMaximized() == False:  # Not maximized
                # Move window only when window is normal size
                # if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    # Move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        # Add click event/Mouse move event/drag event to the top header to move the window
        self.ui.main_header.mouseMoveEvent = moveWindow

        # ###############################################
        # show attend button
        self.ui.show_attend_faculty_btn.clicked.connect(lambda: self.showAttendFacultyFromDb())
        self.ui.show_attend_semsester_btn.clicked.connect(lambda: self.showAttendSemesterFromDb())

        # ###############################################
        # accounts page --> checkbox
        self.c1 = self.ui.checkBox
        self.c1.stateChanged.connect(lambda: self.checkboxClicked(self.c1))

        # ###############################################
        # send email button
        self.ui.send_email_button.clicked.connect(lambda: self.emailValidation())

        # ###############################################
        # refresh button homepage
        self.ui.refresh_db_button.clicked.connect(lambda: self.refreshDB())
        # ###############################################
        # create an admin account button
        self.ui.create_an_account_button.clicked.connect(lambda: self.createAdminAccount())

        # ###############################################
        # take photo for attendance
        self.ui.take_photo_attend.clicked.connect(lambda: self.takePhotoAttendance())

        # ###############################################
        # auto fill date and time field
        self.ui.auto_fill_button.clicked.connect(lambda: self.auto_fill_datetime())

        # ###############################################
        # auto generate 5 digit student id
        self.ui.generate_button.clicked.connect(lambda: self.auto_generate_roll_id())
        self.ui.register_button.clicked.connect(lambda: self.studentRegistration())
        # auto generate 10 digit password
        self.ui.password_generator.clicked.connect(lambda: self.passwordGenerator())

        # ###############################################
        # take attendance page response message
        self.ui.take_attend_res_frame.hide()
        self.ui.take_attend_res_ok_btn.clicked.connect(lambda: self.ui.take_attend_res_frame.hide())

        self.ui.submit_button.clicked.connect(lambda: self.validateSubmitButton())

        # SLIDABLE LEFT MENU
        # Left Menu toggle button
        self.ui.left_menu_toggle_btn.clicked.connect(lambda: self.slideLeftMenu())

        # ###############################################
        # left menu styling
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)

        # STACKED PAGES (DEFAULT / CURRENT PAGE)
        # Set the page that will be visible by default when the app is opened
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

        # STACKED PAGES NAVIGATION
        # Using side menu buttons
        # navigate to Home page
        self.ui.home_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))

        # navigate to Accounts page
        self.ui.account_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.accounts_page))

        # navigate to Settings page
        # self.ui.setting_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))

        # navigate to take attendance page
        self.ui.take_attendance.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.take_attend_page))

        # navigate to show attendance page
        self.ui.show_attendance.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.show_attend_page))

        # navigate to chart page
        self.ui.chart_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.charts_page))

        # navigate to download page
        self.ui.download_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.download_page))

        # navigate to profile page
        self.ui.profile_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.std_profile_page))

        # navigate to logout page
        self.ui.logout_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.logout_page))
        self.ui.logout_no_btn.clicked.connect(lambda: self.logoutNoBtn())
        self.ui.logout_yes_btn.clicked.connect(lambda: self.logoutYesBtn())

        # Show window
        self.show()

    # ###############################################
    # logout yes button function
    def logoutYesBtn(self):
        sys.exit()

    def logoutNoBtn(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.logout_frame.hide()

    # ###############################################
    # convert to csv name function
    def convertToCsvName(self):
        # self.ui.convert_to_csv.show()
        na_me = self.ui.lineEdit_2.text()
        filename = f"CSVs/{datetime.datetime.now().strftime('%Y-%m-%d_%I-%M-%S')}_{na_me}.csv"
        # filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%I-%M-%S')}_Fac.csv"
        db = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
        sql_1_ = f"""SELECT a.std_id, s.fullname,a.date,a.time,f.name,sem.name
                            FROM student as s
                            LEFT JOIN attendance as a
                            ON a.std_id = s.std_id
                            LEFT JOIN faculty as f
                            ON s.faculty_id = f.f_id
                            LEFT JOIN semester as sem
                            ON s.semester_id = sem.sem_id
                            HAVING s.fullname = '{na_me}'
                            ORDER BY a.date;"""
        if db.open:
            results = pandas.read_sql_query(sql_1_, db)
            results.to_csv(filename, index=False)
            self.ui.convert_tocsv_name.setText('Converted!')
        else:
            print(Exception)
        db.close()

    # ###############################################
    # convert to csv faculty function
    def convertToCsvFaculty(self):
        # self.ui.convert_to_csv.show()
        facultyId = self.ui.comboBox_3.currentIndex() + 1
        filename = f"CSVs/{datetime.datetime.now().strftime('%Y-%m-%d_%I-%M-%S')}_Fac.csv"
        # filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%I-%M-%S')}_Fac.csv"
        db = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
        sql = f"""SELECT s.std_id,s.fullname,f.name,a.date,a.time
                    FROM student as s
                    LEFT JOIN attendance as a
                    ON s.std_id = a.std_id
                    LEFT JOIN faculty as f
                    ON s.faculty_id = f.f_id
                    WHERE s.faculty_id = {facultyId};"""
        if db.open:
            results = pandas.read_sql_query(sql, db)
            results.to_csv(filename, index=False)
            self.ui.convert_to_csv.setText('Converted!')
        else:
            print(Exception)
        db.close()

    # ###############################################
    # convert to csv Semester function
    def convertToCsvSemester(self):
        # self.ui.convert_to_csv_2.show()
        semesterId = self.ui.comboBox_4.currentIndex() + 1
        filename = f"CSVs/{datetime.datetime.now().strftime('%Y-%m-%d_%I-%M-%S')}_Sem.csv"
        # filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%I-%M-%S')}_Sem.csv"
        db = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
        sql = f"""SELECT s.std_id,s.fullname,f.name,sem.name,a.date,a.time
                            FROM student as s
                            LEFT JOIN attendance as a
                            ON s.std_id = a.std_id
                            LEFT JOIN faculty as f
                            ON s.faculty_id = f.f_id
                            LEFT JOIN semester as sem
                            ON s.semester_id = sem.sem_id
                            WHERE s.semester_id = {semesterId};"""
        if db.open:
            results = pandas.read_sql_query(sql, db)
            results.to_csv(filename, index=False)
            self.ui.convert_to_csv_2.setText('Converted!')
        else:
            print(Exception)
        db.close()

    # ###############################################
    # register response ok button function
    def registerResMsgOk(self):
        self.ui.register_res_frame.hide()

    # ###############################################
    # refresh db button function
    def refreshDB(self):
        db_conn = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
        cursor = db_conn.cursor()
        sql11 = """SELECT COUNT(std_id) FROM student"""
        sql22 = """SELECT COUNT(a_id) FROM attendance"""
        sql1 = """CREATE TABLE attendance_temp LIKE attendance;"""
        cursor.execute(sql1)
        sql3 = """INSERT INTO attendance_temp SELECT * FROM attendance GROUP BY std_id, date;"""
        cursor.execute(sql3)
        sql2 = """DROP TABLE attendance;"""
        cursor.execute(sql2)
        sql4 = """ALTER TABLE attendance_temp RENAME TO attendance;"""
        cursor.execute(sql4)
        try:
            if db_conn.open:
                cursor.execute(sql11)
                data = cursor.fetchone()
                cursor.execute(sql22)
                data1 = cursor.fetchone()
            else:
                print(Exception)
        except Exception as e:
            print(e)

        for x in data:
            x
        for y in data1:
            y
        c = x
        c1 = y
        # print(c)
        # print(c1)
        self.ui.label_53.setText(str(c))
        self.ui.label_56.setText(str(c1))
        db_conn.close()

    # ###############################################
    # take photo for attendance
    def takePhotoAttendance(self):
        webcam = cv2.VideoCapture(0)
        # sampleNum = 0
        name_ = self.ui.username.text().upper()
        stdid_ = self.ui.std_roll.text()
        regex = '^[a-zA-Z\s]+$'
        if name_ != '':
            if re.search(regex, name_):
                if stdid_ != '':
                    while webcam.isOpened():
                        _, img = webcam.read()

                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                        text = 'W: ' + str(webcam.get(3)) + ' H: ' + str(webcam.get(4))
                        dt = datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')
                        msg1 = 'Press \'Q/q\' to exit camera.'
                        msg2 = 'Press \'S/s\' to save images.'
                        cv2.putText(gray, text, (450, 20), cv2.FONT_HERSHEY_SIMPLEX, .6, (0, 0, 0), 1)
                        cv2.putText(gray, dt, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, .6, (0, 0, 0), 1)
                        cv2.putText(gray, msg1, (10, 45), cv2.FONT_HERSHEY_COMPLEX, .7, (0, 0, 0), 1)
                        cv2.putText(gray, msg2, (10, 70), cv2.FONT_HERSHEY_COMPLEX, .7, (0, 0, 0), 1)

                        cv2.imshow('Face', gray)

                        k = cv2.waitKey(1) & 0xFF

                        if k == ord('q'):
                            break
                        elif k == ord('s'):
                            file_path_name = f'ImagesAttendance/{name_}.{stdid_}.jpg'
                            cv2.imwrite(file_path_name, gray)
                            # sampleNum += 1
                else:
                    self.showRegisterMsg('Mandatory(*) field is empty!')
            else:
                self.showRegisterMsg('Invalid Name!')
        else:
            self.showRegisterMsg('Mandatory(*) field is empty!')
        webcam.release()
        cv2.destroyAllWindows()

    # Add mouse events to the window
    def mousePressEvent(self, event):

        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window

    # Restore or maximize your window
    # def restore_or_maximize_window(self):
    #     # Global windows state
    #     global WINDOW_SIZE  # The default value is zero to show that the size is not maximized
    #     win_status = WINDOW_SIZE
    #
    #     if win_status == 0:
    #         # If the window is not maximized
    #         WINDOW_SIZE = 1  # Update value to show that the window has been maximized
    #         self.showMaximized()
    #
    # # Update button icon  when window is maximized self.ui.restoreButton.setIcon(QtGui.QIcon(
    # u":/icons/icons/cil-window-restore.png"))  # Show minimized icon else: # If the window is on its default size
    # WINDOW_SIZE = 0  # Update value to show that the window has been minimized/set to normal size (which is 800 by
    # 400) self.showNormal()
    #
    #         # Update button icon when window is minimized
    #         self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-maximize.png"))  # Show maximize icon

    # Slide left menu
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.left_side_menu.width()

        # If minimized
        if width == 65:
            # Expand menu
            newWidth = 220
        # If maximized
        else:
            # Restore menu
            newWidth = 60

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.left_side_menu, b"minimumWidth")  # Animate minimumWidth
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    # ###############################################
    # auto fill datetime function
    def auto_fill_datetime(self):
        now = datetime.datetime.now()
        date_ = now.strftime('%Y-%m-%d')
        time_ = now.strftime('%I:%M %p')
        self.ui.date_fill.setText(date_)
        self.ui.time_fill.setText(time_)

    # ###############################################
    # take attendance page response function
    def showTakeAttendResponse(self, responseMessage):
        self.ui.take_attend_res_frame.show()
        self.ui.take_attend_res_msg.setText(responseMessage)
        # self.ui.username_2.clear()
        self.ui.username_3.clear()
        self.ui.date_fill.clear()
        self.ui.time_fill.clear()
        # self.ui.comboBox.setCurrentIndex(0)
        # self.ui.comboBox_2.setCurrentIndex(0)

    # ###############################################
    # validate submit function
    def validateSubmitButton(self):
        global db_con
        # m_full_name = self.ui.username_2.text()
        m_std_id = self.ui.username_3.text()
        # m_faculty = self.ui.comboBox.currentText()
        # m_semester = self.ui.comboBox_2.currentText()
        m_date = self.ui.date_fill.text()
        m_time = self.ui.time_fill.text()

        db_con = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
        cursor = db_con.cursor()
        sql = """select std_id from student"""
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as e:
            print(e)

        registered_std = [item for x in data for item in x]
        # print(registered_std)
        # if registered_std.count(int(m_std_id)) > 0:
        #     print('cha')
        # else:
        #     print('chaina')

        if db_con.open:
            querry = f"""INSERT INTO attendance(std_id, time, date) 
            VALUES ('{m_std_id}','{m_time}','{m_date}') """
            if m_std_id != '':
                if registered_std.count(int(m_std_id)) > 0:
                    if m_time != '':
                        if m_date != '':
                            try:
                                cursor.execute(querry)
                                db_con.commit()
                                msgtxt = 'Attendance Submitted Successfully.'
                                self.showTakeAttendResponse(msgtxt)
                            except Exception as e:
                                self.showTakeAttendResponse(str(e))
                                db_con.rollback()
                        else:
                            self.showTakeAttendResponse('Mandatory(*) field cannot be empty!')
                    else:
                        self.showTakeAttendResponse('Mandatory(*) field cannot be empty!')
                else:
                    self.showTakeAttendResponse('Student not registered in database!')
            else:
                self.showTakeAttendResponse('Mandatory(*) field cannot be empty!')
        else:
            self.showTakeAttendResponse(str(Exception))
        db_con.close()

    def applyButtonStyle(self):
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            if w.objectName() != self.sender().objectName():
                defaultStyle = w.styleSheet().replace("border-left: 3px solid rgb(75,134,180);border-bottom: 3px solid "
                                                      "rgb(75,134,180);border-top: 3px solid rgb(75,134,"
                                                      "180);border-right: 3px solid rgb(75,134,180);", "")
                # defaultStyle = defaultStyle.styleSheet().replace("border-left: 3px solid rgb(75,134,180);", "")
                w.setStyleSheet(defaultStyle)

        newStyle = self.sender().styleSheet() + ("border-left: 3px solid rgb(75,134,180);border-bottom: 3px solid "
                                                 "rgb(75,134,180);border-top: 3px solid rgb(75,134,180);border-right: "
                                                 "3px solid rgb(75,134,180);")
        self.sender().setStyleSheet(newStyle)
        return

    # ###############################################
    # generate 4 digit student id function
    def auto_generate_roll_id(self):
        s1 = string.digits
        id_length = 4
        s = []
        s.extend(list(s1))
        std_id_ = "".join(random.sample(s, id_length))
        self.ui.std_roll.setText(std_id_)

    # ###############################################
    # register students details show message frame function
    def showRegisterMsg(self, reg_text):
        self.ui.register_res_frame.show()
        self.ui.register_res_msg.setText(reg_text)

    # ###############################################
    # register students details in database function
    def studentRegistration(self):
        # successStyle = 'border: 3px solid rgb(0, 255, 255);border-radius:25px;'
        # errorStyle = 'border: 3px solid rgb(255, 0, 0);border-radius:25px;'
        db_conn = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
        cursor = db_conn.cursor()
        full_name = self.ui.username.text()
        std_id = self.ui.std_roll.text()
        faculty = self.ui.comboBox_5.currentIndex() + 1
        semester = self.ui.comboBox_6.currentIndex() + 1
        regex = '^[a-zA-Z\s]+$'

        if full_name != '':
            if re.search(regex, full_name):
                if std_id == '':
                    text_empty = 'Mandatory(*) field is/are empty!'
                    self.showRegisterMsg(text_empty)
                else:
                    if db_conn.open:
                        # print('Database Connected successfully!')
                        sql_querry = f""" INSERT INTO student(std_id, fullname, faculty_id, semester_id)
                                            VALUES ('{std_id}', '{full_name}', '{faculty}', '{semester}')"""
                        try:
                            cursor.execute(sql_querry)
                            db_conn.commit()
                            text = 'You have been registered.'
                            self.showRegisterMsg(text)
                            self.ui.username.clear()
                            self.ui.std_roll.clear()
                            self.ui.comboBox_5.setCurrentIndex(0)
                            self.ui.comboBox_6.setCurrentIndex(0)
                        except Exception as e:
                            db_conn.rollback()
                            self.showRegisterMsg(str(e))
                    else:
                        self.showRegisterMsg(str(Exception))
                    db_conn.close()
            else:
                t1 = 'Invalid Name!'
                self.showRegisterMsg(t1)
        else:
            t2 = 'Mandatory (*) field is/are empty!'
            self.showRegisterMsg(t2)

    # ###############################################
    # generate 10 digit password function
    def passwordGenerator(self):
        s1 = string.digits
        s2 = string.ascii_letters
        s3 = string.punctuation
        id_length = 10
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        password_ = "".join(random.sample(s, id_length))
        self.ui.password_label.setText(password_)
        self.ui.confirm_password_label.setText(password_)

    # ###############################################
    # ckeckbox clicked change state function
    def checkboxClicked(self, c):
        if c.isChecked():
            self.ui.password_label.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.confirm_password_label.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.password_label.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.confirm_password_label.setEchoMode(QtWidgets.QLineEdit.Password)

    # ###############################################
    # create an admin account function
    def createAdminAccount(self):
        db_conn = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
        cursor = db_conn.cursor()
        admin_name = self.ui.admin_username.text()
        admin_pass = self.ui.password_label.text()
        pass_confirm = self.ui.confirm_password_label.text()

        sql = """SELECT name FROM admin"""
        try:
            cursor.execute(sql)
            # print('done')
            details = cursor.fetchall()
            # print('d')
        except Exception as e:
            print(e)
        # print(details)

        namelist = [item for x in details for item in x]
        # print(namelist)

        textAdmin = 'Congrats! You have been registered as Admin.'
        if db_conn.open:
            # print('Database Connected successfully!')
            sql_querry = f""" INSERT INTO admin(name, pass)
                                        VALUES ('{admin_name}', '{admin_pass}')"""
            if admin_name != '' and admin_pass != '' and pass_confirm != '':
                if admin_name.isalpha() and len(admin_name) > 2:
                    if admin_name not in namelist:
                        if len(admin_pass) < 6:
                            self.showRegisterMsg('Use 6 characters or more for your password!')
                        else:
                            if admin_pass != pass_confirm:
                                self.showRegisterMsg('Those passwords didn’t match. Try again.')
                            else:
                                try:
                                    cursor.execute(sql_querry)
                                    db_conn.commit()
                                    self.showRegisterMsg(textAdmin)
                                    self.ui.admin_username.clear()
                                    self.ui.password_label.clear()
                                    self.ui.confirm_password_label.clear()
                                except Exception as e:
                                    db_conn.rollback()
                                    self.showRegisterMsg(str(e))
                    else:
                        t1 = 'Given Name Already Registered!'
                        self.showRegisterMsg(t1)
                else:
                    t = 'Invalid Username'
                    self.showRegisterMsg(t)
            else:
                text_empty = 'Mandatory(*) field is/are empty!'
                self.showRegisterMsg(text_empty)
        else:
            self.showRegisterMsg(str(Exception))
        db_conn.close()

    # ###############################################
    # home page --> clock function
    def displayTime(self):
        current_time = datetime.datetime.now()
        displaytxt = current_time.strftime('%I:%M:%S')
        ampm = current_time.strftime('%p')
        # print(displaytxt)

        self.ui.label_50.setText(displaytxt)
        self.ui.label_49.setText(ampm)

    # ###############################################
    # home page --> date function
    def showDate(self):
        dt = datetime.datetime.now()
        month = dt.strftime('%B')
        day = dt.strftime('%d')
        year = dt.strftime('%Y')
        weekday = dt.strftime('%A')
        self.ui.label_45.setText(month)
        self.ui.label_43.setText(day)
        self.ui.label_44.setText(f'/{year}')
        self.ui.label_42.setText(weekday)

    # ###############################################
    # show attend by name button function
    def ShowAttendByName(self):

        global sql_all_
        name = self.ui.lineEdit_2.text()

        db_conn = pymysql.connect(host='localhost', user='root', passwd='', db='finalproject')
        cursor = db_conn.cursor()

        sql1_ = f"""SELECT s.std_id,s.fullname,a.date,a.time,f.name,sem.name
                FROM student as s
                LEFT JOIN attendance as a
                ON s.std_id = a.std_id
                LEFT JOIN faculty as f
                ON s.faculty_id = f.f_id
                LEFT JOIN semester as sem
                ON s.semester_id = sem.sem_id
                HAVING s.fullname = '{name}'
                ORDER BY a.date;"""
        sql1 = """CREATE TABLE attendance_temp LIKE attendance;"""
        cursor.execute(sql1)
        sql3 = """INSERT INTO attendance_temp SELECT * FROM attendance GROUP BY std_id, date;"""
        cursor.execute(sql3)
        sql2 = """DROP TABLE attendance;"""
        cursor.execute(sql2)
        sql4 = """ALTER TABLE attendance_temp RENAME TO attendance;"""
        cursor.execute(sql4)

        # querry = """select fullname from student"""

        # cursor.execute(querry)
        # namelist = cursor.fetchall()
        # namelist_ = [item for x in namelist for item in x]
        # print(namelist_)
        # self._sql = ''
        # self.ui.convert_to_csv.show()
        # self.ui.convert_to_csv_2.hide()
        if db_conn.open:
            if name != '':
                self.ui.convert_tocsv_name.show()
                try:
                    cursor.execute(sql1_)

                    sql_all_ = cursor.fetchall()

                    # self._sql = [list(x) for x in sql_all_]

                except Exception as e:
                    self.ui.show_attend_input_field_frame_4.show()
                    self.ui.label_4.setText(str(e))
            else:
                self.ui.show_attend_input_field_frame_4.show()
                self.ui.label_4.setText('Mandatory (*) field cannot be empty')
        else:
            self.ui.show_attend_input_field_frame_4.show()
            self.ui.label_4.setText(str(Exception))

        self._sql = [list(x) for x in sql_all_]
        # print(self._sql)

        for row in self._sql:
            self.ui.tableWidget_3.insertRow(0)

        for col in self._sql:
            self.ui.tableWidget_3.insertColumn(0)

        for rowNr, rowValue in enumerate(self._sql):
            for itemNr, itemValue in enumerate(rowValue):
                self.ui.tableWidget_3.setItem(rowNr, itemNr, QtWidgets.QTableWidgetItem(str(self._sql[rowNr][itemNr])))
        print('Success')
        db_conn.close()

    # ###############################################
    # show attend by faculty button function
    def showAttendFacultyFromDb(self):
        global sql_all
        facultyId = self.ui.comboBox_3.currentIndex() + 1
        self.ui.convert_to_csv.setText('Convert to\nCSV')
        try:
            db_conn = pymysql.connect(host='localhost', user='root', passwd='', db='finalproject')
            cursor = db_conn.cursor()

            sql = f"""SELECT s.std_id,s.fullname,f.name,a.date,a.time
                    FROM student as s
                    LEFT JOIN attendance as a
                    ON s.std_id = a.std_id
                    LEFT JOIN faculty as f
                    ON s.faculty_id = f.f_id
                    WHERE s.faculty_id = {facultyId}
                    ORDER BY a.date;"""
            sql1 = """CREATE TABLE attendance_temp LIKE attendance;"""
            cursor.execute(sql1)
            sql3 = """INSERT INTO attendance_temp SELECT * FROM attendance GROUP BY std_id, date;"""
            cursor.execute(sql3)
            sql2 = """DROP TABLE attendance;"""
            cursor.execute(sql2)
            sql4 = """ALTER TABLE attendance_temp RENAME TO attendance;"""
            cursor.execute(sql4)

            self.ui.convert_to_csv.show()
            self.ui.convert_to_csv_2.hide()
            try:
                cursor.execute(sql)

                sql_all = cursor.fetchall()

            except Exception as e:
                print(e)
        except Exception as err:
            print(err)

        self._sql = [list(x) for x in sql_all]
        # print(self._sql)

        for row in self._sql:
            self.ui.tableWidget.insertRow(0)

        for col in self._sql:
            self.ui.tableWidget.insertColumn(0)

        for rowNr, rowValue in enumerate(self._sql):
            for itemNr, itemValue in enumerate(rowValue):
                self.ui.tableWidget.setItem(rowNr, itemNr, QtWidgets.QTableWidgetItem(str(self._sql[rowNr][itemNr])))
        print('Success')
        db_conn.close()

    # ###############################################
    # show attend by semester button function
    def showAttendSemesterFromDb(self):
        global sql_all, db_conn
        semId = self.ui.comboBox_4.currentIndex() + 1
        self.ui.convert_to_csv_2.setText('Convert to\nCSV')
        try:
            db_conn = pymysql.connect(host='localhost', user='root', passwd='', db='finalproject')
            cursor = db_conn.cursor()

            sql = f"""SELECT s.std_id,s.fullname,f.name,sem.name,a.date,a.time
                    FROM student as s
                    LEFT JOIN attendance as a
                    ON s.std_id = a.std_id
                    LEFT JOIN faculty as f
                    ON s.faculty_id = f.f_id
                    LEFT JOIN semester as sem
                    ON s.semester_id = sem.sem_id
                    WHERE s.semester_id = {semId}
                    ORDER BY a.date;"""
            sql1 = """CREATE TABLE attendance_temp LIKE attendance;"""
            cursor.execute(sql1)
            sql3 = """INSERT INTO attendance_temp SELECT * FROM attendance GROUP BY std_id, date;"""
            cursor.execute(sql3)
            sql2 = """DROP TABLE attendance;"""
            cursor.execute(sql2)
            sql4 = """ALTER TABLE attendance_temp RENAME TO attendance;"""
            cursor.execute(sql4)
            self.ui.convert_to_csv_2.show()
            self.ui.convert_to_csv.hide()

            try:
                cursor.execute(sql)

                sql_all = cursor.fetchall()

            except Exception as e:
                print(e)
        except Exception as err:
            print(err)

        self._sql = [list(x) for x in sql_all]
        # print(self._sql)

        for row in self._sql:
            self.ui.tableWidget.insertRow(0)

        for col in self._sql:
            self.ui.tableWidget.insertColumn(0)

        for rowNr, rowValue in enumerate(self._sql):
            for itemNr, itemValue in enumerate(rowValue):
                self.ui.tableWidget.setItem(rowNr, itemNr, QtWidgets.QTableWidgetItem(str(self._sql[rowNr][itemNr])))
        print('Success')
        db_conn.close()

    # ###############################################
    # take smart attendance button function
    def markAttendance(self):
        global id_
        path = 'ImagesAttendance'
        images = []
        classNames = []
        ids = []
        mylist = os.listdir(path)
        print(mylist)

        def markAttend(name):
            now = datetime.datetime.now()
            date = now.strftime('%Y-%m-%d')
            time = now.strftime('%I:%M %p')
            try:
                db = pymysql.connect(host="localhost", user="root", passwd="", db="finalproject")
                cursor = db.cursor()
                if db.open:
                    sql = f"""
                            INSERT INTO attendance(std_id, date, time) 
                            VALUES ('{id_}', '{date}', '{time}')
                    """
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except Exception as e:
                        db.rollback()
                        print(e)

                    # with open('Attendance.csv', 'r+') as f:
                    #     if name != 'unknown':
                    #         myDataList = f.readline()
                    #         f.writelines(f'\n{name},{ids},{date},{time}')
                else:
                    print(Exception)
            except Exception as e:
                print(e)

        for cl in mylist:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(cl.split('.')[0])
            ids.append(cl.split('.')[1])
        print(classNames)

        print(ids)

        # def voice(text):
        #     engine = tts.init()
        #     engine.setProperty('rate', 200)
        #     engine.setProperty('volume', 1)
        #     voices = engine.getProperty('voices')
        #     engine.setProperty('voice', voices[1].id)
        #     engine.say(text)
        #     engine.runAndWait()
        #     engine.stop()

        def findEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList

        encodeListKnown = findEncodings(images)
        print("Encoding Complete")

        cap = cv2.VideoCapture(0)

        while True:
            success, image = cap.read()
            imageS = cv2.resize(image, (0, 0), None, 0.25, 0.25)
            imageS = cv2.cvtColor(imageS, cv2.COLOR_BGR2RGB)
            text = 'Please press \'Q/q or Esc\' to exit from webcam'
            cv2.putText(image, text, (25, 20), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (0, 0, 0), 1)

            facesCurFrame = face.face_locations(imageS)
            # print(facesCurFrame)
            encodeCurFrame = face.face_encodings(imageS, facesCurFrame)
            # print(encodeCurFrame)
            for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
                matches = face.compare_faces(encodeListKnown, encodeFace, tolerance=0.50)
                faceDis = face.face_distance(encodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)
                # print(matchIndex)
                name = 'unknown'

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    id_ = ids[matchIndex]
                    name_id = name + '-' + id_
                    # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(image, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(image, name_id, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

                    # voice("Attendance taken successfully")
                else:
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cv2.rectangle(image, (x1, y2 - 20), (x2, y2), (0, 0, 255), cv2.FILLED)
                    cv2.putText(image, 'Unknown', (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(image, 'Face not', (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)
                    cv2.putText(image, 'registered in', (10, 115), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)
                    cv2.putText(image, 'Database', (10, 165), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)
                    # voice('Unknown face detected')
                if name != 'unknown':
                    markAttend(name)
                    with open('Attendance.csv', 'r+') as f:
                        time = datetime.datetime.now().strftime('%I:%M %p')
                        date = datetime.datetime.now().strftime('%Y-%m-%d')
                        myDataList = f.readline()
                        f.writelines(f'\n{name},{date},{time}')

            cv2.imshow('Webcam', image)
            k = cv2.waitKey(1)
            if k & 0xFF == ord('q'):
                break
            # break if the sample number is more than given number
            # elif img_counter > 2:
            #     break

            if k % 256 == 27:
                # print("Escape hit, Exiting")
                break
            # elif k % 256 == 32:
            #     img_name = "{}_{}.png".format(name, img_counter)
            #     cv2.imwrite(img_name, image)
            #     print("screenshot taken")
            #     img_counter = img_counter + 1

        # voice("Escape key pressed, Exiting")

        cap.release()
        cv2.destroyAllWindows()

    # ###############################################
    # display chart function
    def showChart(self):
        db = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
        cursor = db.cursor()

        sqll = """SELECT s.fullname, COUNT(a.std_id)
        FROM attendance as a
        LEFT JOIN student as s
        ON a.std_id = s.std_id
        GROUP BY a.std_id;"""
        name = []
        days = []

        try:
            cursor.execute(sqll)
            data = cursor.fetchall()
        except Exception as e:
            print(e)

        std_id_count = [list(x) for x in data]
        # print(std_id_count)

        for l1 in std_id_count:
            name.append(l1[0])
            days.append(l1[1])
        # print(name)
        # print(days)

        ypos = np.arange(len(name))
        # print(ypos)

        plt.barh(ypos, days, align='center', alpha=0.5, label='students', color='r')
        # plt.bar(ypos + 0.2, total, width=0.4, label='total')
        plt.yticks(ypos, name)
        plt.ylabel('Name of students')
        plt.xlabel('No of present days')
        plt.title('Attendance')

        plt.legend()
        plt.show()
        print('Success')
        db.close()

    def chartStudentLine(self):
        db = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
        cursor = db.cursor()

        sqll = """SELECT s.std_id, COUNT(a.std_id)
                FROM attendance as a
                LEFT JOIN student as s
                ON a.std_id = s.std_id
                GROUP BY a.std_id;"""
        ids = []
        days = []

        try:
            cursor.execute(sqll)
            data = cursor.fetchall()
        except Exception as e:
            print(e)

        std_id_count = [list(x) for x in data]
        # print(std_id_count)

        for l1 in std_id_count:
            ids.append(l1[0])
            days.append(l1[1])
        # print(ids)
        # print(days)

        # ypos = np.arange(len(ids))
        # print(ypos)
        plt.plot(ids, days, 'r-o')
        # plt.xticks(ypos, ids)
        plt.ylabel('No of present days')
        plt.xlabel('Students Id')
        plt.title('Attendance')

        # plt.legend()
        plt.show()
        print('Success')
        db.close()

    def chartFacultyBar(self):
        db = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
        cursor = db.cursor()

        sqll = """SELECT f.name, COUNT(a.std_id)
                FROM attendance as a
                LEFT JOIN student as s
                ON a.std_id = s.std_id
                LEFT JOIN faculty as f
                ON s.faculty_id = f.f_id
                LEFT JOIN semester as sem
                ON s.semester_id = sem.sem_id
                GROUP BY f.f_id;"""
        fname = []
        ta = []

        try:
            cursor.execute(sqll)
            data = cursor.fetchall()
        except Exception as e:
            print(e)

        std_id_count = [list(x) for x in data]
        # print(std_id_count)

        for l1 in std_id_count:
            fname.append(l1[0])
            ta.append(l1[1])
        # print(fname)
        # print(ta)

        # ypos = np.arange(len(fname))
        # print(ypos)

        # plt.barh(ypos, ta, align='center', alpha=0.5, label='Faculty')
        plt.bar(fname, ta, width=0.4, label='faculty', color='g')
        # plt.yticks(ypos, fname)
        # plt.ylabel('Faculty')
        # plt.xlabel('Total attendences')
        plt.title('Attendance')

        plt.legend()
        plt.show()
        print('Success')
        db.close()

    def chartFacultyLine(self):
        db = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
        cursor = db.cursor()

        sqll = """SELECT f.name, COUNT(a.std_id)
                        FROM attendance as a
                        LEFT JOIN student as s
                        ON a.std_id = s.std_id
                        LEFT JOIN faculty as f
                        ON s.faculty_id = f.f_id
                        LEFT JOIN semester as sem
                        ON s.semester_id = sem.sem_id
                        GROUP BY f.f_id;"""
        fname = []
        ta = []

        try:
            cursor.execute(sqll)
            data = cursor.fetchall()
        except Exception as e:
            print(e)

        std_id_count = [list(x) for x in data]
        # print(std_id_count)

        for l1 in std_id_count:
            fname.append(l1[0])
            ta.append(l1[1])
        # print(fname)
        # print(ta)

        # ypos = np.arange(len(ids))
        # print(ypos)
        plt.plot(fname, ta, 'b-o')
        # plt.xticks(ypos, ids)
        plt.ylabel('Attendance')
        plt.xlabel('Faculty')
        plt.title('Attendance')

        # plt.legend()
        plt.show()
        print('Success')
        db.close()

    def chartSemesterBar(self):
        db = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
        cursor = db.cursor()

        sqll = """SELECT f.name,sem.name, COUNT(a.std_id)
        FROM attendance as a
        LEFT JOIN student as s
        ON a.std_id = s.std_id
        LEFT JOIN faculty as f
        ON s.faculty_id = f.f_id
        LEFT JOIN semester as sem
        ON s.semester_id = sem.sem_id
        GROUP BY sem.sem_id;"""
        fname = []
        ta = []

        try:
            cursor.execute(sqll)
            data = cursor.fetchall()
        except Exception as e:
            print(e)

        std_id_count = [list(x) for x in data]
        # print(std_id_count)

        for l1 in std_id_count:
            fname.append(l1[0] + '-' + l1[1])
            ta.append(l1[2])
        # print(fname)
        # print(ta)

        # ypos = np.arange(len(fname))
        # print(ypos)

        # plt.barh(ypos, ta, align='center', alpha=0.5, label='Faculty')
        plt.bar(fname, ta, width=0.4, label='faculty', color='b')
        # plt.yticks(ypos, fname)
        # plt.ylabel('Faculty')
        # plt.xlabel('Total attendences')
        plt.title('Attendance')

        plt.legend()
        plt.show()
        print('Success')
        db.close()

    def chartSemesterLine(self):
        db = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
        cursor = db.cursor()

        sqll = """SELECT f.name,sem.name, COUNT(a.std_id)
                FROM attendance as a
                LEFT JOIN student as s
                ON a.std_id = s.std_id
                LEFT JOIN faculty as f
                ON s.faculty_id = f.f_id
                LEFT JOIN semester as sem
                ON s.semester_id = sem.sem_id
                GROUP BY sem.sem_id;"""
        fname = []
        ta = []

        try:
            cursor.execute(sqll)
            data = cursor.fetchall()
        except Exception as e:
            print(e)

        std_id_count = [list(x) for x in data]
        # print(std_id_count)

        for l1 in std_id_count:
            fname.append(l1[0] + '-' + l1[1])
            ta.append(l1[2])
        # print(fname)
        # print(ta)

        # ypos = np.arange(len(fname))
        # print(ypos)

        # plt.barh(ypos, ta, align='center', alpha=0.5, label='Faculty')
        plt.plot(fname, ta, 'g-o')
        # plt.xticks(ypos, ids)
        plt.ylabel('Attendance')
        plt.xlabel('Faculty')
        plt.title('Attendance')

        # plt.legend()
        plt.show()
        print('Success')
        db.close()

    # ###############################################
    # browse file from system function
    def browseFile(self):
        self.filename = QFileDialog.getOpenFileName(filter='(*.csv)')[0]
        self.base_name = os.path.normpath(self.filename)
        # self.Title = os.path.splitext(base_name)[0]
        self.ui.file_name.setText(self.base_name)
        # print('FILE', self.base_name)
        # print('browse file')

    # ###############################################
    # email page validation function
    def emailValidation(self):
        send_to_email = self.ui.email_address.text()  # Who you are sending the message to
        subject = self.ui.subject.text()  # The subject line
        file_location = self.ui.file_name.text()
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if send_to_email != '':
            if re.search(regex, send_to_email):
                if subject != '':
                    if file_location != '':
                        self.sendEmailToUser()
                    else:
                        msg = 'File not Found!'
                        self.showEmailResponse(msg)
                else:
                    msg3 = 'Mandatory(*) field is empty!'
                    self.showEmailResponse(msg3)
            else:
                msg1 = 'Invalid Email!'
                self.showEmailResponse(msg1)
        else:
            msg2 = 'Mandatory(*) field is empty!'
            self.showEmailResponse(msg2)

    # ###############################################
    # send email function
    def sendEmailToUser(self):
        # print('clicked!')
        email = 'rocker6captain9@gmail.com'  # Your email
        password = 'eHjK&v%RnM6]A+/'  # Your email account password
        send_to_email = self.ui.email_address.text()  # Who you are sending the message to
        subject = self.ui.subject.text()  # The subject line
        message = self.ui.textEdit.toPlainText()  # The message in the email
        file_location = self.ui.file_name.text()

        # Create the attachment file (only do it once)
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
        server.starttls()  # Use TLS
        server.login(email, password)  # Login to the email server

        # for send_to_email in send_to_emails:
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        # Attach the message to the MIMEMultipart object
        msg.attach(MIMEText(message, 'plain'))
        # Attach the attachment file
        msg.attach(part)

        text = msg.as_string()  # You now need to convert the MIMEMultipart object to a string to send
        server.sendmail(email, send_to_email, text)  # Send the email
        self.showEmailResponse('Message Sent')
        print('Success')
        server.quit()  # Logout of the email server

    def showEmailResponse(self, msg):
        self.ui.email_res_frame.show()
        self.ui.label_26.setText(msg)

    # ###############################################
    # clear all the field button on email page function
    def clearAllField(self):
        self.ui.email_address.clear()
        self.ui.subject.clear()
        self.ui.textEdit.clear()
        self.ui.file_name.clear()


class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=120):
        fig = Figure(figsize=(width, height), dpi=dpi)
        super(MatplotlibCanvas, self).__init__(fig)
        self.axes = fig.add_subplot(111)
        fig.tight_layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
