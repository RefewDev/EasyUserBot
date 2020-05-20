from logging import getLogger, basicConfig, INFO
import platform
from telethon import TelegramClient
from telethon.sessions import StringSession
import json
import os


clients = []

if platform.system() == "Windows":
    path = os.path.dirname(os.getcwd())
    resp = json.load(open("settings.json"))
    API_ID = resp['api_id']
    API_HASH = resp['api_hash']
    lang = resp['language']
    p = os.listdir("sessions/")
    if not API_ID and not API_HASH:
        if lang == "Italian" or lang == "Italiano":
            print("Configura le API ID e API HASH su settings.json o avviando EasyUserBot")
        elif lang == "English" or lang == "Inglese":
            print("Configure the API ID and API HASH on settings.json or by starting EasyUserBot")
        exit()
    else:
        LOGS = getLogger(__name__)
        num = 0
        for i in p:
            i = "sessions/" + i
            sessfile = json.load(open(i))
            nomess = ""
            nomess += nomess.join(sessfile).replace(".json", "")
            stringss = sessfile[nomess]
            bot = TelegramClient(StringSession(stringss), API_ID, API_HASH)
            clients.append(bot)
            num += 1

elif platform.system() == "Linux" or platform.system() == "Darwin":
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'settings.json')
    with open(path) as f:
        resp = json.load(f)
    API_ID = resp['api_id']
    API_HASH = resp['api_hash']
    lang = resp['language']
    p = os.listdir(os.path.abspath("sessions/"))
    if not API_ID and not API_HASH:
        if lang == "Italian" or lang == "Italiano":
            print("Configura le API ID e API HASH su settings.json o avviando EasyUserBot")
        elif lang == "English" or lang == "Inglese":
            print("Configure the API ID and API HASH on settings.json or by starting EasyUserBot")
        exit()
    else:
        LOGS = getLogger(__name__)
        num = 0
        for i in p:
            bot = ""
            bots = {}
            i = os.path.abspath("sessions/" + i)
            sessfile = json.load(open(i))
            nomess = ""
            nomess += nomess.join(sessfile).replace(".json", "")
            stringss = sessfile[nomess]
            bots['bot'] = TelegramClient(StringSession(stringss), API_ID, API_HASH)
            clients.append(bots['bot'])
            num += 1

basicConfig(
    format="%(asctime)s | %(name)s - [%(levelname)s] --> %(message)s",
    level=INFO)
