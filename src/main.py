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

if len(argv) != 4 + 1:
	print >>stderr, inf + "Usa un bot di Telegram per inviare N messaggi uguali ad un gruppo/chat"
	exit(err + "Uso: " + nomesw + " token chat_id ripetizioni messaggio")

msg = argv[4]
token = argv[1]
doxbot = telegrambot.Bot(token)
chat_id = argv[2]
ripetizioni = int(argv[3])

if not doxbot.TokenValido(): exit(err + "Token non valido")

for i in range(1, ripetizioni + 1):
	ret = doxbot.Method("sendMessage", {'chat_id': chat_id, 'text': msg})
	if not ret['ok']: 
		exit(err + ret['description'])
	print i, "OK"
