# What is EasyUserBot?
It is a userbot base developed in python 3 using the Telethon library, it will help you create userbot very easily!
It supports both Italian and English, configurable from the settings together with the id & hash API

# How can I install it?
EasyUserBot is available on Windows, Linux & MacOS ..

## General
------
     Download the "EasyUserBot" folder from github
     Install python3
     Install telethon, regex(2020.5.14) e PyInquirer(1.0.3)
     Start EasyUserBot.py


### Installation on Windows
#### You need to have python3 installed on your computer
##### ![You can find a guide on how to install on windows 10 by clicking here](https://phoenixnap.com/kb/how-to-install-python-3-windows)
#### Download the "EasyUserBot" folder from github (click [here](https://github.com/RefewDev/EasyUserBot/archive/refs/heads/master.zip))
------
     By opening the command prompt go to the "EasyUserBot" folder (you can simply open the terminal, drag the "EasyUserBot" folder and click enter)
     pip3 install --user -r requirements.txt
     pip3 install -U telethon --user
     py EasyUserBot.py (or eventually open EasyUserBot.py with python without terminal)

### Installation on Ubuntu
------
     git clone https://github.com/RefewDev/EasyUserBot
     cd EasyUserBot
     chmod 777 installer-ubuntu.sh
     ./installer-ubuntu.sh
     python3 EasyUserBot.py
     
### Installation on Termux
------
     pkg up
     pkg install git screen
     git clone https://github.com/RefewDev/EasyUserBot
     cd EasyUserBot
     chmod 777 installer-termux.sh
     ./installer-termux.sh
     python3 EasyUserBot.py
     
# How do I add commands and functions?
Inside the "EasyUserBot/Telethon/plugins" folder there are already 2 examples "chat_id.py" & "reply.py" where they show how the reply works, edit a message and send it!
To create other plugins just create a .py file in the "plugins" folder in "EasyUser/Telethon" and it will be loaded automatically!
> The console will show which plugins will be loaded correctly and not

Explanation:
------
     @message(outgoing=<bool>(true or false), pattern='<message>')
     async def <functionname>(e):
     # what to do after typing the message in the pattern
        await e.respond("<message to be sent after typing the command>", parse_mode="<html or markdown>")
> Outgoing is for messages that can only be executed by yourself!
> Since the function is async, await must be written
>> The parse_mode is optional, not mandatory!

Example:
------
     from Telethon.events import message

     @message(outgoing=True, pattern='[.]test')
     async def test(e):
        await e.respond("<b>EasyUserBot up and running!</b>", parse_mode="html")

You can find other explanations on https://docs.telethon.dev

##### The base has only been tested on Windows10-64bit & Linux(Ubuntu18)

**For any problem or question you can contact me on telegram:**
### ⛈ [Telegram channel](https://t.me/RefewDevOfficial) ⛈
### 👨‍💻 [Telegram contact](https://t.me/Refew) 👨‍💻
