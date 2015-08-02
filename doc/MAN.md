### Nome 

TELEKRAM-DOX - invia N messaggi ad un gruppo su telegram usando un bot

### Sintassi

main.py token chat_id ripetizioni messaggio

### Funzionamento

* Per prima cosa serve un bot e relativo token, se non se ne ha già uno va creato. 
* Poi va trovato il chat_id, io ho l'ho trovato in questo modo: durante la creazione, o anche dopo, impostate la privacy (/setprivacy) su 'Disable'. Quindi aggiungete il bot al gruppo scelto e scrivete /start@usernamebot (sostituire usernamebot), poi andate a questo indirizzo: https://api.telegram.org/bot\<token\>/getUpdates (ovviamente al posto di \<token\> ci va messo il token). Dovreste vedere quello che avete scritto e anche il chat_id del gruppo, ci dovrebbe essere una cosa simile: [...]"chat":{"id":-666999,"title":"Gruppo di satanisti"}[...].

Il codice è molto semplice, anche le api di telegram sono molto semplici, non ci dovrebbero essere problemi a capire come funziona il software.

