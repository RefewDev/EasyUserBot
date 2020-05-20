#!/bin/bash
sudo apt-get update
sudo apt-get install python3
pip3 install --user -r requirements.txt
pip3 install -U telethon --user
exit
