from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QListWidgetItem, QMessageBox
from PyQt5.QtCore import QTimer, QDateTime, QThreadPool
import datetime
import webbrowser
import getpass
import time
import psutil
import os
from PyQt5.QtWidgets import QMainWindow
from views.createroom import CreateRoomWindow
from utils.managedatabase import getRoomNameList, getFirebaseUrl
from threading import *


class FireChatApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        # constants
        self.FIREBASE_URL = ""
        self.THREAD_STATUS = 0

        self.setFixedSize(849, 842)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 821, 810))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.appverticallayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.appverticallayout.setContentsMargins(0, 0, 0, 0)
        self.appverticallayout.setObjectName("appverticallayout")
        self.headerhorizontallayout = QtWidgets.QHBoxLayout()
        self.headerhorizontallayout.setObjectName("headerhorizontallayout")
        self.appnamelabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.appnamelabel.setFont(font)
        self.appnamelabel.setObjectName("appnamelabel")
        self.headerhorizontallayout.addWidget(self.appnamelabel)
        self.createroombutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createroombutton.sizePolicy().hasHeightForWidth())
        self.createroombutton.setSizePolicy(sizePolicy)
        self.createroombutton.setObjectName("createroombutton")
        self.createroombutton.clicked.connect(self.onCreateRoomClick)
        self.headerhorizontallayout.addWidget(self.createroombutton)

        self.refreshbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshbutton.sizePolicy().hasHeightForWidth())
        self.refreshbutton.clicked.connect(self.onRefreshClick)
        self.refreshbutton.setSizePolicy(sizePolicy)
        self.refreshbutton.setText("Refresh")
        self.refreshbutton.setObjectName("refreshbutton")
        self.headerhorizontallayout.addWidget(self.refreshbutton)

        self.contributebutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contributebutton.sizePolicy().hasHeightForWidth())
        self.contributebutton.clicked.connect(self.open_github)
        self.contributebutton.setSizePolicy(sizePolicy)
        self.contributebutton.setObjectName("contributebutton")
        self.headerhorizontallayout.addWidget(self.contributebutton)
        self.appverticallayout.addLayout(self.headerhorizontallayout)
        self.secondhorizontallayout = QtWidgets.QHBoxLayout()
        self.secondhorizontallayout.setObjectName("secondhorizontallayout")
        self.chooseyourroontext = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.chooseyourroontext.setObjectName("chooseyourroontext")
        self.secondhorizontallayout.addWidget(self.chooseyourroontext)
        self.chooseroomdropdown = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.chooseroomdropdown.activated.connect(self.onRoomNameChange)
        self.chooseroomdropdown.setObjectName("chooseroomdropdown")
        self.secondhorizontallayout.addWidget(self.chooseroomdropdown)
        self.usernameinput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameinput.sizePolicy().hasHeightForWidth())
        self.usernameinput.setSizePolicy(sizePolicy)
        self.usernameinput.setMinimumSize(QtCore.QSize(150, 0))
        self.usernameinput.setObjectName("usernameinput")
        self.secondhorizontallayout.addWidget(self.usernameinput)
        self.joinbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.joinbutton.setObjectName("joinbutton")
        self.joinbutton.clicked.connect(self.onJoinButtonClick)
        self.secondhorizontallayout.addWidget(self.joinbutton)
        self.leavebutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.leavebutton.setEnabled(False)
        self.leavebutton.setObjectName("leavebutton")
        self.leavebutton.clicked.connect(self.leave_chat)
        self.secondhorizontallayout.addWidget(self.leavebutton)
        self.exitbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exitbutton.setObjectName("exitbutton")
        self.exitbutton.clicked.connect(self.close_app)
        self.secondhorizontallayout.addWidget(self.exitbutton)
        self.appverticallayout.addLayout(self.secondhorizontallayout)
        self.listWidget = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.listWidget.setReadOnly(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.listWidget.verticalScrollBar().minimum()
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 650))
        self.listWidget.setObjectName("listWidget")
        self.appverticallayout.addWidget(self.listWidget)
        self.footerhorizontallayout = QtWidgets.QHBoxLayout()
        self.footerhorizontallayout.setObjectName("footerhorizontallayout")
        self.entermessageinput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.entermessageinput.returnPressed.connect(self.send_message)
        self.entermessageinput.setObjectName("entermessageinput")
        self.footerhorizontallayout.addWidget(self.entermessageinput)
        self.sendmessagebutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sendmessagebutton.setObjectName("sendmessagebutton")
        self.sendmessagebutton.clicked.connect(self.send_message)
        self.footerhorizontallayout.addWidget(self.sendmessagebutton)
        self.appverticallayout.addLayout(self.footerhorizontallayout)
        self.retranslateUi(MainWindow)
        self.show()
        self.updateUsername()
        self.updateroomnamelist()
        self.threadpool = QThreadPool()
        self.unique_id = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Welcome to Firechat - send private messages using google firebase"))
        self.appnamelabel.setText(_translate("MainWindow", "FireChat🔥"))
        self.createroombutton.setText(_translate("MainWindow", "Manage Rooms"))
        self.contributebutton.setText(_translate("MainWindow", "Contribute"))
        self.chooseyourroontext.setText(_translate("MainWindow", "Choose your room:"))
        self.usernameinput.setPlaceholderText(_translate("MainWindow", "Username"))
        self.joinbutton.setText(_translate("MainWindow", "Join"))
        self.leavebutton.setText(_translate("MainWindow", "Leave"))
        self.exitbutton.setText(_translate("MainWindow", "Exit"))
        self.entermessageinput.setPlaceholderText(_translate("MainWindow", "Enter your message and hit enter"))
        self.sendmessagebutton.setText(_translate("MainWindow", "Send Messsage"))


    def onCreateRoomClick(self):
        self.creatRoom = CreateRoomWindow()

    def leave_chat(self):
        self.THREAD_STATUS = 0
        self.chooseroomdropdown.setEnabled(True)
        self.usernameinput.setEnabled(True)
        self.joinbutton.setEnabled(True)
        self.refreshbutton.setEnabled(True)
        self.leavebutton.setEnabled(False)
        self.createroombutton.setEnabled(False)
        self.listWidget.clear()
        self.unique_id = []

    def open_github(self):
        webbrowser.open("https://github.com/Santhoshlm10/FireChat-Python")

    def updateUsername(self):
        sys_name = getpass.getuser()
        self.usernameinput.setText(sys_name)

    def updateroomnamelist(self):
        a = getRoomNameList()[2]
        if len(a) != 0:
            for i in a:
                self.chooseroomdropdown.addItem(i[0])
        b = getFirebaseUrl(self.chooseroomdropdown.currentText())
        self.FIREBASE_URL = b[2][0][0]



    def onRefreshClick(self):
        self.chooseroomdropdown.clear()
        self.updateroomnamelist()

    def close_app(self):
        self.close()


    def onJoinButtonClick(self):
        try:
            username = self.usernameinput.text()
            if not (username):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("Username cannot be Empty")
                msgBox.setWindowTitle("Empty field found")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
                return
            self.chooseroomdropdown.setEnabled(False)
            self.usernameinput.setEnabled(False)
            self.joinbutton.setEnabled(False)
            self.refreshbutton.setEnabled(False)
            self.leavebutton.setEnabled(True)
            self.exitbutton.setEnabled(True)
            self.createroombutton.setEnabled(False)
            self.THREAD_STATUS = 1
            self.messageUpdateThread()

        except Exception as e:
            err = str(e)
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText(err + "\n" + "Try,\n1.Checking firebase.io URL is active\n2.Entered inputs are valid")
            msgBox.setWindowTitle("Error while connecting")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
            return

    def execute_this_fn(self, progress_callback):
        while True:
            time.sleep(0.5)
            progress_callback.emit(1)

    def onRoomNameChange(self):
        b = getFirebaseUrl(self.chooseroomdropdown.currentText())
        self.FIREBASE_URL = b[2][0][0]


    # def getPeriodic(self):
    #     if self.THREAD_STATUS == 1:
    #         try:
    #             from firebase import firebase
    #             firebase_link = self.FIREBASE_URL
    #             firebase = firebase.FirebaseApplication(firebase_link, None)
    #             try:
    #                 result = firebase.get('/FireChat/', '')
    #                 result_length = len(result)
    #             except Exception as e:
    #                 data = {'name': 'FireChat Bot',
    #                                 'message': 'Hey, Welcome to firechat',
    #                                 'time': datetime.datetime.now().strftime("%D %I:%M:%S %p")
    #                                 }
    #                 result1 = firebase.post('/FireChat/', data)
    #                 return
    #             id_list = list(result)
    #             for i in range(0, result_length):
    #                 if id_list[i] not in self.unique_id:
    #                     time_stamp = str(result[id_list[i]]['time']).replace("T", " ")
    #                     final_time = time_stamp[:20]
    #                     final_data = final_time + " - " + result[id_list[i]]['name'] + " > " + result[id_list[i]]['message']
    #                     self.listWidget.append(final_data)
    #                     self.unique_id.append(id_list[i])
    #         except Exception as err:
    #             msgBox = QMessageBox()
    #             msgBox.setIcon(QMessageBox.Critical)
    #             msgBox.setText("Unable to connect firebase")
    #             msgBox.setWindowTitle("Error while connecting")
    #             msgBox.setStandardButtons(QMessageBox.Ok)
    #             msgBox.exec()
    #             self.chooseroomdropdown.setEnabled(True)
    #             self.usernameinput.setEnabled(True)
    #             self.joinbutton.setEnabled(True)
    #             self.refreshbutton.setEnabled(True)
    #             self.leavebutton.setEnabled(False)
    #             self.exitbutton.setEnabled(False)
    #             self.createroombutton.setEnabled(False)
    #             self.THREAD_STATUS = 0
    #             return





    def getPeriodic(self):
        while True:
            if self.THREAD_STATUS == 1:
                try:
                    from firebase import firebase
                    firebase_link = self.FIREBASE_URL
                    firebase = firebase.FirebaseApplication(firebase_link, None)
                    try:
                        result = firebase.get('/FireChat/', '')
                        result_length = len(result)
                    except Exception as e:
                        data = {'name': 'FireChat Bot',
                                    'message': 'Hey, Welcome to firechat',
                                    'time': datetime.datetime.now().strftime("%D %I:%M:%S %p")
                                    }
                        result1 = firebase.post('/FireChat/', data)
                        return
                    id_list = list(result)
                    for i in range(0, result_length):
                        if id_list[i] not in self.unique_id:
                            time_stamp = str(result[id_list[i]]['time']).replace("T", " ")
                            final_time = time_stamp[:20]
                            final_data = final_time + " - " + result[id_list[i]]['name'] + " > " + result[id_list[i]]['message']
                            self.listWidget.append(final_data)
                            self.unique_id.append(id_list[i])
                except Exception as err:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setText("Unable to connect firebase")
                    msgBox.setWindowTitle("Error while connecting")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                    self.chooseroomdropdown.setEnabled(True)
                    self.usernameinput.setEnabled(True)
                    self.joinbutton.setEnabled(True)
                    self.refreshbutton.setEnabled(True)
                    self.leavebutton.setEnabled(False)
                    self.exitbutton.setEnabled(False)
                    self.createroombutton.setEnabled(False)
                    self.THREAD_STATUS = 0
                    return
                time.sleep(1)
            else:
                break

    def send_message(self):
        from firebase import firebase
        firebase_link = self.FIREBASE_URL
        message = self.entermessageinput.text()
        if not message:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Message cannot be Empty")
            msgBox.setWindowTitle("Empty field found")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
            return

        firebase = firebase.FirebaseApplication(firebase_link, None)
        data = {'name': self.usernameinput.text(),
                'message': message,
                'time': datetime.datetime.now().strftime("%D %I:%M:%S %p")
                }
        result = firebase.post('/FireChat/', data)
        self.entermessageinput.clear()
        return

    def messageUpdateThread(self):
        # self.worker = MessageWorker(self.execute_this_fn)
        # self.worker.signals.progress.connect(self.getPeriodic)
        # self.threadpool.start(self.worker)
        self.messageThread = Thread(target=self.getPeriodic)
        self.messageThread.start()

    def closeEvent(self, event):
            close = QtWidgets.QMessageBox.question(self,
                                         "QUIT",
                                         "Are you sure want to exit?",
                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if close == QtWidgets.QMessageBox.Yes:
                event.accept()
                self.close()
                p = psutil.Process(os.getpid())
                p.terminate()
            else:
                event.ignore()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FireChatApplication()
    sys.exit(app.exec_())
