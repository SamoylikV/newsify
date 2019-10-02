# -*- coding: utf-8 -*-
import json
import sys
import kod
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
		self.ui.find.clicked.connect(self.find)
		self.ui.else_1.clicked.connect(self.find1)
		self.combo = self.ui.filter  # подключение комбо-бокса
		self.combo.activated[str].connect(self.filters)
		self.acs = ''  # инициализация переменной токена
		self.ui.list.itemDoubleClicked.connect(self.listing)
		self.kat = ''  # инициализация переменной категории
		self.kat1 = ''  # инициализация переменной категории
		self.next = ''
		self.old = ''
		self.region_text = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
		self.region_id = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
		self.city_text = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']

		self.countri_text = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
		self.countri_id = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
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
		#tokken)
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
								if tokken != "PyQt5.QtCore.QUrl('https://m.vk.com/login?act=authcheck" and tokken != "PyQt5.QtCore.QUrl('http://www.fort-dev.ml/newsify/wait.php')" and tokken != "PyQt5.QtCore.QUrl('http://www.fort-dev.ml/newsify/wait.php?i=1')" and tokken != "PyQt5.QtCore.QUrl('http://www.fort-dev.ml/newsify/wait.php?i=2')" and tokken != "PyQt5.QtCore.QUrl('http://www.fort-dev.ml/newsify/wait2.php')" and tokken != "PyQt5.QtCore.QUrl('https://oauth.vk.com/authorize?client_id=7080257" and tokken != "PyQt5.QtCore.QUrl('https://oauth.vk.com/oauth/authorize?client_id=7080257":
															self.acs = tokken.split('=')[-1]  # обработка строки и запись токена в переменную
															self.town = 'https://api.vk.com/method/account.getProfileInfo?access_token=' + self.acs + '&v=5.101'  # запрос информации о пользователе
															self.town = requests.get(self.town)
															self.town = self.town.text  # обработка json кода
															self.town = json.loads(self.town)
															#self.town)
															self.town = self.town.get('response')
															#self.town)
															self.ui.find.setEnabled(True)  # разблокировка кнопки
															#'self.acs=', self.acs)
															self.countri = 'https://api.vk.com/method/database.getCountries?count=234&need_all=1&access_token=' + self.acs + '&v=5.101'
															self.countri =  requests.get(self.countri)
															self.countri = self.countri.text
															self.countri = json.loads(self.countri)
															self.countri = self.countri.get('response')
															self.countri = self.countri.get('items')
															#self.countri)
															i=0
															while i<234:
																self.countri_text[i] = self.countri[i].get('title')
																#self.countri_text[i])
																self.countri_id[i] = self.countri[i].get('id')
																#self.countri_id[i])
																i= i+1
															self.ui.countri.setEnabled(True) 
															self.ui.countri.activated[str].connect(self.Countri)
															#self.countri_text)
															#self.countri_id)
															self.ui.countri.addItems(self.countri_text)
															i = self.ui.countri.currentIndex()
															self.countri = self.countri_id[i]
															#self.countri)

															self.region_lnk = 'https://api.vk.com/method/database.getRegions?country_id='+str(self.countri)+'&count=1000&need_all=1&access_token=' + self.acs + '&v=5.101'
															self.region =  requests.get(self.region_lnk)
															self.region = self.region.text
															self.region = json.loads(self.region)
															self.region = self.region.get('response')
															counter = self.region.get('count')
															self.region = self.region.get('items')
															#self.region)
															i=0
															while i<counter:
																self.region_text[i] = self.region[i].get('title')
																#self.region_text[i])
																self.region_id[i] = self.region[i].get('id')
																#self.region_id[i])
																self.ui.region.addItem(self.region_text[i])
																i= i+1
															self.ui.filter.setEnabled(True) 
															self.ui.region.activated[str].connect(self.Region)
															#self.region_text)
															#self.region_id)
															i = self.ui.region.currentIndex()
															self.region = self.region_id[i]
															#self.region)
															#self.countri)
															self.city_lnk = 'https://api.vk.com/method/database.getCities?country_id='+str(self.countri)+'&region_id='+ str(self.region) +'&count=1000&need_all=0&access_token=' + self.acs + '&v=5.101'
															#self.city_lnk)
															self.city =  requests.get(self.city_lnk)
															self.city = self.city.text
															#self.city)
															self.city = json.loads(self.city)
															self.city = self.city.get('response')
															counterc = self.city.get('count')
															self.city = self.city.get('items')
															#self.region)
															i=0
															while i<counterc:
																self.city_text[i] = self.city[i].get('title')
																#self.region_text[i])
																self.ui.citi.addItem(self.city_text[i])
																i= i+1
															self.ui.citi.setEnabled(True) 
															self.ui.citi.activated[str].connect(self.Citi)
															#self.city_text)
															self.age = self.town.get('bdate')
															self.age = str(self.age)
															self.age = self.age.split('.')[-1]
															#self.age)
															self.age = int(self.age)
															self.age = 2019 - self.age
															#"age:",self.age)
															self.town = self.town.get('home_town')  # извлечение данных о городе
															#self.town)
															self.hometown = str(self.town)
															self.town = str(self.town)  # запись города
															#self.town)
															if self.town != '':
																self.ui.citi.addItem(self.town)
																self.find()
															else:
																self.my_web.load(QUrl(
																	'http://www.fort-dev.ml/newsify/wait.php'))  # загрузка страницы ожидания
	def Countri(self):
		i = self.ui.countri.currentIndex()
		self.countri = self.countri_id[i]
		self.region_lnk = 'https://api.vk.com/method/database.getRegions?country_id='+str(self.countri)+'&count=1000&need_all=1&access_token=' + self.acs + '&v=5.101'
		self.region =  requests.get(self.region_lnk)
		self.region = self.region.text
		self.region = json.loads(self.region)
		self.region = self.region.get('response')
		counter = self.region.get('count')
		self.region = self.region.get('items')
		self.ui.region.clear()
		i=0
		while i<counter:
			self.region_text[i] = self.region[i].get('title')
			#self.region_text[i])
			self.region_id[i] = self.region[i].get('id')
			#self.region_id[i])
			self.ui.region.addItem(self.region_text[i])
			i= i+1
		self.ui.region.setEnabled(True) 
		i = self.ui.region.currentIndex()
		self.region = self.region_id[i]
		self.ui.citi.clear()
#		self.ui.citi.addItem(self.hometown)
		i = self.ui.region.currentIndex()
		self.region = self.region_id[i]
		self.city_lnk = 'https://api.vk.com/method/database.getCities?country_id='+str(self.countri)+'&count=1000&need_all=0&access_token=' + self.acs + '&v=5.101'
		self.city =  requests.get(self.city_lnk)
		print(self.city_lnk)
		self.city = self.city.text
		self.city = json.loads(self.city)
		self.city = self.city.get('response')
		counterc = self.city.get('count')
		self.city = self.city.get('items')
		i=0
		if counterc >1000:
			counterc=1000
		while i<counterc:
			self.city_text[i] = self.city[i].get('title')
			self.ui.citi.addItem(self.city_text[i])
			i= i+1
		self.ui.citi.setEnabled(True) 
		self.Region()

	def Region(self):
		
		self.ui.citi.clear()
		i = self.ui.region.currentIndex()
		self.region = self.region_id[i]
		self.city_lnk = 'https://api.vk.com/method/database.getCities?country_id='+str(self.countri)+'&region_id='+ str(self.region) +'&count=1000&need_all=0&access_token=' + self.acs + '&v=5.101'
		self.city =  requests.get(self.city_lnk)
		print(self.city_lnk)
		self.city = self.city.text
		self.city = json.loads(self.city)
		self.city = self.city.get('response')
		counterc = self.city.get('count')
		self.city = self.city.get('items')
		i=0
		if counterc >1000:
			counterc=1000
		while i<counterc:
			self.city_text[i] = self.city[i].get('title')
			self.ui.citi.addItem(self.city_text[i])
			i= i+1
		self.ui.citi.setEnabled(True) 
		self.ui.citi.addItem(self.hometown)
		self.Citi()

	def Citi(self):
		self.town=self.ui.citi.currentText()

	def filters(self):  # получение даных комбо-бокса и запись в переменную
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
		self.fnd = 'https://api.vk.com/method/newsfeed.search?q=' + self.town + ', ' + self.kat + ' новости&count=200&extended=1&start_from=' + str(
			self.next_1) + '&access_token=' + self.acs + '&v=5.101'  # создание ссылки поиска новостей
		self.Site()

	def find(self):
		self.town = self.ui.citi.currentText()  # запись данных в переменную из поля ввода
		self.my_web.load(QUrl("http://www.fort-dev.ml/newsify/wait2.php"))  # отображение страницы "Выберите новость"
		if self.town == '':
			self.ui.errors.setText("Введите название населенного пункта")  # Вывод текста в поле ошибок

		else:
			if self.kat != self.kat1:
				self.ui.errors.setText("")  # очистка поля ошибок
				self.kat1 = self.kat
				self.fnd = 'https://api.vk.com/method/newsfeed.search?q=' + self.town + ', ' + self.kat + ' новости&count=200&extended=1&access_token=' + self.acs + '&v=5.101'  # создание ссылки поиска новостей
				#self.fnd)
			else:
				self.fnd = 'https://api.vk.com/method/newsfeed.search?q=' + self.town + ', ' + self.kat + ' новости&count=200&extended=1&start_from=' + str(
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
		self.req = req.get('items')# извлечение новостей
		i = 0
		#count)
		if count == 1000:
			e = 15  # если новостей больше чем запрашивалось то задаем число которое запросили
			self.ui.else_1.setEnabled(True)
		else:
			e = count - 1  # если новостей меньше чем запрашивалось то задаем число новостей которое пришло
			self.ui.else_1.setEnabled(False)
		while i < e:
			id_x = self.req[i].get('id')
			owner_id = self.req[i].get('owner_id')
			self.text_x[i] = str(self.req[i].get('text'))[0:100] + '...'
			if self.old == self.text_x[i]:
				self.text_x[i]=str(self.req[i+15].get('text'))[0:100] + '...'
				#self.text_x[i])
			while self.text_x[i].split(',',1)[0]=='Уважаемая администрация':
				self.text_x[i]=str(self.req[i+15].get('text'))[0:100] + '...'
				#self.text_x[i])
			else:
				#self.text_x[i].split(',',1)[0]=='Уважаемая администрация')
				self.old = self.text_x[i]
			if self.age < 18:
				if self.text_x[i].find(kod.DeKod('0101020101')) == -1 and self.text_x[i].find(kod.DeKod('0201020101')) == -1 and self.text_x[i].find(kod.DeKod('0502010201')) == -1 and self.text_x[i].find(kod.DeKod('0705040503')) == -1 and self.text_x[i].find(kod.DeKod('0805040503')) == -1 and self.text_x[i].find(kod.DeKod('0403050404')) == -1 and self.text_x[i].find(kod.DeKod('0303050404')) == -1 and self.text_x[i].find(kod.DeKod('0101020101')) == -1 and self.text_x[i].find(kod.DeKod('0101020101')) == -1 and self.text_x[i].find(kod.DeKod('0101020101')) == -1 and self.text_x[i].find(kod.DeKod('0101020101')) == -1: 
															lnk = 'https://m.vk.com/wall' + str(owner_id) + '_' + str(id_x)  # создаем ссылки на посты
															self.link[i] = lnk  # запись ссылок в массив
															i = i + 1
				else:
					self.text_x[i]=''
					i=i+0
			else:
				lnk = 'https://m.vk.com/wall' + str(owner_id) + '_' + str(id_x)  # создаем ссылки на посты
				self.link[i] = lnk  # запись ссылок в массив
				i = i + 1

			#lnk)
		i=0
		self.ui.list.addItems(self.text_x)  # добавление ссылок из масива в список




app = QtWidgets.QApplication([])  # открытие интерфейса
application = mywindow()  # открытие интерфейса
application.show()  # отображение интерфейса
sys.exit(app.exec())  # при нажатии крестика закрыть окно
