#
#              AdvancedPresence
#                 by @fxcvd
#
#   header.py
#   created at 07.06.21
#   modifed at 07.06.21
#

# install with pip
import applescript
from pypresence import Presence

# standart libs
from time import sleep, time
from sys import platform
import json

import plugins


def get_active_title():
    return applescript.run("applescript/title.applescript").out


def get_active_url():
    return applescript.run("applescript/url.applescript").out


def get_active_window():
    appl_r = applescript.run("applescript/current.applescript").out

    window = appl_r.split(":")[:-1][-1].replace(".app", "")

    return window


def icon_for_app(app):
    try:    
        return config["icons"][app]
    except:
        return "other"


with open("assets/config.json") as file:
    config = json.load(file)
    file.close()
