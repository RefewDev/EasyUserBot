from importlib import import_module
from Telethon.plugins import ALL_MODULES
from Telethon import LOGS, clients
import asyncio
import json
import platform
import os

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'settings.json')
with open(path) as f:
    resp = json.load(f)
API_ID = resp['api_id']
API_HASH = resp['api_hash']
lang = resp['language']
loop = asyncio.get_event_loop()

async def main():
    await asyncio.gather(*[client.start() for client in clients])
    tot = 0
    enable = 0
    error = ""
    for module_name in ALL_MODULES:
        try:
            imported_module = import_module("Telethon.plugins." + module_name)
            if lang == "Italian" or lang == "Italiano":
                LOGS.info(module_name + " attivato.")
            elif lang == "English" or lang == "Inglese":
                LOGS.info(module_name + " activated.")
            tot += 1
            enable += 1
        except:
            error += module_name
            tot += 1
    if error:
        if lang == "Italian" or lang == "Italiano":
            LOGS.error(error + " non attivato.")
        elif lang == "English" or lang == "Inglese":
            LOGS.error(error + " not activated.")
    if lang == "Italian" or lang == "Italiano":
        LOGS.info("Attivati " + str(enable) + "/" + str(tot) + " plugins.")
    elif lang == "English" or lang == "Inglese":
        LOGS.info("Activated " + str(enable) + "/" + str(tot) + " plugins.")

if not API_ID and not API_HASH:
    if lang == "Italian" or lang == "Italiano":
        print("Configura le API ID e API HASH su settings.json o avviando EasyUserBot")
    elif lang == "English" or lang == "Inglese":
        print("Configure the API ID and API HASH on settings.json or by starting EasyUserBot")
    exit()
else:
    loop.run_until_complete(main())
    if lang == "Italian" or lang == "Italiano":
        LOGS.info("Tutti gli userbot sono stati avviati correttamente.")
    elif lang == "English" or lang == "Inglese":
        LOGS.info("All userbots have started successfully.")
    loop.run_forever()
