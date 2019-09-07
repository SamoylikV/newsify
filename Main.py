#-*- coding: utf-8 -*-

import json
import sys

import requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

from Newsify import Ui_MainWindow  # импорт нашего сгенерированного файла


class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.count = 0
		self.my_web = self.ui.brs
		self.ui.brs.urlChanged.connect(self.token)
		self.ui.errors.setStyleSheet("color: rgb(255, 0, 0);")
		self.ui.list.setStyleSheet("color: rgb(160, 160, 160);")
		self.ui.raion.setReadOnly(True)
		self.ui.find.setEnabled(False)
		self.ui.find.clicked.connect(self.Find)
		self.acs = ''
		self.fnd = ''
		self.n = [0,0,0,0,0,0,0]
		self.my_web.load(QUrl("https://oauth.vk.com/authorize?client_id=7080257&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.101&scope=photos,audio,video,pages,wall,docs,groups,offset&response_type=token"))
		self.hash = ''
		self.tmp = ''
		self.link = 'fort-dev.ml/newsify/frame.php/'
	def token(self):

		tokken = self.my_web.url()
		tokken = str(tokken)
		if tokken == "PyQt5.QtCore.QUrl('about:blank')":
			print (tokken)
		else :
			if tokken != "PyQt5.QtCore.QUrl('')":
				if tokken != "PyQt5.QtCore.QUrl('fort-dev.ml/newsify/wait.php'')":
					print(self.fnd)
					if self.fnd == '':
						self.count=self.count+1
						print (tokken)
						res_tmp = tokken.split('#')[-1]
						self.tmp = res_tmp
						res_tmp1 = res_tmp.split('&',1)[0]
						if res_tmp1 != "PyQt5.QtCore.QUrl('https://m.vk.com/login?act=authcheck":
							if res_tmp1 !="PyQt5.QtCore.QUrl('https://oauth.vk.com/authorize?client_id=7080257":
								res_tmp = res_tmp1.split('=')[-1]
								self.acs = res_tmp
								self.ui.raion.setReadOnly(False)
								self.ui.find.setEnabled(True)
								print('self.acs=',self.acs)
								self.my_web.load(QUrl('fort-dev.ml/newsify/wait.php'))
						else:
							self.hash = self.tmp.split('=')[-1]
							self.hash = self.hash.split("'")[0]
							self.hash ('hash=',self.hash)
							print (self.hash)



	def Find(self):	
		Tokkens = self.acs
		question = self.ui.raion.text()
		if question == '':
			self.ui.errors.setText("Введите название населенного пункта")
		else: 
			if question != '':
				self.ui.errors.setText("")
				fn = 'https://api.vk.com/method/newsfeed.search?q=' + question + ' новости&count=100&access_token=' + Tokkens + '&v=5.101'
				req = requests.get(fn)
				self.fnd = fn
				resp = req.text
#				resp = eval(resp)
#				print (resp)
				dict = json.loads(resp);
#				print (dict)
				dict = dict.get('response')
#				print (dict)
				dict = dict.get('items')
				i=0
				while i<7:
					id_x = dict[i].get('id')
					owner_id = dict[i].get('owner_id')
					if owner_id == abs(owner_id):
						lnk = 'https://vk.com/id' + str(owner_id) + '?w=wall' + str(owner_id) + '_' + str(id_x)
					else :
						lnk = 'https://vk.com/public' + str(abs(owner_id)) + '?w=wall' + str(owner_id) + '_' + str(id_x)
					print(self.n[i])
					self.link = self.link + 'l' + str(i+1) + '=' + lnk + '&'
					i= i+1
				self.my_web.load(QUrl(self.link))
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())


