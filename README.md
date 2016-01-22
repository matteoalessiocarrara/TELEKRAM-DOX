# Telegram Bot APY #

Semplicissimo wrapper in python per le Telegram Bot API.

## Funzionamento ##

Tutti i metodi delle Telegram Bot API sono utilizzabili con il metodo Method() della classe Bot: basta passargli il nome del metodo, eventualmente i parametri, e verrà restituito l'output in json decodificato. 
Per i metodi disponibili e relativi return vedere https://core.telegram.org/bots/api

Esempio:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src import telegrambot

token = "123456789:abcdefghijklmnopqrstuvzfoobarFOOBAR"
bot = telegrambot.Bot(token)

if bot.TokenValido():
	print "Il token", bot.Token(), "è valido"
	#Ora usiamo il metodo "sendMessage" delle Telegram Bot API
	#La stringa è il nome del metodo, il dizionario (opzionale) contiene i parametri
	ret = bot.Method("sendMessage", {'chat_id' : 999, 'text' : "KI 666 TU???"})
	#La variabile ret contiene il return di sendMessage() in json decodificato
	print ret
	exit(0)
else:
	print "Token", bot.Token(), "non valido"
	exit(1)
```
## Altre informazioni ##

> This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.  

Aggiornamenti: [GitHub] (https://github.com/matteoalessiocarrara)  
Email: sw.matteoac@gmail.com
