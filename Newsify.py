# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FindNews.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1235, 665)
        MainWindow.setMinimumSize(QtCore.QSize(1235, 665))
        MainWindow.setMaximumSize(QtCore.QSize(1235, 877))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 0, 1209, 641))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.raion = QtWidgets.QLineEdit(self.widget)
        self.raion.setMinimumSize(QtCore.QSize(1119, 0))
        self.raion.setMaximumSize(QtCore.QSize(1119, 16777215))
        self.raion.setObjectName("raion")
        self.raion.setStyleSheet('''background-color: rgb(250, 250, 250);
        		    border-radius: 10px;''')
        self.horizontalLayout.addWidget(self.raion)
        self.find = QtWidgets.QPushButton(self.widget)
        self.find.setMinimumSize(QtCore.QSize(80, 25))
        self.find.setMaximumSize(QtCore.QSize(80, 25))
        self.find.setObjectName("find")
        self.find.setStyleSheet('''background-color: rgb(200, 200, 200);
        		    border-radius: 10px;''')
        self.horizontalLayout.addWidget(self.find)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.filter = QtWidgets.QComboBox(self.widget)
        self.filter.setMinimumSize(QtCore.QSize(1207, 0))
        self.filter.setMaximumSize(QtCore.QSize(1207, 16777215))
        self.filter.setObjectName("filter")
        self.filter.setStyleSheet('''background-color: rgb(200, 200, 200);
                		    border-radius: 10px;''')
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.verticalLayout.addWidget(self.filter)
        self.errors = QtWidgets.QLabel(self.widget)
        self.errors.setMinimumSize(QtCore.QSize(1207, 0))
        self.errors.setMaximumSize(QtCore.QSize(1207, 16777215))
        self.errors.setObjectName("errors")
        self.verticalLayout.addWidget(self.errors)
        self.brs = QtWebEngineWidgets.QWebEngineView(self.splitter)
        self.brs.setMinimumSize(QtCore.QSize(1209, 581))
        self.brs.setMaximumSize(QtCore.QSize(1209, 16777215))
        self.brs.setProperty("url", QtCore.QUrl("about:blank"))
        self.brs.setObjectName("brs")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Newsify"))
        self.find.setText(_translate("MainWindow", "Поиск"))
        self.filter.setItemText(0, _translate("MainWindow", "Все"))
        self.filter.setItemText(1, _translate("MainWindow", "Культура"))
        self.filter.setItemText(2, _translate("MainWindow", "Наука"))
        self.filter.setItemText(3, _translate("MainWindow", "Технологии"))
        self.filter.setItemText(4, _translate("MainWindow", "Политика"))
        self.filter.setItemText(5, _translate("MainWindow", "Правительство"))
        self.filter.setItemText(6, _translate("MainWindow", "Проишествие"))
        self.filter.setItemText(7, _translate("MainWindow", "Религия"))
        self.filter.setItemText(8, _translate("MainWindow", "Спорт"))
        self.filter.setItemText(9, _translate("MainWindow", "Экономика"))
        self.filter.setItemText(10, _translate("MainWindow", "Музыка"))
        self.filter.setItemText(11, _translate("MainWindow", "Игры"))
        self.filter.setItemText(12, _translate("MainWindow", "Веселье"))
        self.filter.setItemText(13, _translate("MainWindow", "История"))
        self.filter.setItemText(14, _translate("MainWindow", "Природа"))
from PyQt5 import QtWebEngineWidgets
