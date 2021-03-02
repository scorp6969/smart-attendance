import pymysql
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import sys

from ui_loginScreen import Ui_LoginWindow

from CopyMain import MainWindow


# # YOUR APPLICATION
# class MyHomepage(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.ui = MainWindow()
#         # self.ui.setupUi(self)
#         self.ui.show()

# login Window
class LogInWin(QMainWindow):
    def __init__(self):
        super(LogInWin, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        # imagepath
        self.image1path = 'icons/profile-user.png'
        self.image2path = 'icons/password (1).png'
        self.image3path = 'icons/enter.png'
        self.image4path = 'icons2/login.png'
        self.image5path = 'icons/user (1).png'
        self.image6path = 'icons/close.png'
        # self.image7path = 'icons/hide.png'

        self.image1 = QtGui.QImage(self.image1path)
        self.image2 = QtGui.QImage(self.image2path)
        self.image3 = QtGui.QImage(self.image3path)
        self.image4 = QtGui.QImage(self.image4path)
        self.image5 = QtGui.QImage(self.image5path)
        self.image6 = QtGui.QImage(self.image6path)
        # self.image7 = QtGui.QImage(self.image7path)

        self.ui.label.setPixmap(QtGui.QPixmap.fromImage(self.image1))
        self.ui.label_2.setPixmap(QtGui.QPixmap.fromImage(self.image2))
        self.ui.pushButton_3.setIcon(QtGui.QPixmap.fromImage(self.image3))
        self.ui.label_4.setPixmap(QtGui.QPixmap.fromImage(self.image4))
        self.ui.label_4.setScaledContents(True)
        self.ui.label_5.setPixmap(QtGui.QPixmap.fromImage(self.image5))
        self.ui.label_5.setScaledContents(True)
        self.ui.label_5.setGeometry(140, 40, 80, 70)
        self.ui.close_btn.setIcon(QtGui.QPixmap.fromImage(self.image6))
        # self.ui.checkBox.setIcon(QtGui.QPixmap.fromImage(self.image7))

        self.c1 = self.ui.pass_show_hide
        self.c1.stateChanged.connect(lambda: self.checkboxClicked(self.c1))

        # message frame hidden
        self.ui.login_res_frame.hide()
        self.ui.login_res_ok_btn.clicked.connect(lambda: self.loginResOkBtn())

        # login button clicked
        self.ui.pushButton_3.clicked.connect(lambda: self.validateLogin())
        self.ui.login_button.clicked.connect(lambda: self.validateLogin())

    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()

    def checkboxClicked(self, c):
        if c.isChecked():
            self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def loginResOkBtn(self):
        original = 'background-color:#424549; border-radius: 30px;padding:10px;border:2px solid #7289da;color: rgb(' \
                   '255, 255, 255); '
        self.ui.login_res_frame.hide()
        self.ui.lineEdit.setStyleSheet(original)
        self.ui.lineEdit_2.setStyleSheet(original)

    def showLoginResponse(self, responseMsg):
        self.ui.login_res_frame.show()
        self.ui.login_res_msg.setText(responseMsg)

    def validateLogin(self):
        successStyle = 'border: 3px solid rgb(0, 255, 255);border-radius:25px;'
        errorStyle = 'border: 3px solid rgb(255, 0, 0);border-radius:25px;'
        global db
        uname = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        # username empty
        if not self.ui.lineEdit.text():
            usernameResponse = 'Username Field Empty!'
            self.ui.lineEdit.setStyleSheet(errorStyle)
        else:
            usernameResponse = ''

        # password empty
        if not self.ui.lineEdit_2.text():
            passResponse = 'Password Field Empty!'
            self.ui.lineEdit_2.setStyleSheet(errorStyle)
        else:
            passResponse = ''

        # anyone or both of the field empty
        if usernameResponse != '' or passResponse != '':
            loginResponse = usernameResponse + '\n' + passResponse
            self.showLoginResponse(loginResponse)
        else:
            try:
                db = pymysql.connect(host='localhost', user='root', passwd='', database='finalproject')
                cursor = db.cursor()
                # msg = "Connected to database!"
                # print(msg)
                pass_ = f"""SELECT pass FROM admin WHERE name = '{uname}'"""
                admin_uname_ = """SELECT name FROM admin"""
                try:
                    cursor.execute(admin_uname_)
                    uname_ = cursor.fetchall()
                    # print(uname_)
                    uname_list = list(sum(uname_, ()))
                    # print(uname_list)

                    cursor.execute(pass_)
                    passWd_ = cursor.fetchone()
                    # print(passWd_[0])
                    # username not in database
                    if uname not in uname_list:
                        uname_Res = 'Username doesnot exists!'
                        self.ui.login_res_frame.show()
                        self.ui.login_res_msg.setText(uname_Res)
                        self.ui.lineEdit.setStyleSheet(errorStyle)
                        # self.ui.login_res_frame.setStyleSheet(errorStyle)
                    # password not matching
                    elif password != passWd_[0]:
                        uname_Res = 'Incorrect Password!'
                        self.ui.login_res_frame.show()
                        self.ui.login_res_msg.setText(uname_Res)
                        self.ui.lineEdit_2.setStyleSheet(errorStyle)
                        # self.ui.login_res_frame.setStyleSheet(errorStyle)
                    # login successful
                    else:
                        uname_Res = 'Login SuccessFull!'
                        self.ui.login_res_frame.show()
                        self.ui.login_res_msg.setText(uname_Res)
                        self.ui.lineEdit.setStyleSheet(successStyle)
                        self.ui.lineEdit_2.setStyleSheet(successStyle)
                        self.ui.login_res_frame.setStyleSheet(successStyle)
                        self.adminUsername(uname)
                        # self._new_window_ = MainWindow()
                        self.close()
                        # self.ui.login_button.setEnabled(False)
                        # self.ui.pushButton_3.setEnabled(False)
                except Exception as e:
                    self.showLoginResponse(str(e))
                    self.ui.login_res_frame.setStyleSheet(errorStyle)
            except Exception as e:
                self.showLoginResponse(str(e))
                self.ui.login_res_frame.setStyleSheet(errorStyle)

    def adminUsername(self, username):
        self._new_window_ = MainWindow()
        self._new_window_.getAdminUsername(username)

    # def GoTOMainApp(self):
    #     self.validateLogin()
    #     self._new_window_ = MainWindow()
    #     self._new_window_.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LogInWin()
    win.show()
    sys.exit(app.exec_())
