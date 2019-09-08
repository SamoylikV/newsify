# -*- coding: utf-8 -*-
# vasya.samoylik@gmail.com
# Sverdlovo20
import json
import sys

import requests
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

from Newsify import Ui_MainWindow  # импорт нашего сгенерированного файла


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.my_web = self.ui.brs
        self.ui.errors.setStyleSheet("color: rgb(255, 0, 0);")
        self.ui.centralwidget.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.raion.setReadOnly(True)
        self.ui.raion.setStyleSheet('''border-radius: 8px;background-color: rgb(200,200,200);''')
        self.ui.list.setStyleSheet('''border-radius: 10px;background-color: rgb(200,200,200); color:rgb(26,26,26);''')
        self.ui.find.setStyleSheet('''border-radius: 8px;background-color: rgb(200,200,200);''')
        self.ui.filter.setStyleSheet('''border-radius: 8px;background-color: rgb(240,240,240);''')
        # self.ui.filter.setStyleSheet("QComboBox{border-radius: 8px;background-color: rgb(255,255,255); color: rgb(255,255,255);}QComboBox QAbstractItemView{border: 8px;color:rgb(255,255,255);background-color: rgb(255,255,255);}")
        self.ui.find.setEnabled(False)
        self.ui.find.clicked.connect(self.find)
        self.combo = self.ui.filter
        self.combo.activated[str].connect(self.filters)
        self.acs = ''
        self.ui.list.itemDoubleClicked.connect(self.listing)
        self.kat = ''
        self.fnd = ''
        self.link = ['','','','','','','','','','','','','','']
        self.text_x = ['','','','','','','','','','','','','','']
        self.my_web.load(QUrl(
            "https://oauth.vk.com/authorize?client_id=7080257&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.101&scope=photos,audio,video,pages,wall,docs,groups,offline&revoke=1&response_type=token"))
        self.hash = ''
        self.tmp = ''
        self.town = ''
        self.l =''
        self.ui.brs.urlChanged.connect(self.token)

    def token(self):
        tokken = self.my_web.url()
        tokken = str(tokken)
        if tokken == "PyQt5.QtCore.QUrl('about:blank')":
            print(tokken)
        else:
            if tokken != "PyQt5.QtCore.QUrl('')":
                inf = 'https://api.vk.com/method/account.getProfileInfo?access_token=/?i=1' + str(self.acs) + '&v=5.101'
                if tokken != inf:
                    if tokken != self.fnd:
                        if tokken != "PyQt5.QtCore.QUrl('http://www.fort-dev.ml/newsify/wait.php')":
                            print(self.fnd)
                            if self.fnd == '':
                                print(tokken)
                                res_tmp = tokken.split('#')[-1]
                                self.tmp = res_tmp
                                res_tmp1 = res_tmp.split('&', 1)[0]
                                if res_tmp1 == "PyQt5.QtCore.QUrl('https://m.vk.com/login?act=authcheck":
                                    self.hash = self.tmp.split('=')[-1]
                                    self.hash = self.hash.split("'")[0]
                                    self.hash('hash=', self.hash)
                                    print(self.hash)
                                print(self.tmp)
                                if res_tmp1 != "PyQt5.QtCore.QUrl('https://m.vk.com/login?act=authcheck":
                                    if res_tmp1 != "PyQt5.QtCore.QUrl('" + self.l + "')":
                                        if res_tmp1 != "PyQt5.QtCore.QUrl('http://www.fort-dev.ml/newsify/wait.php?i=1')":
                                            if res_tmp1 != "PyQt5.QtCore.QUrl('http://www.fort-dev.ml/newsify/wait.php?i=2')":
                                                if res_tmp1 != "PyQt5.QtCore.QUrl('https://oauth.vk.com/authorize?client_id=7080257":
                                                    res_tmp1 = self.tmp.split('&', 1)[0]
                                                    res_tmp = res_tmp1.split('=')[-1]
                                                    self.acs = res_tmp

                                                    self.ui.find.setEnabled(True)
                                                    self.ui.raion.setReadOnly(False)
                                                    print('self.acs=', self.acs)
                                                    if self.hash == '':
                                                        self.l = 'http://www.fort-dev.ml/newsify/wait2.php'
                                                        self.my_web.load(QUrl(self.l))
                                                    else:
                                                        self.l = 'http://www.fort-dev.ml/newsify/wait.php&hash=' + self.hash
                                                        self.my_web.load(QUrl(self.l))

    def filters(self):
        print(self.combo.currentText())
        if self.combo.currentText() != "Все":
            self.kat = self.combo.currentText()
        else:
            self.kat = ''

    def listing(self):
        self.my_web.load(QUrl(self.link[self.ui.list.currentRow()]))
    def find(self):
        self.ui.list.clear()
        inf = 'https://api.vk.com/method/account.getProfileInfo?access_token=' + str(self.acs) + '&v=5.101'
        inf = requests.get(inf)
        resp = inf.text
        dict = json.loads(resp)
        print(dict)
        dict = dict.get('response')
        print(dict)
        dict = dict.get('home_town')
        print(dict)
        self.town = str(dict)
        print(self.town)

        Tokkens = self.acs

        if self.town == '':
            self.town = self.ui.raion.text()
            if self.town == '':
                self.ui.errors.setText("Введите название населенного пункта")

            self.ui.raion.setReadOnly(False)
            self.town = self.ui.raion.text()
            if self.town != '':
                self.ui.errors.setText("")
                self.ui.raion.setText(self.town)
                fn = 'https://api.vk.com/method/newsfeed.search?q=' + self.town + ' ' + self.kat + ' новости&count=14&access_token=' + Tokkens + '&v=5.101'
                req = requests.get(fn)
                self.fnd = fn
                print(fn)
                resp = req.text
                dict = json.loads(resp)
                dict = dict.get('response')
                dict = dict.get('items')
                i = 0
                while i < 14:
                    id_x = dict[i].get('id')
                    owner_id = dict[i].get('owner_id')
                    self.text_x[i] = str(dict[i].get('text'))[0:100] + '...'
                    if owner_id == abs(owner_id):
                        lnk = 'https://vk.com/id' + str(owner_id) + '?w=wall' + str(owner_id) + '_' + str(id_x)
                    else:
                        lnk = 'https://vk.com/public' + str(abs(owner_id)) + '?w=wall' + str(owner_id) + '_' + str(id_x)
                    self.link[i] = lnk
                    i = i + 1
                    print(lnk)


        else:
            self.ui.errors.setText("")
            self.ui.raion.setText(self.town)
            fn = 'https://api.vk.com/method/newsfeed.search?q=' + self.town +' '+ self.kat + ' новости&count=100&access_token=' + Tokkens + '&v=5.101'
            req = requests.get(fn)
            self.fnd = fn
            resp = req.text
            print(fn)
            dict = json.loads(resp)
            dict = dict.get('response')
            dict = dict.get('items')
            i = 0
            while i < 14:
                id_x = dict[i].get('id')
                owner_id = dict[i].get('owner_id')
                self.text_x[i] = str(dict[i].get('text'))[0:100] + '...'
                if owner_id == abs(owner_id):
                    lnk = 'https://vk.com/id' + str(owner_id) + '?w=wall' + str(owner_id) + '_' + str(id_x)
                else:
                    lnk = 'https://vk.com/public' + str(abs(owner_id)) + '?w=wall' + str(owner_id) + '_' + str(id_x)
                self.link[i] = lnk
                i = i + 1

                print(lnk)
        self.ui.list.addItems(self.text_x)
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
