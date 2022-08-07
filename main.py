from PyQt5 import QtCore, QtGui, QtWidgets
from signal import signal
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QListWidgetItem, QMessageBox
from PyQt5.QtCore import QTimer, QDateTime
import datetime
import webbrowser
from threading import *
import getpass
import time
import psutil
import os
from PyQt5.QtWidgets import QMainWindow
from views.createroom import CreateRoomWindow

class FireChatApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(849, 842)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
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
        self.secondhorizontallayout.addWidget(self.joinbutton)
        self.leavebutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.leavebutton.setObjectName("leavebutton")
        self.secondhorizontallayout.addWidget(self.leavebutton)
        self.exitbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exitbutton.setObjectName("exitbutton")
        self.secondhorizontallayout.addWidget(self.exitbutton)
        self.appverticallayout.addLayout(self.secondhorizontallayout)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
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
        self.entermessageinput.setObjectName("entermessageinput")
        self.footerhorizontallayout.addWidget(self.entermessageinput)
        self.sendmessagebutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sendmessagebutton.setObjectName("sendmessagebutton")
        self.footerhorizontallayout.addWidget(self.sendmessagebutton)
        self.appverticallayout.addLayout(self.footerhorizontallayout)
        self.retranslateUi(MainWindow)
        self.show()
        self.updateUsername()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.appnamelabel.setText(_translate("MainWindow", "FireChat🔥"))
        self.createroombutton.setText(_translate("MainWindow", "Create Room"))
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


    def open_github(self):
        webbrowser.open("https://github.com/Santhoshlm10/FireChat-Python")

    def updateUsername(self):
        sys_name = getpass.getuser()
        self.usernameinput.setText(sys_name)

    def closeEvent(self, event):
            close = QtWidgets.QMessageBox.question(self,
                                         "QUIT",
                                         "Are you sure want to exit?",
                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if close == QtWidgets.QMessageBox.Yes:
                event.accept()
                # MainWindow.close()
                # p = psutil.Process(os.getpid())
                # p.terminate()
            else:
                event.ignore()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FireChatApplication()
    sys.exit(app.exec_())
