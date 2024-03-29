# -*- coding: utf-8 -*-
import json
import sys
import requests
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

from Newsify import Ui_MainWindow  # импорт нашего сгенерированного файла

app = QtWidgets.QApplication([])  # открытие интерфейса


class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)  # Подключение графики
		self.my_web = self.ui.brs  # Подключение браузера
		self.ui.find.clicked.connect(self.find)
		self.ui.else_1.clicked.connect(self.find1)
		self.combo = self.ui.filter  # подключение комбо-бокса
		self.combo.activated[str].connect(self.filters)
		self.acs = ''  # инициализация переменной токена
		self.ui.list.itemDoubleClicked.connect(self.listing)
		self.kat = ''  # инициализация переменной категории
		self.next = ''
		self.old = ''
		self.ui.countri.activated[str].connect(self.Countri)
		self.ui.region.activated[str].connect(self.Region)
		self.ui.citi.activated[str].connect(self.Citi)
		self.region_text = [''] * 600
		self.region_id = [''] * 600
		self.city_text = [''] * 2000
		self.countri_text = [''] * 240
		self.countri_id = [''] * 240
		self.next_1 = 0
		self.fnd = ''  # инициализация переменной поискового запросы
		self.link = [''] * 16  # инициализация массива ссылок
		self.text_x = [''] * 16  # инициализация массива текста постов
		self.town = ''  # инициализация переменной города
		self.ui.brs.urlChanged.connect(self.token)
		self.ui.else_1.setEnabled(False)

	def token(self):
		tokken = str(self.my_web.url())  # получение данных из адресной строки
		if tokken.split("#")[0] == "PyQt5.QtCore.QUrl('https://oauth.vk.com/blank.html":
			tokken = tokken.split('#')[-1]  # обработка строки для получения токена
			tokken = tokken.split('&', 1)[0]
			self.acs = tokken.split('=')[-1]  # обработка строки и запись токена в переменную
			self.town = 'https://api.vk.com/method/account.getProfileInfo?access_token=' + self.acs + '&v=5.103'  # запрос информации о пользователе
			self.town = requests.get(self.town)
			self.town = self.town.text  # обработка json кода
			self.town = json.loads(self.town)
			self.town = self.town.get('response')
			self.countrihome = self.town.get('country')
			self.countrihome_id = self.countrihome.get('id')
			self.countrihome_text = self.countrihome.get('title')
			self.ui.find.setEnabled(True)  # разблокировка кнопки
			self.countri = 'https://api.vk.com/method/database.getCountries?count=234&need_all=1&access_token=' + self.acs + '&v=5.103'
			self.countri = requests.get(self.countri)
			self.countri = self.countri.text
			self.countri = json.loads(self.countri)
			self.countri = self.countri.get('response')
			self.countri = self.countri.get('items')
			self.ui.filter.setEnabled(True)
			self.ui.countri.setEnabled(True)
			self.ui.citi.setEnabled(True)
			self.ui.region.setEnabled(True)
			i = 0
			for i in range(234):
				self.countri_text[i] = self.countri[i].get('title')
				self.countri_id[i + 1] = self.countri[i].get('id')
				i = i + 1
			self.countri_id[0] = self.countrihome_id
			self.ui.countri.addItem(self.countrihome_text)
			self.ui.countri.addItems(self.countri_text)
			self.age = self.town.get('bdate')
			self.age = str(self.age)
			self.age = self.age.split('.')[-1]
			self.age = int(self.age)
			self.age = 2019 - self.age
			self.town = self.town.get('home_town')  # извлечение данных о городе
			self.hometown = str(self.town)
			self.fnd = 'https://api.vk.com/method/groups.get?extended=1&filter=publics&fields=activity&count=1&&access_token=' + self.acs + '&v=5.103'
			self.fnd = requests.get(self.fnd)
			self.fnd = self.fnd.text
			self.fnd = json.loads(self.fnd)
			self.fnd = self.fnd.get('response')
			self.fnd = self.fnd.get('items')
			self.fnd = self.fnd[0].get('activity')
			self.combo.setItemText(0, self.fnd)
			self.Countri()
			if self.hometown != None:
				self.ui.citi.addItem(self.hometown)
				self.find()
			else:
				self.my_web.load(QUrl('http://www.fort-dev.ml/newsify/wait.php'))  # загрузка страницы ожидания
			self.Countri()
		elif tokken == "PyQt5.QtCore.QUrl('https://oauth.vk.com/blank.html#error=access_denied&error_reason=user_denied&error_description=User denied your request')":
			self.my_web.load(QUrl(
				"https://oauth.vk.com/authorize?client_id=7080257&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.103&scope=photos,audio,video,pages,wall,docs,groups,offline&revoke=1&response_type=token"))  # если нажали выход загрузить страницу авторизации
		elif tokken == "PyQt5.QtCore.QUrl('https://oauth.vk.com/')":
			self.my_web.load(QUrl(
				"https://oauth.vk.com/authorize?client_id=7080257&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.103&scope=photos,audio,video,pages,wall,docs,groups,offline&revoke=1&response_type=token")) 

	def Countri(self):
		i = self.ui.countri.currentIndex()
		self.countri = self.countri_id[i]
		self.ui.citi.addItem(self.hometown)
		self.region_lnk = 'https://api.vk.com/method/database.getRegions?country_id=' + str(self.countri) + '&count=1000&need_all=1&access_token=' + self.acs + '&v=5.103'
		self.region = requests.get(self.region_lnk)
		self.region = self.region.text
		self.region = json.loads(self.region)
		self.region = self.region.get('response')
		counter = self.region.get('count')
		self.region = self.region.get('items')
		self.ui.region.clear()
		i = 0
		self.ui.region.addItem("")
		for i in range(counter):
			self.region_text[i] = self.region[i].get('title')
			self.region_id[i + 1] = self.region[i].get('id')
			self.ui.region.addItem(self.region_text[i])
			i = i + 1
		self.ui.region.setEnabled(True)
		i = self.ui.region.currentIndex()
		self.region = self.region_id[i]
		self.Region()

	def Region(self):
		self.ui.citi.clear()
		self.ui.citi.addItem(self.hometown)
		i = self.ui.region.currentIndex()
		self.region = self.region_id[i]
		self.city_lnk = 'https://api.vk.com/method/database.getCities?country_id=' + str(self.countri) + '&region_id=' + str(self.region) + '&count=1000&need_all=0&access_token=' + self.acs + '&v=5.103'
		self.city = requests.get(self.city_lnk)
		self.city = self.city.text
		self.city = json.loads(self.city)
		self.city = self.city.get('response')
		counterc = self.city.get('count')
		self.city = self.city.get('items')
		i = 0
		n = 0
		if counterc > 1000:
			next = counterc - 1000
			n = 1
			counterc = 1000
		for i in range(counterc):
			self.city_text[i] = self.city[i].get('title')
			self.ui.citi.addItem(self.city_text[i])
			i = i + 1
		if n == 1:
			self.city_lnk = 'https://api.vk.com/method/database.getCities?country_id=' + str(self.countri) + '&region_id=' + str(self.region) + '&count=' + str(next) + '&offset=1000' + '&need_all=0&access_token=' + self.acs + '&v=5.103'
			self.city = requests.get(self.city_lnk)
			self.city = self.city.text
			self.city = json.loads(self.city)
			self.city = self.city.get('response')
			counterc = self.city.get('count')
			self.city = self.city.get('items')
			i = 0
			counterc = counterc - 1000
			if counterc > 1000:
				counterc = 1000
			for i in range(counterc):
				self.city_text[i + 1000] = self.city[i].get('title')
				self.ui.citi.addItem(self.city_text[i + 1000])
				i = i + 1
		self.ui.citi.setEnabled(True)
		self.Citi()
	def Citi(self):
		self.town = self.ui.citi.currentText()
	def filters(self):  # получение даных комбо-бокса и запись в переменную
		if self.combo.currentText() != "Все":
			self.kat = self.combo.currentText()
		else:
			self.kat = ''
	def listing(self):
		self.my_web.load(QUrl(self.link[self.ui.list.currentRow()]))  # при двойном клике списка элемент открывает ссылку на этот пост
	def find1(self):
		self.fnd = 'https://api.vk.com/method/execute.next?q=' + self.town + ' ' + self.kat + '&count=150&post=15&age=' + str(self.age) + '&start_from=' + str(self.next) + '&access_token=' + self.acs + '&v=5.103'
		self.Site()
	def find(self):
		self.town = self.ui.citi.currentText()  # запись данных в переменную из поля ввода
		self.my_web.load(QUrl("http://www.fort-dev.ml/newsify/wait2.php"))  # отображение страницы "Выберите новость"
		self.fnd = 'https://api.vk.com/method/execute.newsify?q=' + self.town + ' ' + self.kat + '&count=150&post=15&age=' + str(self.age) + '&access_token=' + self.acs + '&v=5.103'  # создание ссылки поиска новостей
		self.Site()
	def Site(self):
		self.ui.list.clear()  # очистка списка
		self.my_web.load(QUrl("http://www.fort-dev.ml/newsify/wait2.php"))  # отображение страницы "Выберите новость"
		req = requests.get(self.fnd)  # получение json кода
		req = req.text
		req = json.loads(req)
		req = req.get('response')
		self.next = req.get('next_from')
		self.text_x = req.get('text')  # извлечение новостей
		self.link = req.get('lnk')  # запись ссылок в массив
		sync=req.get('sync')
		for i in range(sync):
			if i<10:
				cod="0"+str(i+1)
			else:
				cod=i
			self.ui.list.addItem(str(cod)+") "+self.text_x[i])
		if self.next == None:
			self.ui.else_1.setEnabled(False)
		else:
			self.ui.else_1.setEnabled(True)

window = mywindow()  # открытие интерфейса
window.show()  # отображение интерфейса

sys.exit(app.exec())  # при нажатии крестика закрыть окно

