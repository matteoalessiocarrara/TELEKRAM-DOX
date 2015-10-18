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

import lib.Telegram_Bot_APY.src.telegrambot as telegrambot
from lib.out import *
from sys import argv, stderr

nomesw = argv[0]

if (len(argv) != 1 + 1) or ("-h" in argv) or ("--help" in argv):
	print >>stderr, inf + "Mostra i chat_id delle chat con messaggi ancora non letti da un bot di Telegram"
	exit(err + "Uso: " + nomesw + " token")

token = argv[1]
bot = telegrambot.Bot(token)

if not bot.TokenValido():
	exit(err + "Token non valido")

listaChat = []
ret = bot.Method("getUpdates")

for i in range(len(ret['result'])):
	chat = ret['result'][i]['message']['chat']
	if chat not in listaChat:
		listaChat.append(chat)
		# separatore chat
		print ""
		for elemento in chat:
			print elemento, chat[elemento]

print ""
