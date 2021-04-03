from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QListWidgetItem, QMessageBox
from PyQt5.QtCore import QTimer, QDateTime
import datetime
import webbrowser
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 572)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(150, 10, 61, 41))
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 251, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 60, 131, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 60, 91, 27))
        self.pushButton.clicked.connect(self.startChat)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 60, 71, 27))
        self.pushButton_2.clicked.connect(self.leave_chat)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(588, 60, 71, 27))
        self.pushButton_3.clicked.connect(self.close_app)
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QTextEdit(self.centralwidget)
        self.listWidget.setReadOnly(True)
        self.listWidget.setGeometry(QtCore.QRect(10, 101, 641, 411))
        self.listWidget.setObjectName("textEdit")

        # self.listWidget.setAutoScroll(True)
        # list_widget.setAutoScroll(True)
        self.timer = QTimer()
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 520, 511, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.returnPressed.connect(self.send_message)
        self.lineEdit_3.setEnabled(False)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(528, 520, 121, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.send_message)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(590, 10, 71, 32))
        self.pushButton_5.clicked.connect(self.open_github)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.unique_id = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "FireChat - a private chat application using google firebase"))
        self.label.setText(_translate("MainWindow", "FireChat"))
        self.label_1.setText(_translate("MainWindow", "🔥"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "firebase.io URL"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Your name"))
        self.pushButton.setText(_translate("MainWindow", "Join"))
        self.pushButton_2.setText(_translate("MainWindow", "Leave"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Type your message and hit enter"))
        self.pushButton_4.setText(_translate("MainWindow", "Send Message"))
        self.pushButton_5.setText(_translate("MainWindow", 'Github♥'))

    def send_message(self):
        from firebase import firebase
        firebase_link = self.lineEdit.text()
        message = self.lineEdit_3.text()
        if not message:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Message cannot be Empty")
            msgBox.setWindowTitle("Empty field found")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
            return

        firebase = firebase.FirebaseApplication(firebase_link, None)
        data = {'name': self.lineEdit_2.text(),
                'message': message,
                'time': datetime.datetime.now()
                }
        result = firebase.post('/FireChat/', data)
        self.lineEdit_3.clear()
        return

    def close_app(self):
        MainWindow.close()

    def open_github(self):
        webbrowser.open("https://github.com/Santhoshlm10/FireChat-Python/edit/main/FireChat")

    def leave_chat(self):
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.lineEdit_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.listWidget.clear()
        self.pushButton_2.setEnabled(False)
        self.lineEdit_3.clear()
        self.label_1.setStyleSheet('color: #000000')
        self.timer.stop()
        self.unique_id = []

    def startChat(self):
        try:
            firebase_link = self.lineEdit.text()
            if not (firebase_link):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("Firebase URL cannot be Empty")
                msgBox.setWindowTitle("Empty field found")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
                return
            # get the name of the application user
            username = self.lineEdit_2.text()
            if not (username):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("Username cannot be Empty")
                msgBox.setWindowTitle("Empty field found")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
                return
            self.lineEdit.setEnabled(False)
            self.lineEdit_2.setEnabled(False)
            self.pushButton.setEnabled(False)
            self.lineEdit_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.label_1.setStyleSheet('color: #ffae42')

            self.timer.setInterval(500)
            self.timer.timeout.connect(self.getPeriodic)
            self.timer.start()

        except Exception as e:
            err = str(e)
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText(err + "\n" + "Try,\n1.Checking firebase.io URL is active\n2.Entered inputs are valid")
            msgBox.setWindowTitle("Error while connecting")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.lineEdit_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.listWidget.clear()
            self.pushButton_2.setEnabled(False)
            self.label_1.setStyleSheet('color: #000000')
            return

    def getPeriodic(self):
        try:
            from firebase import firebase
            firebase_link = self.lineEdit.text()
            firebase = firebase.FirebaseApplication(firebase_link, None)
            try:
                result = firebase.get('/FireChat/', '')
                result_length = len(result)
            except Exception as e:
                data = {'name': 'FireChat Bot',
                        'message': 'Hey, Welcome to firechat',
                        'time': datetime.datetime.now()
                        }
                result1 = firebase.post('/FireChat/', data)
                return
            id_list = list(result)
            for i in range(0, result_length):
                if id_list[i] not in self.unique_id:
                    time_stamp = str(result[id_list[i]]['time']).replace("T", " ")
                    final_time = time_stamp[:19]
                    final_data = final_time + " - " + result[id_list[i]]['name'] + " > " + result[id_list[i]]['message']
                    self.listWidget.append(final_data)
                    self.unique_id.append(id_list[i])
        except Exception as err:
            self.timer.stop()
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Sorry something went wrong while connecting"+"\n"+"Please make sure firebase.io URL is valid and active")
            msgBox.setWindowTitle("Error while connecting")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.lineEdit_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.listWidget.clear()
            self.pushButton_2.setEnabled(False)
            self.label_1.setStyleSheet('color: #000000')
            return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
