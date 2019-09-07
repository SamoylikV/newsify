# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FindNews.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1235, 877)
        MainWindow.setMinimumSize(QtCore.QSize(1235, 877))
        MainWindow.setMaximumSize(QtCore.QSize(1235, 877))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(12, 12, 1211, 841))
        self.splitter.setMinimumSize(QtCore.QSize(1211, 841))
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.raion = QtWidgets.QLineEdit(self.widget)
        self.raion.setMinimumSize(QtCore.QSize(401, 25))
        self.raion.setObjectName("raion")
        self.horizontalLayout.addWidget(self.raion)
        self.raion.setStyleSheet('''background-color: rgb(250, 250, 250);
            border-radius: 10px;''')
        self.find = QtWidgets.QPushButton(self.widget)
        self.find.setMinimumSize(QtCore.QSize(80, 25))
        self.find.setMaximumSize(QtCore.QSize(80, 25))
        self.find.setObjectName("find")
        self.find.setStyleSheet('''background-color: rgb(200, 200, 200);
            border-radius: 10px;''')
        self.horizontalLayout.addWidget(self.find)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.errors = QtWidgets.QLabel(self.widget)
        self.errors.setObjectName("errors")
        self.verticalLayout.addWidget(self.errors)
        self.list = QtWidgets.QListWidget(self.widget)
        self.list.setObjectName("list")
        self.verticalLayout.addWidget(self.list)
        self.brs = QtWebEngineWidgets.QWebEngineView(self.splitter)
        self.brs.setMinimumSize(QtCore.QSize(671, 841))
        self.brs.setUrl(QtCore.QUrl("about:blank"))
        self.brs.setObjectName("brs")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FindNews"))
        self.find.setText(_translate("MainWindow", "Поиск"))
from PyQt5 import QtWebEngineWidgets
