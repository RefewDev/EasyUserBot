#!/bin/bash
pkg update -y
pkg install python
pip3 install --user -r requirements.txt
pip3 install -U telethon --user
exit
