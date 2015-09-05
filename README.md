# TELEKRAM-DOX #

Invia N messaggi ad un gruppo o ad una chat su telegram usando un bot.

## File ##

* Main.py: invia i messaggi
* Chat.py: mostra i chat_id

## Sintassi ##

* main.py token chat_id ripetizioni messaggio
* chat.py token

## Token ##

Per usare questo software serve un bot con relativo token. Per creare un bot, vedere @BotFather su telegram.

## Trovare il chat_id ##

Chat.py mostra tutti i chat_id delle chat/gruppi con messaggi non letti. Usa il metodo getUpdates(), vedere le API di telegram per avere più informazioni.
**Attenzione: potrebbe non funzionare quando il bot è utilizzato da altri software (potrebbero inviare la conferma di lettura al server con conseguente eliminazione dei messaggi, prima che questo software li abbia scaricati)**

## Altre informazioni ##

> This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.  

Aggiornamenti: [GitHub] (https://github.com/matteoalessiocarrara)  
Email: sw.matteoac@gmail.com