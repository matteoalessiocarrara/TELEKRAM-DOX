#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Copyright 2015 Matteo Alessio Carrara <sw.matteoac@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import requests

turl = "https://api.telegram.org/bot"

class Bot:
	__tv = False #TokenValido
	__token = "devil666"
	
	def TokenValido(self):
		return self.__tv

	def __init__(self, token):
		self.__token = token
		#verifica token
		self.__tv = requests.get(turl+token+"/getMe").json()['ok']
			 
	def InviaMessaggio(self, chat_id, msg):
		#Return:
		#Descrizione dell'errore per errori
		#"OK" altrimenti
		req = requests.get(turl+self.__token+"/sendMessage", params = { "chat_id" : chat_id, "text" : msg}).json()
		if req['ok'] == False:
			return req['description']
		return "OK"

