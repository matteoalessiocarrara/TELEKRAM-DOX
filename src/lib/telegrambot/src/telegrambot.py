#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

import requests

turl = "https://api.telegram.org/bot"


class Bot:

	__tokenValido = False
	__token = None

	def __init__(self, token):
		self.__token = token
		# in tutti i token c'è il carattere ":"
		self.__tokenValido = self.Method("getMe")['ok'] if ":" in token else False

	def Method(self, method, params={}):
		"""
		"Collegamento" a un metodo delle Telegram Bot Api
		Passare in method il nome del metodo, in params gli eventuali parametri
		Restituisce un dizionario ricavato dalla decodifica del return in json
		"""
		return requests.get(turl + self.__token + "/" + method, params=params).json()

	def TokenValido(self):
		return self.__tokenValido

	def Token(self):
		"""Restituisce il token di questo bot"""
		return self.__token
