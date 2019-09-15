# -*- coding: utf-8 -*-
import json
import sys

import requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

from Newsify import Ui_MainWindow  # импорт нашего сгенерированного файла


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Подключение графики
        self.my_web = self.ui.brs  # Подключение браузера
        self.ui.errors.setStyleSheet("color: rgb(255, 0, 0);")  # изменение цвета текста поля ошибок
        self.ui.centralwidget.setStyleSheet("background-color: rgb(255,255,255);")  # изменение цвета фона главного окна
        self.ui.raion.setReadOnly(True)  # блокировка поля ввода
        self.ui.raion.setStyleSheet(
            '''border-radius: 8px;background-color: rgb(200,200,200);''')  # изменение скругленности и цвета фона поля ввода
        self.ui.list.setStyleSheet(
            '''border-radius: 10px;background-color: rgb(200,200,200); color:rgb(26,26,26);''')  # изменение скругленности, цвета текста и цвета фона списка
        self.ui.find.setStyleSheet(
            '''border-radius: 8px;background-color: rgb(200,200,200);''')  # изменение скругленности и цвета фона кнопки поиск
        self.ui.else_1.setStyleSheet(
            '''border-radius: 8px;background-color: rgb(200,200,200);''')  # изменение скругленности и цвета фона кнопки поиск
        self.ui.filter.setStyleSheet(
            '''border-radius: 8px;background-color: rgb(240,240,240);''')  # изменение скругленности и цвета фона комбо-бокса
        self.ui.find.setEnabled(False)  # блокировка кнопки поиск
        self.ui.find.clicked.connect(self.find)
        self.ui.else_1.clicked.connect(self.find1)
        self.combo = self.ui.filter  # подключение комбо-бокса
        self.combo.activated[str].connect(self.filters)
        self.acs = ''  # инициализация переменной токена
        self.ui.list.itemDoubleClicked.connect(self.listing)
        self.kat = ''  # инициализация переменной категории
        self.kat1 = ''  # инициализация переменной категории
        self.next = ''
        self.next_1 = 0
        self.fnd = ''  # инициализация переменной поискового запросы
        self.link = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                     '']  # инициализация массива ссылок
        self.text_x = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                       '']  # инициализация массива текста постов
        self.my_web.load(QUrl(
            "https://oauth.vk.com/authorize?client_id=7080257&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.101&scope=photos,audio,video,pages,wall,docs,groups,offline&revoke=1&response_type=token"))  # открытие страницы авторизации и запроса прав
        self.town = ''  # инициализация переменной города
        self.ui.brs.urlChanged.connect(self.token)
        self.ui.else_1.setEnabled(False)

    def token(self):
        tokken = str(self.my_web.url())  # получение данных из адресной строки
        print(tokken)
        if tokken == "PyQt5.QtCore.QUrl('about:blank')":
            print(tokken)
        else:
            if tokken == "PyQt5.QtCore.QUrl('https://oauth.vk.com/blank.html#error=access_denied&error_reason=user_denied&error_description=User denied your request')":
                self.my_web.load(QUrl(
                    "https://oauth.vk.com/authorize?client_id=7080257&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.101&scope=photos,audio,video,pages,wall,docs,groups,offline&revoke=1&response_type=token"))  # если нажали выход загрузить страницу авторизации
            elif tokken == "PyQt5.QtCore.QUrl('https://oauth.vk.com/')":
                self.my_web.load(QUrl(
                    "https://oauth.vk.com/authorize?client_id=7080257&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.101&scope=photos,audio,video,pages,wall,docs,groups,offline&revoke=1&response_type=token"))  # если нажали выход загрузить страницу авторизации
            elif tokken != "PyQt5.QtCore.QUrl('')":
                inf = 'https://api.vk.com/method/account.getProfileInfo?access_token=' + str(self.acs) + '&v=5.101'
                if tokken != inf:
                    if tokken != self.fnd:
                        if tokken != "PyQt5.QtCore.QUrl('http://www.fort-dev.ml/newsify/wait.php')":
                            print(self.fnd)
                            if self.fnd == '':
                                print(tokken)
                                tokken = tokken.split('#')[-1]  # обработка строки для получения токена
                                tokken = tokken.split('&', 1)[0]
                                print(tokken)
                                if tokken != "PyQt5.QtCore.QUrl('https://m.vk.com/login?act=authcheck":
                                    if tokken != "PyQt5.QtCore.QUrl('http://www.fort-dev.ml/newsify/wait.php')":
                                        if tokken != "PyQt5.QtCore.QUrl('http://www.fort-dev.ml/newsify/wait.php?i=1')":
                                            if tokken != "PyQt5.QtCore.QUrl('http://www.fort-dev.ml/newsify/wait.php?i=2')":
                                                if tokken != "PyQt5.QtCore.QUrl('http://www.fort-dev.ml/newsify/wait2.php')":
                                                    if tokken != "PyQt5.QtCore.QUrl('https://oauth.vk.com/authorize?client_id=7080257":
                                                        if tokken != "PyQt5.QtCore.QUrl('https://oauth.vk.com/oauth/authorize?client_id=7080257":
                                                            self.acs = tokken.split('=')[
                                                                -1]  # обработка строки и запись токена в переменную

                                                            self.ui.find.setEnabled(True)  # разблокировка кнопки
                                                            self.ui.raion.setReadOnly(False)  # разблокировка поля ввода
                                                            print('self.acs=', self.acs)
                                                            self.town = 'https://api.vk.com/method/account.getProfileInfo?access_token=' + self.acs + '&v=5.101'  # запрос информации о пользователе
                                                            self.town = requests.get(self.town)
                                                            self.town = self.town.text  # обработка json кода
                                                            self.town = json.loads(self.town)
                                                            print(self.town)
                                                            self.town = self.town.get('response')
                                                            print(self.town)
                                                            self.town = self.town.get(
                                                                'home_town')  # извлечение данных о городе
                                                            print(self.town)
                                                            self.town = str(self.town)  # запись города
                                                            print(self.town)
                                                            if self.town != '':
                                                                self.town = 'г.'+ self.town
                                                                self.ui.raion.setText(self.town)
                                                                self.find()
                                                            else:
                                                                self.my_web.load(QUrl(
                                                                    'http://www.fort-dev.ml/newsify/wait.php'))  # загрузка страницы ожидания

    def filters(self):  # получение даных комбо-бокса и запись в переменную
        print(self.combo.currentText())
        if self.combo.currentText() != "Все":
            self.kat = self.combo.currentText()
        else:
            self.kat = ''

    def listing(self):
        self.my_web.load(QUrl(
            self.link[self.ui.list.currentRow()]))  # при двойном клике списка элемент открывает ссылку на этот пост

    def find1(self):
        self.next_1 = int(self.next.split('/')[0]) + int(self.next_1)
        self.ui.errors.setText("")  # очистка поля ошибок
        self.fnd = 'https://api.vk.com/method/newsfeed.search?q=' + self.town + ' ' + self.kat + ' новости&count=20&start_from=' + str(
            self.next_1) + '&access_token=' + self.acs + '&v=5.101'  # создание ссылки поиска новостей
        self.Site()

    def find(self):
        self.town = self.ui.raion.text()  # запись данных в переменную из поля ввода
        self.my_web.load(QUrl("http://www.fort-dev.ml/newsify/wait2.php"))  # отображение страницы "Выберите новость"
        if self.town == '':
            self.ui.errors.setText("Введите название населенного пункта")  # Вывод текста в поле ошибок

        else:
            if self.kat != self.kat1:
                self.ui.errors.setText("")  # очистка поля ошибок
                self.kat1 = self.kat
                self.fnd = 'https://api.vk.com/method/newsfeed.search?q=' + self.town + ' ' + self.kat + ' новости&count=20&access_token=' + self.acs + '&v=5.101'  # создание ссылки поиска новостей
                print(self.fnd)
            else:
                self.fnd = 'https://api.vk.com/method/newsfeed.search?q=' + self.town + ' ' + self.kat + ' новости&count=20&start_from=' + str(
                    self.next_1) + '&access_token=' + self.acs + '&v=5.101'  # создание ссылки поиска новостей
        self.Site()

    def Site(self):
        self.ui.list.clear()  # очистка списка
        self.my_web.load(QUrl("http://www.fort-dev.ml/newsify/wait2.php"))  # отображение страницы "Выберите новость"
        req = requests.get(self.fnd)  # получение json кода
        req = req.text
        req = json.loads(req)
        req = req.get('response')
        count = req.get('count')  # извлечение количества новостей
        self.next = req.get('next_from')
        req = req.get('items')
        print(req)  # извлечение новостей
        i = 0
        print(count)
        if count == 1000:
            e = 20  # если новостей больше чем запрашивалось то задаем число которое запросили
            self.ui.else_1.setEnabled(True)
        else:
            e = count - 1  # если новостей меньше чем запрашивалось то задаем число новостей которое пришло
            self.ui.else_1.setEnabled(False)
        while i < e:
            id_x = req[i].get('id')
            owner_id = req[i].get('owner_id')
            self.text_x[i] = str(req[i].get('text'))[0:100] + '...'
            lnk = 'https://m.vk.com/wall' + str(owner_id) + '_' + str(id_x)  # создаем ссылки на посты
            self.link[i] = lnk  # запись ссылок в массив
            i = i + 1
            print(lnk)
        self.ui.list.addItems(self.text_x)  # добавление ссылок из масива в список


app = QtWidgets.QApplication([])  # открытие интерфейса
application = mywindow()  # открытие интерфейса
application.show()  # отображение интерфейса
sys.exit(app.exec())  # при нажатии крестика закрыть окно
