# Cos'è EasyUserBot?
E' una base per userbot sviluppata in python 3 utilizzando la libreria Telethon, ti aiuterà a creare userbot molto facilmente!
Supporta sia italiano che inglese, configurabile dalle impostazioni assieme alle API id & hash

# Come posso installarlo?
EasyUserBot è disponibile su Windows, Linux & MacOS..

## Generale
------
     Scarica la cartella "EasyUserBot" da github
     Installare python3
     Installare telethon, regex(2020.5.14) e PyInquirer(1.0.3)
     Avviare EasyUserBot.py


### Installazione su Windows
#### E' necessario avere installato sul proprio computer python3
##### ![Puoi trovare una guida su come installare su windows 10 cliccando qui](https://phoenixnap.com/kb/how-to-install-python-3-windows)
------
     Scarica la cartella "EasyUserBot" da github
     Aprendo il prompt dei comandi recarsi nella cartella "EasyUserBot"(potete semplicemente aprire il terminale, trascinare la cartella "EasyUserBot" e cliccare invio)
     pip3 install --user -r requirements.txt
     pip3 install -U telethon --user
     py EasyUserBot.py (o eventualmente aprire EasyUserBot.py con python senza terminale)

### Installazione su Ubuntu
------
     git clone https://github.com/RefewDev/EasyUserBot
     cd EasyUserBot
     chmod 777 installer-ubuntu.sh
     ./installer-ubuntu.sh
     python3 EasyUserBot.py
     
### Installazione su Termux
------
     pkg up
     pkg install git
     git clone https://github.com/RefewDev/EasyUserBot
     cd EasyUserBot
     chmod 777 installer-termux.sh
     ./installer-termux.sh
     python3 EasyUserBot.py
     
# Come aggiungo i comandi e le funzioni?
All'interno della cartella "EasyUserBot/Telethon/plugins" sono presenti già 2 esempi "chat_id.py" & "reply.py" dove mostrano come funziona il reply, modificare un messaggio e inviarlo!
Per creare altri plugin basterà creare un file .py nella cartella "plugins" in "EasyUser/Telethon" e verrà caricato automaticamente!
> Nella console apparirà quali plugin verranno caricati correttamente e non

Spiegazione:
------
     @message(outgoing=<bool>(vero o falso), pattern='<messaggio>')
     async def <nomefunzione>(e):
     # cosa fare dopo aver digitato il messaggio presente in pattern
        await e.respond("<messaggio da inviare dopo aver digitato il comando>", parse_mode="<html o markdown>")
> Outgoing è per i messaggi che potranno essere eseguiti solo da voi stessi!
> Visto che la funzione è async, è necessario scrivere await
>> La parse_mode è opzionale, non obbligatoria!

Esempio:
------
     from Telethon.events import message

     @message(outgoing=True, pattern='[.]test')
     async def test(e):
        await e.respond("<b>EasyUserBot attivo e funzionante!</b>", parse_mode="html")

![Puoi trovare altre spiegazioni cliccando qui!](https://docs.telethon.dev/en/latest/basic/quick-start.html)

##### La base è stata testata solo su Windows10-64bit & Linux(Ubuntu18)

**Per qualsiasi problema o domanda puoi contattare me su telegram:**
### ⛈ [Canale telegram](https://t.me/RefewDevOfficial) ⛈
### 👨‍💻 [Contatto telegram](https://t.me/Refew) 👨‍💻
