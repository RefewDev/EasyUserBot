from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError
import platform
import os
import regex
import random
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import json
import time

colore = '\033[91m'
stop = '\033[0m'
settings = "settings.json"
sessioni = "sessions/"
width = os.get_terminal_size().columns

style = style_from_dict({
Token.Separator: '',
Token.QuestionMark: '#c675ff',
Token.Selected: '#85ffff',
Token.Pointer: '#85ffff',
Token.Instruction: '#d9fc38 bold',
Token.Answer: '#85ffff',
Token.Question: '#c675ff',
})

questionsen = [
    {
        'type': 'list',
        'name': 'operation',
        'message': 'What do you want to do',
        'choices': [
            'Start all sessions',
            'Stop all sessions',
            Separator(' '),
            'Add new session',
            'Remove a session',
            Separator(' '),
            'Reset settings',
            Separator(' '),
            'Exit',
        ]
    },
]

questionsit = [
    {
        'type': 'list',
        'name': 'operation',
        'message': 'Che cosa vuoi fare',
        'choices': [
            'Avvia tutte le sessioni',
            'Interrompi tutte le sessioni',
            Separator(' '),
            'Aggiungi una nuova sessione',
            'Rimuovi una sessione',
            Separator(' '),
            'Reimposta le impostazioni generali',
            Separator(' '),
            'Esci',
        ]
    },
]


class CheckAPI_ID(Validator):
    def validate(self, document):
        ok = regex.match(
            '[0-9]',
            document.text)
        if not ok or not len(document.text) == 7:
            if os.path.isfile(settings):
                sett = json.load(open(settings))
                if sett['language'] == "Italian" or sett['language'] == "Italiano":
                    raise ValidationError(
                        message='Perfavore, inserisci un Api ID valido',
                        cursor_position=len(document.text))
                elif sett['language'] == "English" or sett['language'] == "Inglese":
                    raise ValidationError(
                        message='Please enter a valid Api ID',
                        cursor_position=len(document.text))
            else:
                raise ValidationError(
                    message='Please enter a valid Api ID',
                    cursor_position=len(document.text))



class CheckAPI_HASH(Validator):
    def validate(self, document):
        if not len(document.text) == 32:
            if os.path.isfile(settings):
                sett = json.load(open(settings))
                if sett['language'] == "Italian" or sett['language'] == "Italiano":
                    raise ValidationError(
                        message='Perfavore, inserisci delle Api HASH valide',
                        cursor_position=len(document.text))
                elif sett['language'] == "English" or sett['language'] == "Inglese":
                    raise ValidationError(
                        message='Please enter a valid Api HASH',
                        cursor_position=len(document.text))
            else:
                raise ValidationError(
                    message='Please enter a valid Api HASH',
                    cursor_position=len(document.text))


questionset = [
    {
        'type': 'list',
        'name': 'language',
        'message': 'What language do you want to use',
        'choices': [
            'English',
            'Italian',
        ]
    },
    {
        'type': 'input',
        'name': 'api_id',
        'message': 'Enter your api_id',
        'validate': CheckAPI_ID
    },
    {
        'type': 'input',
        'name': 'api_hash',
        'message': 'Enter your api_hash',
        'validate': CheckAPI_HASH
    },
]

questionsetit = [
    {
        'type': 'list',
        'name': 'language',
        'message': 'Che lingua vuoi usare',
        'choices': [
            'Inglese',
            'Italiano',
        ]
    },
    {
        'type': 'input',
        'name': 'api_id',
        'message': 'Inserisci il tuo api_id',
        'validate': CheckAPI_ID
    },
    {
        'type': 'input',
        'name': 'api_hash',
        'message': 'Inserisci la tua api_hash',
        'validate': CheckAPI_HASH
    },
]


def ressettings():
    global resp
    if os.path.isfile(settings):
        sett = json.load(open(settings))
        if sett['language'] == "Italian" or sett['language'] == "Italiano":
            resp = prompt(questionsetit, style=style)
        elif sett['language'] == "English" or sett['language'] == "Inglese":
            resp = prompt(questionset, style=style)
        with open(settings, "w") as o:
            json.dump(resp, o)
    else:
        print("Hi! Let's start by setting the general settings")
        data = prompt(questionset, style=style)
        with open(settings, "w") as o:
            json.dump(data, o)
        print("Done.")
        time.sleep(2)
        startdo()


def startsessions():
    p = os.listdir("sessions")
    sett = json.load(open(settings))
    if not p:
        if sett['language'] == "Italian" or sett['language'] == "Italiano":
            print("Non sono presenti sessioni!")
        elif sett['language'] == "English" or sett['language'] == "Inglese":
            print("There are no sessions!")
        time.sleep(2)
        startdo()
    else:
        if platform.system() == "Windows":
            nome = "EasyUserBot_Console"
            os.system('start "' + nome + '" cmd /k py -m Telethon')
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            nome = "EasyUserBot_" + str(random.randint(1, 9999))
            os.system('screen -ls | awk -vFS=\'\\t|[.]\' \'/EasyUserBot/ {system("screen -S "$2" -X quit")}\'')
            if sett['language'] == "Italian" or sett['language'] == "Italiano":
                try:
                    os.system("screen -d -m -S " + nome)
                    os.system("screen -S " + nome + " -X stuff \"python3 -m Telethon\"'\n'")
                    print("Operazione completata. \nPer accedere alla console delle sessioni digita screen -x " + nome)
                except:
                    print("Errore")
            elif sett['language'] == "English" or sett['language'] == "Inglese":
                try:
                    os.system("screen -d -m -S " + nome)
                    os.system("screen -S " + nome + " -X stuff \"python3 -m Telethon\"'\n'")
                    print("Operation complete. \nTo access the console, type screen -x " + nome)
                except:
                    print("Error")
        time.sleep(3)
        startdo()



def stopsessions():
    p = os.listdir("sessions")
    sett = json.load(open(settings))
    if not p:
        if sett['language'] == "Italian" or sett['language'] == "Italiano":
            print("Non sono presenti sessioni!")
        elif sett['language'] == "English" or sett['language'] == "Inglese":
            print("There are no sessions!")
        time.sleep(2)
        startdo()
    else:
        if platform.system() == "Windows":
            try:
                os.system('taskkill /fi "WINDOWTITLE eq EasyUserBot_Console" /Im Cmd.exe /F /T')
                if sett['language'] == "Italian" or sett['language'] == "Italiano":
                    print("Operazione completata.")
                elif sett['language'] == "English" or sett['language'] == "Inglese":
                    print("Operation complete.")
            except:
                if sett['language'] == "Italian" or sett['language'] == "Italiano":
                    print("Errore")
                elif sett['language'] == "English" or sett['language'] == "Inglese":
                    print("Error")
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            try:
                os.system('screen -ls | awk -vFS=\'\\t|[.]\' \'/EasyUserBot/ {system("screen -S "$2" -X quit")}\'')
                if sett['language'] == "Italian" or sett['language'] == "Italiano":
                    print("Operazione completata.")
                elif sett['language'] == "English" or sett['language'] == "Inglese":
                    print("Operation complete.")
            except:
                if sett['language'] == "Italian" or sett['language'] == "Italiano":
                    print("Errore")
                elif sett['language'] == "English" or sett['language'] == "Inglese":
                    print("Error")
        time.sleep(2)
        startdo()

def addsession():
    global path, nome
    sett = json.load(open(settings))
    if sett['language'] == "Italian" or sett['language'] == "Italiano":
        nome = input('Inserisci nome sessione: ')
        while nome == "":
            nome = input('Inserisci nome sessione: ')
        path = "sessions/" + nome + ".json"
        while os.path.isfile(path):
            print("Esiste già una sessione con questo nome, per favore scegline un altro")
            nome = input('Inserisci nome sessione: ')
            path = "sessions/" + nome + ".json"
    elif sett['language'] == "English" or sett['language'] == "Inglese":
        nome = input('Enter session name: ')
        while nome == "":
            nome = input('Enter session name: ')
        path = "sessions/" + nome + ".json"
        while os.path.isfile(path):
            print("A session with this name already exists, please choose another one")
            nome = input('Enter session name: ')
            path = "sessions/" + nome + ".json"
    resp = json.load(open(settings))
    API_ID = resp['api_id']
    API_HASH = resp['api_hash']
    with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        string = client.session.save()
        print(client.session.save())
    entry = {''+nome: ''+string}
    rpath = path
    with open(rpath, 'w') as f:
        f.write(json.dumps(entry))
    time.sleep(2)
    startdo()


def remsession():
    global msg
    sett = json.load(open(settings))
    p = os.listdir("sessions")
    if not p:
        if sett['language'] == "Italian" or sett['language'] == "Italiano":
            print("Non sono presenti sessioni!")
        elif sett['language'] == "English" or sett['language'] == "Inglese":
            print("There are no sessions!")
        time.sleep(2)
        startdo()
    else:
        new_strings = []
        for string in p:
            new_string = string.replace(".json", "")
            new_strings.append(new_string)
        if sett['language'] == "Italian" or sett['language'] == "Italiano":
            msg = "Quale sessione vuoi eliminare"
            new_strings.append("Indietro")
        elif sett['language'] == "English" or sett['language'] == "Inglese":
            msg = "Which session do you want to delete"
            new_strings.append("Back")
        questionsrem = [
        {
            'type': 'list',
            'name': 'sessionr',
            'message': msg,
            'choices': new_strings
        },
        ]
        resp = prompt(questionsrem, style=style)
        if resp['sessionr'] == "Indietro" or resp['sessionr'] == "Back":
            time.sleep(1)
            startdo()
        else:
            os.remove(sessioni + resp['sessionr'] + ".json")
            if sett['language'] == "Italian" or sett['language'] == "Italiano":
                print("La sessione " + resp['sessionr'] + " è stata rimossa correttamente!")
            elif sett['language'] == "English" or sett['language'] == "Inglese":
                print("The session " + resp['sessionr'] + " has been successfully removed!")
            time.sleep(2)
            startdo()

def do(operation):
    if operation == "Start all sessions" or operation == "Avvia tutte le sessioni":
        startsessions()
    elif operation == "Stop all sessions" or operation == "Interrompi tutte le sessioni":
        stopsessions()
    elif operation == "Add new session" or operation == "Aggiungi una nuova sessione":
        addsession()
    elif operation == "Remove a session" or operation == "Rimuovi una sessione":
        remsession()
    elif operation == "Reset settings" or operation == "Reimposta le impostazioni generali":
        ressettings()
    else:
        sett = json.load(open(settings))
        if sett['language'] == "Italian" or sett['language'] == "Italiano":
            print("Ci vediamo, spero di rivederti presto! Telegram: @RefewDevOfficial - @Refew")
        elif sett['language'] == "English" or sett['language'] == "Inglese":
            print("Goodbye, I hope to see you soon! Telegram: @RefewDevOfficial - @Refew")
        time.sleep(3)
        if platform.system() == "Windows":
            os.system('cls')
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system('clear')
        exit()

def startdo():
    global resp
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('clear')
    print(colore + "██████╗ ███████╗███████╗███████╗██╗    ██╗██████╗ ███████╗██╗   ██╗".center(width))
    print("██╔══██╗██╔════╝██╔════╝██╔════╝██║    ██║██╔══██╗██╔════╝██║   ██║".center(width))
    print("██████╔╝█████╗  █████╗  █████╗  ██║ █╗ ██║██║  ██║█████╗  ██║   ██║".center(width))
    print("██╔══██╗██╔══╝  ██╔══╝  ██╔══╝  ██║███╗██║██║  ██║██╔══╝  ╚██╗ ██╔╝".center(width))
    print("██║  ██║███████╗██║     ███████╗╚███╔███╔╝██████╔╝███████╗ ╚████╔╝ ".center(width))
    print("╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝ ╚══╝╚══╝ ╚═════╝ ╚══════╝  ╚═══╝  ".center(width) + stop)
    print("EasyUserBot Version 1.0".center(width))
    sett = json.load(open(settings))
    p = os.listdir("sessions")
    parla = "\n"
    parla += parla.join(p).replace(".json", "")
    n = len(p)
    if 'language' in sett:
        if sett['language'] == "Italian" or sett['language'] == "Italiano":
            print("Sessioni presenti [" + str(n) + "]" + parla + "\n" + stop)
            resp = prompt(questionsit, style=style)
        elif sett['language'] == "English" or sett['language'] == "Inglese":
            print("Sessions found [" + str(n) + "]" + parla + "\n" + stop)
            resp = prompt(questionsen, style=style)
        if 'operation' not in resp:
            startdo()
        else:
            do(resp['operation'])

try:
    os.makedirs("sessions", 0o755)
except OSError:
    a = 0

try:
    sett = json.load(open(settings))
    if not 'language' in sett and not 'api_id' in sett and not 'api_hash' in sett:
        if platform.system() == "Windows":
            os.system('del /f settings.json')
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("rm -f settings.json")
    else:
        if sett['language'] == "" or sett['api_id'] == "" or sett['api_hash'] == "":
            if platform.system() == "Windows":
                os.system('del /f settings.json')
            elif platform.system() == "Linux" or platform.system() == "Darwin":
                os.system("rm -f settings.json")
except ValueError as e:
    os.system("rm -f settings.json")
except FileNotFoundError as e:
    a = 0


if platform.system() == "Windows":
    os.system("title EasyUserBot")
    if os.path.isfile(settings):
            startdo()
    else:
        os.system('cls')
        ressettings()
        startdo()
elif platform.system() == "Linux" or platform.system() == "Darwin":
    if os.path.isfile(settings):
            startdo()
    else:
        os.system('clear')
        ressettings()
        startdo()
else:
    print("[ERROR] I'm sorry, this program does not support this operating system.")
